#!/usr/bin/env python3
"""
Deterministic path and document-resolution helpers for amendment intake.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
DEFAULT_AGENT_KB_MANIFEST = BASE_DIR / "reference" / "knowledge_base" / "agents" / "agent_kb_manifest.yaml"
DEFAULT_AGENT_KB_BUNDLE = (
    BASE_DIR / "reference" / "knowledge_base" / "agents" / "corpus" / "government_and_reports_bundle.md"
)
DEFAULT_AGENT_KB_BUILD_MANIFEST = (
    BASE_DIR / "reference" / "knowledge_base" / "agents" / "corpus" / "build_manifest.json"
)
DEFAULT_PRODUCT_CONTEXT_SNAPSHOT = (
    BASE_DIR / "reference" / "knowledge_base" / "snapshots" / "product_context_bundle.md"
)
LANE_AGENT_KB_DIRNAME = "agent_kb"


@dataclass(frozen=True)
class IntakePaths:
    base_dir: Path
    document_abs: Path
    document_path: str
    document_id: str
    amendment_slug: str
    current_head_version: str
    review_root: Path
    intake_dir: Path
    intake_identity: Path
    intake_status: Path
    intake_events: Path
    intake_handoff: Path
    planning_dir: Path
    kernel_dir: Path
    ratification_dir: Path

    @property
    def round_1_dir(self) -> Path:
        return self.review_root / "round_1"

    @property
    def round_2_dir(self) -> Path:
        return self.review_root / "round_2"


@dataclass(frozen=True)
class ArchitectLaneContract:
    amendment_slug: str
    manifest_path: Path
    bundle_path: Path
    build_manifest_path: Path
    product_snapshot_path: Path
    planning_dir: Path
    architect_output_path: Path

    def repo_rel(self, path: Path) -> str:
        return path.resolve().relative_to(BASE_DIR.resolve()).as_posix()


def default_lane_manifest_path(paths: IntakePaths) -> Path:
    return (paths.planning_dir / "KNOWLEDGE_PACKET.yaml").resolve()


def default_lane_bundle_dir(paths: IntakePaths) -> Path:
    return (paths.planning_dir / LANE_AGENT_KB_DIRNAME).resolve()


def default_lane_bundle_path(paths: IntakePaths) -> Path:
    return (default_lane_bundle_dir(paths) / "government_and_reports_bundle.md").resolve()


def default_lane_build_manifest_path(paths: IntakePaths) -> Path:
    return (default_lane_bundle_dir(paths) / "build_manifest.json").resolve()


def amendment_slug_from_path(document_path: str) -> str:
    stem = Path(document_path.replace("\\", "/")).stem.lower()
    return re.sub(r"[^a-z0-9_]+", "_", stem).strip("_")


def _parse_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        data = yaml.safe_load(text[3:end]) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def _resolve_repo_path(path: str | Path) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = (BASE_DIR / str(candidate).replace("\\", "/")).resolve()
    else:
        candidate = candidate.resolve()
    try:
        candidate.relative_to(BASE_DIR.resolve())
    except ValueError as exc:
        raise ValueError(f"Path is outside repo root: {path}") from exc
    return candidate


def _load_manifest_yaml(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"Manifest not found: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"Unreadable YAML manifest: {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Manifest must be a YAML object: {path}")
    return data


def manifest_declares_path(manifest_path: Path, repo_relative_path: str) -> bool:
    manifest = _load_manifest_yaml(manifest_path)
    needle = repo_relative_path.replace("\\", "/").lstrip("/")
    for key in ("governing_documents", "reports_and_snapshots"):
        for raw in manifest.get(key) or []:
            if str(raw).replace("\\", "/").lstrip("/") == needle:
                return True
    return False


def resolve_architect_lane_contract(
    paths: IntakePaths,
    *,
    invoked_slug: str,
    bundle_override: str | None = None,
    manifest_override: str | None = None,
) -> ArchitectLaneContract:
    """
    Owner of architect-lane path reconciliation.

    The intake wrapper must derive the slug from the amendment path and confirm
    that the architect lane writes to the exact `reviews/<slug>/planning/`
    location expected by intake state.
    """
    if invoked_slug != paths.amendment_slug:
        raise ValueError(
            f"Architect lane slug mismatch: invoked {invoked_slug!r} != expected {paths.amendment_slug!r}"
        )

    manifest_path = _resolve_repo_path(manifest_override) if manifest_override else default_lane_manifest_path(paths)
    bundle_path = _resolve_repo_path(bundle_override) if bundle_override else default_lane_bundle_path(paths)
    build_manifest_path = (
        bundle_path.parent / "build_manifest.json"
        if bundle_override
        else default_lane_build_manifest_path(paths)
    )
    planning_dir = BASE_DIR / "reviews" / invoked_slug / "planning"
    architect_output_path = planning_dir / "ARCHITECT_PLAN.md"
    if planning_dir.resolve() != paths.planning_dir.resolve():
        raise ValueError(
            "Architect planning directory mismatch: "
            f"{planning_dir.resolve()} != {paths.planning_dir.resolve()}"
        )
    if architect_output_path.resolve() != (paths.planning_dir / "ARCHITECT_PLAN.md").resolve():
        raise ValueError(
            "Architect output path mismatch: "
            f"{architect_output_path.resolve()} != {(paths.planning_dir / 'ARCHITECT_PLAN.md').resolve()}"
        )
    return ArchitectLaneContract(
        amendment_slug=invoked_slug,
        manifest_path=manifest_path,
        bundle_path=bundle_path,
        build_manifest_path=build_manifest_path,
        product_snapshot_path=DEFAULT_PRODUCT_CONTEXT_SNAPSHOT.resolve(),
        planning_dir=planning_dir.resolve(),
        architect_output_path=architect_output_path.resolve(),
    )


def resolve_intake_paths(document_path: str) -> IntakePaths:
    rel = document_path.replace("\\", "/").lstrip("/")
    document_abs = (BASE_DIR / rel).resolve()
    try:
        document_abs.relative_to(BASE_DIR.resolve())
    except ValueError as exc:
        raise ValueError(f"Document path is outside repo root: {document_path}") from exc
    if not document_abs.is_file():
        raise FileNotFoundError(f"Document not found: {document_path}")

    meta = _parse_front_matter(document_abs)
    document_id = str(meta.get("document_id") or document_abs.stem).strip()
    current_head_version = str(meta.get("version") or "").strip()
    amendment_slug = amendment_slug_from_path(rel)

    review_root = BASE_DIR / "reviews" / amendment_slug
    intake_dir = review_root / "intake"
    return IntakePaths(
        base_dir=BASE_DIR,
        document_abs=document_abs,
        document_path=rel,
        document_id=document_id,
        amendment_slug=amendment_slug,
        current_head_version=current_head_version,
        review_root=review_root,
        intake_dir=intake_dir,
        intake_identity=intake_dir / "INTAKE_IDENTITY.yaml",
        intake_status=intake_dir / "INTAKE_STATUS.yaml",
        intake_events=intake_dir / "INTAKE_EVENTS.yaml",
        intake_handoff=intake_dir / "HANDOFF_NOTE.md",
        planning_dir=review_root / "planning",
        kernel_dir=review_root / "kernel",
        ratification_dir=review_root / "ratification",
    )


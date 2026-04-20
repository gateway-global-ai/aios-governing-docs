#!/usr/bin/env python3
"""
Narrow architect-lane evidence and conformance checks for the intake scaffold.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ArchitectCheckResult:
    ok: bool
    reasons: list[str]


def _load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Manifest must be a YAML object: {path}")
    return data


def _load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Build manifest must be a JSON object: {path}")
    return data


def _snapshot_generated_date(snapshot_path: Path) -> date | None:
    for line in snapshot_path.read_text(encoding="utf-8", errors="replace").splitlines()[:12]:
        stripped = line.strip()
        if stripped.startswith("**Generated:**"):
            raw = stripped.split("**Generated:**", 1)[1].strip()
            try:
                return date.fromisoformat(raw)
            except ValueError:
                return None
    return None


def _manifest_declared_paths(manifest_path: Path) -> tuple[str, list[str]]:
    doc = _load_yaml(manifest_path)
    label = str(doc.get("label") or "default").strip()
    ordered_paths: list[str] = []
    for key in ("governing_documents", "reports_and_snapshots"):
        for raw in doc.get(key) or []:
            ordered_paths.append(str(raw).replace("\\", "/").lstrip("/"))
    return label, ordered_paths


def validate_bundle_manifest_correspondence(
    manifest_path: Path,
    bundle_path: Path,
    build_manifest_path: Path,
) -> ArchitectCheckResult:
    reasons: list[str] = []
    label, expected_paths = _manifest_declared_paths(manifest_path)
    build_doc = _load_json(build_manifest_path)
    bundle_text = bundle_path.read_text(encoding="utf-8", errors="replace")

    build_label = str(build_doc.get("label") or "").strip()
    if build_label != label:
        reasons.append(
            f"build_manifest label {build_label!r} does not match selected manifest label {label!r}"
        )

    build_files = build_doc.get("files")
    if not isinstance(build_files, list):
        reasons.append("build_manifest files must be a list")
        return ArchitectCheckResult(ok=False, reasons=reasons)

    build_paths: list[str] = []
    for idx, item in enumerate(build_files):
        if not isinstance(item, dict):
            reasons.append(f"build_manifest files[{idx}] must be an object")
            continue
        raw_path = str(item.get("path") or "").replace("\\", "/").lstrip("/")
        if not raw_path:
            reasons.append(f"build_manifest files[{idx}] missing path")
            continue
        build_paths.append(raw_path)
        status = str(item.get("status") or "").strip()
        if status != "ok":
            reasons.append(f"build_manifest file {raw_path!r} has non-ok status {status!r}")
        marker = f"## Source: `{raw_path}`"
        if marker not in bundle_text:
            reasons.append(f"bundle is missing source section for build_manifest path {raw_path!r}")

    if build_paths != expected_paths:
        reasons.append("selected manifest paths do not exactly match build_manifest file paths")

    expected_bundle_header = f"# Agent knowledge bundle — {label}"
    leading_text = bundle_text.lstrip()
    if not leading_text.startswith(expected_bundle_header):
        reasons.append(
            f"bundle header does not start with selected manifest label header {expected_bundle_header!r}"
        )

    if bundle_path.parent.resolve() != build_manifest_path.parent.resolve():
        reasons.append("bundle and build_manifest.json are not in the same corpus directory")

    return ArchitectCheckResult(ok=not reasons, reasons=reasons)


def validate_snapshot_freshness(snapshot_path: Path, build_manifest_path: Path) -> ArchitectCheckResult:
    reasons: list[str] = []
    build_doc = _load_json(build_manifest_path)
    build_generated_raw = str(build_doc.get("generated") or "").strip()
    snapshot_generated = _snapshot_generated_date(snapshot_path)
    if build_generated_raw and snapshot_generated:
        try:
            build_generated = date.fromisoformat(build_generated_raw)
        except ValueError:
            return ArchitectCheckResult(
                ok=False,
                reasons=[f"freshness metadata unavailable: invalid build_manifest generated value {build_generated_raw!r}"],
            )
        if snapshot_generated < build_generated:
            reasons.append(
                "required product snapshot generated date is older than the selected KB build record and must be refreshed"
            )
        return ArchitectCheckResult(ok=not reasons, reasons=reasons)

    try:
        snapshot_stat = snapshot_path.stat()
        build_stat = build_manifest_path.stat()
    except OSError as exc:
        return ArchitectCheckResult(ok=False, reasons=[f"freshness metadata unavailable: {exc}"])

    snapshot_mtime = getattr(snapshot_stat, "st_mtime_ns", 0)
    build_mtime = getattr(build_stat, "st_mtime_ns", 0)
    if snapshot_mtime <= 0 or build_mtime <= 0:
        reasons.append("freshness metadata unavailable")
    elif snapshot_mtime < build_mtime:
        reasons.append(
            "required product snapshot is older than the selected KB build manifest and must be refreshed"
        )

    return ArchitectCheckResult(ok=not reasons, reasons=reasons)


def _required_template_headings(template_text: str) -> list[str]:
    headings: list[str] = []
    for line in template_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            headings.append(stripped)
    return headings


def _required_metadata_labels() -> tuple[str, ...]:
    return (
        "**Current state:**",
        "**Intent:**",
        "**Desired outcome:**",
    )


def _validate_plan_output_conformance(
    output_path: Path,
    template_path: Path,
    *,
    expected_heading_prefix: str,
    min_length: int,
    empty_reason: str,
    short_reason: str,
    heading_reason: str,
    placeholders: tuple[str, ...],
) -> ArchitectCheckResult:
    reasons: list[str] = []
    text = output_path.read_text(encoding="utf-8", errors="replace")
    template_text = template_path.read_text(encoding="utf-8", errors="replace")

    if not text.strip():
        reasons.append(empty_reason)
        return ArchitectCheckResult(ok=False, reasons=reasons)

    if len(text.strip()) < min_length:
        reasons.append(short_reason)

    first_nonempty = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if not first_nonempty.lower().startswith(expected_heading_prefix.lower()):
        reasons.append(heading_reason)

    for placeholder in placeholders:
        if placeholder in text:
            reasons.append(f"output still contains unresolved template placeholder {placeholder!r}")

    for label in _required_metadata_labels():
        if label not in text:
            reasons.append(f"output missing required planning metadata field {label!r}")

    required_headings = _required_template_headings(template_text)
    cursor = 0
    for heading in required_headings:
        idx = text.find(heading, cursor)
        if idx == -1:
            reasons.append(f"architect output missing required heading {heading!r}")
            continue
        cursor = idx + len(heading)

    return ArchitectCheckResult(ok=not reasons, reasons=reasons)


def validate_architect_output_conformance(output_path: Path, template_path: Path) -> ArchitectCheckResult:
    return _validate_plan_output_conformance(
        output_path,
        template_path,
        expected_heading_prefix="# architect plan",
        min_length=400,
        empty_reason="architect output is empty",
        short_reason="architect output is too short to satisfy the architect-plan contract",
        heading_reason="architect output does not begin with the expected architect-plan heading",
        placeholders=(
            "YYYY-MM-DD",
            "<document_id>",
            "reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml",
            "_name / role_",
            "_3–6 sentences",
            "_JSON Schema fragments",
            "_Table:",
            "| | | |",
            "<summarize the actual current state for this lane>",
            "<state why this planning lane exists and what it is trying to resolve>",
            "<state the successful review/ratification/integration outcome for this lane>",
        ),
    )


def validate_ui_output_conformance(output_path: Path, template_path: Path) -> ArchitectCheckResult:
    return _validate_plan_output_conformance(
        output_path,
        template_path,
        expected_heading_prefix="# ui plan",
        min_length=250,
        empty_reason="ui output is empty",
        short_reason="ui output is too short to satisfy the ui-plan contract",
        heading_reason="ui output does not begin with the expected ui-plan heading",
        placeholders=(
            "YYYY-MM-DD",
            "`<document_id>`",
            "| | | |",
            "| | |",
            "Summarize the intended user-facing posture",
            "State what the user must be able to see",
            "Describe what is owned by the shell",
            "<summarize the actual current UI or shell-review posture for this lane>",
            "<state why this UI planning lane exists and what it is trying to resolve>",
            "<state the successful review/ratification/integration outcome for this lane>",
        ),
    )

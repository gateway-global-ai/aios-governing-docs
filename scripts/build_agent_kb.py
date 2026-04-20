#!/usr/bin/env python3
"""
Build a declared knowledge bundle for local planning and review lanes.

Usage (repo root):
  py -3 scripts/build_agent_kb.py
  py -3 scripts/build_agent_kb.py --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml
"""

from __future__ import annotations

import argparse
import json
from datetime import UTC, date, datetime
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
DEFAULT_MANIFEST = BASE_DIR / "reference" / "knowledge_base" / "agents" / "agent_kb_manifest.yaml"
OUT_BUNDLE = BASE_DIR / "reference" / "knowledge_base" / "agents" / "corpus" / "government_and_reports_bundle.md"
OUT_MANIFEST = BASE_DIR / "reference" / "knowledge_base" / "agents" / "corpus" / "build_manifest.json"


def _repo_rel(path: Path) -> str:
    return path.resolve().relative_to(BASE_DIR.resolve()).as_posix()


def _resolve_output_dir(path: Path | None) -> Path:
    candidate = OUT_BUNDLE.parent if path is None else path
    if not candidate.is_absolute():
        candidate = (BASE_DIR / candidate).resolve()
    else:
        candidate = candidate.resolve()
    try:
        candidate.relative_to(BASE_DIR.resolve())
    except ValueError as exc:
        raise ValueError(f"Output directory is outside repo root: {path}") from exc
    return candidate


def _collect_declared_paths(manifest: dict) -> list[str]:
    ordered: list[str] = []
    for key in ("governing_documents", "reports_and_snapshots"):
        for raw in manifest.get(key) or []:
            normalized = str(raw).replace("\\", "/").lstrip("/")
            if normalized and normalized not in ordered:
                ordered.append(normalized)
    return ordered


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Ollama agent knowledge bundle")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="YAML manifest path")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory for generated government_and_reports_bundle.md and build_manifest.json",
    )
    args = parser.parse_args()

    if not args.manifest.is_file():
        print(f"Error: manifest not found: {args.manifest}")
        raise SystemExit(1)
    output_dir = _resolve_output_dir(args.output_dir)
    out_bundle = output_dir / "government_and_reports_bundle.md"
    out_manifest = output_dir / "build_manifest.json"
    generated_at = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    raw = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    label = str(raw.get("label") or "default").strip()
    packet_id = str(raw.get("packet_id") or "").strip()
    role = str(raw.get("role") or "").strip()
    description = str(raw.get("description") or "").strip()
    manifest_rel = _repo_rel(args.manifest.resolve())
    declared_paths = _collect_declared_paths(raw)
    parts: list[str] = [
        f"# Agent knowledge bundle — {label}",
        "",
        f"**Generated:** {date.today().isoformat()}",
        f"**Manifest:** `{manifest_rel}`",
        f"**Packet ID:** `{packet_id or 'unspecified'}`",
        f"**Role:** `{role or 'unspecified'}`",
        "",
        description,
        "",
        "---",
        "",
    ]

    manifest_log: dict = {
        "label": label,
        "packet_id": packet_id,
        "role": role,
        "generated": date.today().isoformat(),
        "generated_at": generated_at,
        "manifest_path": manifest_rel,
        "bundle_path": _repo_rel(out_bundle),
        "corpus_directory": _repo_rel(output_dir),
        "review_intents": raw.get("review_intents") or [],
        "files": [],
    }

    missing: list[str] = []
    for rel_norm in declared_paths:
        path = (BASE_DIR / rel_norm).resolve()
        try:
            path.relative_to(BASE_DIR.resolve())
        except ValueError:
            missing.append(rel_norm)
            continue
        if not path.is_file():
            missing.append(rel_norm)
            parts.append(f"## MISSING FILE: `{rel_norm}`\n\n*(Skipped)*\n\n---\n\n")
            manifest_log["files"].append({"path": rel_norm, "status": "missing"})
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        parts.append(f"## Source: `{rel_norm}`\n\n")
        parts.append(text)
        parts.append("\n\n---\n\n")
        manifest_log["files"].append({"path": rel_norm, "status": "ok", "bytes": len(text.encode("utf-8"))})

    if missing:
        print(f"Warning: {len(missing)} path(s) missing or outside repo:", ", ".join(missing[:10]))
        if len(missing) > 10:
            print("...")

    output_dir.mkdir(parents=True, exist_ok=True)
    bundle_text = "".join(parts)
    out_bundle.write_text(bundle_text, encoding="utf-8")
    out_manifest.write_text(json.dumps(manifest_log, indent=2), encoding="utf-8")

    print(f"Wrote {out_bundle.relative_to(BASE_DIR)} ({len(bundle_text):,} chars)")
    print(f"Wrote {out_manifest.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()

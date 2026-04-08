#!/usr/bin/env python3
"""
Concatenate ratified/normative governing documents + knowledge-base reports into one
markdown bundle for local Ollama planning agents (Architect / UI).

Usage (repo root):
  py -3 scripts/build_agent_kb.py
  py -3 scripts/build_agent_kb.py --manifest reference/knowledge_base/agents/agent_kb_manifest.yaml
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
DEFAULT_MANIFEST = BASE_DIR / "reference" / "knowledge_base" / "agents" / "agent_kb_manifest.yaml"
OUT_BUNDLE = BASE_DIR / "reference" / "knowledge_base" / "agents" / "corpus" / "government_and_reports_bundle.md"
OUT_MANIFEST = BASE_DIR / "reference" / "knowledge_base" / "agents" / "corpus" / "build_manifest.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Ollama agent knowledge bundle")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="YAML manifest path")
    args = parser.parse_args()

    if not args.manifest.is_file():
        print(f"Error: manifest not found: {args.manifest}")
        raise SystemExit(1)

    raw = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    label = raw.get("label", "default")
    parts: list[str] = [
        f"# Agent knowledge bundle — {label}",
        "",
        f"**Generated:** {date.today().isoformat()}",
        "",
        "---",
        "",
    ]

    manifest_log: dict = {"label": label, "generated": date.today().isoformat(), "files": []}

    all_paths: list[str] = []
    for key in ("governing_documents", "reports_and_snapshots"):
        for p in raw.get(key) or []:
            all_paths.append(p)

    missing: list[str] = []
    for rel in all_paths:
        rel_norm = rel.replace("\\", "/").lstrip("/")
        path = (BASE_DIR / rel_norm).resolve()
        try:
            rel_pos = path.relative_to(BASE_DIR.resolve())
        except ValueError:
            missing.append(rel)
            continue
        if not path.is_file():
            missing.append(rel)
            parts.append(f"## MISSING FILE: `{rel}`\n\n*(Skipped)*\n\n---\n\n")
            manifest_log["files"].append({"path": rel, "status": "missing"})
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        parts.append(f"## Source: `{rel}`\n\n")
        parts.append(text)
        parts.append("\n\n---\n\n")
        manifest_log["files"].append({"path": rel, "status": "ok", "bytes": len(text.encode("utf-8"))})

    if missing:
        print(f"Warning: {len(missing)} path(s) missing or outside repo:", ", ".join(missing[:10]))
        if len(missing) > 10:
            print("...")

    OUT_BUNDLE.parent.mkdir(parents=True, exist_ok=True)
    bundle_text = "".join(parts)
    OUT_BUNDLE.write_text(bundle_text, encoding="utf-8")
    OUT_MANIFEST.write_text(json.dumps(manifest_log, indent=2), encoding="utf-8")

    print(f"Wrote {OUT_BUNDLE.relative_to(BASE_DIR)} ({len(bundle_text):,} chars)")
    print(f"Wrote {OUT_MANIFEST.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()

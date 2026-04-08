#!/usr/bin/env python3
"""
Build reference/knowledge_base/snapshots/product_context_bundle.md from the
ai-os-voice-interface repo (schemas, workspace intents, MCP map, control plane).

Used by peer_review.py when --product-context is passed (see prompts/peer_review_prompt.md).

Usage (from governing_docs repo root):
  py -3 scripts/generate_product_context_bundle.py
  py -3 scripts/generate_product_context_bundle.py --voice-root C:/Apps/ai-os-voice-interface

Env:
  AIOS_VOICE_INTERFACE_ROOT — default voice repo path if --voice-root omitted.
"""

from __future__ import annotations

import argparse
import os
from datetime import date
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
MANIFEST_PATH = BASE_DIR / "reference" / "knowledge_base" / "ai_os_voice_bundle_manifest.yaml"
DEFAULT_OUT = BASE_DIR / "reference" / "knowledge_base" / "snapshots" / "product_context_bundle.md"


def resolve_voice_root(explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit.expanduser().resolve()
    env = os.environ.get("AIOS_VOICE_INTERFACE_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    candidates = [
        Path(r"C:\Apps\ai-os-voice-interface"),
        BASE_DIR.parent.parent / "ai-os-voice-interface",
        BASE_DIR.parent / "ai-os-voice-interface",
    ]
    for c in candidates:
        if c.exists():
            return c.resolve()
    return Path(r"C:\Apps\ai-os-voice-interface")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate product_context_bundle.md for peer review")
    parser.add_argument(
        "--voice-root",
        type=Path,
        default=None,
        help="Path to ai-os-voice-interface (default: AIOS_VOICE_INTERFACE_ROOT or common paths)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="Output markdown path",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=MANIFEST_PATH,
        help="YAML manifest of relative file paths",
    )
    args = parser.parse_args()

    voice = resolve_voice_root(args.voice_root)
    if not voice.is_dir():
        print(f"Error: voice repo not found: {voice}")
        print("Set AIOS_VOICE_INTERFACE_ROOT or pass --voice-root.")
        raise SystemExit(1)

    if not args.manifest.exists():
        print(f"Error: manifest not found: {args.manifest}")
        raise SystemExit(1)

    data = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    label = data.get("voice_repo_label", "ai-os-voice-interface")
    include = data.get("include") or []

    parts: list[str] = [
        f"# Product implementation snapshot — {label}",
        "",
        f"**Generated:** {date.today().isoformat()}",
        f"**Source root:** `{voice}`",
        "",
        "This file is **informative** for **peer review** of Workspace / integration **AMD** and **SPEC** text. "
        "It concatenates **current** TypeScript sources so reviewers can align governance claims with **implemented** "
        "intents, scope classes, and MCP mapping. Regenerate before binding review rounds when the product repo changes.",
        "",
        "---",
        "",
    ]

    missing: list[str] = []
    for rel in include:
        p = voice / rel.replace("/", os.sep)
        if not p.is_file():
            missing.append(rel)
            parts.append(f"## MISSING: `{rel}`")
            parts.append("")
            parts.append(f"*(File not found at `{p}`)*")
            parts.append("")
            parts.append("---")
            parts.append("")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        parts.append(f"## File: `{rel}`")
        parts.append("")
        parts.append("```")
        parts.append(text)
        parts.append("```")
        parts.append("")
        parts.append("---")
        parts.append("")

    if missing:
        print(f"Warning: {len(missing)} path(s) missing from voice repo:", ", ".join(missing))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {args.out.relative_to(BASE_DIR)} ({args.out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

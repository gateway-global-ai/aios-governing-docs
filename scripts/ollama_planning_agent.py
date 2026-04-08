#!/usr/bin/env python3
"""
Run local Ollama planning agents for amendment pre-ratification (Architect → UI).

Prerequisites:
  py -3 scripts/build_agent_kb.py
  py -3 scripts/generate_product_context_bundle.py   # if product snapshot is stale
  Ollama running (default http://127.0.0.1:11434)

Usage (repo root):
  py -3 scripts/ollama_planning_agent.py --role architect --amd-slug amd_2026_006
  py -3 scripts/ollama_planning_agent.py --role ui --amd-slug amd_2026_006
  # UI refuses to run until ARCHITECT_PLAN.md exists; use --force only in emergencies.

Env:
  OLLAMA_HOST   — default http://127.0.0.1:11434
  OLLAMA_MODEL  — default llama3.2
"""

from __future__ import annotations

import argparse
import os
from datetime import date
from pathlib import Path

import httpx

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent

DEFAULT_BUNDLE = (
    BASE_DIR / "reference/knowledge_base/agents/corpus/government_and_reports_bundle.md"
)


def read_text(path: Path) -> str:
    if not path.is_file():
        return f"[MISSING: {path}]"
    return path.read_text(encoding="utf-8", errors="replace")


def ollama_chat(host: str, model: str, system: str, user: str, timeout: float = 600.0) -> str:
    url = f"{host.rstrip('/')}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
    }
    with httpx.Client(timeout=timeout) as client:
        r = client.post(url, json=payload)
        r.raise_for_status()
        data = r.json()
    msg = data.get("message") or {}
    return msg.get("content") or data.get("response") or str(data)


def planning_paths(amd_slug: str) -> tuple[Path, Path, Path, Path]:
    base = BASE_DIR / "reviews" / amd_slug / "planning"
    return (
        base / "ARCHITECT_PLAN_TEMPLATE.md",
        base / "UI_PLAN_TEMPLATE.md",
        base / "ARCHITECT_PLAN.md",
        base / "UI_PLAN.md",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Ollama Architect / UI planning agents")
    parser.add_argument("--role", choices=["architect", "ui"], required=True)
    parser.add_argument("--amd-slug", default="amd_2026_006", help="reviews/<slug>/planning/")
    parser.add_argument(
        "--bundle",
        type=Path,
        default=DEFAULT_BUNDLE,
        help="KB bundle from build_agent_kb.py",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print sizes only; do not call Ollama")
    parser.add_argument(
        "--force",
        action="store_true",
        help="UI role only: run without ARCHITECT_PLAN.md (not recommended)",
    )
    args = parser.parse_args()

    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")

    tpl_arch, tpl_ui, out_arch, out_ui = planning_paths(args.amd_slug)

    kb = read_text(args.bundle)
    if args.bundle.is_file() and not kb.startswith("[MISSING"):
        print(f"KB bundle: {args.bundle.relative_to(BASE_DIR)} ({len(kb):,} chars)")
    else:
        print(f"ERROR: Run `py -3 scripts/build_agent_kb.py` first. Missing: {args.bundle}")
        raise SystemExit(1)

    if args.role == "architect":
        system = read_text(BASE_DIR / "prompts/ollama_architect_agent.md")
        template = read_text(tpl_arch)
        user = (
            "## Knowledge bundle (governing docs + reports)\n\n"
            + kb
            + "\n\n## Template to complete\n\n"
            + template
            + "\n\nProduce a complete `ARCHITECT_PLAN.md` body following the template. "
            "Use today's date where YYYY-MM-DD appears."
        )
        out = out_arch
    else:
        arch = read_text(out_arch)
        if (arch.startswith("[MISSING") or not out_arch.is_file()) and not args.force:
            print(f"ERROR: Architect output missing. Run --role architect first: {out_arch}")
            print("       Or pass --force only if you intentionally skip the architect step.")
            raise SystemExit(2)
        if args.force and (not out_arch.is_file() or arch.startswith("[MISSING")):
            arch = (
                "*No architect plan was provided (`--force`). Complete the UI plan from the "
                "knowledge bundle and template only; flag all assumptions.*\n"
            )
        system = read_text(BASE_DIR / "prompts/ollama_ui_agent.md")
        template = read_text(tpl_ui)
        user = (
            "## Knowledge bundle\n\n"
            + kb
            + "\n\n## Architect plan (complete this UI plan consistently)\n\n"
            + arch
            + "\n\n## Template to complete\n\n"
            + template
            + "\n\nProduce a complete `UI_PLAN.md` body following the template.\n\n"
            f"**Today's date (use exactly):** {date.today().isoformat()}\n\n"
            "**Constraints:** Output **only** markdown for the plan — no \"I can help\", no "
            "\"Here is a complete\", no assistant preamble or closing disclaimer. "
            "**First character** of your output must be `#` (the title heading). "
            "Do not use placeholder person names "
            "(e.g. John Doe); use `TBD` or `unknown — reason` if a verifier is unknown.\n"
            "**Depends on:** link `./ARCHITECT_PLAN.md` (same directory) — no example.com or "
            "external placeholder URLs. End at the **last** `- [ ]` checklist line — **no** text, "
            "headings, or \"verify your work\" lines after that."
        )
        out = out_ui

    print(f"Role: {args.role} | Model: {model} | Ollama: {host}")
    print(f"System prompt chars: {len(system):,} | User prompt chars: {len(user):,}")

    if args.dry_run:
        print("Dry run: not calling Ollama.")
        return

    text = ollama_chat(host, model, system, user)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text.strip() + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()

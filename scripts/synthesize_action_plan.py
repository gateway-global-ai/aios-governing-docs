"""
Merge impact_report_*.md files into a single action_plan.json using one LLM call.

Usage:
    py synthesize_action_plan.py AMD-2026-a10b9a
    py synthesize_action_plan.py AMD-2026-a10b9a --model gemini
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from context_assembler import (
    BASE_DIR,
    read_file,
    read_document_registry,
    read_introduction,
    call_deepseek,
    call_gemini,
)

PROMPT_PATH = BASE_DIR / "prompts" / "action_plan_synthesis_prompt.md"
MAX_EXCERPT = 120_000  # per report — trim if huge


def _trim(s: str, max_len: int) -> str:
    if len(s) <= max_len:
        return s
    return s[: max_len // 2] + "\n\n[... truncated ...]\n\n" + s[-max_len // 2 :]


def _load_reports(source_dir: Path) -> dict[str, str]:
    out = {}
    for name in ("deepseek", "openai", "gemini"):
        p = source_dir / f"impact_report_{name}.md"
        if not p.exists():
            raise FileNotFoundError(f"Missing {p.name}")
        out[name] = read_file(p)
    return out


def _extract_json_object(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            pass
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        return json.loads(text[start : end + 1])
    raise ValueError("Could not parse JSON from model response")


async def synthesize(source_name: str, model: str = "deepseek") -> dict:
    source_dir = BASE_DIR / "sources" / source_name
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Source folder not found: {source_dir}")

    reports = _load_reports(source_dir)
    source_md = source_dir / "source.md"
    source_excerpt = _trim(read_file(source_md), 8000) if source_md.exists() else ""

    reg = read_document_registry()
    reg_excerpt = _trim(reg, 25_000)
    intro = _trim(read_introduction(), 4000)

    template = read_file(PROMPT_PATH)
    user_block = template.replace("{{SOURCE_NAME}}", source_name)
    user_block = user_block.replace("{{SOURCE_EXCERPT}}", source_excerpt or "(no source.md)")
    user_block = user_block.replace("{{REPORT_DEEPSEEK}}", _trim(reports["deepseek"], MAX_EXCERPT))
    user_block = user_block.replace("{{REPORT_OPENAI}}", _trim(reports["openai"], MAX_EXCERPT))
    user_block = user_block.replace("{{REPORT_GEMINI}}", _trim(reports["gemini"], MAX_EXCERPT))
    user_block = user_block.replace(
        "{{DOCUMENT_REGISTRY_EXCERPT}}",
        f"## introduction.md (excerpt)\n{intro}\n\n## DOCUMENT_REGISTRY\n{reg_excerpt}",
    )

    system = (
        "You output only valid JSON. No markdown, no commentary outside the JSON object. "
        "Follow the schema in the user message exactly."
    )

    if model == "gemini":
        raw = await call_gemini(system, user_block, model="gemini-2.5-pro")
    else:
        raw = await call_deepseek(system, user_block, model="deepseek-chat")

    data = _extract_json_object(raw)
    data["version"] = 1
    data["source_name"] = source_name
    data["synthesized_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    data["synthesis_model"] = model

    for a in data.get("actions", []):
        if "status" not in a:
            a["status"] = "proposed"

    return data


def main():
    parser = argparse.ArgumentParser(description="Synthesize action_plan.json from impact reports")
    parser.add_argument("source_name", help="Folder name under sources/, e.g. AMD-2026-a10b9a")
    parser.add_argument("--model", choices=("deepseek", "gemini"), default="deepseek")
    args = parser.parse_args()

    try:
        plan = asyncio.run(synthesize(args.source_name, args.model))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    out_path = BASE_DIR / "sources" / args.source_name / "action_plan.json"
    out_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"  actions: {len(plan.get('actions', []))}")


if __name__ == "__main__":
    main()

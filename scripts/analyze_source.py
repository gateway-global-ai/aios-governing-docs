"""
Source material analysis pipeline with quarantine support.
Analyzes external articles/research against the AIOS governance framework.
Produces impact reports and draft amendments.

Sources are quarantined on submission and require human clearance before
amendments can proceed to the lifecycle.

Usage:
    python analyze_source.py sources/token_trap/source.md --name token_trap
    python analyze_source.py path/to/article.md --name market_analysis
    python analyze_source.py --clear token_trap
    python analyze_source.py --reject token_trap
    python analyze_source.py --status token_trap
"""

import argparse
import asyncio
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

from context_assembler import (
    BASE_DIR, read_file, read_core_docs, read_style_guide, read_grading_rubric,
    read_document_registry, read_prompt_template, assemble_prompt,
    call_models_parallel, today,
)
from llm_pricing import format_source_analysis_three_way_note

QUARANTINE_FILE = "quarantine.json"


def _quarantine_path(name: str) -> Path:
    return BASE_DIR / "sources" / name / QUARANTINE_FILE


def _read_quarantine(name: str) -> dict | None:
    path = _quarantine_path(name)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None


def _write_quarantine(name: str, data: dict):
    path = _quarantine_path(name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _create_quarantine(name: str, source_content: str) -> dict:
    source_hash = hashlib.sha256(source_content.encode("utf-8")).hexdigest()[:16]
    data = {
        "status": "quarantined",
        "submitted": datetime.now().isoformat(),
        "source_hash": source_hash,
        "cleared_by": None,
        "cleared_at": None,
    }
    _write_quarantine(name, data)
    return data


def _update_quarantine_status(name: str, status: str):
    data = _read_quarantine(name)
    if not data:
        print(f"Error: No quarantine record found for '{name}'")
        sys.exit(1)
    data["status"] = status
    if status in ("cleared", "rejected"):
        data["cleared_at"] = datetime.now().isoformat()
        data["cleared_by"] = "human"
    _write_quarantine(name, data)
    print(f"  Source '{name}' status updated to: {status}")


async def run_analysis(source_path: str, name: str):
    print(f"\n{'='*60}")
    print(f"AIOS Source Material Analysis")
    print(f"Source: {source_path}")
    print(f"Name: {name}")
    print(f"{'='*60}\n")

    source_full = Path(source_path)
    if not source_full.is_absolute():
        source_full = BASE_DIR / source_path

    if not source_full.exists():
        print(f"Error: Source file not found: {source_path}")
        sys.exit(1)

    source_content = read_file(source_full)

    source_dir = BASE_DIR / "sources" / name
    source_dir.mkdir(parents=True, exist_ok=True)

    source_copy = source_dir / "source.md"
    if not source_copy.exists():
        source_copy.write_text(source_content, encoding="utf-8")
        print(f"Source preserved: sources/{name}/source.md")

    quarantine = _create_quarantine(name, source_content)
    print(f"Source quarantined: {quarantine['source_hash']}")

    template = read_prompt_template("source_analysis_prompt.md")
    core = read_core_docs()

    replacements = {
        "TECHNICAL_MANIFESTO": core["technical_manifesto"],
        "GOVERNANCE_CONSTITUTION": core["governance_constitution"],
        "MPOA": core["mpoa"],
        "STYLE_GUIDE": read_style_guide(),
        "GRADING_RUBRIC": read_grading_rubric(),
        "DOCUMENT_REGISTRY": read_document_registry(),
        "SOURCE_MATERIAL": source_content,
    }

    assembled = assemble_prompt(template, replacements)

    system_part = assembled.split("## Source Material to Analyze")[0]
    user_part = "## Source Material to Analyze\n\n" + assembled.split("## Source Material to Analyze")[1]

    print("Sending to all 3 models in parallel...")
    models = ["deepseek", "openai", "gemini"]
    results = await call_models_parallel(models, system_part, user_part)

    for model_name, content in results.items():
        if content.startswith("[ERROR"):
            print(f"  [{model_name}] {content}")
        else:
            print(f"  [{model_name}] Analysis received ({len(content)} chars)")
            out_path = source_dir / f"impact_report_{model_name}.md"
            out_path.write_text(content, encoding="utf-8")
            print(f"  Saved: sources/{name}/impact_report_{model_name}.md")

    _update_quarantine_status(name, "analyzed")
    print(f"\nAnalysis complete. Source status: analyzed (awaiting human clearance).")
    print(f"To clear:  python analyze_source.py --clear {name}")
    print(f"To reject: python analyze_source.py --reject {name}")
    print()
    print(format_source_analysis_three_way_note())


def main():
    parser = argparse.ArgumentParser(description="AIOS Source Material Analysis")
    parser.add_argument("source", nargs="?", help="Path to source material (.md file)")
    parser.add_argument("--name", help="Name for the source (used as folder name)")
    parser.add_argument("--clear", metavar="NAME", help="Clear a quarantined source for use")
    parser.add_argument("--reject", metavar="NAME", help="Reject a quarantined source")
    parser.add_argument("--status", metavar="NAME", help="Check quarantine status of a source")
    args = parser.parse_args()

    if args.clear:
        _update_quarantine_status(args.clear, "cleared")
    elif args.reject:
        _update_quarantine_status(args.reject, "rejected")
    elif args.status:
        data = _read_quarantine(args.status)
        if data:
            print(json.dumps(data, indent=2))
        else:
            print(f"No quarantine record found for '{args.status}'")
    else:
        if not args.source or not args.name:
            print("Error: Provide a source path and --name, or use --clear/--reject/--status")
            sys.exit(1)
        asyncio.run(run_analysis(args.source, args.name))


if __name__ == "__main__":
    main()

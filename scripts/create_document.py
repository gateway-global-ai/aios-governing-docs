"""
Context-aware document generator.
Creates new governing documents with full context injection.

Usage:
    python create_document.py --title "Security & Sandboxing Model" --category specification --description "Deep dive on tenant isolation, cryptographic attestations, and supply chain security."
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path

from context_assembler import (
    BASE_DIR, read_core_docs, read_style_guide, read_document_template,
    read_introduction, read_prompt_template, read_existing_specs,
    assemble_prompt, call_deepseek, today,
)

CATEGORY_DIRS = {
    "core": "core",
    "specification": "specifications",
    "commercial": "commercial",
    "amendment": "amendments",
    "article": "articles",
}


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return slug


async def run_creation(title: str, category: str, description: str, audience: str = ""):
    print(f"\n{'='*60}")
    print(f"AIOS Document Creation")
    print(f"Title: {title}")
    print(f"Category: {category}")
    print(f"{'='*60}\n")

    template = read_prompt_template("document_creation_prompt.md")
    core = read_core_docs()

    doc_spec = f"""
**Title:** {title}
**Category:** {category}
**Target Audience:** {audience or 'See introduction.md for audience guidance'}
**Description/Requirements:** {description}
**Date:** {today()}
"""

    replacements = {
        "DOCUMENT_SPEC": doc_spec,
        "TECHNICAL_MANIFESTO": core["technical_manifesto"],
        "GOVERNANCE_CONSTITUTION": core["governance_constitution"],
        "MPOA": core["mpoa"],
        "INTRODUCTION": read_introduction(),
        "STYLE_GUIDE": read_style_guide(),
        "DOCUMENT_TEMPLATE": read_document_template(),
        "EXISTING_SPECS": read_existing_specs(),
    }

    assembled = assemble_prompt(template, replacements)

    system_part = assembled.split("## Output Requirements")[0]
    user_part = "## Output Requirements" + assembled.split("## Output Requirements")[1]

    print("Sending to DeepSeek for document creation...")
    response = await call_deepseek(system_part, user_part)
    print(f"Document received ({len(response)} chars)")

    category_dir = CATEGORY_DIRS.get(category, "specifications")
    out_dir = BASE_DIR / category_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = slugify(title) + ".md"
    out_path = out_dir / filename
    out_path.write_text(response, encoding="utf-8")
    print(f"Document saved: {out_path.relative_to(BASE_DIR)}")

    print("\nDocument creation complete. Run peer_review.py --round 1 to begin review.")


def main():
    parser = argparse.ArgumentParser(description="AIOS Document Creation Engine")
    parser.add_argument("--title", required=True, help="Document title")
    parser.add_argument("--category", required=True, choices=list(CATEGORY_DIRS.keys()), help="Document category")
    parser.add_argument("--description", required=True, help="Description and specific requirements")
    parser.add_argument("--audience", default="", help="Target audience")
    args = parser.parse_args()

    asyncio.run(run_creation(args.title, args.category, args.description, args.audience))


if __name__ == "__main__":
    main()

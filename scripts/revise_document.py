"""
Review-driven document revision engine.
Reads Round 1 reviews and sends the original document + reviews to DeepSeek for revision.

Usage:
    python revise_document.py core/technical_manifesto.md
"""

import argparse
import asyncio
import sys
from pathlib import Path

from context_assembler import (
    BASE_DIR, read_file, read_core_docs, read_style_guide,
    read_prompt_template, assemble_prompt, find_reviews,
    call_deepseek, get_doc_slug, today,
)


async def run_revision(doc_path: str):
    print(f"\n{'='*60}")
    print(f"AIOS Document Revision")
    print(f"Document: {doc_path}")
    print(f"{'='*60}\n")

    r1_reviews = find_reviews(doc_path, review_round=1)
    if not r1_reviews:
        print("Error: No Round 1 reviews found. Run peer_review.py --round 1 first.")
        sys.exit(1)

    print(f"Found {len(r1_reviews)} Round 1 review(s)")

    template = read_prompt_template("revision_prompt.md")
    core = read_core_docs()

    review_sections = ""
    for i, review in enumerate(r1_reviews, 1):
        review_sections += f"\n### Review {i}\n\n{review}\n"

    replacements = {
        "TECHNICAL_MANIFESTO": core["technical_manifesto"],
        "GOVERNANCE_CONSTITUTION": core["governance_constitution"],
        "MPOA": core["mpoa"],
        "STYLE_GUIDE": read_style_guide(),
        "TARGET_DOCUMENT": read_file(BASE_DIR / doc_path),
        "REVIEW_1": r1_reviews[0] if len(r1_reviews) > 0 else "[No review]",
        "REVIEW_2": r1_reviews[1] if len(r1_reviews) > 1 else "[No second review]",
    }

    assembled = assemble_prompt(template, replacements)

    system_part = assembled.split("## The Original Document")[0]
    user_part = "## The Original Document" + assembled.split("## The Original Document")[1]

    print("Sending to DeepSeek for revision...")
    response = await call_deepseek(system_part, user_part)
    print(f"Revision received ({len(response)} chars)")

    if "===REVISION_LOG_START===" in response:
        parts = response.split("===REVISION_LOG_START===")
        revised_doc = parts[0].strip()
        revision_log = parts[1].strip()
    else:
        revised_doc = response
        revision_log = "# Revision Log\n\n[Revision log was not separated by the model. Manual extraction needed.]"

    doc_full_path = BASE_DIR / doc_path
    doc_full_path.write_text(revised_doc, encoding="utf-8")
    print(f"Revised document saved: {doc_path}")

    slug = get_doc_slug(doc_path)
    log_path = BASE_DIR / "reviews" / slug / "revision_log.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(revision_log, encoding="utf-8")
    print(f"Revision log saved: {log_path.relative_to(BASE_DIR)}")

    print("\nRevision complete. Run peer_review.py --round 2 for the final review.")


def main():
    parser = argparse.ArgumentParser(description="AIOS Document Revision Engine")
    parser.add_argument("document", help="Path to document relative to governing_docs/")
    args = parser.parse_args()

    if not (BASE_DIR / args.document).exists():
        print(f"Error: Document not found: {args.document}")
        sys.exit(1)

    asyncio.run(run_revision(args.document))


if __name__ == "__main__":
    main()

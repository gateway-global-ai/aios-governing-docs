"""
Triangulated peer review engine.
Sends a document to multiple AI models for independent review.

Supports full (11-dimension) or light (5-dimension) rubric.
Supports smart context injection (only cross-referenced docs) or full context (all core docs).

Usage:
    python peer_review.py core/technical_manifesto.md --round 1
    python peer_review.py specifications/NodeContract.md --round 1 --rubric light --smart-context
"""

import argparse
import asyncio
import sys
from pathlib import Path

from context_assembler import (
    BASE_DIR, read_file, read_core_docs, read_relevant_context,
    read_style_guide, read_grading_rubric, read_peer_review_template,
    read_prompt_template, assemble_prompt,
    find_reviews, find_revision_log, call_models_parallel,
    save_review, today, MODEL_CALLERS,
)

ROUND_1_MODELS = ["openai", "gemini"]
ROUND_2_MODELS = ["deepseek", "openai", "gemini"]

REVIEWER_FOCUS = {
    "deepseek": "Your primary focus is TECHNICAL/ARCHITECTURAL RIGOR.",
    "openai": "Your primary focus is EDITORIAL CLARITY and CROSS-DOCUMENT COHERENCE.",
    "gemini": "Your primary focus is LEGAL/COMPLIANCE GAPS.",
}


def _is_core_doc(doc_path: str) -> bool:
    return doc_path.startswith("core/") or doc_path.startswith("core\\")


def build_prompt(
    doc_path: str,
    review_round: int,
    model_name: str,
    rubric: str = "full",
    smart_context: bool = False,
) -> tuple[str, str]:
    """Build the system and user prompts for a peer review."""
    template = read_prompt_template("peer_review_prompt.md")

    if smart_context and not _is_core_doc(doc_path):
        context_docs = read_relevant_context(doc_path)
        context_text = "\n\n---\n\n".join(
            f"### {doc_id}\n\n{content}" for doc_id, content in context_docs.items()
        )
    else:
        core = read_core_docs()
        context_text = (
            f"### Technical Manifesto (the architectural North Star)\n\n{core['technical_manifesto']}\n\n---\n\n"
            f"### Governance Constitution (human oversight and legislative process)\n\n{core['governance_constitution']}\n\n---\n\n"
            f"### Master Platform Operating Agreement (economics, liability, data sovereignty)\n\n{core['mpoa']}"
        )

    prior_reviews_text = ""
    if review_round == 2:
        r1_reviews = find_reviews(doc_path, review_round=1)
        if r1_reviews:
            prior_reviews_text = "\n\n---\n\n".join(r1_reviews)
        else:
            prior_reviews_text = "[No Round 1 reviews found]"

    revision_log = find_revision_log(doc_path) or "[No revision log found]"

    rubric_instruction = ""
    if rubric == "light":
        rubric_instruction = (
            "\n\n**RUBRIC MODE: LIGHT** — Score only the 5 dimensions listed in the rubric below. "
            "Do not score dimensions that are not listed."
        )
    else:
        rubric_instruction = (
            "\n\n**RUBRIC MODE: FULL** — Score all 11 dimensions listed in the rubric below."
        )

    replacements = {
        "REVIEWER_FOCUS": REVIEWER_FOCUS.get(model_name, ""),
        "REVIEW_ROUND": f"This is **Round {review_round}**.{rubric_instruction}",
        "GOVERNING_CONTEXT": context_text,
        "STYLE_GUIDE": read_style_guide(),
        "GRADING_RUBRIC": read_grading_rubric(rubric),
        "PRIOR_REVIEWS": prior_reviews_text,
        "REVISION_LOG": revision_log if review_round == 2 else "[N/A — Round 1]",
        "TARGET_DOCUMENT": read_file(BASE_DIR / doc_path),
        "PEER_REVIEW_TEMPLATE": read_peer_review_template(),
    }

    assembled = assemble_prompt(template, replacements)

    split_marker = "## Document Under Review"
    if split_marker in assembled:
        system_part = assembled.split(split_marker)[0]
        user_part = f"{split_marker}\n\n" + assembled.split(split_marker)[1]
    else:
        system_part = assembled[:len(assembled)//2]
        user_part = assembled[len(assembled)//2:]

    return system_part, user_part


async def run_review(
    doc_path: str,
    review_round: int,
    models_override: list[str] | None = None,
    rubric_override: str | None = None,
    smart_context: bool = False,
):
    rubric = rubric_override or ("full" if _is_core_doc(doc_path) else "full")
    models = models_override or (ROUND_1_MODELS if review_round == 1 else ROUND_2_MODELS)

    print(f"\n{'='*60}")
    print(f"AIOS Peer Review — Round {review_round}")
    print(f"Document: {doc_path}")
    print(f"Models: {', '.join(models)}")
    print(f"Rubric: {rubric}")
    print(f"Context: {'smart (cross-refs only)' if smart_context else 'full (all core docs)'}")
    print(f"{'='*60}\n")

    prompts = {}
    for model in models:
        sys_prompt, user_prompt = build_prompt(
            doc_path, review_round, model,
            rubric=rubric, smart_context=smart_context,
        )
        prompts[model] = (sys_prompt, user_prompt)

    print("Sending to models in parallel...")

    tasks = {}
    for model_name in models:
        sys_p, usr_p = prompts[model_name]
        caller = MODEL_CALLERS[model_name]
        tasks[model_name] = asyncio.create_task(caller(sys_p, usr_p))

    results = {}
    for model_name, task in tasks.items():
        try:
            results[model_name] = await task
            print(f"  [{model_name}] Review received ({len(results[model_name])} chars)")
        except Exception as e:
            results[model_name] = f"[ERROR: {e}]"
            print(f"  [{model_name}] ERROR: {e}")

    print("\nSaving reviews...")
    for model_name, content in results.items():
        out_path = save_review(doc_path, review_round, model_name, content)
        print(f"  Saved: {out_path.relative_to(BASE_DIR)}")

    print(f"\nRound {review_round} review complete.")


def main():
    parser = argparse.ArgumentParser(description="AIOS Peer Review Engine")
    parser.add_argument("document", help="Path to document relative to governing_docs/")
    parser.add_argument("--round", type=int, choices=[1, 2], required=True, help="Review round")
    parser.add_argument("--rubric", choices=["full", "light"], default=None,
                        help="Rubric variant (default: full for core, full for others)")
    parser.add_argument("--smart-context", action="store_true",
                        help="Inject only cross-referenced docs instead of all core docs")
    args = parser.parse_args()

    if not (BASE_DIR / args.document).exists():
        print(f"Error: Document not found: {args.document}")
        sys.exit(1)

    asyncio.run(run_review(
        args.document, args.round,
        rubric_override=args.rubric,
        smart_context=args.smart_context,
    ))


if __name__ == "__main__":
    main()

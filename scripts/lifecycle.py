"""
End-to-end document lifecycle orchestrator.
Chains stages from Draft through Ratification with human approval gates.

Full mode (5 stages):  Draft -> Round 1 Review -> Revision -> Round 2 Review -> Ratification
Quick mode (3 stages): Draft -> Single Review -> Human Ratification

Usage:
    python lifecycle.py core/technical_manifesto.md
    python lifecycle.py core/technical_manifesto.md --auto
    python lifecycle.py core/technical_manifesto.md --quick
    python lifecycle.py --create --title "Security Model" --category specification --description "..."
"""

import argparse
import asyncio
import re
import subprocess
import sys
from pathlib import Path

from context_assembler import BASE_DIR, read_file, parse_front_matter, add_front_matter


def prompt_continue(stage_name: str) -> bool:
    response = input(f"\nProceed to {stage_name}? [Y/n] ").strip().lower()
    return response in ("", "y", "yes")


def prompt_ratify() -> bool:
    print("\n  ┌────────────────────────────────────────────┐")
    print("  │  HUMAN RATIFICATION REQUIRED               │")
    print("  │  Review the document and peer reviews       │")
    print("  │  before approving.                          │")
    print("  └────────────────────────────────────────────┘")
    response = input("\n  Ratify this document? [Y/n] ").strip().lower()
    return response in ("", "y", "yes")


def extract_dispositions(review_content: str) -> str:
    """Extract the disposition from a review."""
    if "**Disposition:**" in review_content:
        match = re.search(
            r"\*\*Disposition:\*\*\s*(approved|approved_with_changes|major_revision_required)",
            review_content, re.IGNORECASE,
        )
        if match:
            return match.group(1).lower()
    if "disposition:" in review_content.lower():
        match = re.search(
            r"disposition:\s*(approved|approved_with_changes|major_revision_required)",
            review_content, re.IGNORECASE,
        )
        if match:
            return match.group(1).lower()
    return "unknown"


def _ratify_document(doc_path: str, metadata: dict, body: str):
    """Update document status to ratified and write to disk."""
    metadata["status"] = "ratified"
    updated = add_front_matter(body, metadata)
    (BASE_DIR / doc_path).write_text(updated, encoding="utf-8")
    print("  Document status updated to 'ratified'.")


def _archive_ratified_version(doc_path: str, metadata: dict):
    """Copy the ratified document to archive/ with version in filename."""
    version = metadata.get("version", "0.0.0")
    slug = re.sub(r"[^a-z0-9]+", "_", Path(doc_path).stem.lower()).strip("_")
    archive_dir = BASE_DIR / "archive" / "ratified"
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_name = f"{slug}_v{version}.md"
    archive_path = archive_dir / archive_name
    import shutil
    shutil.copy2(BASE_DIR / doc_path, archive_path)
    print(f"  Archived ratified version: archive/ratified/{archive_name}")


def _git_tag_ratification(doc_path: str, metadata: dict):
    """Attempt to git commit and tag the ratified document."""
    title = metadata.get("title", Path(doc_path).stem)
    version = metadata.get("version", "0.0.0")
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    tag = f"v{version}-{slug}"
    commit_msg = f"ratify: {title} v{version}"

    try:
        subprocess.run(["git", "add", str(doc_path)], cwd=str(BASE_DIR),
                        check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(BASE_DIR),
                        check=True, capture_output=True)
        subprocess.run(["git", "tag", tag], cwd=str(BASE_DIR),
                        check=True, capture_output=True)
        print(f"  Git: committed and tagged as '{tag}'")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("  Git: skipped (not a git repo or git not available)")


def _handle_ratification(doc_path: str, auto: bool, require_human: bool):
    """Shared ratification logic with human gate."""
    doc_content = read_file(BASE_DIR / doc_path)
    metadata, body = parse_front_matter(doc_content)

    if require_human and not auto:
        if prompt_ratify():
            _ratify_document(doc_path, metadata, body)
            _archive_ratified_version(doc_path, metadata)
            _git_tag_ratification(doc_path, metadata)
        else:
            print("  Ratification declined. Document remains under review.")
    elif auto and not require_human:
        print("  [WARNING] Auto-ratified without human approval (--no-require-human).")
        _ratify_document(doc_path, metadata, body)
        _archive_ratified_version(doc_path, metadata)
        _git_tag_ratification(doc_path, metadata)
    else:
        print("  --auto is set but --require-human is active. Pausing for approval.")
        if prompt_ratify():
            _ratify_document(doc_path, metadata, body)
            _archive_ratified_version(doc_path, metadata)
            _git_tag_ratification(doc_path, metadata)
        else:
            print("  Ratification declined.")


async def run_lifecycle(
    doc_path: str | None,
    create_args: dict | None = None,
    auto: bool = False,
    quick: bool = False,
    require_human: bool = True,
):
    mode = "QUICK (3-stage)" if quick else "FULL (5-stage)"
    print(f"\n{'='*60}")
    print(f"AIOS Document Lifecycle Pipeline — {mode}")
    print(f"{'='*60}\n")

    # --- Stage 1: Draft ---
    if create_args:
        print("STAGE 1: DRAFT (Creating new document)")
        if not auto and not prompt_continue("Stage 1: Draft Creation"):
            print("Aborted.")
            return

        from create_document import run_creation
        await run_creation(**create_args)
        from context_assembler import CATEGORY_DIRS
        category_dir = CATEGORY_DIRS.get(create_args["category"], "specifications")
        slug = re.sub(r"[^a-z0-9]+", "_", create_args["title"].lower()).strip("_")
        doc_path = f"{category_dir}/{slug}.md"
        print(f"\nDraft created: {doc_path}")
    else:
        if not (BASE_DIR / doc_path).exists():
            print(f"Error: Document not found: {doc_path}")
            sys.exit(1)
        print(f"STAGE 1: DRAFT (Using existing document: {doc_path})")

    # --- Stage 2: Review ---
    from peer_review import run_review

    print(f"\n{'='*60}")
    if quick:
        print("STAGE 2: SINGLE REVIEW (DeepSeek, light rubric)")
        if not auto and not prompt_continue("Stage 2: Single Review"):
            print(f"Paused. Run: python peer_review.py {doc_path} --round 1 --rubric light")
            return
        await run_review(doc_path, review_round=1,
                         models_override=["deepseek"], rubric_override="light")
    else:
        print("STAGE 2: ROUND 1 REVIEW (OpenAI + Gemini)")
        if not auto and not prompt_continue("Stage 2: Round 1 Review"):
            print(f"Paused. Run: python peer_review.py {doc_path} --round 1")
            return
        await run_review(doc_path, review_round=1)

    # --- Quick mode: skip to ratification ---
    if quick:
        print(f"\n{'='*60}")
        print("STAGE 3: HUMAN RATIFICATION (quick mode)")
        _handle_ratification(doc_path, auto, require_human)
        print(f"\n{'='*60}")
        print("Lifecycle complete.")
        return

    # --- Full mode: Stages 3-5 ---

    # Stage 3: Revision
    print(f"\n{'='*60}")
    print("STAGE 3: REVISION (DeepSeek)")
    if not auto and not prompt_continue("Stage 3: Revision"):
        print(f"Paused. Run: python revise_document.py {doc_path}")
        return

    from revise_document import run_revision
    await run_revision(doc_path)

    # Stage 4: Round 2 Review
    print(f"\n{'='*60}")
    print("STAGE 4: ROUND 2 REVIEW (All 3 models)")
    if not auto and not prompt_continue("Stage 4: Round 2 Review"):
        print(f"Paused. Run: python peer_review.py {doc_path} --round 2")
        return

    await run_review(doc_path, review_round=2)

    # Stage 5: Ratification Gate
    print(f"\n{'='*60}")
    print("STAGE 5: RATIFICATION GATE")

    from context_assembler import find_reviews
    r2_reviews = find_reviews(doc_path, review_round=2)

    dispositions = []
    for review in r2_reviews:
        d = extract_dispositions(review)
        dispositions.append(d)
        print(f"  Review disposition: {d}")

    approved_count = sum(1 for d in dispositions if d in ("approved", "approved_with_changes"))
    major_revision_count = sum(1 for d in dispositions if d == "major_revision_required")

    if approved_count >= 2:
        print(f"\n  RECOMMENDATION: Ratify — {approved_count}/{len(dispositions)} reviewers approved.")
        _handle_ratification(doc_path, auto, require_human)
    elif major_revision_count >= 2:
        print(f"\n  REVISION REQUIRED: {major_revision_count}/{len(dispositions)} require major revision.")
        print(f"  Return to Stage 3. Run: python lifecycle.py {doc_path}")
    else:
        print(f"\n  INCONCLUSIVE: Dispositions were mixed. Manual review recommended.")
        print(f"  Dispositions: {dispositions}")

    print(f"\n{'='*60}")
    print("Lifecycle complete.")


def main():
    parser = argparse.ArgumentParser(description="AIOS Document Lifecycle Pipeline")
    parser.add_argument("document", nargs="?", help="Path to document relative to governing_docs/")
    parser.add_argument("--create", action="store_true", help="Create a new document first")
    parser.add_argument("--title", help="Title for new document")
    parser.add_argument("--category", help="Category for new document")
    parser.add_argument("--description", help="Description for new document")
    parser.add_argument("--audience", default="", help="Audience for new document")
    parser.add_argument("--auto", action="store_true", help="Skip stage confirmation prompts")
    parser.add_argument("--quick", action="store_true",
                        help="3-stage flow: draft, single review, human ratify")
    parser.add_argument("--no-require-human", dest="require_human", action="store_false",
                        default=True,
                        help="Allow auto-ratification without human approval (use with caution)")
    args = parser.parse_args()

    if args.create:
        if not all([args.title, args.category, args.description]):
            print("Error: --create requires --title, --category, and --description")
            sys.exit(1)
        create_args = {
            "title": args.title,
            "category": args.category,
            "description": args.description,
            "audience": args.audience,
        }
        asyncio.run(run_lifecycle(None, create_args=create_args, auto=args.auto,
                                  quick=args.quick, require_human=args.require_human))
    else:
        if not args.document:
            print("Error: Provide a document path or use --create")
            sys.exit(1)
        asyncio.run(run_lifecycle(args.document, auto=args.auto,
                                  quick=args.quick, require_human=args.require_human))


if __name__ == "__main__":
    main()

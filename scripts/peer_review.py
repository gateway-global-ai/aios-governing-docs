"""
Triangulated peer review engine.
Sends a document to multiple AI models for independent review.

Supports full (11-dimension) or light (5-dimension) rubric.
Supports smart context injection (only cross-referenced docs) or full context (all core docs).

Usage:
    python peer_review.py core/technical_manifesto.md --round 1
    python peer_review.py specifications/NodeContract.md --round 1 --rubric light --smart-context
    python peer_review.py amendments/AMD-2026-006.md --round 1 --smart-context --product-context
      # --product-context loads reference/knowledge_base/snapshots/product_context_bundle.md
      # after: py -3 scripts/generate_product_context_bundle.py

Env (optional): OPENAI_PEER_REVIEW_MODEL (default gpt-5.4), GEMINI_PEER_REVIEW_MODEL,
  DEEPSEEK_PEER_REVIEW_MODEL (default deepseek-chat), CLAUDE_PEER_REVIEW_MODEL
  (default claude-sonnet-4-20250514), MINIMAX_PEER_REVIEW_MODEL
  (default MiniMax-M2.5). Each run writes peer_review_manifest_*.json
  PACKET_IDENTITY.yaml, PACKET_STATUS.yaml, PACKET_EVENTS.yaml, and optional HANDOFF_NOTE.md
  under reviews/<slug>/round_N/. Review files are named
  review_<NNN>_<model>__<DOCUMENT_ID>.md so attachments cannot be confused across amendments.
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from context_assembler import (
    BASE_DIR, read_file, read_core_docs, read_relevant_context,
    read_style_guide, read_grading_rubric, read_peer_review_template,
    read_prompt_template, assemble_prompt,
    find_reviews, find_revision_log, call_models_parallel,
    save_review, today, MODEL_CALLERS,
    resolve_product_implementation_text,
    peer_review_context_bundle_info,
    product_context_bundle_info,
    classify_peer_review_output,
    get_doc_slug,
    read_governing_front_matter_dict,
)
from review_packet_taxonomy import (
    append_packet_events_peer_review,
    ensure_default_handoff_note,
    infer_amd_2026_005_gate_from_round_dir,
    merge_and_write_packet_status,
    write_packet_identity_v2,
)

ROUND_1_MODELS = ["openai", "gemini"]
ROUND_2_MODELS = ["deepseek", "openai", "gemini"]
EXPANDED_MODELS = ["deepseek", "openai", "gemini", "claude", "minimax"]
FALLBACK_MODELS = ["claude", "minimax"]
ALL_MODELS = ["deepseek", "openai", "gemini", "claude", "minimax"]

REVIEWER_FOCUS = {
    "deepseek": "Your primary focus is TECHNICAL/ARCHITECTURAL RIGOR.",
    "openai": "Your primary focus is EDITORIAL CLARITY and CROSS-DOCUMENT COHERENCE.",
    "gemini": "Your primary focus is LEGAL/COMPLIANCE GAPS.",
    "claude": "Your primary focus is GOVERNANCE PRECISION, FAILURE MODES, and POLICY EDGE CASES.",
    "minimax": "Your primary focus is OPERABILITY, IMPLEMENTATION GAPS, and ACTIONABLE REMEDIATION.",
}


def _is_core_doc(doc_path: str) -> bool:
    return doc_path.startswith("core/") or doc_path.startswith("core\\")


def _rough_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _utc_timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _resolved_api_model(model_name: str) -> str:
    if model_name == "openai":
        return os.environ.get("OPENAI_PEER_REVIEW_MODEL", "gpt-5.4")
    if model_name == "gemini":
        return os.environ.get("GEMINI_PEER_REVIEW_MODEL", "gemini-2.5-pro")
    if model_name == "deepseek":
        return os.environ.get("DEEPSEEK_PEER_REVIEW_MODEL", "deepseek-chat")
    if model_name == "claude":
        return os.environ.get("CLAUDE_PEER_REVIEW_MODEL", "claude-sonnet-4-20250514")
    if model_name == "minimax":
        return os.environ.get("MINIMAX_PEER_REVIEW_MODEL", "MiniMax-M2.5")
    return model_name


def _is_error_output(content: str) -> bool:
    return content.strip().startswith("[ERROR:")


async def _execute_review_batch(
    prompts: dict[str, tuple[str, str]],
    models: list[str],
) -> tuple[dict[str, str], list[dict]]:
    print("Sending to models in parallel...")
    tasks = {}
    for model_name in models:
        sys_p, usr_p = prompts[model_name]
        caller = MODEL_CALLERS[model_name]
        tasks[model_name] = asyncio.create_task(caller(sys_p, usr_p))

    results = {}
    result_rows = []
    for model_name, task in tasks.items():
        sys_p, usr_p = prompts[model_name]
        try:
            content = await task
            results[model_name] = content
            print(f"  [{model_name}] Review received ({len(content)} chars)")
        except Exception as e:
            content = f"[ERROR: {e}]"
            results[model_name] = content
            print(f"  [{model_name}] ERROR: {e}")

        result_rows.append(
            {
                "model_lane": model_name,
                "resolved_api_model": _resolved_api_model(model_name),
                "output_chars": len(content),
                "output_classification": classify_peer_review_output(content),
                "estimated_prompt_tokens_system": _rough_tokens(sys_p),
                "estimated_prompt_tokens_user": _rough_tokens(usr_p),
                "estimated_prompt_tokens_total": _rough_tokens(sys_p) + _rough_tokens(usr_p),
            }
        )

    return results, result_rows


def build_prompt(
    doc_path: str,
    review_round: int,
    model_name: str,
    rubric: str = "full",
    smart_context: bool = False,
    product_context_arg: str | None = None,
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

    product_impl = resolve_product_implementation_text(product_context_arg)

    replacements = {
        "REVIEWER_FOCUS": REVIEWER_FOCUS.get(model_name, ""),
        "REVIEW_ROUND": f"This is **Round {review_round}**.{rubric_instruction}",
        "GOVERNING_CONTEXT": context_text,
        "PRODUCT_IMPLEMENTATION_CONTEXT": product_impl,
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
    product_context_arg: str | None = None,
    expanded: bool = False,
    fallback_unavailable: bool = False,
    fallback_models_override: list[str] | None = None,
):
    rubric = rubric_override or ("full" if _is_core_doc(doc_path) else "full")
    default_models = EXPANDED_MODELS if expanded else (ROUND_1_MODELS if review_round == 1 else ROUND_2_MODELS)
    models = models_override or default_models
    fallback_models = fallback_models_override or FALLBACK_MODELS

    print(f"\n{'='*60}")
    print(f"AIOS Peer Review — Round {review_round}")
    print(f"Document: {doc_path}")
    print(f"Models: {', '.join(models)}")
    print(f"Rubric: {rubric}")
    print(f"Context: {'smart (cross-refs only)' if smart_context else 'full (all core docs)'}")
    if product_context_arg:
        print(f"Product snapshot: {'default bundle' if product_context_arg == 'default' else product_context_arg}")
    print(f"{'='*60}\n")

    bundle_info = peer_review_context_bundle_info(doc_path, smart_context)
    prod_info = product_context_bundle_info(product_context_arg)

    prompts = {}
    for model in models:
        sys_prompt, user_prompt = build_prompt(
            doc_path, review_round, model,
            rubric=rubric, smart_context=smart_context,
            product_context_arg=product_context_arg,
        )
        prompts[model] = (sys_prompt, user_prompt)

    results, result_rows = await _execute_review_batch(prompts, models)

    if fallback_unavailable:
        needed_successes = len(models)
        successful_reviews = sum(1 for content in results.values() if not _is_error_output(content))
        attempted = set(models)
        fallback_candidates = [m for m in fallback_models if m not in attempted]

        while successful_reviews < needed_successes and fallback_candidates:
            fallback_model = fallback_candidates.pop(0)
            print(f"Attempting fallback provider: {fallback_model}")
            sys_prompt, user_prompt = build_prompt(
                doc_path,
                review_round,
                fallback_model,
                rubric=rubric,
                smart_context=smart_context,
                product_context_arg=product_context_arg,
            )
            prompts[fallback_model] = (sys_prompt, user_prompt)
            fallback_results, fallback_rows = await _execute_review_batch(prompts, [fallback_model])
            results.update(fallback_results)
            result_rows.extend(fallback_rows)
            attempted.add(fallback_model)
            if not _is_error_output(fallback_results[fallback_model]):
                successful_reviews += 1

    print("\nSaving reviews...")
    for model_name, content in results.items():
        sys_p, usr_p = prompts[model_name]
        out_path = save_review(doc_path, review_round, model_name, content)
        print(f"  Saved: {out_path.relative_to(BASE_DIR)}")
        for row in result_rows:
            if row["model_lane"] == model_name and "output_path" not in row:
                row["output_path"] = str(out_path.relative_to(BASE_DIR)).replace("\\", "/")
                break

    slug = get_doc_slug(doc_path)
    round_dir = BASE_DIR / "reviews" / slug / f"round_{review_round}"
    round_dir.mkdir(parents=True, exist_ok=True)
    # Short filename only (slug in JSON) — long paths hit Windows MAX_PATH when slug is repeated.
    manifest_name = f"peer_review_manifest_{_utc_timestamp_slug()}.json"
    manifest_path = round_dir / manifest_name
    manifest_body = {
        "schema": "aios.peer_review_manifest.v1",
        "document_slug": slug,
        "document": doc_path.replace("\\", "/"),
        "review_round": review_round,
        "rubric": rubric,
        "smart_context": smart_context,
        "product_context_arg": product_context_arg,
        "context_bundle": bundle_info,
        "product_context_bundle": prod_info,
        "models_requested": models,
        "expanded_review": expanded,
        "fallback_unavailable": fallback_unavailable,
        "fallback_models": fallback_models if fallback_unavailable else [],
        "results": result_rows,
    }
    manifest_path.write_text(json.dumps(manifest_body, indent=2), encoding="utf-8")
    print(f"\nManifest: {manifest_path.relative_to(BASE_DIR)}")

    fm = read_governing_front_matter_dict(doc_path)
    doc_id = (fm.get("document_id") or "").strip() or Path(doc_path.replace("\\", "/")).stem
    head_ver = str(fm.get("version") or "").strip()
    manifest_rel = manifest_path.relative_to(BASE_DIR).as_posix()

    gate, gate_summary = infer_amd_2026_005_gate_from_round_dir(round_dir)

    write_packet_identity_v2(
        round_dir,
        BASE_DIR,
        document_id=doc_id,
        document_path=doc_path.replace("\\", "/"),
        packet_slug=slug,
        current_head_version=head_ver,
        review_round=review_round,
        manifest_rel=manifest_rel,
        generated_by="peer_review.py",
    )
    print(f"Packet identity: {round_dir / 'PACKET_IDENTITY.yaml'}")

    merge_and_write_packet_status(
        round_dir,
        document_id=doc_id,
        packet_slug=slug,
        current_head_version=head_ver,
        last_reviewed_version=head_ver,
        review_round=review_round,
        gate=gate,
        gate_summary=gate_summary,
    )
    print(f"Packet status: {round_dir / 'PACKET_STATUS.yaml'}")

    append_packet_events_peer_review(
        round_dir,
        BASE_DIR,
        document_id=doc_id,
        packet_slug=slug,
        from_version=head_ver,
        reviewed_version=head_ver,
        review_round=review_round,
        gate=gate,
        gate_summary=gate_summary,
    )
    print(f"Packet events appended: {round_dir / 'PACKET_EVENTS.yaml'}")

    ensure_default_handoff_note(round_dir)

    print(f"\nRound {review_round} review complete.")


def main():
    parser = argparse.ArgumentParser(description="AIOS Peer Review Engine")
    parser.add_argument("document", help="Path to document relative to governing_docs/")
    parser.add_argument("--round", type=int, choices=[1, 2], required=True, help="Review round")
    parser.add_argument("--rubric", choices=["full", "light"], default=None,
                        help="Rubric variant (default: full for core, full for others)")
    parser.add_argument("--smart-context", action="store_true",
                        help="Inject only cross-referenced docs instead of all core docs")
    parser.add_argument(
        "--models",
        nargs="+",
        choices=ALL_MODELS,
        default=None,
        metavar="MODEL",
        help="Override default Round 1/2 model lists (e.g. --models deepseek openai gemini claude minimax)",
    )
    parser.add_argument(
        "--expanded",
        action="store_true",
        help="Run the expanded five-provider review set: deepseek, openai, gemini, claude, minimax.",
    )
    parser.add_argument(
        "--fallback-unavailable",
        action="store_true",
        help="Backfill provider errors with additional fallback providers until the intended review count is met or fallbacks are exhausted.",
    )
    parser.add_argument(
        "--fallback-models",
        nargs="+",
        choices=ALL_MODELS,
        default=None,
        metavar="MODEL",
        help="Fallback providers to try in order when --fallback-unavailable is enabled (default: claude minimax).",
    )
    parser.add_argument(
        "--product-context",
        nargs="?",
        const="default",
        default=None,
        metavar="REL_PATH",
        help="Include ai-os-voice-interface snapshot (run generate_product_context_bundle.py first). "
        "Use flag alone for reference/knowledge_base/snapshots/product_context_bundle.md, or pass a path under repo root.",
    )
    args = parser.parse_args()

    if not (BASE_DIR / args.document).exists():
        print(f"Error: Document not found: {args.document}")
        sys.exit(1)

    asyncio.run(run_review(
        args.document, args.round,
        models_override=args.models,
        rubric_override=args.rubric,
        smart_context=args.smart_context,
        product_context_arg=args.product_context,
        expanded=args.expanded,
        fallback_unavailable=args.fallback_unavailable,
        fallback_models_override=args.fallback_models,
    ))


if __name__ == "__main__":
    main()

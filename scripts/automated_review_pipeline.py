"""
Fully automated peer-review → OpenAI amendment loop.

For each document (from --document or the next pending item in review_queue.json):
  1. Run peer_review Round 1 (openai + gemini), then Round 2 (deepseek + openai + gemini).
  2. If all three Round-2 reviews have ratifiable dispositions, stop — success.
  3. Otherwise send this iteration's Round 1 + Round 2 text to OpenAI to revise the document; repeat.
  4. Maximum 3 amendment iterations by default. If still not ratifiable, write failure reports (MD + JSON).

Requires OPENAI_API_KEY, DEEPSEEK_API_KEY, GEMINI_API_KEY (same as peer_review.py).

Usage:
  py -3 automated_review_pipeline.py --document amendments/AMD-2026-007.md
  py -3 automated_review_pipeline.py --next
  py -3 automated_review_pipeline.py --next --dry-run --verbose

Full (non-dry) runs write reviews/<slug>/LAST_RUN_POINTER.json and
reviews/<slug>/automated_runs/<run_id>/run_manifest.json for CI and dashboards.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from context_assembler import (
    BASE_DIR,
    call_openai,
    get_doc_slug,
    parse_front_matter,
    read_core_docs,
    read_file,
    read_prompt_template,
    read_style_guide,
    assemble_prompt,
)
from peer_review import ROUND_1_MODELS, ROUND_2_MODELS, build_prompt, run_review

# Disposition helpers (inlined from sandbox context_assembler so this narrow salvage does not
# require changes to context_assembler.py; see compare-first pass if you prefer centralizing them.)
_RATIFIABLE_PEER_DISPOSITIONS = frozenset(
    {
        "approved",
        "approved_with_changes",
        "approved_with_minor_changes",
    }
)


def _normalize_disposition_value(raw: str | None) -> str | None:
    if raw is None:
        return None
    s = str(raw).strip().lower()
    s = re.sub(r"[\s\-]+", "_", s)
    s = re.sub(r"[^a-z0-9_]", "", s)
    return s or None


def sorted_review_paths(doc_path: str, review_round: int) -> list[Path]:
    """Return review markdown files for a round, sorted by review_NNN sequence."""
    slug = get_doc_slug(doc_path)
    round_dir = BASE_DIR / "reviews" / slug / f"round_{review_round}"
    if not round_dir.exists():
        return []
    files = list(round_dir.glob("review_*.md"))

    def sort_key(p: Path) -> int:
        match = re.search(r"review_(\d+)", p.name)
        return int(match.group(1)) if match else 0

    return sorted(files, key=sort_key)


def is_ratifiable_peer_disposition(disposition: str | None) -> bool:
    n = _normalize_disposition_value(disposition)
    return n in _RATIFIABLE_PEER_DISPOSITIONS if n else False


def extract_disposition_from_review(content: str) -> str | None:
    """Read disposition from YAML front matter, else first 'disposition:' line in body."""
    meta, _ = parse_front_matter(content)
    if meta and meta.get("disposition"):
        return str(meta["disposition"]).strip()
    match = re.search(r"(?im)^disposition:\s*(.+)$", content)
    if match:
        return match.group(1).strip()
    return None


QUEUE_PATH = BASE_DIR / "review_queue.json"
EXPECTED_R1 = 2
EXPECTED_R2 = 3
DEFAULT_MAX_RUNS = 3


def _norm_path(p: str) -> str:
    return str(Path(p).as_posix())


def _review_has_api_error(content: str) -> bool:
    return "[ERROR:" in (content or "")


def _load_queue() -> dict:
    if not QUEUE_PATH.exists():
        return {"items": []}
    return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))


def _save_queue(data: dict) -> None:
    tmp = QUEUE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    tmp.replace(QUEUE_PATH)


def _split_revision_prompt(assembled: str) -> tuple[str, str]:
    marker = "## The Original Document"
    if marker not in assembled:
        return "You are a senior governance architect.", assembled
    before, after = assembled.split(marker, 1)
    return before, marker + after


def _strip_json_fence(raw: str) -> str:
    s = raw.strip()
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s, count=1, flags=re.IGNORECASE)
        s = re.sub(r"\s*```\s*$", "", s)
    return s.strip()


def _parse_openai_revision_response(response: str) -> tuple[str, str, dict | None]:
    if "===REVISION_LOG_START===" not in response:
        return (
            response.strip(),
            "# Revision log\n\n[Delimiter ===REVISION_LOG_START=== missing; manual split may be needed.]\n",
            None,
        )
    doc, rest = response.split("===REVISION_LOG_START===", 1)
    doc = doc.strip()
    rest = rest.strip()
    if "===REVISION_SYNTHESIS_JSON_START===" in rest:
        rev_log, synth_body = rest.split("===REVISION_SYNTHESIS_JSON_START===", 1)
        rev_log = rev_log.strip()
        synth_body = synth_body.split("===REVISION_SYNTHESIS_JSON_END===", 1)[0].strip()
        synth_body = _strip_json_fence(synth_body)
        try:
            synthesis = json.loads(synth_body)
        except json.JSONDecodeError:
            synthesis = {
                "_parse_error": True,
                "_raw_excerpt": synth_body[:2000],
            }
    else:
        rev_log = rest
        synthesis = None
    return doc, rev_log, synthesis


async def _openai_revise_document(
    doc_path: str,
    round_1_texts: list[str],
    round_2_texts: list[str],
    model: str,
) -> tuple[str, str, dict | None]:
    core = read_core_docs()
    template = read_prompt_template("automated_openai_revision.md")
    r1_block = "\n\n---\n\n".join(
        f"### Round 1 review {i}\n\n{t}" for i, t in enumerate(round_1_texts, 1)
    )
    r2_block = "\n\n---\n\n".join(
        f"### Round 2 review {i}\n\n{t}" for i, t in enumerate(round_2_texts, 1)
    )
    replacements = {
        "TECHNICAL_MANIFESTO": core["technical_manifesto"],
        "GOVERNANCE_CONSTITUTION": core["governance_constitution"],
        "MPOA": core["mpoa"],
        "STYLE_GUIDE": read_style_guide(),
        "TARGET_DOCUMENT": read_file(BASE_DIR / doc_path),
        "ROUND_1_REVIEWS": r1_block,
        "ROUND_2_REVIEWS": r2_block,
    }
    assembled = assemble_prompt(template, replacements)
    system_part, user_part = _split_revision_prompt(assembled)
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set (required for amendment revision).")
    response = await call_openai(system_part, user_part, model=model)
    return _parse_openai_revision_response(response)


def _round2_ratifiable(round_2_texts: list[str]) -> tuple[bool, list[dict]]:
    """Return (all ratifiable, per-review detail dicts)."""
    details: list[dict] = []
    ok = True
    for i, text in enumerate(round_2_texts, 1):
        err = _review_has_api_error(text)
        disp = extract_disposition_from_review(text) if not err else None
        rat = (not err) and is_ratifiable_peer_disposition(disp)
        details.append(
            {
                "index": i,
                "disposition": disp,
                "ratifiable": rat,
                "api_error": err,
            }
        )
        if not rat:
            ok = False
    return ok, details


def _normalize_disp_str(d: str | None) -> str | None:
    if not d:
        return None
    return str(d).strip().lower().replace(" ", "_").replace("-", "_")


def _ratification_recommendation(details: list[dict]) -> str:
    normalized = [_normalize_disp_str(d.get("disposition")) for d in details]
    normalized = [x for x in normalized if x]
    if normalized and all(x == "approved" for x in normalized):
        return "ratify_now"
    return "ratify_with_editorial_note"


def _run_dir(doc_path: str, run_id: str) -> Path:
    slug = get_doc_slug(doc_path)
    d = BASE_DIR / "reviews" / slug / "automated_runs" / run_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def _write_run_manifest(
    doc_path: str,
    out_dir: Path,
    run_id: str,
    *,
    exit_code: int,
    status: str,
    final_report_md: str,
    report_json_name: str | None,
    iterations_used: int | None,
    failure_kind: str | None = None,
) -> None:
    """Single artifact-root manifest for dashboards and downstream tooling (written in out_dir)."""
    slug = get_doc_slug(doc_path)
    peer_root = f"reviews/{slug}"
    manifest: dict = {
        "schema_version": "1.0",
        "document": doc_path,
        "run_id": run_id,
        "status": status,
        "exit_code": exit_code,
        "final_report": final_report_md,
        "artifact_directory": out_dir.relative_to(BASE_DIR).as_posix(),
        "peer_reviews_path": peer_root,
        "peer_reviews_round_1": f"{peer_root}/round_1",
        "peer_reviews_round_2": f"{peer_root}/round_2",
    }
    if report_json_name:
        manifest["report_json"] = report_json_name
    if iterations_used is not None:
        manifest["iterations_used"] = iterations_used
    if failure_kind:
        manifest["failure_kind"] = failure_kind
    (out_dir / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


def _write_last_run_pointer(doc_path: str, out_dir: Path, run_id: str, exit_code: int) -> None:
    """Written after each full (non-dry) run so CI can upload the correct artifact directory."""
    slug = get_doc_slug(doc_path)
    ptr = {
        "document": doc_path,
        "run_id": run_id,
        "artifact_relative_path": out_dir.relative_to(BASE_DIR).as_posix(),
        "run_manifest": (out_dir / "run_manifest.json").relative_to(BASE_DIR).as_posix(),
        "exit_code": exit_code,
        "completed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }
    path = BASE_DIR / "reviews" / slug / "LAST_RUN_POINTER.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ptr, indent=2) + "\n", encoding="utf-8")


def _dry_run_report(
    doc_path: str,
    run_id: str,
    out_dir: Path,
    smart_context: bool,
    verbose: bool,
) -> dict:
    """Build peer-review prompt size preview and revision prompt estimate (no API calls)."""
    validation_errors: list[str] = []
    probe = out_dir / ".write_probe"
    artifact_dir_writable = False
    try:
        probe.write_text("1", encoding="utf-8")
        probe.unlink()
        artifact_dir_writable = True
    except OSError as e:
        validation_errors.append(f"artifact_dir_not_writable:{e}")

    path_resolved = (BASE_DIR / doc_path).is_file()
    if not path_resolved:
        validation_errors.append("document_path_not_a_file")

    peer: dict[str, dict] = {}
    revision_preview: dict = {}
    prompt_generation_ok = False

    try:
        for round_num, models in ((1, ROUND_1_MODELS), (2, ROUND_2_MODELS)):
            for m in models:
                sys_p, usr_p = build_prompt(doc_path, round_num, m, smart_context=smart_context)
                total = len(sys_p) + len(usr_p)
                key = f"round_{round_num}_{m}"
                entry: dict = {
                    "chars_total": total,
                    "chars_system": len(sys_p),
                    "chars_user": len(usr_p),
                }
                if verbose:
                    combo = sys_p + "\n\n---\n\n" + usr_p
                    entry["preview_head"] = combo[:1200]
                    entry["preview_tail"] = combo[-800:] if len(combo) > 2000 else None
                peer[key] = entry

        core = read_core_docs()
        template = read_prompt_template("automated_openai_revision.md")
        r1_block = "[dry-run placeholder: Round 1 reviews]\n"
        r2_block = "[dry-run placeholder: Round 2 reviews]\n"
        replacements = {
            "TECHNICAL_MANIFESTO": core["technical_manifesto"],
            "GOVERNANCE_CONSTITUTION": core["governance_constitution"],
            "MPOA": core["mpoa"],
            "STYLE_GUIDE": read_style_guide(),
            "TARGET_DOCUMENT": read_file(BASE_DIR / doc_path),
            "ROUND_1_REVIEWS": r1_block,
            "ROUND_2_REVIEWS": r2_block,
        }
        assembled = assemble_prompt(template, replacements)
        system_part, user_part = _split_revision_prompt(assembled)
        rev_total = len(system_part) + len(user_part)
        revision_preview = {
            "chars_total": rev_total,
            "chars_system": len(system_part),
            "chars_user": len(user_part),
        }
        if verbose:
            combo = system_part + "\n\n---\n\n" + user_part
            revision_preview["preview_head"] = combo[:1200]

        prompt_generation_ok = len(peer) == 5 and rev_total > 0
    except Exception as e:
        validation_errors.append(f"prompt_generation:{e!s}")

    ready_for_full_run = bool(
        artifact_dir_writable
        and path_resolved
        and prompt_generation_ok
        and not validation_errors
    )

    report = {
        "dry_run": True,
        "ready_for_full_run": ready_for_full_run,
        "validation_errors": validation_errors,
        "checks": {
            "path_resolved": path_resolved,
            "artifact_dir_writable": artifact_dir_writable,
            "prompt_generation_ok": prompt_generation_ok,
        },
        "document": doc_path,
        "run_id": run_id,
        "resolved_path": str((BASE_DIR / doc_path).resolve()),
        "artifact_directory": str(out_dir.relative_to(BASE_DIR)),
        "smart_context": smart_context,
        "peer_review_prompts": peer,
        "openai_revision_prompt": revision_preview,
        "would_call_models": {
            "round_1": list(ROUND_1_MODELS),
            "round_2": list(ROUND_2_MODELS),
            "revision": os.getenv("AUTOMATED_REVISION_MODEL", "gpt-4o"),
        },
    }
    (out_dir / "dry_run_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


async def _process_document(
    doc_path: str,
    max_runs: int,
    smart_context: bool,
    dry_run: bool,
    verbose: bool,
) -> int:
    doc_path = _norm_path(doc_path)
    full = BASE_DIR / doc_path
    if not full.exists():
        print(f"Error: Document not found: {doc_path}")
        return 1

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = _run_dir(doc_path, run_id)
    revision_model = os.getenv("AUTOMATED_REVISION_MODEL", "gpt-4o")

    print(f"\n{'='*60}")
    print("AIOS Automated Review -> Amendment Pipeline")
    if dry_run:
        print("[DRY RUN - no model APIs will be called]")
    print(f"Document: {doc_path}")
    print(f"Max amendment iterations: {max_runs}")
    print(f"Run artifacts: {out_dir.relative_to(BASE_DIR)}")
    print(f"{'='*60}\n")

    if dry_run:
        report = _dry_run_report(doc_path, run_id, out_dir, smart_context, verbose)
        ready = report.get("ready_for_full_run")
        print(f"  ready_for_full_run: {ready}")
        if report.get("validation_errors"):
            print(f"  validation_errors: {report['validation_errors']}")
        print(f"  Artifact dir: {out_dir}")
        print(f"  Peer review prompt entries: {len(report.get('peer_review_prompts') or {})}")
        pr = report.get("openai_revision_prompt") or {}
        print(f"  OpenAI revision prompt (est. chars): {pr.get('chars_total', 0)}")
        if verbose:
            print("\n--- Sample: first peer prompt preview (round_1_openai) ---\n")
            k = "round_1_openai"
            peer = report.get("peer_review_prompts") or {}
            if k in peer and peer[k].get("preview_head"):
                print(peer[k]["preview_head"][:2000])
        print(f"\nWrote {out_dir / 'dry_run_report.json'}")
        if not ready:
            print("\nDry-run did not pass all checks (see dry_run_report.json).")
            return 1
        print("Dry-run validation OK.")
        return 0

    def _finish(rc: int) -> int:
        _write_last_run_pointer(doc_path, out_dir, run_id, rc)
        return rc

    iteration_history: list[dict] = []
    last_synthesis: dict | None = None
    iter_dir: Path | None = None

    for iteration in range(1, max_runs + 1):
        print(f"\n--- Iteration {iteration}/{max_runs} ---\n")

        iter_dir = out_dir / f"iteration_{iteration:02d}"
        iter_dir.mkdir(parents=True, exist_ok=True)

        idx_r1 = len(sorted_review_paths(doc_path, 1))
        idx_r2 = len(sorted_review_paths(doc_path, 2))

        await run_review(doc_path, 1, smart_context=smart_context)

        paths_r1 = sorted_review_paths(doc_path, 1)[idx_r1:]
        r1_texts = [read_file(p) for p in paths_r1]
        if len(r1_texts) != EXPECTED_R1:
            print(
                f"Warning: expected {EXPECTED_R1} new Round 1 reviews, got {len(r1_texts)}"
            )

        await run_review(doc_path, 2, smart_context=smart_context)

        paths_r2 = sorted_review_paths(doc_path, 2)[idx_r2:]
        r2_texts = [read_file(p) for p in paths_r2]
        if len(r2_texts) != EXPECTED_R2:
            print(
                f"Warning: expected {EXPECTED_R2} new Round 2 reviews, got {len(r2_texts)}"
            )

        (iter_dir / "round_1_paths.txt").write_text(
            "\n".join(str(p.relative_to(BASE_DIR)) for p in paths_r1), encoding="utf-8"
        )
        (iter_dir / "round_2_paths.txt").write_text(
            "\n".join(str(p.relative_to(BASE_DIR)) for p in paths_r2), encoding="utf-8"
        )

        rat_ok, details = _round2_ratifiable(r2_texts)
        (iter_dir / "round_2_dispositions.json").write_text(
            json.dumps(details, indent=2) + "\n", encoding="utf-8"
        )

        iteration_history.append(
            {
                "iteration": iteration,
                "round_2_dispositions": details,
            }
        )

        if rat_ok:
            meta, _ = parse_front_matter(read_file(full))
            final_version = meta.get("version", "unknown")
            recommendation = _ratification_recommendation(details)
            non_blocking: list = []
            if last_synthesis and isinstance(last_synthesis, dict):
                non_blocking = list(last_synthesis.get("non_blocking_issues") or [])

            report_md = (
                f"# Automated pipeline — completion report\n\n"
                f"- **Document:** `{doc_path}`\n"
                f"- **Run ID:** `{run_id}`\n"
                f"- **Final version (front matter):** `{final_version}`\n"
                f"- **Iterations used:** {iteration}\n"
                f"- **Result:** Ratifiable (all Round 2 dispositions OK)\n"
                f"- **Recommendation:** **{recommendation}** "
                f"(`ratify_now` = all reviewers approved; "
                f"`ratify_with_editorial_note` = includes approved-with-changes or minor items)\n\n"
                f"## Dispositions by iteration\n\n"
            )
            for h in iteration_history:
                report_md += f"### Iteration {h['iteration']}\n\n"
                report_md += "```json\n"
                report_md += json.dumps(h["round_2_dispositions"], indent=2)
                report_md += "\n```\n\n"

            report_md += (
                "## Remaining non-blocking issues\n\n"
            )
            if non_blocking:
                for item in non_blocking:
                    report_md += f"- {item}\n"
            else:
                report_md += (
                    "- None recorded (narrative reviews may still mention minor editorial items).\n"
                )

            report_md += (
                "\n## Council use\n\n"
                "Attach this report with the document for ratification. "
                "If recommendation is `ratify_with_editorial_note`, record optional follow-ups as maintenance.\n"
            )

            (out_dir / "completion_report.md").write_text(report_md, encoding="utf-8")

            completion_json = {
                "status": "completed",
                "document": doc_path,
                "run_id": run_id,
                "final_version": final_version,
                "iterations_used": iteration,
                "dispositions_by_iteration": iteration_history,
                "recommendation": recommendation,
                "non_blocking_issues": non_blocking,
                "exit_code": 0,
            }
            (out_dir / "completion_report.json").write_text(
                json.dumps(completion_json, indent=2) + "\n", encoding="utf-8"
            )
            _write_run_manifest(
                doc_path,
                out_dir,
                run_id,
                exit_code=0,
                status="completed",
                final_report_md="completion_report.md",
                report_json_name="completion_report.json",
                iterations_used=iteration,
                failure_kind=None,
            )
            print(
                f"\nRatifiable after {iteration} iteration(s). "
                f"See {out_dir / 'completion_report.md'} and completion_report.json"
            )
            return _finish(0)

        if iteration >= max_runs:
            break

        print("Not yet ratifiable; sending Round 1 + Round 2 feedback to OpenAI for revision...")
        try:
            revised, rev_log, synthesis = await _openai_revise_document(
                doc_path, r1_texts, r2_texts, model=revision_model
            )
        except Exception as e:
            fail_md = (
                f"# Automated pipeline — failure report\n\n"
                f"**Reason:** OpenAI revision failed: `{e}`\n\n"
                f"**Iteration:** {iteration}\n"
            )
            (out_dir / "failure_report.md").write_text(fail_md, encoding="utf-8")
            fail_json = {
                "status": "failed",
                "failure_kind": "openai_revision_error",
                "document": doc_path,
                "run_id": run_id,
                "iteration": iteration,
                "error": str(e),
                "exit_code": 2,
            }
            (out_dir / "failure_report.json").write_text(
                json.dumps(fail_json, indent=2) + "\n", encoding="utf-8"
            )
            _write_run_manifest(
                doc_path,
                out_dir,
                run_id,
                exit_code=2,
                status="failed",
                final_report_md="failure_report.md",
                report_json_name="failure_report.json",
                iterations_used=iteration,
                failure_kind="openai_revision_error",
            )
            print(f"ERROR: {e}")
            return _finish(2)

        last_synthesis = synthesis
        if synthesis is not None:
            (iter_dir / "synthesis.json").write_text(
                json.dumps(synthesis, indent=2) + "\n", encoding="utf-8"
            )

        full.write_text(revised, encoding="utf-8")
        log_path = BASE_DIR / "reviews" / get_doc_slug(doc_path) / "revision_log.md"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(rev_log, encoding="utf-8")
        (iter_dir / "revision_log_snapshot.md").write_text(rev_log, encoding="utf-8")
        print(f"Document and revision log updated. Continuing to iteration {iteration + 1}...")

    disp_path = (iter_dir / "round_2_dispositions.json") if iter_dir else None
    if disp_path and disp_path.exists():
        last_details = json.loads(disp_path.read_text(encoding="utf-8"))
    else:
        last_details = []

    fail_md = (
        f"# Automated pipeline — failure report\n\n"
        f"- **Document:** `{doc_path}`\n"
        f"- **Run ID:** `{run_id}`\n"
        f"- **Max iterations:** {max_runs}\n"
        f"- **Outcome:** Round 2 triangulation did not reach ratifiable dispositions within the limit.\n\n"
        f"## Last Round 2 disposition check\n\n```json\n"
        f"{json.dumps(last_details, indent=2)}\n```\n\n"
        f"## Next steps\n\n"
        f"1. Manually edit `{doc_path}` to address remaining feedback, or\n"
        f"2. Re-queue the document and run this pipeline again.\n"
    )
    (out_dir / "failure_report.md").write_text(fail_md, encoding="utf-8")

    fail_json = {
        "status": "failed",
        "failure_kind": "max_iterations_exhausted",
        "document": doc_path,
        "run_id": run_id,
        "max_iterations": max_runs,
        "last_round_2_dispositions": last_details,
        "iterations_attempted": iteration_history,
        "exit_code": 3,
    }
    (out_dir / "failure_report.json").write_text(json.dumps(fail_json, indent=2) + "\n", encoding="utf-8")

    _write_run_manifest(
        doc_path,
        out_dir,
        run_id,
        exit_code=3,
        status="failed",
        final_report_md="failure_report.md",
        report_json_name="failure_report.json",
        iterations_used=len(iteration_history),
        failure_kind="max_iterations_exhausted",
    )
    print(
        f"\nStopped after {max_runs} iteration(s). "
        f"See {out_dir / 'failure_report.md'} and failure_report.json"
    )
    return _finish(3)


def _set_queue_item_status(doc_path: str, status: str) -> None:
    data = _load_queue()
    p = _norm_path(doc_path)
    for item in data.get("items", []):
        if _norm_path(item.get("path", "")) == p:
            item["status"] = status
            break
    _save_queue(data)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Automated peer review + OpenAI amendment loop (max 3 iterations by default).",
    )
    parser.add_argument(
        "--document",
        help="Path relative to governing_docs/ (bypasses queue)",
    )
    parser.add_argument(
        "--next",
        action="store_true",
        help="Process the first queue item with status pending",
    )
    parser.add_argument(
        "--max-runs",
        type=int,
        default=DEFAULT_MAX_RUNS,
        help=f"Maximum amendment iterations (default {DEFAULT_MAX_RUNS})",
    )
    parser.add_argument(
        "--smart-context",
        action="store_true",
        help="Use cross-reference-only context for peer review (non-core docs)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call model APIs; validate paths/queue, create artifact dir, write dry_run_report.json",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="With --dry-run, include prompt previews (large) in dry_run_report.json",
    )
    args = parser.parse_args()

    if args.max_runs < 1:
        print("--max-runs must be at least 1.")
        sys.exit(1)

    if args.document and args.next:
        print("Use either --document or --next, not both.")
        sys.exit(1)

    if not args.document and not args.next:
        print("Specify --document PATH or --next.")
        sys.exit(1)

    if args.verbose and not args.dry_run:
        print("--verbose applies to --dry-run only; ignored.")
        args.verbose = False

    doc_path: str | None = None
    if args.document:
        doc_path = _norm_path(args.document)
    else:
        data = _load_queue()
        pending = None
        for item in data.get("items", []):
            if item.get("status") == "pending":
                pending = item
                break
        if not pending:
            print("No pending items in review_queue.json.")
            sys.exit(1)
        doc_path = _norm_path(pending["path"])
        if not args.dry_run:
            pending["status"] = "in_progress"
            _save_queue(data)

    assert doc_path is not None
    rc = asyncio.run(
        _process_document(
            doc_path,
            args.max_runs,
            args.smart_context,
            dry_run=args.dry_run,
            verbose=args.verbose,
        )
    )

    if args.next and not args.dry_run:
        if rc == 0:
            _set_queue_item_status(doc_path, "completed")
        elif rc != 0:
            _set_queue_item_status(doc_path, "failed")

    sys.exit(rc)


if __name__ == "__main__":
    main()

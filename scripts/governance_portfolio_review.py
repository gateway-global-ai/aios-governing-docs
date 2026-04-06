"""
Governance portfolio (corpus) review — separate from single-document peer review.

Reads the document registry plus a digest of governing markdown, calls OpenAI once,
and writes five outputs under portfolio_reviews/<UTC-run>/:

  - framework_summary.md
  - risk_register.md
  - next_logical_work.md
  - cross_document_conflicts.md
  - implementation_priority_list.json

Usage:
  py -3 governance_portfolio_review.py
  py -3 governance_portfolio_review.py --dry-run
  py -3 governance_portfolio_review.py --model gpt-4o --max-tokens 16384
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
    CORE_DOCS,
    DOCUMENT_REGISTRY_JSON_PATH,
    INTRODUCTION_PATH,
    STYLE_GUIDE_PATH,
    assemble_prompt,
    call_openai,
    load_registry_json,
    read_core_docs,
    read_file,
    read_prompt_template,
)


REQUIRED_OUTPUTS = (
    "framework_summary.md",
    "risk_register.md",
    "next_logical_work.md",
    "cross_document_conflicts.md",
    "implementation_priority_list.json",
)


def _norm_registry_path(p: str) -> str:
    return str(Path(p).as_posix())


def _build_corpus_digest(
    max_chars_per_doc: int,
    max_total_chars: int,
) -> str:
    """Concatenate core docs, introduction, and truncated registry-linked bodies."""
    parts: list[str] = []
    total = 0

    def push(s: str) -> bool:
        nonlocal total
        if total + len(s) > max_total_chars:
            return False
        parts.append(s)
        total += len(s)
        return True

    core = read_core_docs()
    if not push("# Core governing documents (full text)\n\n"):
        return "".join(parts) + "\n[Digest empty: max_total_chars too small]\n"

    for key in sorted(core.keys()):
        block = f"## {key}\n\n{core[key]}\n\n---\n\n"
        if not push(block):
            parts.append("\n[Core section truncated at max_total_chars]\n")
            break

    if INTRODUCTION_PATH.exists():
        intro = read_file(INTRODUCTION_PATH)
        if intro and not intro.startswith("[File not found"):
            block = f"# introduction.md\n\n{intro[:max_chars_per_doc]}\n\n---\n\n"
            if not push(block):
                return "".join(parts)

    registry = load_registry_json()
    seen_paths: set[str] = set()
    core_paths = {_norm_registry_path(str(p)) for p in CORE_DOCS.values()}

    for entry in sorted(registry, key=lambda e: str(e.get("document_id", ""))):
        doc_id = entry.get("document_id", "")
        raw_path = entry.get("_path")
        if not raw_path:
            continue
        rel = _norm_registry_path(raw_path)
        if rel in seen_paths:
            continue
        seen_paths.add(rel)

        if rel in core_paths:
            continue

        full_path = BASE_DIR / rel
        if not full_path.is_file():
            continue
        body = read_file(full_path)
        if body.startswith("[File not found"):
            continue
        if len(body) > max_chars_per_doc:
            body = body[:max_chars_per_doc] + "\n\n[TRUNCATED — increase --max-chars-per-doc to include more]\n"

        block = f"## Registry document: {doc_id}\n**Path:** `{rel}`\n\n{body}\n\n---\n\n"
        if not push(block):
            parts.append(
                f"\n[Corpus digest stopped at max_total_chars={max_total_chars}]\n"
            )
            break

    return "".join(parts)


def _split_delimited_outputs(text: str) -> dict[str, str]:
    """Parse ===FILE:filename=== sections."""
    pat = re.compile(r"^===FILE:([^=\n]+)===$", re.MULTILINE)
    matches = list(pat.finditer(text))
    out: dict[str, str] = {}
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[name] = text[start:end].strip()
    return out


async def _run(
    dry_run: bool,
    model: str,
    max_tokens: int,
    max_chars_per_doc: int,
    max_total_chars: int,
) -> int:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = BASE_DIR / "portfolio_reviews" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    registry = load_registry_json()
    if not registry and not DOCUMENT_REGISTRY_JSON_PATH.exists():
        print("Warning: DOCUMENT_REGISTRY.json missing or empty.", file=sys.stderr)

    digest = _build_corpus_digest(max_chars_per_doc, max_total_chars)
    reg_json = (
        json.dumps(registry, indent=2)
        if registry
        else "[No registry JSON loaded]"
    )
    sg_full = read_file(STYLE_GUIDE_PATH)
    style_excerpt = sg_full[:8000]
    if len(sg_full) > 8000:
        style_excerpt += "\n\n[Style guide truncated for prompt size]\n"

    (out_dir / "corpus_digest_input.md").write_text(digest, encoding="utf-8")
    (out_dir / "registry_snapshot.json").write_text(reg_json, encoding="utf-8")

    print(f"Corpus digest chars: {len(digest)}")
    print(f"Output directory: {out_dir.relative_to(BASE_DIR)}")

    if dry_run:
        print("Dry run - wrote digest and registry snapshot only.")
        return 0

    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set.", file=sys.stderr)
        return 1

    template = read_prompt_template("governance_portfolio_review_prompt.md")
    assembled = assemble_prompt(
        template,
        {
            "STYLE_GUIDE_EXCERPT": style_excerpt,
            "DOCUMENT_REGISTRY_JSON": reg_json,
            "CORPUS_DIGEST": digest,
        },
    )

    system = (
        "You are a senior governance architect for Gateway Global AIOS. "
        "Follow the user message exactly. "
        "Begin your answer with the first ===FILE:framework_summary.md=== line; "
        "no preamble before it."
    )

    response = await call_openai(
        system,
        assembled,
        model=model,
        max_tokens=max_tokens,
    )
    (out_dir / "raw_model_response.md").write_text(response, encoding="utf-8")

    parsed = _split_delimited_outputs(response)
    missing = [n for n in REQUIRED_OUTPUTS if n not in parsed]

    for name in REQUIRED_OUTPUTS:
        if name in parsed:
            (out_dir / name).write_text(parsed[name], encoding="utf-8")

    if "implementation_priority_list.json" in parsed:
        try:
            json.loads(parsed["implementation_priority_list.json"])
        except json.JSONDecodeError as e:
            print(f"Warning: implementation_priority_list.json is not valid JSON: {e}", file=sys.stderr)

    manifest = {
        "schema_version": "1.0",
        "run_id": run_id,
        "mode": "portfolio_review",
        "model": model,
        "outputs_expected": list(REQUIRED_OUTPUTS),
        "outputs_written": [n for n in REQUIRED_OUTPUTS if (out_dir / n).exists()],
        "missing_delimited_sections": missing,
    }
    (out_dir / "portfolio_run_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    if missing:
        print(
            f"Warning: missing sections (see raw_model_response.md): {missing}",
            file=sys.stderr,
        )
        return 2

    print("Portfolio review complete.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Governance corpus / portfolio review")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build digest and registry snapshot only; do not call OpenAI",
    )
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model id")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16384,
        help="Max completion tokens (default 16384)",
    )
    parser.add_argument(
        "--max-chars-per-doc",
        type=int,
        default=6000,
        help="Max characters per non-core registry document body in digest",
    )
    parser.add_argument(
        "--max-total-chars",
        type=int,
        default=400_000,
        help="Approximate cap on total corpus digest size",
    )
    args = parser.parse_args()

    rc = asyncio.run(
        _run(
            dry_run=args.dry_run,
            model=args.model,
            max_tokens=args.max_tokens,
            max_chars_per_doc=args.max_chars_per_doc,
            max_total_chars=args.max_total_chars,
        )
    )
    sys.exit(rc)


if __name__ == "__main__":
    main()

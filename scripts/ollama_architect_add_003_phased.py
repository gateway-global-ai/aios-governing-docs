#!/usr/bin/env python3
"""
Phased Ollama Architect for AMD-2026-008-ADD-003 — slim KB + context preflight + composite.

Uses ~94k chars of doctrine (ADD-003 + architecture memo) in phase 1 and ~25k chars
(OPS-020 + ADD-003 §5.9 excerpt) in phase 2 instead of the full ~260k government bundle.

Repo root:
  py -3 scripts/ollama_architect_add_003_phased.py
  py -3 scripts/ollama_architect_add_003_phased.py --dry-run
  py -3 scripts/ollama_architect_add_003_phased.py --ollama-merge   # recommended third pass

Env: OLLAMA_HOST (default http://127.0.0.1:11434), OLLAMA_MODEL (default llama3.2).
For heavier analysis try: ollama pull llama3.3 / mistral / qwen2.5 then OLLAMA_MODEL=...
"""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path

import httpx

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent

AMD_SLUG = "amd_2026_008_add_003"
PLANNING = BASE_DIR / "reviews" / AMD_SLUG / "planning"

ADD003 = BASE_DIR / (
    "amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md"
)
OPS020 = BASE_DIR / "operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md"
MEMO = BASE_DIR / "reference/implementation/AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md"
SYSTEM_PROMPT = BASE_DIR / "prompts/ollama_architect_agent.md"
TEMPLATE = PLANNING / "ARCHITECT_PLAN_TEMPLATE.md"

OUT_P1 = PLANNING / "ARCHITECT_PLAN_PHASE1.md"
OUT_P2 = PLANNING / "ARCHITECT_PLAN_PHASE2.md"
OUT_COMPOSITE = PLANNING / "ARCHITECT_PLAN.md"


def read_text(path: Path) -> str:
    if not path.is_file():
        return f"[MISSING: {path}]"
    return path.read_text(encoding="utf-8", errors="replace")


def rough_tokens(chars: int) -> int:
    return max(1, chars // 4)


def ollama_chat(host: str, model: str, system: str, user: str, timeout: float = 900.0) -> str:
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


def ollama_alive(host: str) -> bool:
    try:
        with httpx.Client(timeout=5.0) as client:
            r = client.get(f"{host.rstrip('/')}/api/tags")
            return r.status_code == 200
    except httpx.HTTPError:
        return False
    except OSError:
        return False


def ollama_model_context_length(host: str, model: str) -> int | None:
    """Return context length in tokens if Ollama exposes it; else None."""
    try:
        with httpx.Client(timeout=15.0) as client:
            r = client.post(
                f"{host.rstrip('/')}/api/show",
                json={"name": model},
            )
            r.raise_for_status()
            data = r.json()
    except (httpx.HTTPError, OSError, json.JSONDecodeError):
        return None

    # Newer Ollama: top-level or nested model_info
    for key in ("context_length", "num_ctx"):
        v = data.get(key)
        if isinstance(v, int) and v > 0:
            return v
    mi = data.get("model_info") or {}
    if isinstance(mi, dict):
        for k, v in mi.items():
            if "context" in k.lower() and isinstance(v, int) and v > 0:
                return v
    return None


def extract_add003_section_59(full: str) -> str:
    """Narrow excerpt for phase 2: §5.9 + fail-closed table through OPS cross-ref."""
    start = full.find("### 5.9 Normative fields")
    if start < 0:
        return "[Could not locate §5.9 in ADD-003]\n\n" + full[:8000]
    end = full.find("## 6. Control-plane axes", start)
    chunk = full[start:end] if end > start else full[start : start + 12000]
    return chunk.strip()


def split_template(template: str) -> tuple[str, str]:
    """Split at '## 5. DCP' for phase 1 (header + §1-4) vs phase 2 (§5-7)."""
    m = re.search(r"^## 5\. DCP", template, re.MULTILINE)
    if not m:
        raise ValueError("ARCHITECT_PLAN_TEMPLATE.md: expected '## 5. DCP' heading")
    head_and_1_4 = template[: m.start()].rstrip()
    five_to_seven = template[m.start() :].strip()
    return head_and_1_4, five_to_seven


def build_phase1_user(kb: str, head_and_1_4: str) -> str:
    return (
        "## Knowledge (phase 1 — doctrine + architecture memo)\n\n"
        + kb
        + "\n\n## Instructions\n\n"
        "Complete **only** sections **1–4** of the template below (Executive summary through "
        "Gate flow). Reproduce the section headings **## 1.** … **## 4.** as in the template. "
        "Do **not** include sections 5–7 yet.\n\n"
        "### Anti-template rules (mandatory)\n\n"
        "- **Do not** copy italic placeholder lines from the template (e.g. `_3–6 sentences_`) as your "
        "final text — **replace** them with **substantive** prose grounded in the Knowledge section.\n"
        "- **Do not** wrap the entire answer in ` ```markdown ` fences.\n"
        "- Ground technical claims with **file paths** or **document section IDs** (e.g. ADD-003 §18.11).\n"
        "- **Do not** copy the \"Anti-template rules\" block into your output. Start at **## 1.** "
        "from the template.\n\n"
        "## Template (sections 1–4 only)\n\n"
        + head_and_1_4
        + "\n\nUse today's date where YYYY-MM-DD appears. Output **only** markdown — no preamble."
    )


def build_phase2_user(kb: str, five_to_seven: str) -> str:
    return (
        "## Knowledge (phase 2 — OPS-020 + ADD-003 §5.9 excerpt)\n\n"
        + kb
        + "\n\n## Instructions\n\n"
        "Complete **only** sections **5–7** of the template below (DCP table, gaps, checklist). "
        "Reproduce headings **## 5.** … **## 7.**.\n\n"
        "### OPS-020 binding (mandatory — weave into **## 5** and **## 6** prose, not only tables)\n\n"
        "You must **name** the following strings at least once each in **## 5** or **## 6** "
        "(paragraph or bullet, not hidden in table cells only): "
        "`OPS-020 §15`, `Appendix B`, `CompositionPlaneDcpV1`, and one sentence on the "
        "**addendum vs operations-standard** boundary (ADD-003 doctrine vs AIOS-OPS-020 metrics/schemas).\n\n"
        "Grounding checklist (for your reasoning — do not paste this block verbatim):\n"
        "- **§15** — implementation binding matrix; §18 ↔ §19 handoff (artifact_id alignment; "
        "optional **knowledge_basis_state** on **Appendix A**).\n"
        "- **Appendix B** — JSON Schema **`CompositionPlaneDcpV1`** "
        "(`$id` `https://aios.governance/schemas/composition-plane-dcp-v1.json`).\n"
        "- **§14** — minimum DCP envelope fields; optional **related_evaluation_record_id**.\n"
        "- **Doctrine vs ops boundary** — **ADD-003** owns normative requirements; **AIOS-OPS-020** "
        "owns metrics, evaluation record shape, DCP codes, and machine-readable schemas.\n\n"
        "### Anti-template rules (mandatory)\n\n"
        "- The **gaps** table must have **at least one** row: either a real gap from the Knowledge "
        "section or `| unknown | — | <one-line reason> |`.\n"
        "- **Do not** leave checklists empty of actionable items.\n"
        "- **Do not** wrap the entire answer in ` ```markdown ` fences.\n"
        "- **Do not** copy the instruction blocks above (\"OPS-020 binding\", \"Anti-template\") "
        "into your output — they are for you only. Your answer must **start** at **## 5.** from "
        "the template.\n\n"
        "## Template (sections 5–7 only)\n\n"
        + five_to_seven
        + "\n\nUse today's date where YYYY-MM-DD appears. Output **only** markdown — no preamble."
    )


def composite_markdown(phase1: str, phase2: str, *, merged: bool = False) -> str:
    today = date.today().isoformat()
    method = (
        "Local Ollama — phase 1 (§§1–4) + phase 2 (§§5–7); stitched deterministically."
        if not merged
        else "Local Ollama — phased phases + Ollama merge pass into single body."
    )
    if merged:
        body = f"{phase1.strip()}\n"
        return (
            f"# Architect plan — AMD-2026-008-ADD-003 (merged)\n\n"
            f"**Date:** {today}  \n"
            f"**Method:** {method}\n\n"
            f"---\n\n"
            f"{body}"
        )
    return (
        f"# Architect plan — AMD-2026-008-ADD-003 (phased composite)\n\n"
        f"**Date:** {today}  \n"
        f"**Method:** {method}\n\n"
        f"---\n\n"
        f"## Phase 1 output\n\n"
        f"{phase1.strip()}\n\n"
        f"---\n\n"
        f"## Phase 2 output\n\n"
        f"{phase2.strip()}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Phased Ollama architect for ADD-003")
    parser.add_argument("--dry-run", action="store_true", help="Print sizes and exit; no HTTP")
    parser.add_argument(
        "--ollama-merge",
        action="store_true",
        help="After phases, ask Ollama to merge into one coherent doc (replaces ARCHITECT_PLAN.md)",
    )
    args = parser.parse_args()

    host = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")

    system = read_text(SYSTEM_PROMPT)
    template_full = read_text(TEMPLATE)
    if template_full.startswith("[MISSING"):
        raise SystemExit(f"Missing template: {TEMPLATE}")

    add003 = read_text(ADD003)
    ops020 = read_text(OPS020)
    memo = read_text(MEMO)
    s59 = extract_add003_section_59(add003)

    kb1 = (
        "### AMD-2026-008-ADD-003 (full)\n\n"
        + add003
        + "\n\n### AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001\n\n"
        + memo
    )
    kb2 = (
        "### AIOS-OPS-020 (ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD)\n\n"
        + ops020
        + "\n\n### ADD-003 excerpt — §5.9 (normative fields + fail-closed)\n\n"
        + s59
    )

    head_14, five_7 = split_template(template_full)

    u1 = build_phase1_user(kb1, head_14)
    u2 = build_phase2_user(kb2, five_7)

    sys_tok = rough_tokens(len(system))
    p1_tok = rough_tokens(len(u1))
    p2_tok = rough_tokens(len(u2))
    total_p1 = sys_tok + p1_tok
    total_p2 = sys_tok + p2_tok

    print(f"Ollama: {host} | Model: {model}")
    print(f"System prompt: ~{sys_tok:,} tok (~{len(system):,} chars)")
    print(f"Phase 1 user: ~{p1_tok:,} tok (~{len(u1):,} chars) | total in ~{total_p1:,} tok")
    print(f"Phase 2 user: ~{p2_tok:,} tok (~{len(u2):,} chars) | total in ~{total_p2:,} tok")

    ctx = None if args.dry_run else ollama_model_context_length(host, model)
    if ctx is not None:
        print(f"Model context_length (from Ollama): {ctx:,} tokens")
        reserve = 6000
        if total_p1 > ctx - reserve or total_p2 > ctx - reserve:
            print(
                "WARNING: Estimated prompt may exceed context (with reserve). "
                "Use a larger-context model or trim KB."
            )
    elif not args.dry_run:
        print(
            "Context length not returned by Ollama API; assuming >=128k tok for llama3.2-class models."
        )

    if args.dry_run:
        print("Dry run: not calling Ollama.")
        return

    if not ollama_alive(host):
        print(
            "ERROR: Cannot reach Ollama. Start it (e.g. `ollama serve` or the Windows app) and "
            f"ensure `{model}` is pulled. Then re-run this script."
        )
        raise SystemExit(3)

    PLANNING.mkdir(parents=True, exist_ok=True)

    print("Running phase 1...")
    out1 = ollama_chat(host, model, system, u1)
    OUT_P1.write_text(out1.strip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT_P1.relative_to(BASE_DIR)}")

    print("Running phase 2...")
    out2 = ollama_chat(host, model, system, u2)
    OUT_P2.write_text(out2.strip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT_P2.relative_to(BASE_DIR)}")

    if args.ollama_merge:
        print("Running Ollama merge pass...")
        merge_user = (
            "Merge the following two partial architect plan fragments into **one** coherent "
            "markdown document for AMD-2026-008-ADD-003.\n\n"
            "Requirements:\n"
            "- Keep **## 1** through **## 7** **once each** (single document flow).\n"
            "- **Remove** duplicate headings, triple-backtick markdown fences wrapping the whole doc, "
            "and literal template placeholder italic lines.\n"
            "- **Preserve** substantive tables, DCP code names, and any explicit references to "
            "**OPS-020 §15**, **Appendix B**, **CompositionPlaneDcpV1**.\n"
            "- Output **only** the merged markdown — no preamble.\n\n"
            "## Fragment A\n\n"
            + out1
            + "\n\n## Fragment B\n\n"
            + out2
        )
        merged_body = ollama_chat(host, model, system, merge_user)
        final_text = composite_markdown(merged_body, "", merged=True)
    else:
        final_text = composite_markdown(out1, out2, merged=False)

    OUT_COMPOSITE.write_text(final_text.strip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT_COMPOSITE.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()

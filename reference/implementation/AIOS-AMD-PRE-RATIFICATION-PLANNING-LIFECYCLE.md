---
document_id: AIOS-AMD-PLAN-001
version: 1.0.2
status: draft
category: reference
title: Amendment pre-ratification planning lifecycle (architect → UI → committee → peer review)
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AMD-2026-005
  - doc_id: AIOS-SPEC-007
  - doc_id: AIOS-REF-013
  - doc_id: AIOS-EXEC-DEMO-001
amendment_history:
  - version: 1.0.2
    date: 2026-04-07
    summary: Cross-reference draft AIOS-EXEC-DEMO-001 (isolated execution demonstration pipeline after planning).
  - version: 1.0.1
    date: 2026-04-07
    summary: Document local Ollama automation — `build_agent_kb.py` corpus + `ollama_planning_agent.py` (Architect → UI); env vars `OLLAMA_HOST` / `OLLAMA_MODEL`.
  - version: 1.0.0
    date: 2026-04-07
    summary: Initial lifecycle — architect and UI planning packets before committee and binding peer review.
---

# Amendment pre-ratification planning lifecycle

**Purpose:** **Non-normative** workflow for amendments whose **ratification** depends on **end-to-end** alignment between **governing text** and the **product** (e.g. **AMD-2026-006** + **AIOS-SPEC-007**). It inserts **planning and committee** stages **before** the next **binding** **`peer_review.py`** round so triangulation scores **substance**, not a **stub amendment** alone.

**Binding law** remains **[AMD-2026-005](../amendments/AMD-2026-005.md)** — this lifecycle does **not** replace triangulation thresholds or Council motion.

---

## When to use

**SHOULD** use this lifecycle when **any** of the following apply:

- The amendment **ratifies** or **heavily references** a **specification** whose compliance is **proved in code** (Workspace, shell, MCP, canvas).
- Round 1 (or prior) **FAIL** cited **completeness**, **missing annexes**, or **implementation alignment**.
- **Council** or **coordinator** needs a **single packet** to approve before author edits are frozen for Round 2.

**May** skip for purely editorial amendments (coordinator judgment).

---

## Phase map

| Phase | Name | Owner | Output |
|-------|------|--------|--------|
| **A** | **Evidence** | Coordinator | Regenerated [`reference/knowledge_base/snapshots/product_context_bundle.md`](../knowledge_base/snapshots/product_context_bundle.md); [`reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_*.md`](../knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-07.md) (or successor). |
| **B** | **Architect** | Agent + human verification | **`ARCHITECT_PLAN.md`** (from [`ARCHITECT_PLAN_TEMPLATE.md`](../reviews/amd_2026_006/planning/ARCHITECT_PLAN_TEMPLATE.md)) — schemas, routes, storage/session; **every claim** cites **repo path** or **governing §**. |
| **C** | **UI** | Agent + human verification | **`UI_PLAN.md`** (from [`UI_PLAN_TEMPLATE.md`](../reviews/amd_2026_006/planning/UI_PLAN_TEMPLATE.md)) — surfaces, disclosure, Shell/Workspace behavior vs **AMD-2026-007** / **AIOS-SPEC-006**. |
| **D** | **Committee** | Council / designated reviewers | **`COMMITTEE_PACKET.md`** (from [`COMMITTEE_PACKET_TEMPLATE.md`](../reviews/amd_2026_006/planning/COMMITTEE_PACKET_TEMPLATE.md)) — approved **or** change requests; **no** ratification vote here — **informs** author revision. |
| **E** | **Author revision** | Author | Updated **AMD** + **SPEC** + [`revision_log.md`](../reviews/amd_2026_006/revision_log.md); bumped **`version`** / **`last_updated`**. |
| **F** | **Peer review (binding)** | `peer_review.py` | **Round 2** (or re-run Round 1 on **revised** text) with **`--product-context`** (default bundle **and/or** merged planning doc per coordinator). **`TARGET_DOCUMENT`** should include **normative** bulk — prefer **`specifications/...`** run or merged prompt per [`reviews/amd_2026_006/round_1/REVIEW_SYNTHESIS.md`](../reviews/amd_2026_006/round_1/REVIEW_SYNTHESIS.md) coordinator note. |

---

## Automation (local Ollama)

**Optional** tooling for Phases **B** and **C** using a **local** LLM via [Ollama](https://ollama.com/) (no cloud API required for the agent step). **Requires** `scripts/requirements.txt` (includes `httpx`) and a running Ollama server with a pulled chat model.

1. **Knowledge bundle:** `py -3 scripts/build_agent_kb.py` — reads [`reference/knowledge_base/agents/agent_kb_manifest.yaml`](../knowledge_base/agents/agent_kb_manifest.yaml), writes [`reference/knowledge_base/agents/corpus/government_and_reports_bundle.md`](../knowledge_base/agents/corpus/government_and_reports_bundle.md) (generated; gitignored). Adjust the manifest per amendment track.
2. **Architect (Phase B):** `py -3 scripts/ollama_planning_agent.py --role architect --amd-slug <slug>` — completes the template into **`reviews/<slug>/planning/ARCHITECT_PLAN.md`**.
3. **UI (Phase C):** `py -3 scripts/ollama_planning_agent.py --role ui --amd-slug <slug>` — completes **`UI_PLAN.md`** using the bundle, **and** the architect output. **Order is enforced:** the UI step **refuses** to run until **`ARCHITECT_PLAN.md`** exists (use **`--force`** only in emergencies).

**Environment:** `OLLAMA_HOST` (default `http://127.0.0.1:11434`), `OLLAMA_MODEL` (default `llama3.2`). **See:** [`reference/knowledge_base/agents/README.md`](../knowledge_base/agents/README.md).

---

## Proposed — isolated execution demonstration lane (draft)

Planning automation above produces **draft** `ARCHITECT_PLAN.md` / `UI_PLAN.md` only. A **separate non-normative proposal**, **[AIOS-EXEC-DEMO-001](AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** (*Isolated execution demonstration pipeline*), describes a **Phase X** lane that would add **branch-isolated implementation**, **repo-truth validation**, **visual evidence**, and a **human review packet** under `reviews/<slug>/execution/` — **without** replacing the planning stack or **AMD-2026-005** ratification rules.

---

## Rules

1. **Verification:** Architect and UI outputs are **drafts** until a **human** checks them against **`ai-os-voice-interface`** (diff, file open, or CI) — **no** unverified agent output becomes **normative** text without edit.
2. **Single amendment ID:** Planning artifacts live under **`reviews/<slug>/planning/`** for traceability.
3. **Registry:** After changing amendment or spec **YAML**, run **`py -3 scripts/registry_generator.py`**.
4. **Sequential execution** with other AMDs per **[AIOS-AMD-TRACKER-001](AMD-AMENDMENT-REVIEW-TRACKER-001.md)** unless Council approves overlap.

---

## Reference — product repo

Implementation memo (non-normative): **`ai-os-voice-interface`** — see **[AIOS-REF-013](AIOS-IMPLEMENTATION-RUNWAY-POINTER.md)**.

---

*End of AIOS-AMD-PLAN-001 v1.0.2.*

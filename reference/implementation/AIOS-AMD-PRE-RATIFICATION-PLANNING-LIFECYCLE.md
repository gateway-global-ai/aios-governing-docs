---
document_id: AIOS-AMD-PLAN-001
version: 1.0.4
status: draft
category: reference
title: Amendment pre-ratification planning lifecycle (architect → UI → committee → peer review)
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-005
  - doc_id: AIOS-SPEC-007
  - doc_id: AIOS-REF-013
  - doc_id: AIOS-EXEC-DEMO-001
  - doc_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
amendment_history:
  - version: 1.0.4
    date: 2026-04-10
    summary: Formalize the five-pass research family as a governed pre-architecture discovery profile inside Phase A0 when current-system mapping is needed before architect planning.
  - version: 1.0.3
    date: 2026-04-08
    summary: Phase A evidence table — CURRENT_SYSTEM_RESEARCH example path → 2026-04-08 successor.
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
| **A0** | **Discovery** | discover agent + human verification | `DISCOVERY_SCOPE.yaml`, `DISCOVERY_REPORT.md`, `DISCOVERED_KNOWLEDGE_PACKET.yaml`, and when required the five-pass pre-architecture suite under `pre_architecture/`. |
| **A** | **Evidence** | Coordinator | Regenerated [`reference/knowledge_base/snapshots/product_context_bundle.md`](../knowledge_base/snapshots/product_context_bundle.md); [`reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_*.md`](../knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md) (or dated successor). |
| **B** | **Architect** | Agent + human verification | **`ARCHITECT_PLAN.md`** (from [`ARCHITECT_PLAN_TEMPLATE.md`](../reviews/amd_2026_006/planning/ARCHITECT_PLAN_TEMPLATE.md)) — schemas, routes, storage/session; **every claim** cites **repo path** or **governing §**. |
| **C** | **UI** | Agent + human verification | **`UI_PLAN.md`** (from [`UI_PLAN_TEMPLATE.md`](../reviews/amd_2026_006/planning/UI_PLAN_TEMPLATE.md)) — surfaces, disclosure, Shell/Workspace behavior vs **AMD-2026-007** / **AIOS-SPEC-006**. |
| **D** | **Committee** | Council / designated reviewers | **`COMMITTEE_PACKET.md`** (from [`COMMITTEE_PACKET_TEMPLATE.md`](../reviews/amd_2026_006/planning/COMMITTEE_PACKET_TEMPLATE.md)) — approved **or** change requests; **no** ratification vote here — **informs** author revision. |
| **E** | **Author revision** | Author | Updated **AMD** + **SPEC** + [`revision_log.md`](../reviews/amd_2026_006/revision_log.md); bumped **`version`** / **`last_updated`**. |
| **F** | **Peer review (binding)** | `peer_review.py` | **Round 2** (or re-run Round 1 on **revised** text) with **`--product-context`** (default bundle **and/or** merged planning doc per coordinator). **`TARGET_DOCUMENT`** should include **normative** bulk — prefer **`specifications/...`** run or merged prompt per [`reviews/amd_2026_006/round_1/REVIEW_SYNTHESIS.md`](../reviews/amd_2026_006/round_1/REVIEW_SYNTHESIS.md) coordinator note. |

---

## Automation (local Ollama)

**Optional** tooling for Phases **B** and **C** using a **local** LLM via [Ollama](https://ollama.com/) (no cloud API required for the agent step). **Requires** `scripts/requirements.txt` (includes `httpx`) and a running Ollama server with a pulled chat model.

1. **Discovery (transitional local wrapper):** `py -3 scripts/run_ollama_revision_loop.py --review-slug <slug> --manifest <manifest> --step discovery` — writes `DISCOVERY_REPORT.md` and establishes a separated discovery lane before downstream architect, research, or drafting work. This is a transitional local surface until a dedicated discover runner emits `DISCOVERED_KNOWLEDGE_PACKET.yaml` directly.
2. **Knowledge bundle:** `py -3 scripts/build_agent_kb.py --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --output-dir reviews/<slug>/planning/agent_kb` — reads the lane packet and writes a lane-local bundle plus `build_manifest.json`. The neutral global corpus under [`reference/knowledge_base/agents/corpus/`](../knowledge_base/agents/corpus/README.md) remains available for manual exploratory runs but is not the default governed lane target.
3. **Architect (Phase B):** `py -3 scripts/ollama_planning_agent.py --role architect --amd-slug <slug> --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md` — completes the template into **`reviews/<slug>/planning/ARCHITECT_PLAN.md`** and writes **`ARCHITECT_PLAN.md.run_record.json`**.
4. **UI (Phase C):** `py -3 scripts/ollama_planning_agent.py --role ui --amd-slug <slug> --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md` — completes **`UI_PLAN.md`** using the lane-local bundle, the manifest identity, and the architect output. **Order is enforced:** the UI step **refuses** to run until **`ARCHITECT_PLAN.md`** exists (use **`--force`** only in emergencies). The UI run also writes **`UI_PLAN.md.run_record.json`**.

If a planning run uses bounded author-like style or narration inputs, those inputs **SHALL** be explicitly declared and remain advisory only — see **[AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001](AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md)** and **[AMD-2026-014](../../amendments/AMD-2026-014-governed-authoring-knowledge-inputs-and-bounded-author-like-drafting.md)**. They **MUST NOT** replace the planning template, repo truth, or human verification.

**Environment:** `OLLAMA_HOST` (default `http://127.0.0.1:11434`), `OLLAMA_MODEL` (default `llama3.2`). **See:** [`reference/knowledge_base/agents/README.md`](../knowledge_base/agents/README.md).

---

## Phase A0 discovery profile rule

Phase A0 has two valid shapes:

1. **packet discovery only** — use when taxonomy-first source selection is the main discovery need
2. **pre-architecture five-pass discovery** — use when the lane must first map current runtime structure before the architect planner can be trusted

The pre-architecture profile should produce:

- `pre_architecture/01_architecture_cartography.md`
- `pre_architecture/02_implicit_capability_extractor.md`
- `pre_architecture/03_governance_breach_audit.md`
- `pre_architecture/04_registry_migration_planner.md`
- `pre_architecture/05_control_plane_coverage_audit.md`

The architect planner should not be expected to rediscover those surfaces from scratch if the lane required this discovery profile.

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

*End of AIOS-AMD-PLAN-001 v1.0.3.*

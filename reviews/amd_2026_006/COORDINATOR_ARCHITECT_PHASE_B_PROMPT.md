# Coordinator prompt — AMD-2026-006 — Phase B (Architect planning)

**Purpose:** Produce **`planning/ARCHITECT_PLAN.md`** for **AMD-2026-006** / **AIOS-SPEC-007** after **Phase A** is **explicitly accepted** — not before.

**Pairing:** Run **after** [`COORDINATOR_RESEARCH_REFRESH_PROMPT.md`](COORDINATOR_RESEARCH_REFRESH_PROMPT.md) if the coordinator chose **Option B** (research refresh first). If **Option A** (bundle-only), run **after** that choice is **recorded** in [`planning/EVIDENCE-PHASE-A-STATUS.md`](planning/EVIDENCE-PHASE-A-STATUS.md) and **`product_context_bundle.md`** is current.

---

## Preconditions (all must be true)

| Gate | Check |
|------|--------|
| **Phase A decision** | [`EVIDENCE-PHASE-A-STATUS.md`](planning/EVIDENCE-PHASE-A-STATUS.md) documents **bundle-only** or **research + bundle**; coordinator has **frozen** Phase A for planning purposes. |
| **Evidence** | [`reference/knowledge_base/snapshots/product_context_bundle.md`](../../reference/knowledge_base/snapshots/product_context_bundle.md) — **Generated** date noted in **`ARCHITECT_PLAN.md`** header. |
| **Research (if Option B)** | [`reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_*.md`](../../reference/knowledge_base/cursor_research_outputs/) — **latest** file matches **`cursor_research_outputs/README.md`** “active” pointer. |

**Do not** start Phase B if Phase A is still ambiguous.

---

## Inputs (read before drafting)

| Artifact | Role |
|----------|------|
| [`amendments/AMD-2026-006.md`](../../amendments/AMD-2026-006.md) | Amendment stub — what ratification must cover |
| [`specifications/GoogleWorkspaceIntegrationGovernance.md`](../../specifications/GoogleWorkspaceIntegrationGovernance.md) | **AIOS-SPEC-007** normative bulk |
| [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md) | Round 1 **FAIL** themes — **do not** ignore |
| **`product_context_bundle.md`** | Verbatim implementation excerpts |
| **`CURRENT_SYSTEM_RESEARCH_*.md`** | Narrative / gap layer (if applicable) |
| [`planning/ARCHITECT_PLAN_TEMPLATE.md`](planning/ARCHITECT_PLAN_TEMPLATE.md) | **Structure** for output |

---

## Prompt (paste into Cursor / hand to agent)

You are working in a workspace that includes **`aios-governing-docs`** and **`ai-os-voice-interface`** (local clone).

**Task:** Create **`reviews/amd_2026_006/planning/ARCHITECT_PLAN.md`** by **filling** [`ARCHITECT_PLAN_TEMPLATE.md`](planning/ARCHITECT_PLAN_TEMPLATE.md). Replace placeholders (`YYYY-MM-DD`, `_name / role_`, table rows, narrative sections).

**Rules:**

1. **Every** technical claim about the product **must** cite a **repo path** under `ai-os-voice-interface` **or** a **governing document §** — no uncited architecture.
2. **Address** Round 1 synthesis themes: **stub vs spec**, **normative depth**, **Annex / § pointers** into **AIOS-SPEC-007** where the amendment is thin.
3. **Scope:** Architect plan only — **do not** write **`UI_PLAN.md`**, **`COMMITTEE_PACKET.md`**, or amend **AMD-2026-006** / **SPEC-007** normative text in this pass (planning draft only).
4. **Optional automation (local):** From governing-docs repo root:  
   `py -3 scripts/ollama_planning_agent.py --role architect --amd-slug amd_2026_006`  
   **If used:** output is **draft** until a **human** verifies against the real repo per **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)**.

**Output:** Single file **`planning/ARCHITECT_PLAN.md`** ready for **human verification** before **Phase C (UI)**.

---

## After the file exists

1. Human verifier **confirms** paths and claims against **`ai-os-voice-interface`**.
2. Update [`planning/README.md`](planning/README.md) — Phase **B** row → **Draft complete — pending verification** (or **Verified** when done).
3. **Then** run **Phase C** using the UI template / UI coordinator prompt (separate artifact).

---

*Non-normative coordinator artifact for AMD-2026-006 — Phase B.*

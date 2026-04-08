# Coordinator prompt — AMD-2026-006 — `CURRENT_SYSTEM_RESEARCH` refresh

**Purpose:** Close **Phase A** evidence with an **explicit** narrative/system snapshot **before** **Phase B (Architect)** planning, when the coordinator chooses **not** to rely on **`product_context_bundle.md`** alone.

**When to use:** After **`product_context_bundle.md`** has been regenerated (see [`planning/EVIDENCE-PHASE-A-STATUS.md`](planning/EVIDENCE-PHASE-A-STATUS.md)). **Recommended for AMD-2026-006** because Round 1 **FAIL** — a disciplined evidence base reduces weak planning risk.

**Alternative:** If the coordinator **accepts** only the refreshed bundle as the implementation anchor, **skip** this pass and proceed to **Architect**; record that decision in **`EVIDENCE-PHASE-A-STATUS.md`**.

---

## Decision record (fill in)

| Field | Value |
|-------|--------|
| **Coordinator decision** | ☑ **Option B** — Run this research refresh first (**executed 2026-04-08** — [`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`](../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md)) |
| **Date** | **2026-04-08** |
| **Rationale** | Phase A Option B — successor research before Architect ([`EVIDENCE-PHASE-A-STATUS.md`](planning/EVIDENCE-PHASE-A-STATUS.md)). |

---

## Prompt (paste into Cursor / hand to agent)

You are working in a **multi-root** or **side-by-side** workspace that includes:

1. **`aios-governing-docs`** (this repo)
2. **`ai-os-voice-interface`** at a known local path (e.g. `C:\Apps\ai-os-voice-interface`)

**Objective:** Produce a **new** file:

`aios-governing-docs/reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_YYYY-MM-DD.md`

Use **today’s date** in the filename (replace `YYYY-MM-DD`).

**Method (aligned with existing research):** **Repository inspection** — file reads, structure scan, targeted `grep` — **not** invented architecture. The prior model is **[`CURRENT_SYSTEM_RESEARCH_2026-04-07.md`](../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-07.md)** and **[`cursor_research_pack.md`](../../reference/knowledge_base/cursor_research_pack.md)**. **Supersede** outdated narrative where the tree has changed; **cite file paths** for every claim.

**Scope for AMD-2026-006 / AIOS-SPEC-007 alignment:**

- Workspace routing: `workspaceIntentRouter`, `integrationControlPlane`, `mcpAdapter`, `mcpIntentToolMap`, `intentRegistry`, `scopeClasses`
- Shell / canvas: how Workspace surfaces relate to `WorkspaceCanvasContext`, `canvasTypes`, onboarding/hub flows
- **Gap hunt:** what the **governing** docs assume vs what the **repo** implements (no speculation; mark **unknown** if not in tree)

**Non-goals:**

- Do **not** edit **AMD-2026-006** or **specifications/GoogleWorkspaceIntegrationGovernance.md** in this pass (research only).
- Do **not** produce **ARCHITECT_PLAN** or **UI_PLAN** (Phase B/C).

**After writing the file:**

1. Update **[`reference/knowledge_base/cursor_research_outputs/README.md`](../../reference/knowledge_base/cursor_research_outputs/README.md)** so the **active** current research line points to the **new** file.
2. Append a row to **`reviews/amd_2026_006/planning/EVIDENCE-PHASE-A-STATUS.md`** — **CURRENT_SYSTEM_RESEARCH** completed with date + filename.
3. Optionally note in **`reviews/amd_2026_006/revision_log.md`** that Phase A narrative evidence is complete.

**Human verification:** Coordinator skims the new file for obvious mistakes, then **freezes Phase A** and authorizes **Phase B** per **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)**.

---

*Non-normative coordinator artifact for AMD-2026-006.*

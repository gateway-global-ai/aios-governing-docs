# Committee review packet — AMD-2026-006 / AIOS-SPEC-007

**Date:** 2026-04-08  
**Reviewers:** Maintainer / coordinator (single approver — recorded in §3)  
**Purpose:** **Advisory** sign-off that **planning** (Phases A–C) is **complete enough** to authorize **author revision** toward **Round 2** — **not** ratification (**[AMD-2026-005](../../../amendments/AMD-2026-005.md)** + Council motion still apply).

**Phase E:** **Authorized** — §3 recorded. **[`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md)** and **[`UI_PLAN.md`](UI_PLAN.md)** approved **with no changes** to those planning files.

---

## 1. Cover summary

| Item | Status / link |
|------|----------------|
| Amendment | [`AMD-2026-006.md`](../../../amendments/AMD-2026-006.md) — Round 1 **FAIL** — [`round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md) |
| Specification | [`GoogleWorkspaceIntegrationGovernance.md`](../../../specifications/GoogleWorkspaceIntegrationGovernance.md) (**AIOS-SPEC-007**) |
| Evidence (Phase A) | [`product_context_bundle.md`](../../../reference/knowledge_base/snapshots/product_context_bundle.md); [`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`](../../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md) — **Accepted** |
| Architect (Phase B) | [`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md) — **Verified** |
| UI (Phase C) | [`UI_PLAN.md`](UI_PLAN.md) — **Accepted** 2026-04-08 |

---

## 2. Decision questions

Answer each: **Approve** / **Revise** / **Reject** (one line each; optional comment).

1. **Normative depth:** Is the **implementation mapping** in [`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md) (envelope, ICP, routes) **sufficient** to drive **AIOS-SPEC-007** redlines (including annex / § tables addressing Round 1 **Completeness**), or do you require **more** planning before author work?
2. **Hub fallback UX:** [`UI_PLAN.md`](UI_PLAN.md) documents **`workspace_hub`** fallback for e.g. `workspace.calendar.events.list`, **`workspace.docs.*`**, **tasks** — **acceptable MVP** for Round 2 narrative, or **must** the product or spec add dedicated surfaces **before** author revision?
3. **Shell vs Workspace:** Any **material conflict** with **AMD-2026-007** / **AIOS-SPEC-006** given the documented split (**`shellIntentRouter.ts`** vs Workspace canvas + ICP)?
4. **Round 2 target:** Confirm **`peer_review.py`** should target **primarily** **`specifications/GoogleWorkspaceIntegrationGovernance.md`** (per Round 1 coordinator note), **or** insist on a **merged** AMD+SPEC target — **which**?

**Recorded answers (2026-04-08):**

| # | Answer | Comment |
|---|--------|---------|
| 1 | **Approve** | Implementation mapping sufficient to drive **AIOS-SPEC-007** redlines. |
| 2 | **Approve** | Hub fallback documented in **UI_PLAN** is **acceptable MVP** for Round 2 narrative; **no** product/spec surface mandate **before** author revision. |
| 3 | **Approve** | **No** material conflict with **AMD-2026-007** / **AIOS-SPEC-006** as documented. |
| 4 | **Approve** | **Primary** **`peer_review.py`** target: **`specifications/GoogleWorkspaceIntegrationGovernance.md`** (per [`round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md) coordinator note); merged AMD+SPEC prompt **optional** at coordinator discretion. |

---

## 3. Committee outcome

| Field | Value |
|-------|--------|
| **Outcome** | **Approved** (planning complete; **no** changes required to **ARCHITECT_PLAN** / **UI_PLAN**) |
| **Recorded by** | Maintainer (approver in thread) |
| **Date** | 2026-04-08 |

**Author instructions:** **[`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md)** and **[`UI_PLAN.md`](UI_PLAN.md)** — **freeze as-is** (no replanning). **Phase E:** revise **[`AMD-2026-006.md`](../../../amendments/AMD-2026-006.md)** and **[`GoogleWorkspaceIntegrationGovernance.md`](../../../specifications/GoogleWorkspaceIntegrationGovernance.md)** to close Round 1 gaps (**Completeness**, annex / § mapping, cross-refs) using **accepted** evidence and planning; bump **`version`** / **`last_updated`**; log in **[`revision_log.md`](../revision_log.md)**.

---

## 4. Next step

| Step | Owner | When |
|------|--------|------|
| ~~Record **§3**~~ | Committee | **Done** 2026-04-08 |
| ~~Author revision (**Phase E**)~~ | Amendment author | **Done** 2026-04-08 — **[AMD-2026-006](../../../amendments/AMD-2026-006.md)** **v0.2.0**, **[AIOS-SPEC-007](../../../specifications/GoogleWorkspaceIntegrationGovernance.md)** **v0.2.0** |
| `revision_log.md` + freeze | Author | **Done** — [`../revision_log.md`](../revision_log.md) |
| **`peer_review.py` Round 2** (`--product-context`) | Coordinator | **Next** — [`../round_2/README.md`](../round_2/README.md) |

See **[AIOS-AMD-PLAN-001](../../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** Phase F.

---

*Phase D complete — **Approved** 2026-04-08 — **Phase E** authorized.*

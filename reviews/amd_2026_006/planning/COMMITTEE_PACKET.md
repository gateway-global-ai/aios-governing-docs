# Committee review packet — AMD-2026-006 / AIOS-SPEC-007

**Date:** 2026-04-08  
**Reviewers:** _assign at review time_  
**Purpose:** **Advisory** sign-off that **planning** (Phases A–C) is **complete enough** to authorize **author revision** toward **Round 2** — **not** ratification (**[AMD-2026-005](../../../amendments/AMD-2026-005.md)** + Council motion still apply).

**Blocking rule:** **Do not** start **Phase E** (AMD + SPEC edits) until **§3** below is filled with **real** committee input. This file is **not** an author instruction by itself.

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

---

## 3. Committee outcome

| Field | Value |
|-------|--------|
| **Outcome** | _Pending — not filled_ |
| **Recorded by** | |
| **Date** | |

**Author instructions (after outcome only):** _Committee fills when ready — **empty until then**._

---

## 4. Next step

| Step | Owner | When |
|------|--------|------|
| Record **§3** | Committee / designated reviewers | After review |
| Author revision (**Phase E**) | Amendment author | **After** §3 **Approve** or **Approved with changes** |
| `revision_log.md` + version bumps | Author | With E |
| **`peer_review.py` Round 2** (`--product-context`) | Coordinator | **After** E |

See **[AIOS-AMD-PLAN-001](../../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** Phase F.

---

*Packet issued for committee scheduling — **Phase D** — 2026-04-08.*

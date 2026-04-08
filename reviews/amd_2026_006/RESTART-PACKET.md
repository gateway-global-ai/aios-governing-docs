# AMD-2026-006 — governed restart packet

**Purpose:** Declare **AMD-2026-006** as the **active** cohesion-critical track (**006 → 009 → 008**) and record **what failed**, **what exists**, and the **next disciplined steps** under **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** — **not** to complete the amendment in one pass.

**Amendment:** [`../../amendments/AMD-2026-006.md`](../../amendments/AMD-2026-006.md) — **v0.1.0** `draft`.  
**Normative bulk (ratification target):** [`../../specifications/GoogleWorkspaceIntegrationGovernance.md`](../../specifications/GoogleWorkspaceIntegrationGovernance.md) — **AIOS-SPEC-007**.

---

## 1. Why 006 is next

Per **[AMD-AMENDMENT-REVIEW-TRACKER-001](../../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)** foundation order, **AMD-2026-006** is **first** among the remaining **draft** cohesion-critical amendments: it locks **Workspace → control plane → MCP** and **AIOS-SPEC-007** before **009** (web/envelope) and **008** (local runtime). **AMD-001** is **classified** separately and does **not** block this track.

---

## 2. What Round 1 failure implies

- **[AMD-2026-005](../../amendments/AMD-2026-005.md)** numerical gate **failed**: mean composite **2.7**; dimension floor **1**; composites not all **≥ 3.5**.
- **Themes:** stub vs spec (need normative depth / annexes or explicit **§** pointers into **SPEC-007**); cross-document consistency; completeness.
- **Consequence:** **No** Round 2 until **author revision** informed by **AIOS-AMD-PLAN-001** planning outputs. **TARGET_DOCUMENT** scope for a future run should follow **[`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md)** coordinator note (amendment-only vs **SPEC-007**-heavy run).

---

## 3. What must happen next (AMD-PLAN-001)

| Phase | Artifact | Status (this repo) |
|-------|-----------|---------------------|
| **A — Evidence** | Regenerated `product_context_bundle`; current Cursor research snapshot | **Exists but stale** — **refresh** before architect |
| **B — Architect** | `planning/ARCHITECT_PLAN.md` | **Missing** — from [`planning/ARCHITECT_PLAN_TEMPLATE.md`](planning/ARCHITECT_PLAN_TEMPLATE.md) |
| **C — UI** | `planning/UI_PLAN.md` | **Missing** — from template; **after** B |
| **D — Committee** | `planning/COMMITTEE_PACKET.md` | **Missing** — from template |
| **E — Author revision** | `revision_log.md` + **AMD-2026-006** + **AIOS-SPEC-007** | **After** committee approval / change requests |
| **F — Peer review** | `round_2/` | **After** E |

**Blockers before Round 2:** Phases **A–D** satisfied per coordinator (human-verified drafts for B/C); **E** complete with version bumps logged.

---

## 4. What can be deferred

- **Round 2** / ratification motion / council vote.
- **Optional** isolated execution demo (`reviews/amd_2026_006/execution/`) per **[AIOS-EXEC-DEMO-001](../../reference/implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** — **not** required to **open** the planning cycle.
- **AMD-2026-009** / **008** work.

---

## 5. Success criteria for “track reopened”

- Evidence artifacts **refreshed** (Phase A) with a dated note in `planning/README.md` or this packet’s successor revision log entry.
- **ARCHITECT_PLAN.md** and **UI_PLAN.md** exist as **drafts** from templates (or Ollama scripts) **and** are **human-verified** per **AIOS-AMD-PLAN-001** rules.
- **COMMITTEE_PACKET.md** ready for committee review.
- **Author revision** then addresses Round 1 themes + committee; **revision_log** records versions.

---

## 6. Earliest next pass (coordinator choice)

**Phase A — evidence refresh** — regenerate [`reference/knowledge_base/snapshots/product_context_bundle.md`](../../reference/knowledge_base/snapshots/product_context_bundle.md) and refresh or supersede [`reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-07.md`](../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-07.md) so **Architect** (Phase B) cites **current** repo truth.

---

*Restart packet — non-normative; amend only via governed edits.*

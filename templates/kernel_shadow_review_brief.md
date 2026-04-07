---
artifact: kernel_shadow_review_brief
status: template
binding: false
normative_basis: AMD-2026-010 v0.2.0
---

# Kernel shadow review brief — {DOCUMENT_ID} @ {VERSION}

| Field | Value |
|-------|--------|
| **Target** | `{path/to/document.md}` |
| **Triangulation round** | e.g. parallel to **Round 1** or **Round 2** (record which) |
| **Kernel reviewer(s)** | Name(s) or role — **Kernel Engineer** or delegate |
| **Date** | ISO date |
| **AMD-2026-010** | [§4.2 focus areas](../amendments/AMD-2026-010.md#42-kernel-review-lane); [§4.4 advisory status](../amendments/AMD-2026-010.md#44-legal-status-of-pilot-findings-normative) |

## Purpose (read first)

This brief drives a **kernel shadow** pass — **not** a substitute for **[AMD-2026-005](../amendments/AMD-2026-005.md)** triangulated peer review.

- **Triangulated committee** = **binding** dispositions for ratification gates.
- **Kernel shadow** = **advisory** findings for **pilot metrics** and architecture focus only (**AMD-2026-010 §4.4**).

## Role of the kernel reviewer

- Apply **specialist** attention to **shell / state / authority / routing / voice–UI parity** coherence with **[AMD-2026-007](../amendments/AMD-2026-007.md)** (shell vs skills, primary vs operator) and **AIOS-SPEC-006** / **AIOS-SPEC-009** where relevant.
- **Do not** re-score the full 11-dimension rubric unless asked to assist editorially — that remains the **committee** job.
- **Do not** assert blocking merges, veto ratification, or replace Round 1/2 outputs.

## What to check (focus)

| Area | Look for |
|------|----------|
| **Shell invariants** | Shell state, command rail, or UI text that **conflates** shell control with **skills** / domain execution (**POL-SHELL** alignment). |
| **State / skill boundary** | Ambiguous language that could **smuggle** domain execution into shell doctrine. |
| **Authority / disclosure** | Primary vs operator / diagnostics presentation; **truthful** disclosure of “where am I / what is blocked?”. |
| **Routing** | Ambiguity for `app.*` vs `governance.*` vs `workspace.*` vs local lanes where normative. |
| **Voice/UI parity** | Required shell affordances vs **[AMD-2026-007](../amendments/AMD-2026-007.md)** §4.1 class of obligations. |
| **Session truth** | Composed session or chrome language that is **misleading** or collapses dimensions. |

## What not to overreach into

- General **editorial polish** or **legal/compliance** review (committee lanes).
- **Vendor MCP** implementation details (unless they **break** routing or disclosure invariants).
- **Business model** or **platform economics** except where a kernel defect clearly implicates them.

## Output

Complete **`KERNEL_SHADOW_FINDINGS.md`** (see [template](kernel_shadow_findings.md)) in the same `kernel/` folder as this brief.

---

*Template — copy to `reviews/{slug}/kernel/KERNEL_SHADOW_BRIEF.md` when starting a pilot run.*

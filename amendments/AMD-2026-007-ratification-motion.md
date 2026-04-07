---
document_id: AMD-2026-007-RATIFICATION-MOTION
subject_amendment: AMD-2026-007
subject_version: 0.2.1
motion_version: 1.0.0
status: approved
category: council_motion
title: Ratification motion — AMD-2026-007
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
approved: 2026-04-07
execution_path: amendments/AMD-2026-007.md §14 Ratification checklist
---

# Ratification motion — AMD-2026-007

## Statement

Council is asked to **ratify** **[AMD-2026-007](AMD-2026-007.md)** at **version 0.2.1** (*Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI*), as the governing amendment for the **intent primitive**, **shell affordances**, **primary vs operator UI**, and **shell-state vs skills** doctrine, after **peer review Round 2** (triangulated) recorded under `reviews/amd_2026_007/round_2/`. *(Version 0.2.1 adds editorial clarity: §11.9.2 normative non-duplication with **AIOS-SPEC-009**; §11.9.3 “documented” scope for **POL-SHELL-005**; Round 1 non-blocking items addressed without broadening normative scope.)*

## Scope (what this ratifies)

AMD-2026-007 **defines** (non-exhaustive):

| Area | Summary |
|------|---------|
| **Intent primitive (§11)** | Single governed **Intent** object, lifecycle, modalities as expression paths, alignment with **AIOS-SPEC-009**. |
| **Shell vs skills (§11.9)** | **POL-SHELL-004**–**006**; shell **routing/state** **≠** capability-registry **skills**; **§11.9.2** clarifies **§11.9** governs **shell-state** only — **AIOS-SPEC-009** remains canonical for **domain** intent lifecycle/execution semantics. |
| **Voice parity (POL-SHELL-005)** | Parity **within** **documented** shell affordances and policy (**§11.9.3**). |
| **Bootstrap (POL-SHELL-006)** | Narrow engineering exception where stated. |
| **Specs / merges** | Normative propagation **§6**; **not** executed by this motion alone — **§14** **checklist** governs post-ratification execution. |

## Authority (effect upon ratification)

Upon **approval**, the following **SHALL** apply:

1. **AMD-2026-007** becomes **ratified** governing text for this domain; repository state **SHALL** be updated per **Immediate actions** below.
2. **§14 Ratification checklist** in **[AMD-2026-007](AMD-2026-007.md)** is the **authorized execution path** from ratification → policy index entries → spec merges listed in §6 / §14.

## Immediate actions (after approval)

| Step | Action |
|------|--------|
| 1 | **Amendment record:** Set **AMD-2026-007** `status` to **`ratified`** (or Council-equivalent), set **`ratification_target`** to the **ratification date** (ISO), update **`last_updated`**, and record this motion id / date in **`amendment_history`**. |
| 2 | **§14:** Complete **ratification checklist** (governance sign-off, policy register / **POL-SHELL-004**–**006** in master policy index, SPEC-006/007/008 / Domain Pack per §6). |
| 3 | **Child specs:** Update **`amendment_history`** on affected specifications per §6 merges. |

## Deferred items (explicitly not blocking ratification)

- **Policy annex format** for POL-SHELL-005 disclosure detail — may be refined **after** ratification provided **§11.9.3** **minimum** **is** **met**.
- **Implementation** wiring in application repos — follows ratified specs and merges, not this motion alone.

## Decision

| Option | Council use |
|--------|-------------|
| **Approve** | Ratify AMD-2026-007 v0.2.1; execute **§14** as **Authority** above. |
| **Reject** | No normative status change under this motion; amendment remains **draft** until revised. |
| **Amend** | Council records conditions; **SHALL** produce a revised amendment version or supplementary motion before **§14** execution proceeds. |

---

## Execution record (in-repo)

| Field | Value |
|-------|--------|
| **Executed** | 2026-04-07 |
| **AMD-2026-007** | `status: ratified`, `ratification_target: "2026-04-07"` (v0.2.1) |
| **Policy index** | [`reference/AIOS_POLICY_INDEX.md`](../reference/AIOS_POLICY_INDEX.md) |

**§6** specification merges and child-spec `amendment_history` updates are **not** claimed complete in this execution record (follow-on per AMD-2026-007 §14).

---

*End of ratification motion — AMD-2026-007, motion version 1.0.0.*

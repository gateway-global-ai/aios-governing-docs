---
document_id: AMD-2026-010-RATIFICATION-MOTION
subject_amendment: AMD-2026-010
subject_version: 0.2.0
motion_version: 1.0.0
status: approved
category: council_motion
title: Ratification motion — AMD-2026-010
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-08
approved: 2026-04-08
execution_path: amendments/AMD-2026-010.md §9 Ratification checklist
---

# Ratification motion — AMD-2026-010

## Statement

Council is asked to **ratify** **[AMD-2026-010](AMD-2026-010.md)** at **version 0.2.0** (*Kernel Engineer Role and Specialist Kernel Review Lane (Shadow Pilot)*), after **peer review Round 2** (triangulated: DeepSeek, OpenAI, Gemini) recorded under `reviews/amd_2026_010/round_2/`, with **REVIEW_SYNTHESIS.md** and **RATIFICATION_GATE_REPORT.md** confirming **AMD-2026-005** numerical gates and **READY_FOR_RATIFICATION** peer-review readiness.

**Version 0.2.0** adds **§4.4 Legal status of pilot findings (NORMATIVE)** — explicit **advisory / non-binding** status of kernel pilot outputs for ratification gates, per Round 2 consensus (notably Gemini review).

## Scope (what this ratifies)

AMD-2026-010 **defines** (non-exhaustive):

| Area | Summary |
|------|---------|
| **Kernel Engineer** | Role charter for shell control plane integrity, state invariants, authority/disclosure, command rail semantics, action classification, anti-drift (§4.1). |
| **Kernel review lane** | Specialist focus areas for shell/state/authority/routing parity (§4.2). |
| **Triangulation preserved** | **SHALL NOT** replace Round 1/2 triangulation during pilot (§4.3); **AMD-2026-005** thresholds unchanged by this amendment. |
| **Pilot findings** | **§4.4** — kernel outputs **advisory and non-binding** for ratification; triangulated path remains sole **binding** disposition **unless** follow-on authorizes otherwise. |
| **Shadow rollout & evaluation** | §§5–6 — parallel, non-blocking pilot; measurable criteria. |

## Authority (effect upon ratification)

Upon **approval**, the following **SHALL** apply:

1. **AMD-2026-010** becomes **ratified** governing text for this process domain; repository state **SHALL** be updated per **Immediate actions** below.
2. Programs **MAY** assign **Kernel Engineer(s)** and run **kernel shadow review** per §§5–8; pilot findings remain **non-blocking** for gates **until** a follow-on amendment or Council decision changes that.

## Immediate actions (after approval)

| Step | Action |
|------|--------|
| 1 | **Amendment record:** Set **AMD-2026-010** `status` to **`ratified`**, set **`ratification_target`** to the **ratification date** (ISO), update **`last_updated`**, record this motion id / date in **`amendment_history`**. |
| 2 | **Policy index:** Record **AMD-2026-010** in **[reference/AIOS_POLICY_INDEX.md](../reference/AIOS_POLICY_INDEX.md)** (no new **POL-*** ids — process amendment). |
| 3 | **CHANGELOG** and **DOCUMENT_REGISTRY** — regenerate registry after front-matter updates. |

## Deferred items (explicitly not blocking ratification)

- Optional **kernel rubric annex** or **§4.1** concrete examples — may be added in a **revision** or **operational runbook** without blocking ratification of v0.2.0.
- **Blocking** kernel gate — **explicitly** deferred to **follow-on** amendment after pilot evaluation (§10).

## Decision

| Option | Council use |
|--------|-------------|
| **Approve** | Ratify AMD-2026-010 v0.2.0; execute **Immediate actions** above. |
| **Reject** | No normative status change under this motion; amendment remains **draft** until revised. |
| **Amend** | Council records conditions; **SHALL** produce a revised amendment version or supplementary motion. |

---

## Execution record (in-repo)

| Field | Value |
|-------|--------|
| **Executed** | 2026-04-08 |
| **AMD-2026-010** | `status: ratified`, `ratification_target: "2026-04-08"` (v0.2.0) |
| **Policy index** | [`reference/AIOS_POLICY_INDEX.md`](../reference/AIOS_POLICY_INDEX.md) — AMD-2026-010 entry (process; no new POL-* ids) |
| **Peer review** | [`reviews/amd_2026_010/round_2/`](../reviews/amd_2026_010/round_2/) |

---

*End of ratification motion — AMD-2026-010, motion version 1.0.0.*

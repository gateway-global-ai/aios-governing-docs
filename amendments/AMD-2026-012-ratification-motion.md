---
document_id: AMD-2026-012-RATIFICATION-MOTION
subject_amendment: AMD-2026-012
subject_version: 1.0.0
motion_version: 1.0.0
status: approved
category: council_motion
title: Ratification motion — AMD-2026-012
author: Gateway Global AIOS
created: 2026-04-11
last_updated: 2026-04-11
approved: 2026-04-11
execution_path: amendments/AMD-2026-012.md (peer review complete; policy index)
---

# Ratification motion — AMD-2026-012

## Statement

Council is asked to **ratify** **[AMD-2026-012](AMD-2026-012.md)** at **version 1.0.0** (*Shell Authority and Voice-First Entry*), after **peer review Round 2 Pass C** (triangulated: DeepSeek, OpenAI, Gemini) on **v0.1.3** text recorded under `reviews/amd_2026_012/round_2/`, with **[REVIEW_SYNTHESIS.md](../reviews/amd_2026_012/round_2/REVIEW_SYNTHESIS.md)** and **[RATIFICATION_GATE_REPORT.md](../reviews/amd_2026_012/round_2/RATIFICATION_GATE_REPORT.md)** confirming **[AMD-2026-005](AMD-2026-005.md)** numerical gates (**composite ≥ 3.5**, **no dimension < 3**) and **READY_FOR_RATIFICATION** peer-review readiness.

**Version 1.0.0** is the **ratified** release of text frozen at **v0.1.3** substantive content: Shell as single entry and session authority; **§7** finite primary-outcome family with control-plane mapping; **§4.4** auditable fallback; **§8.4.1** interim binding UX defaults; **§4.2** audit and economic **presentation** authority; subordinate skills/tools and governance/admin separation.

## Scope (what this ratifies)

AMD-2026-012 **defines** (non-exhaustive):

| Area | Summary |
|------|--------|
| **Single entry & session authority** | §§4–6 — Shell governs entry, identity, fallback, journey; **new vs returning** before tool posture. |
| **Finite outcomes (§7)** | Shell-exposed primary outcome family; mapping to control-plane / **AIOS-SPEC-009** session objects. |
| **Voice-first & §8.4.1** | Interim numeric defaults; subordinate policy may tighten. |
| **Subordinate tools / §9** | Skills, Kits, Workspace as subordinate; **§9.4** marketplace boundary. |
| **Transparency / control plane** | §§10, 14 — consistent readiness; UI defers to control plane. |
| **Prohibited patterns / separation** | §§12–13 — no dashboard-first default; admin/governance separate from end-user Shell. |

## Authority (effect upon ratification)

Upon **approval**, the following **SHALL** apply:

1. **AMD-2026-012** becomes **ratified** governing text for **Shell authority and voice-first entry** for the AI OS product model; repository state **SHALL** be updated per **Immediate actions** below.
2. **Implementation** in application and control-plane repositories **SHALL** align with this amendment **as a separate workstream** — ratification **does not** substitute for code change tracking.

## Immediate actions (after approval)

| Step | Action |
|------|--------|
| 1 | **Amendment record:** Set **AMD-2026-012** `status` to **`ratified`**, **`version`** to **`1.0.0`**, **`ratification_target`** to **`2026-04-11`**, update **`last_updated`**, record motion in **`amendment_history`**. |
| 2 | **Policy index:** Record **AMD-2026-012** in **[reference/AIOS_POLICY_INDEX.md](../reference/AIOS_POLICY_INDEX.md)** (no new **`POL-*`** identifiers — doctrine amendment). |
| 3 | **CHANGELOG** and **`DOCUMENT_REGISTRY`** — regenerate registry after front-matter updates. |

## Deferred items (explicitly not blocking ratification)

- Optional **§7** schema examples, mapping failure modes, and developer annexes — **non-blocking** follow-on in **AIOS-SPEC-009** or implementation docs.
- **Product** control-plane cleanup (governance manager removal, Workspace subordination, §7 alignment) — **post-ratification** execution.

## Decision

| Option | Council use |
|--------|-------------|
| **Approve** | Ratify AMD-2026-012 v1.0.0; execute **Immediate actions** above. |
| **Reject** | No normative status change under this motion; amendment remains **draft** until revised. |
| **Amend** | Council records conditions; **SHALL** produce a revised amendment version or supplementary motion. |

---

## Execution record (in-repo)

| Field | Value |
|-------|--------|
| **Executed** | 2026-04-11 |
| **AMD-2026-012** | `status: ratified`, `version: 1.0.0`, `ratification_target: "2026-04-11"` |
| **Policy index** | [`reference/AIOS_POLICY_INDEX.md`](../reference/AIOS_POLICY_INDEX.md) — AMD-2026-012 entry |
| **Peer review** | [`reviews/amd_2026_012/round_2/`](../reviews/amd_2026_012/round_2/) Pass C on v0.1.3 |

---

*End of ratification motion — AMD-2026-012, motion version 1.0.0.*

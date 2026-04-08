---
document_id: AIOS-AMD-TRACKER-001
version: 1.0.9
status: draft
category: reference
title: Outstanding amendments — governed review tracker
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AMD-2026-006
  - doc_id: AMD-2026-007
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-009
  - doc_id: AMD-2026-005
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AMD-2026-013
  - doc_id: AIOS-COMMITTEE-BRIEF-AMD-2026-013
amendment_history:
  - version: 1.0.9
    date: 2026-04-07
    summary: AMD-2026-013 ratified v1.0.0 — AMD-2026-013-RATIFICATION-MOTION v1.0.0; AIOS-REPO-TAXONOMY-001 v1.0.0; AIOS_POLICY_INDEX v1.3.0.
  - version: 1.0.8
    date: 2026-04-08
    summary: AMD-2026-013 Round 2 PASS — v0.2.3 revision_log; reviews/amd_2026_013/round_2; R1→R2 delta.
  - version: 1.0.7
    date: 2026-04-08
    summary: AMD-2026-013 Round 1 triangulation PASS — reviews/amd_2026_013/round_1; v0.2.2 frozen.
  - version: 1.0.6
    date: 2026-04-08
    summary: AMD-2026-013 review packet column — COMMITTEE-REVIEW-BRIEF-AMD-2026-013; v0.2.1 pointer.
  - version: 1.0.5
    date: 2026-04-08
    summary: AMD-2026-013 draft row — intent-bearing repository taxonomy; AIOS-REPO-TAXONOMY-001.
  - version: 1.0.4
    date: 2026-04-07
    summary: AIOS-AMD-PLAN-001 pre-ratification lifecycle; amd_2026_006/planning/ for architect → UI → committee before Round 2.
  - version: 1.0.3
    date: 2026-04-07
    summary: AMD-2026-006 Round 1 complete — FAIL gate; next revision + Round 2.
  - version: 1.0.2
    date: 2026-04-07
    summary: Peer review packet opened for AMD-2026-006 — reviews/amd_2026_006/ (Round 1).
  - version: 1.0.1
    date: 2026-04-07
    summary: Reframed execution as sequential (one active governed track at a time); renamed file from AMD-PARALLEL-REVIEW-TRACKER-001.md.
  - version: 1.0.0
    date: 2026-04-07
    summary: Initial tracker — AMD-2026-007 reconciled; 006 / 008 / 009 backlog rows.
---

# Outstanding amendments — governed review tracker

**Purpose:** Single **non-normative** place to track **AMD-2026-006** through **AMD-2026-009** under **AMD-2026-005** (triangulation, synthesis, ratification gate, council motion). **Execution is sequential:** advance **one** amendment through its **binding** peer-review and ratification steps **before** treating the next as the **active** governed track, unless **council** explicitly authorizes overlap. Each row links the **authoritative** amendment file and **reviews/** packet (if any).

---

## Status snapshot

| Amendment | `status` (YAML) | Review packet | Next governed step |
|-----------|-----------------|---------------|---------------------|
| **AMD-2026-006** | `draft` | [`reviews/amd_2026_006/`](../../reviews/amd_2026_006/README.md) | **AIOS-AMD-PLAN-001** — [`planning/`](../../reviews/amd_2026_006/planning/README.md) (architect / UI / committee) **then** author revision **then** **Round 2** |
| **AMD-2026-007** | **`ratified`** **v0.2.1** | [`reviews/amd_2026_007/`](../reviews/amd_2026_007/README.md) | **Follow-on:** §6 spec merges, §14 unchecked items; see amendment **§14** |
| **AMD-2026-008** | `draft` | [`reviews/amd_2026_008/`](../reviews/amd_2026_008/) (R2, R3) | **Close gate:** `REVIEW_SYNTHESIS` + `RATIFICATION_GATE_REPORT` for latest round; motion; council |
| **AMD-2026-009** (+ addenda) | `draft` | [`reviews/amd_2026_009/`](../reviews/amd_2026_009/) | **Round 2** synthesis positive — **next:** finalize motion **[`amendments/AMD-2026-009-ratification-motion.md`](../amendments/AMD-2026-009-ratification-motion.md)**; council; **§10** spec-merge checklist |
| **AMD-2026-013** | **`ratified` `1.0.0`** | [`reviews/amd_2026_013/`](../reviews/amd_2026_013/README.md) — Round 2 **PASS** on **v0.2.3**; ratified **[`AMD-2026-013-ratification-motion.md`](../../amendments/AMD-2026-013-ratification-motion.md)** **2026-04-07** | **Follow-on:** product/architecture alignment; memo **[AIOS-REPO-TAXONOMY-001](AIOS-REPO-TAXONOMY-001.md)** **v1.0.0** |

---

## Operating rules

1. **Sequencing:** Prefer **one** active **AMD-2026-005** cycle (reviews → synthesis → gate → motion) on **one** amendment ID at a time; **hand off** or **park** the prior track before **opening** the next **binding** round, unless **council** approves otherwise.
2. **No** skipping **AMD-2026-005** numerical gates or **triangulation** for **ratification** claims.
3. **Registry:** After any governed amendment front-matter change, run **`py -3 scripts/registry_generator.py`**.

---

## AMD-2026-007 reconciliation (complete)

Canonical **[`amendments/AMD-2026-007.md`](../amendments/AMD-2026-007.md)** now matches **v0.2.1** **ratified** text expected by **Round 2** and the **executed** ratification motion. See **[`reviews/amd_2026_007/README.md`](../reviews/amd_2026_007/README.md)**.

---

*End of AIOS-AMD-TRACKER-001 v1.0.9.*

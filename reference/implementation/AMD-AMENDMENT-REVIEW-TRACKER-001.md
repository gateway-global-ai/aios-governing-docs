---
document_id: AIOS-AMD-TRACKER-001
version: 1.1.0
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
  - version: 1.1.0
    date: 2026-04-07
    summary: Foundation cohesion section — explicit closure order for remaining draft AMDs 006 → 009 (+ addenda) → 008; ratified substrate named.
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

## Foundation cohesion — remaining AMD closure order

**Goal:** Name which **substantive** amendments are still **cohesion-critical** for a **complete foundation** (control plane + acquisition paths + runtime), and the **preferred closure order**. This is **non-normative** planning guidance; **[AMD-2026-005](../amendments/AMD-2026-005.md)** process law still governs peer review and ratification.

### Already ratified (substrate in place)

| Amendment | Role (short) |
|-----------|----------------|
| **AMD-2026-005** | Peer review / triangulation / ratification process |
| **AMD-2026-007** | Intent primitive, Shell affordances, Workspace domain pack |
| **AMD-2026-010** | Kernel engineer lane (shadow pilot) |
| **AMD-2026-011** | External repo acquisition + **AIOS-SPEC-013** package |
| **AMD-2026-012** | Shell authority and voice-first entry |
| **AMD-2026-013** | Intent-bearing repository taxonomy (architecture / builder) |

### Cohesion-critical remainder (three draft AMDs)

Only these **draft** amendments are **in scope** for “close the foundation” sequencing:

| Order | Amendment | Title / scope | Why it belongs in this set |
|-------|-----------|----------------|----------------------------|
| **1** | **[AMD-2026-006](../amendments/AMD-2026-006.md)** | Google Workspace governed integration plane | Locks **Workspace → control plane → MCP** as binding law (**AIOS-SPEC-007** path); everything else that touches Workspace execution assumes this plane eventually **ratifies**. |
| **2** | **[AMD-2026-009](../amendments/AMD-2026-009.md)** (+ **[ADD-001](../amendments/AMD-2026-009-ADD-001-retrieval-backend-neutrality.md)** as packaged addendum, **[§10 spec-merge checklist](../amendments/AMD-2026-009-spec-merge-checklist.md)** execution) | Intent-scoped web retrieval + governed website review | Completes **external knowledge** acquisition **and** **SPEC-007 / SPEC-009 / SPEC-010** alignment; **Round 2** synthesis already **positive**. |
| **3** | **[AMD-2026-008](../amendments/AMD-2026-008.md)** | Sovereign voice + local runtime lanes | Binds **local** STT / TTS / interpret stack **after** remote **Workspace** and **web** paths are defined; reduces cross-cutting churn on shared specs. |

**Not** separate foundation tracks: **ratification motions**, **merge-deltas** artifacts, and **checklists** — they **serve** the AMDs above, not additional AMD IDs.

### Ordering caveats (explicit)

1. **Logical order** above is **006 → 009 → 008** for **dependency and merge hygiene** (Workspace plane **before** web+envelope merge work; **local runtime** **after** both **remote** planes are stable on paper).
2. **Schedule order** may differ: **006** had **Round 1 FAIL** — it **must** complete **[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** revision and a **passing** triangulation round **before** ratification. **009** may therefore **reach council sooner** than **006**; that is acceptable if **§10** spec-merge work is used to **reconcile** **SPEC-007** with **006** when **006** closes.
3. **One active binding track** at a time ([Operating rules](#operating-rules)) still applies unless **council** authorizes overlap.

---

## Operating rules

1. **Sequencing:** Prefer **one** active **AMD-2026-005** cycle (reviews → synthesis → gate → motion) on **one** amendment ID at a time; **hand off** or **park** the prior track before **opening** the next **binding** round, unless **council** approves otherwise.
2. **No** skipping **AMD-2026-005** numerical gates or **triangulation** for **ratification** claims.
3. **Registry:** After any governed amendment front-matter change, run **`py -3 scripts/registry_generator.py`**.

---

## AMD-2026-007 reconciliation (complete)

Canonical **[`amendments/AMD-2026-007.md`](../amendments/AMD-2026-007.md)** now matches **v0.2.1** **ratified** text expected by **Round 2** and the **executed** ratification motion. See **[`reviews/amd_2026_007/README.md`](../reviews/amd_2026_007/README.md)**.

---

*End of AIOS-AMD-TRACKER-001 v1.1.0.*

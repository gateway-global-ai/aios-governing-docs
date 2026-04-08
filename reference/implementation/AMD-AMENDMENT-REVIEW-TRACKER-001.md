---
document_id: AIOS-AMD-TRACKER-001
version: 1.1.6
status: draft
category: reference
title: Outstanding amendments — governed review tracker
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-08
cross_references:
  - doc_id: AMD-001
  - doc_id: AMD-2026-006
  - doc_id: AMD-2026-007
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-009
  - doc_id: AMD-2026-005
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AMD-2026-013
  - doc_id: AIOS-COMMITTEE-BRIEF-AMD-2026-013
  - doc_id: AIOS-AMD-001-DISPOSITION-001
  - doc_id: AMD-2026-006-RATIFICATION-MOTION
amendment_history:
  - version: 1.1.6
    date: 2026-04-08
    summary: AMD-2026-006 + AIOS-SPEC-007 ratified 1.0.0 per AMD-2026-006-RATIFICATION-MOTION v1.0.0; active cohesion track AMD-2026-009.
  - version: 1.1.5
    date: 2026-04-08
    summary: AMD-2026-006 motion Council-ready; post-ratification next cohesion focus AMD-2026-009 (006→009→008).
  - version: 1.1.4
    date: 2026-04-08
    summary: AMD-2026-006 — ratification motion draft AMD-2026-006-RATIFICATION-MOTION; SPEC-007 R2 PASS; Council next.
  - version: 1.1.3
    date: 2026-04-08
    summary: AMD-2026-006 Phase A accepted Option B — CURRENT_SYSTEM_RESEARCH_2026-04-08.md; Phase B Architect next.
  - version: 1.1.2
    date: 2026-04-07
    summary: AMD-2026-006 cohesion track — RESTART-PACKET.md; Phase A evidence refresh next per AIOS-AMD-PLAN-001.
  - version: 1.1.1
    date: 2026-04-07
    summary: AMD-001 taxonomy resolution — AIOS-AMD-001-DISPOSITION-001; legacy_ratified_bridge; ordering before 006/009/008 closure.
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
| **AMD-2026-006** | **`ratified` `1.0.0`** | [`reviews/amd_2026_006/`](../../reviews/amd_2026_006/README.md) — Round 2 **PASS** on **SPEC-007**; **[`AMD-2026-006-ratification-motion.md`](../amendments/AMD-2026-006-ratification-motion.md)** **v1.0.0** **2026-04-08** | **Follow-on:** implementation alignment; **next cohesion track** **[AMD-2026-009](../amendments/AMD-2026-009.md)** |
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
| **AMD-2026-006** | Google Workspace governed integration plane (**AIOS-SPEC-007**) |

### AMD-001 — taxonomy resolution (before 009 / 008 closure)

**[AMD-001](../../amendments/ammendment_google.md)** is **ratified** but uses the **pre-`AMD-2026-*`** numbering era and a **legacy** filename. It is **not** unfinished law; it is a **classification** problem. **Resolve** its place in the amendment universe **before** deep closure on the **2026** draft tracks below—see **[AMD-001 taxonomy and disposition](AMD-001-TAXONOMY-AND-DISPOSITION.md)**. This aligns with **[AMD-2026-013](../amendments/AMD-2026-013.md)** (declared taxonomy and accountability): **AMD-001** is the **explicit** legacy object, not an untracked exception.

### Cohesion-critical remainder (two draft AMDs)

| Order | Amendment | Title / scope | Why it belongs in this set |
|-------|-----------|----------------|----------------------------|
| **1** | **[AMD-2026-009](../amendments/AMD-2026-009.md)** (+ **[ADD-001](../amendments/AMD-2026-009-ADD-001-retrieval-backend-neutrality.md)** as packaged addendum, **[§10 spec-merge checklist](../amendments/AMD-2026-009-spec-merge-checklist.md)** execution) | Intent-scoped web retrieval + governed website review | Completes **external knowledge** acquisition **and** **SPEC-007 / SPEC-009 / SPEC-010** alignment; **Round 2** synthesis already **positive**. |
| **2** | **[AMD-2026-008](../amendments/AMD-2026-008.md)** | Sovereign voice + local runtime lanes | Binds **local** STT / TTS / interpret stack **after** remote **Workspace** and **web** paths are defined; reduces cross-cutting churn on shared specs. |

**Not** separate foundation tracks: **ratification motions**, **merge-deltas** artifacts, and **checklists** — they **serve** the AMDs above, not additional AMD IDs.

### Ordering caveats (explicit)

0. **AMD-001** taxonomy is **documented** (see subsection above); **spec embodiment** of its CLI matrix remains **AIOS-SPEC-003 / 004 / 005** maintenance work.
1. **Logical order** for the **remainder** is **009 → 008** after **006** **ratified** **2026-04-08** (**AIOS-SPEC-007** **v1.0.0**).
2. **Schedule order** may still differ: **009** may advance on its own motion timeline; **§10** spec-merge work **SHOULD** stay consistent with **ratified** **SPEC-007**.
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

*End of AIOS-AMD-TRACKER-001 v1.1.6.*

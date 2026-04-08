---
document_id: AMD-2026-006-RATIFICATION-MOTION
subject_amendment: AMD-2026-006
peer_review_primary_target: AIOS-SPEC-007
peer_review_basis_spec_version: 0.2.0
companion_amendment_version: 0.2.0
motion_version: 1.0.0
status: approved
category: council_motion
title: Ratification motion — AMD-2026-006 / AIOS-SPEC-007
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-08
approved: 2026-04-08
execution_path: amendments/AMD-2026-006.md; specifications/GoogleWorkspaceIntegrationGovernance.md (ratified 2026-04-08)
---

# Ratification motion — AMD-2026-006 / AIOS-SPEC-007

## 1. What passed (peer review record)

**Triangulated peer review Round 2** — **[AMD-2026-005](AMD-2026-005.md)** numerical criteria — applies to the **primary scored artifact**:

| Field | Record |
|-------|--------|
| **Document** | **[AIOS-SPEC-007](../specifications/GoogleWorkspaceIntegrationGovernance.md)** (**`GoogleWorkspaceIntegrationGovernance.md`**) **v0.2.0** (review basis → ratified as **1.0.0**) |
| **Mean composite** | **~3.87** (DeepSeek **3.7**, OpenAI **3.9**, Gemini **4.0**) |
| **Dimension floor** | **3** — no dimension **below** 3 in any reviewer scorecard |
| **Dispositions** | **approved_with_changes** (all three reviewers) |
| **Gate** | **PASS** — [`RATIFICATION_GATE_REPORT.md`](../reviews/googleworkspaceintegrationgovernance/round_2/RATIFICATION_GATE_REPORT.md) |
| **Synthesis** | [`REVIEW_SYNTHESIS.md`](../reviews/googleworkspaceintegrationgovernance/round_2/REVIEW_SYNTHESIS.md) |
| **Reviews** | [`review_001_deepseek.md`](../reviews/googleworkspaceintegrationgovernance/round_2/review_001_deepseek.md), [`review_002_openai.md`](../reviews/googleworkspaceintegrationgovernance/round_2/review_002_openai.md), [`review_003_gemini.md`](../reviews/googleworkspaceintegrationgovernance/round_2/review_003_gemini.md) |

**Round 1** on **[AMD-2026-006](AMD-2026-006.md)** **v0.1.0** — **FAIL** (substantive); recovery via **[AIOS-AMD-PLAN-001](../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** (evidence → architect → UI → committee → Phase E author revision) is **complete** — see **[`reviews/amd_2026_006/revision_log.md`](../reviews/amd_2026_006/revision_log.md)**.

---

## 2. What package is being advanced

Council is asked to **approve / ratify** a **two-part package** at **v0.2.0** substantive alignment:

| Role | Artifact | Version |
|------|----------|---------|
| **Reviewed normative bulk** | **[AIOS-SPEC-007](../specifications/GoogleWorkspaceIntegrationGovernance.md)** — Google Workspace integration governance (routing chain, routing envelope §5, control plane outcomes §6, canvas / SPEC-006 §7, execution scope §8, web retrieval §3, informative Annex A) | **Ratified `1.0.0`** (substantive basis **v0.2.0** peer-reviewed) |
| **Companion amendment instrument** | **[AMD-2026-006](AMD-2026-006.md)** — ratifies **SPEC-007**; extends **AIOS-SPEC-003** and **AIOS-SPEC-006** by reference | **Ratified `1.0.0`** |

**Effect:** **AIOS-SPEC-007** is the **binding technical SHALL/MUST** surface for Workspace integration; **AMD-2026-006** is the **amendment** that **ratifies** that spec and **anchors** adjacent doctrine (**AIP**, **UI registry**) without duplicating the spec body.

---

## 3. What is explicitly non-blocking

The following **SHALL NOT** block Council motion approval or ratification record-updates **unless** Council explicitly chooses to defer for one of these items:

| Item | Nature |
|------|--------|
| **§0 / MPOA wording** | Optional **surgical** clarification in **AIOS-SPEC-007 §0** (e.g. stronger linkage to **[MPOA](../core/master_platform_operating_agreement.md)**) if Council wants **additional** legal posture — **not** required for numeric gate satisfaction. |
| **Peer review on `AMD-2026-006.md` alone** | Optional second **`peer_review.py`** run **only** if a **procedural** record requires an amendment-scored artifact; **Round 2 normative basis** is **SPEC-007** **v0.2.0**. |
| **`types.ts` § reference** | **Product** follow-up: `ai-os-voice-interface` **`src/workspace/types.ts`** comment alignment (**§5** vs legacy **§6** label) — **logged** in **[`reviews/amd_2026_006/revision_log.md`](../reviews/amd_2026_006/revision_log.md)** — **non-blocking** for governance ratification. |

---

## 4. What Council is being asked to do

1. **Approve** this motion (or Council-equivalent decision) per **applicable tier** and **Governance Constitution** / **MPOA** ratification path for **amendments** and **specifications**.
2. **Ratify** the package: **AIOS-SPEC-007 v0.2.0** substantive text and **AMD-2026-006 v0.2.0** as the **ratifying amendment**, advancing both to **`ratified`** (or tier-appropriate **`status`**) with **`version`** / **`last_updated`** / **`ratification_date`** (or equivalent) recorded in each document’s front matter.
3. **Direct** maintainers to execute **Immediate actions** below upon approval.

---

## Authority (effect upon approval)

Upon **approval**:

1. **AIOS-SPEC-007** **SHALL** be recorded as **ratified** at the **version** Council freezes (recommended **1.0.0** ratified line from **v0.2.0** substantive text, or Council-numeric **v0.2.0** ratified — **exact version bump** is an **editorial** follow-on in the spec file).
2. **AMD-2026-006** **SHALL** be recorded as **ratified** with **version** aligned to Council (recommended **1.0.0** alongside spec ratification).
3. **Implementation** in product repositories **SHALL** align with ratified text **as a separate workstream** — ratification **does not** substitute for code verification.

---

## Immediate actions (after approval)

| Step | Action |
|------|--------|
| 1 | **AIOS-SPEC-007:** Set `status: ratified`, bump `version` per Council, set `last_updated`, `ratification_target` / ratification date; `amendment_history` entry; cross-reference **AMD-2026-006-RATIFICATION-MOTION**. |
| 2 | **AMD-2026-006:** Set `status: ratified`, bump `version`, `ratification_date`, `amendment_history`; cross-reference this motion. |
| 3 | **Registry:** Run **`py -3 scripts/registry_generator.py`**; **CHANGELOG** entry. |
| 4 | **Tracker:** Update **[AMD-AMENDMENT-REVIEW-TRACKER-001](../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)** — **AMD-2026-006** row **ratified**. |

---

## Decision

| Option | Council use |
|--------|----------------|
| **Approve** | Ratify **AIOS-SPEC-007** + **AMD-2026-006** package as in **§2**; non-blocking items remain **optional** per **§3**. |
| **Reject** | No ratification; documents remain **`draft`** until revised and re-reviewed per **AMD-2026-005**. |
| **Amend** | Council records conditions; revised text or supplementary motion **before** `ratified` **`status`**. |

---

## Execution record (in-repo)

| Field | Value |
|-------|--------|
| **Executed** | **2026-04-08** |
| **Peer review basis** | **AIOS-SPEC-007** **v0.2.0** — [`reviews/googleworkspaceintegrationgovernance/round_2/`](../reviews/googleworkspaceintegrationgovernance/round_2/) **PASS** |
| **Ratified** | **AIOS-SPEC-007** **`1.0.0`**; **AMD-2026-006** **`1.0.0`** |
| **Revision log** | [`reviews/amd_2026_006/revision_log.md`](../reviews/amd_2026_006/revision_log.md) |

---

## Coordinator status (non-normative)

- **Ratification executed** **2026-04-08** — Immediate actions **§** applied in one maintainer pass.
- **Next cohesion-critical track (historical at execution):** **[AMD-2026-009](AMD-2026-009.md)** — **[AMD-AMENDMENT-REVIEW-TRACKER-001](../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)** (**006 → 009 → 008**). **Update:** **009** and **008** are **ratified**; foundation sequence **complete** — tracker **v1.2.5**.

---

*End of ratification motion — AMD-2026-006 / AIOS-SPEC-007 — motion version **1.0.0** **approved** **2026-04-08**.*

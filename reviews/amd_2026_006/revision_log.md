# Revision log — AMD-2026-006 / AIOS-SPEC-007 (Workspace integration)

**Peer review:** [`README.md`](README.md).

## Round 1 — 2026-04-07

**Triangulation:** [`round_1/review_001_deepseek.md`](round_1/review_001_deepseek.md), [`review_002_openai.md`](round_1/review_002_openai.md), [`review_003_gemini.md`](round_1/review_003_gemini.md). **Synthesis:** [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md). **Gate:** [`round_1/RATIFICATION_GATE_REPORT.md`](round_1/RATIFICATION_GATE_REPORT.md) — **FAIL** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** (mean composite **2.7**; dimension floor **1**).

---

## Traceability — Round 1 → planning → committee → redlines (Phase E)

| Round 1 theme | Architect plan anchor | UI plan anchor | Committee ([`planning/COMMITTEE_PACKET.md`](planning/COMMITTEE_PACKET.md)) | **Resulting redline** |
|----------------|------------------------|----------------|---------------------------------------------------------------------------|------------------------|
| **Stub vs spec** — amendment thin vs normative depth | [`ARCHITECT_PLAN.md`](planning/ARCHITECT_PLAN.md) §3, §6 | — | Approve planning → **SPEC** carries bulk | **[AIOS-SPEC-007](../../specifications/GoogleWorkspaceIntegrationGovernance.md) v0.2.0** — new **§§5–8**, **Annex A**; **[AMD-2026-006](../../amendments/AMD-2026-006.md) v0.2.0** — rationale + **Change 1** ratifies **SPEC-007 v0.2.0** explicitly |
| **Normative depth / Annex A** — envelope, completeness | [`ARCHITECT_PLAN.md`](planning/ARCHITECT_PLAN.md) §3 | — | Q1 **Approve** | **§5** routing envelope table; **§6** control plane codes; **§8** **SPEC-010** |
| **Cross-document / SPEC-006 surfaces** | [`ARCHITECT_PLAN.md`](planning/ARCHITECT_PLAN.md) §4, §6 | [`UI_PLAN.md`](planning/UI_PLAN.md) §2, §7 | Q3 **Approve** | **§7** canvas routing + **SPEC-006** registration; hub **fallback** normative **MAY** |
| **Hub fallback UX** (events/docs/tasks) | [`ARCHITECT_PLAN.md`](planning/ARCHITECT_PLAN.md) §4 | [`UI_PLAN.md`](planning/UI_PLAN.md) §2, §5 | Q2 **Approve** MVP | **§7.3** documents fallback to main hub **without** mandating new product surfaces before review |
| **Legal / liability** (low floor) | Defer in architect §6 | — | Not a planning gate | **SPEC-007 §0** non-normative legal note — **no** invented contract terms |
| **Round 2 target document** | [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md) coordinator note | — | Q4 **Approve** | **Primary:** `specifications/GoogleWorkspaceIntegrationGovernance.md`; merged AMD+SPEC **optional** |

---

## Phase E — revision freeze (Round 2 candidate) — 2026-04-08

| Artifact | Version | Role |
|----------|---------|------|
| **[AIOS-SPEC-007](../../specifications/GoogleWorkspaceIntegrationGovernance.md)** | **0.2.0** (`draft`) | **Primary normative bulk** for Round 2 |
| **[AMD-2026-006](../../amendments/AMD-2026-006.md)** | **0.2.0** (`draft`) | Ratifies **SPEC-007 v0.2.0**; extends **SPEC-003/006** by reference |

**Freeze:** This pair is the **Round 2 candidate** until superseded by a later revision entry or ratification bump. **Planning** artifacts [`planning/ARCHITECT_PLAN.md`](planning/ARCHITECT_PLAN.md), [`planning/UI_PLAN.md`](planning/UI_PLAN.md) remain **frozen** reference (committee **2026-04-08**).

---

## Round 2 — AIOS-SPEC-007 (primary target) — 2026-04-08

**Triangulation** (artifact folder: [`../googleworkspaceintegrationgovernance/round_2/`](../googleworkspaceintegrationgovernance/round_2/)): [`review_001_deepseek.md`](../googleworkspaceintegrationgovernance/round_2/review_001_deepseek.md), [`review_002_openai.md`](../googleworkspaceintegrationgovernance/round_2/review_002_openai.md), [`review_003_gemini.md`](../googleworkspaceintegrationgovernance/round_2/review_003_gemini.md). **Synthesis:** [`REVIEW_SYNTHESIS.md`](../googleworkspaceintegrationgovernance/round_2/REVIEW_SYNTHESIS.md). **Gate:** [`RATIFICATION_GATE_REPORT.md`](../googleworkspaceintegrationgovernance/round_2/RATIFICATION_GATE_REPORT.md) — **PASS** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** (mean composite **~3.87**; dimension floor **3**).

**Product conformance — non-blocking:** `ai-os-voice-interface` **`src/workspace/types.ts`** comment cites **SPEC-007 §6** for **`WorkspaceRoutingEnvelope`**; normative envelope is **§5** in **v0.2.0**. Update the comment to **§5** in a small product PR — **does not** block governance ratification path.

---

## Ratification path — coordinator note (2026-04-08)

**Process validation:** Round 1 **FAIL** for substantive reasons → evidence → Architect / UI → committee → Phase E author revision → normative bulk in **AIOS-SPEC-007** → **Round 2 PASS** on **[AMD-2026-005](../../amendments/AMD-2026-005.md)** numerics (composites **3.7 / 3.9 / 4.0**, floor **3**). Remaining reviewer themes are **narrow** and **non-blocking** (optional tightening, not structural rescue).

**Recommendation:** Advance **AIOS-SPEC-007 v0.2.0** and companion **[AMD-2026-006](../../amendments/AMD-2026-006.md) v0.2.0** to **ratification path** (Council / motion per tier) **without** another full peer review cycle. **Optional** pre-motion: surgical **§0 / MPOA** linkage in **SPEC-007** only if Council wants stronger legal language — **not** a default requirement. **`peer_review.py`** on **`amendments/AMD-2026-006.md`** alone — **only** if a **procedural** reason requires an amendment-scored artifact.

**Ratification motion (draft):** **[`AMD-2026-006-ratification-motion.md`](../../amendments/AMD-2026-006-ratification-motion.md)** — **Council-ready**; no further drafting unless Council requests; on approval execute motion **Immediate actions** in one pass; then advance cohesion focus to **[AMD-2026-009](../../amendments/AMD-2026-009.md)** per **[tracker](../../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)**.

---

## Ratification executed — 2026-04-08

**Motion:** **[`AMD-2026-006-ratification-motion.md`](../../amendments/AMD-2026-006-ratification-motion.md)** **v1.0.0** **`approved`** **2026-04-08** — **Immediate actions** executed in one pass (front matter, registry, **CHANGELOG**, **[AMD-AMENDMENT-REVIEW-TRACKER-001](../../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)** **v1.1.6**).

| Artifact | Version | Status |
|----------|---------|--------|
| **[AIOS-SPEC-007](../../specifications/GoogleWorkspaceIntegrationGovernance.md)** | **1.0.0** | **`ratified`** |
| **[AMD-2026-006](../../amendments/AMD-2026-006.md)** | **1.0.0** | **`ratified`** |

**Next cohesion focus (active governed track):** **[AMD-2026-009](../../amendments/AMD-2026-009.md)** — see **[tracker](../../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)** (**009 → 008** remainder).

---

## Closed — packet complete

**Governed restart** — [`RESTART-PACKET.md`](RESTART-PACKET.md) (**historical**; **006** ratified).

**Phase A (evidence)** — **Accepted 2026-04-08** — **Option B** — [`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`](../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md); [`planning/EVIDENCE-PHASE-A-STATUS.md`](planning/EVIDENCE-PHASE-A-STATUS.md).

**Planning lifecycle** (**[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)**) — [`planning/README.md`](planning/README.md) — Phases **A–F** complete **2026-04-08**; **ratification** executed **2026-04-08**.

# AIOS Peer Review Archive

This directory contains all peer reviews of AIOS governing documents, organized by document and review round.

**Note:** “Ratification” and review stages here are **AIOS in-repo** artifacts (models, rubric, Council path per documents). They are **not** the same as a GitHub pull-request approval; see **README.md** § GitHub vs AIOS governance.

---

## Review Process: The 5-Stage Document Lifecycle

Every governing document follows a mandatory 5-stage pipeline:

```
Stage 1: DRAFT          DeepSeek authors the document
    |
Stage 2: ROUND 1        OpenAI + Gemini independently review
    |
Stage 3: REVISION       DeepSeek revises, producing a revision log
    |
Stage 4: ROUND 2        All 3 models review the revised document
    |
Stage 5: RATIFICATION   2+ approvals = ratified; 2+ major_revision = back to Stage 3
```

### Stage Gates

- **Draft -> Round 1:** Document exists and passes basic structural validation
- **Round 1 -> Revision:** At least 2 reviews received with 11-dimension scores
- **Revision -> Round 2:** Revised document + revision log exist; revision log addresses every recommendation
- **Round 2 -> Ratification:** At least 2 of 3 reviewers issue `approved` or `approved_with_changes`
- **Ratification -> Back to Stage 3:** 2+ reviewers issue `major_revision_required`

---

## Folder Structure

```
reviews/
├── {document_slug}/
│   ├── round_1/
│   │   ├── review_001_{model}.md
│   │   └── review_002_{model}.md
│   ├── round_2/
│   │   ├── review_003_{model}.md
│   │   ├── review_004_{model}.md
│   │   └── review_005_{model}.md
│   ├── kernel/                    # optional — kernel shadow pilot (advisory only)
│   │   ├── KERNEL_SHADOW_BRIEF.md
│   │   └── KERNEL_SHADOW_FINDINGS.md
│   └── revision_log.md
├── kernel_shadow/                 # pilot coordination (not a document slug)
│   ├── README.md
│   └── pilot_runs/
```

---

## Kernel shadow pilot (optional — [AMD-2026-010](../amendments/AMD-2026-010.md))

The **triangulated** pipeline above remains the **binding** ratification path (**[AMD-2026-005](../amendments/AMD-2026-005.md)**). **Kernel shadow** review is an **advisory**, **non-blocking** lane for shell/state/routing focus (**AMD-2026-010 §4.4**).

- **When:** Parallel to Round 1 or Round 2 for documents with shell, routing, or **POL-SHELL**-class impact — **not** instead of triangulation.
- **Where:** Per-document artifacts under `reviews/{document_slug}/kernel/`; coordination and metrics under [`kernel_shadow/README.md`](kernel_shadow/README.md).
- **Templates:** [`templates/kernel_shadow_review_brief.md`](../templates/kernel_shadow_review_brief.md), [`kernel_shadow_findings.md`](../templates/kernel_shadow_findings.md), [`kernel_shadow_pilot_metrics.md`](../templates/kernel_shadow_pilot_metrics.md).

---

## Grading System

All reviews use the 11-dimension rubric defined in `templates/grading_rubric.md`:

1. Cross-Document Consistency
2. Business Model Alignment
3. Legal Enforceability
4. Architectural Fidelity
5. Completeness
6. Conflict Freedom
7. Practical Operability
8. Style & Clarity
9. Developer Synchrony
10. Platform Economics Synchrony
11. Friction Factor

Each dimension is scored 1-5. Disposition is determined by scores:
- **Approved:** No dimension below 4, composite >= 4.0
- **Approved with changes:** No dimension below 3, composite >= 3.5
- **Major revision required:** Any dimension at 1, or 2+ at 2, or composite below 3.0

---

## Running Reviews

```bash
cd scripts/

# Round 1 review (OpenAI + Gemini)
python peer_review.py core/technical_manifesto.md --round 1

# Revision (DeepSeek)
python revise_document.py core/technical_manifesto.md

# Round 2 review (all 3 models)
python peer_review.py core/technical_manifesto.md --round 2

# Or run the full lifecycle
python lifecycle.py core/technical_manifesto.md
```

---

## Review History

### Technical Manifesto
- Round 1: `review_001_deepseek.md` (pre-automation, migrated from root)

### Governance Constitution
- Round 1: `review_001_deepseek.md`, `review_002_deepseek.md` (pre-automation, migrated from root)

### Master Platform Operating Agreement
- Round 1: `review_001_deepseek.md` (pre-automation, migrated from root)

### AMD-2026-010 (Kernel Engineer role, kernel review lane — shadow pilot)
- Round 1: [`amd_2026_010/round_1/review_001_openai.md`](amd_2026_010/round_1/review_001_openai.md), [`review_002_gemini.md`](amd_2026_010/round_1/review_002_gemini.md); brief [`amd_2026_010/round_1/REVIEW_BRIEF.md`](amd_2026_010/round_1/REVIEW_BRIEF.md).
- Round 2: [`amd_2026_010/round_2/review_001_deepseek.md`](amd_2026_010/round_2/review_001_deepseek.md), [`review_002_openai.md`](amd_2026_010/round_2/review_002_openai.md), [`review_003_gemini.md`](amd_2026_010/round_2/review_003_gemini.md); [`REVIEW_SYNTHESIS.md`](amd_2026_010/round_2/REVIEW_SYNTHESIS.md); [`RATIFICATION_GATE_REPORT.md`](amd_2026_010/round_2/RATIFICATION_GATE_REPORT.md). **Ratified:** [`../amendments/AMD-2026-010.md`](../amendments/AMD-2026-010.md) **v0.2.0** with motion [`../amendments/AMD-2026-010-ratification-motion.md`](../amendments/AMD-2026-010-ratification-motion.md); policy index [`../reference/AIOS_POLICY_INDEX.md`](../reference/AIOS_POLICY_INDEX.md).

### AIOS-SPEC-009 (Intent primitive and execution model)
- Round 1 **Pass A** (v0.5.2, superseded): [`intent_primitive_execution_model/round_1/review_001_openai.md`](intent_primitive_execution_model/round_1/review_001_openai.md), [`review_002_gemini.md`](intent_primitive_execution_model/round_1/review_002_gemini.md) — **FAIL** **AMD-2026-005**.
- Round 1 **Pass B** (v0.5.3): [`review_003_openai.md`](intent_primitive_execution_model/round_1/review_003_openai.md), [`review_004_gemini.md`](intent_primitive_execution_model/round_1/review_004_gemini.md) — **PASS** (superseded as **latest** by Pass C).
- Round 1 **Pass C** (v0.5.4): [`review_005_openai.md`](intent_primitive_execution_model/round_1/review_005_openai.md), [`review_006_gemini.md`](intent_primitive_execution_model/round_1/review_006_gemini.md); [`round_1/REVIEW_SYNTHESIS.md`](intent_primitive_execution_model/round_1/REVIEW_SYNTHESIS.md); [`round_1/RATIFICATION_GATE_REPORT.md`](intent_primitive_execution_model/round_1/RATIFICATION_GATE_REPORT.md) — **PASS**.
- Round 2 (v0.5.4): [`review_001_deepseek.md`](intent_primitive_execution_model/round_2/review_001_deepseek.md), [`review_002_openai.md`](intent_primitive_execution_model/round_2/review_002_openai.md), [`review_003_gemini.md`](intent_primitive_execution_model/round_2/review_003_gemini.md); [`round_2/REVIEW_SYNTHESIS.md`](intent_primitive_execution_model/round_2/REVIEW_SYNTHESIS.md); [`round_2/RATIFICATION_GATE_REPORT.md`](intent_primitive_execution_model/round_2/RATIFICATION_GATE_REPORT.md) — **PASS** (**AMD-2026-005**). [`revision_log.md`](intent_primitive_execution_model/revision_log.md). Kernel shadow (advisory): [`intent_primitive_execution_model/kernel/KERNEL_SHADOW_FINDINGS.md`](intent_primitive_execution_model/kernel/KERNEL_SHADOW_FINDINGS.md).
- **Ratified:** [`../specifications/IntentPrimitiveAndExecutionModel.md`](../specifications/IntentPrimitiveAndExecutionModel.md) **v0.5.5** (**2026-04-06**). Path B editorial + coordinator sign-off: [`round_2/EDITORIAL_APPROVAL_v0.5.5.md`](intent_primitive_execution_model/round_2/EDITORIAL_APPROVAL_v0.5.5.md) (**§12.2** **PolicyRecord** threshold; **§12.3** **UX** policy). Gate report **§4:** [`round_2/RATIFICATION_GATE_REPORT.md`](intent_primitive_execution_model/round_2/RATIFICATION_GATE_REPORT.md).

### AMD-2026-007 (Intent primitive, shell affordances, §11.9 shell vs skills)
- Round 1: [`amd_2026_007/round_1/review_001_openai.md`](amd_2026_007/round_1/review_001_openai.md), [`review_002_gemini.md`](amd_2026_007/round_1/review_002_gemini.md); [`REVIEW_SYNTHESIS.md`](amd_2026_007/round_1/REVIEW_SYNTHESIS.md); [`RATIFICATION_GATE_REPORT.md`](amd_2026_007/round_1/RATIFICATION_GATE_REPORT.md) (**Round 1** → **READY_FOR_ROUND_2**).
- Round 2: [`amd_2026_007/round_2/review_001_deepseek.md`](amd_2026_007/round_2/review_001_deepseek.md), [`review_002_openai.md`](amd_2026_007/round_2/review_002_openai.md), [`review_003_gemini.md`](amd_2026_007/round_2/review_003_gemini.md); [`REVIEW_SYNTHESIS.md`](amd_2026_007/round_2/REVIEW_SYNTHESIS.md); [`RATIFICATION_GATE_REPORT.md`](amd_2026_007/round_2/RATIFICATION_GATE_REPORT.md). **Ratified:** [`amendments/AMD-2026-007.md`](../amendments/AMD-2026-007.md) **v0.2.1** with motion [`../amendments/AMD-2026-007-ratification-motion.md`](../amendments/AMD-2026-007-ratification-motion.md); policy index [`../reference/AIOS_POLICY_INDEX.md`](../reference/AIOS_POLICY_INDEX.md).

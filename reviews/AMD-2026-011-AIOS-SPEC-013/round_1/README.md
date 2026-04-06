# Triangulated peer review — AMD-2026-011 + AIOS-SPEC-013 (Round 1)

**Package:** External repository acquisition, quarantine, analysis, promotion, and minimal governance execution dependencies.

| Document | ID | Version | Path |
|----------|----|---------|------|
| Amendment | **AMD-2026-011** | **0.1.2** | [`amendments/AMD-2026-011.md`](../../../amendments/AMD-2026-011.md) |
| Specification | **AIOS-SPEC-013** | **0.1.1** | [`specifications/ExternalRepositoryAcquisitionAnalysisAndPromotion.md`](../../../specifications/ExternalRepositoryAcquisitionAnalysisAndPromotion.md) |

**Relationship:** **AMD-2026-011** states governance principles and amendment-level rules (including minimal execution dependency for this repo’s CI). **AIOS-SPEC-013** states SHALL-level contracts, promotion classes, and evidence expectations. Review **both** as one coordinated package and **each** on its own merits.

---

## Artifacts in this folder

| File | Purpose |
|------|---------|
| [`TRIANGULATED_REVIEW_PROMPT.md`](TRIANGULATED_REVIEW_PROMPT.md) | Full instructions, review questions, rubric, output format |
| [`review_001_openai.md`](review_001_openai.md) | Round 1 triangulated review (composite **4.2**, **approved_with_changes**) |
| [`review_002_gemini.md`](review_002_gemini.md) | Round 1 triangulated review (composite **4.3**, **approved_with_changes**) |
| *(optional)* | `REVIEW_SYNTHESIS.md` — coordinator synthesis |

---

## Instructions for reviewers

1. Read [`TRIANGULATED_REVIEW_PROMPT.md`](TRIANGULATED_REVIEW_PROMPT.md) in full.
2. Read both governed documents end-to-end (not only the prompt excerpts).
3. Produce an independent review file per [`templates/grading_rubric.md`](../../../templates/grading_rubric.md) (11 dimensions, scores 1–5).
4. Save as `review_00N_<your_id>.md` in this directory (`round_1/`).

**Triangulation:** At least **two** independent reviewers (three preferred). Dispositions should be reconcilable against **AMD-2026-005** / **AIOS-SPEC-003** ratification norms where applicable.

---

## Lifecycle note (governed documents)

- Front matter **`status`** on these files remains **`draft`** until a ratification motion and Council process elevate them.
- For GitHub **PRs** that carry only this review package, use the PR template lifecycle **`under_review`** when the PR is open for triangulation; ratification is **out of scope** for this stage.

---

## Supporting material (non-normative)

- [`sources/AMD-2026-011/source_stub.md`](../../../sources/AMD-2026-011/source_stub.md)
- [`sources/AMD-2026-011/impact_study_summary.md`](../../../sources/AMD-2026-011/impact_study_summary.md)

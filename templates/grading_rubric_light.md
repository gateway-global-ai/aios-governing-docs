# AIOS Peer Review Grading Rubric (Light)

This is the lightweight 5-dimension rubric for specification and reference documents. For core documents (Manifesto, Constitution, MPOA), use the full 11-dimension rubric.

---

## Scale Definition (All Dimensions)

| Score | Label | Meaning |
|:-----:|-------|---------|
| **5** | Exemplary | Sets the standard. No issues found. Could be cited as a reference for other documents. |
| **4** | Strong | Meets all requirements with only minor stylistic or editorial suggestions. No substantive gaps. |
| **3** | Acceptable | Functionally sound but has identifiable gaps, ambiguities, or inconsistencies that should be addressed before ratification. |
| **2** | Major Issues | Significant problems that undermine the document's purpose. Requires substantial revision in this dimension. |
| **1** | Critical Failure | Fundamentally broken in this dimension. Contains contradictions, missing critical sections, or actively conflicts with other governing documents. |

---

## Dimension Definitions

### 1. Cross-Document Consistency

Does this document use terminology, defined terms, and structural patterns consistent with the governing set? Does it reference other documents by correct title, Article, and Section? Does it use the canonical glossary from the Technical Manifesto Appendix without inventing new terms or redefining existing ones?

**Score 5:** Every term matches the glossary. Every cross-reference cites the correct Article/Section.
**Score 3:** Most terms are correct but 2-3 inconsistencies exist.
**Score 1:** Invents new terms that conflict with the glossary. References documents by wrong names.

### 2. Completeness

Does this document cover everything its entry in the document plan promises? Are there sections that the plan describes but the document omits? Are edge cases addressed? Are failure modes defined?

**Score 5:** Covers every item described in the plan. Edge cases addressed. Failure modes defined.
**Score 3:** Covers the core requirements but omits 2-3 items. Some edge cases unaddressed.
**Score 1:** Missing entire sections promised by the plan. No failure mode definitions.

### 3. Practical Operability

Could a real developer, enterprise customer, or AI agent actually follow these rules? Are SLAs specific (numbers, not "timely")? Are processes step-by-step? Are thresholds defined?

**Score 5:** Every rule is actionable. SLAs have specific numbers. Ready for day-one use.
**Score 3:** Most rules are actionable but 2-3 provisions are too abstract to implement.
**Score 1:** Rules are aspirational rather than operational. SLAs are vague.

### 4. Conflict Freedom

Does this document contradict any other governing document? Does it respect the Supremacy Clause (Constitution for governance, MPOA for liability/economics, Manifesto for architecture)?

**Score 5:** No contradictions with any other document. Supremacy Clause respected.
**Score 3:** No direct contradictions but 1-2 provisions create tension.
**Score 1:** Direct contradictions with other governing documents.

### 5. Style & Clarity

Does the writing follow the Style Guide? Is it precise and unambiguous? Free of marketing language in specification contexts? Correct heading hierarchy?

**Score 5:** Perfect adherence to the Style Guide. Precise, unambiguous, well-structured.
**Score 3:** Generally follows the Style Guide but has 3-5 formatting inconsistencies.
**Score 1:** Does not follow the Style Guide. Marketing language in specifications.

---

## Composite Score Calculation

The composite score is the arithmetic mean of all 5 dimension scores, rounded to one decimal place.

## Disposition Rules

| Disposition | Criteria |
|-------------|----------|
| **Approved** | No dimension below 4. Composite >= 4.0. |
| **Approved with Changes** | No dimension below 3. Composite >= 3.5. |
| **Major Revision Required** | Any dimension at 1, OR two or more dimensions at 2, OR composite below 3.0. |

---

**This rubric is governed by the AIOS Governance Constitution (v1.0).**

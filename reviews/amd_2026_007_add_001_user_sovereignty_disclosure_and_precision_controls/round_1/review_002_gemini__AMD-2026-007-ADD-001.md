review_id: REV-AMD-2026-007-ADD-001-001
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.1.0
reviewer: Gemini
review_date: 2024-05-19
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 2.7
---

# Peer Review: User Sovereignty Disclosure and Precision Controls

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Aligns in spirit with parent documents, but its principles are not yet translated into consistent, binding language. |
| 2 | Business Model Alignment | 4 | Supports the enterprise trust model, but the "where policy permits" clauses need more definition to protect core platform functions. |
| 3 | Legal Enforceability | 2 | The document is rife with legally vague terms ("materially," "meaningful") and inconsistent use of `SHALL` vs. `SHOULD`, making it largely unenforceable as written. |
| 4 | Architectural Fidelity | 4 | Logically extends the shell's disclosure duties defined in AMD-2026-007 without violating core architectural principles. |
| 5 | Completeness | 2 | Lacks critical components for a legal addendum, such as definitions for its key terms, consequences for non-compliance, and a clear policy hierarchy. |
| 6 | Conflict Freedom | 3 | The "where policy permits" clause is a good defense against conflict, but its ambiguity could still create tension with MPOA logging or security requirements. |
| 7 | Practical Operability | 2 | The requirements are too high-level and subjective for an engineering team to implement without significant further interpretation. |
| 8 | Style & Clarity | 2 | The inconsistent use of `SHOULD` where `SHALL` is expected undermines its authority and violates Style Guide principles for binding rules. |
| 9 | Developer Synchrony | 2 | A developer would not know what to build from this document, as it lacks schemas, concrete thresholds, or references to UI component specifications. |
| 10 | Platform Economics Synchrony | 3 | Fails to explicitly address how disabling logging might conflict with usage-based billing, relying entirely on an undefined "policy" to resolve it. |
| 11 | Friction Factor | 3 | Introduces significant potential UI complexity, and the governance benefit is weak until the enforceability issues are resolved. |
| | **Composite Score** | **2.7** | |

---

## Overall Assessment

This addendum addresses a crucial aspect of platform governance: user sovereignty. Its intent is sound and aligns with building a trustworthy, enterprise-ready system. However, as a piece of "binding shell law," it fails on several legal and operational dimensions.

### Strengths

*   **Principled Stand:** The document correctly identifies a critical failure mode in AI systems—hidden state that benefits the platform at the user's expense—and establishes a strong principled stance against it (Sections 1, 2, 7).
*   **Good Categorization:** The categorization of disclosure classes (Section 3) and precision controls (Section 4) provides a solid, logical framework for what needs to be governed.
*   **Architectural Alignment:** The document successfully extends the disclosure and shell-level responsibilities established in its parent, `AMD-2026-007`, without introducing architectural conflicts.

### Critical Gaps

1.  **Unenforceable Language:** The document is built on a foundation of "weasel words." Terms like "user-comprehensible," "materially," and "meaningful" are subjective and would not survive scrutiny in arbitration. Without objective, testable definitions, these requirements are merely suggestions.
2.  **Inconsistent Modality (`SHALL` vs. `SHOULD`):** The document claims to establish binding requirements but uses `SHOULD` (a recommendation) for many of its core principles (e.g., Sec 2, 5, 6, 7). This makes it unclear what is a rule versus a guideline, rendering it legally ambiguous.
3.  **Missing Consequences:** The addendum defines duties but specifies no consequences for non-compliance. This is a major legal gap. If a shell fails to meet these requirements, the document provides no remedy or failure mode.
4.  **Lack of Operationalization:** There is no mechanism described for how these principles become reality. The document does not mandate `PolicyRecord` definitions, link to UI component specifications in `AIOS-SPEC-006`, or define a testable conformance suite.

---

## Article-by-Article Review

### Section 0. Status and intent

**Feedback:** The purpose is clear, but "binding shell law" is an overstatement given the current text's weaknesses.

**Scores:** Style & Clarity: 3

**Recommendation:** Retain, but the body of the document must be strengthened to match this intent.

### Section 1. Purpose

**Feedback:** Excellent articulation of the problem statement. No issues.

**Scores:** Style & Clarity: 5

**Recommendation:** No changes.

### Section 2. Governing principle

**Feedback:** The use of `SHOULD` in the core governing principle is a critical flaw. A governing principle for a binding legal document must be a `SHALL`.

**Scores:** Legal Enforceability: 1, Style & Clarity: 1

**Recommendation:** Change the text to:
"If a shell or surrounding runtime captures, infers, stores, or applies user-relevant state that materially affects behavior, the user **SHALL** be able to inspect and govern that state."

### Section 3. Required disclosure classes

**Feedback:** This list is well-structured, but the phrase "when they materially exist" is too vague to be enforceable. What constitutes "material" existence? Who decides?

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Add a subsection that defines or points to a definition for "materially."
Proposed addition:
"**3.1 Definition of Materiality:** For the purposes of this section, a state 'materially exists' if its presence or absence is sufficient to alter a `PolicyRecord` evaluation, change a resolved `ExecutionPlan`, or trigger a disclosure requirement defined in `AIOS-SPEC-006`."

### Section 4. Precision controls

**Feedback:** The primary requirements use `SHALL`, which is good. However, the list of distinctions uses `SHOULD`, which makes the "precision" part of the control optional. The phrase "where policy permits" is also ambiguous.

**Scores:** Legal Enforceability: 2, Completeness: 2

**Recommendation:**
1.  Change `SHOULD distinguish` to `SHALL distinguish` to make the list of controls mandatory.
2.  Clarify the policy reference. Change "where policy permits" to "unless prohibited by the Master Platform Operating Agreement (MPOA) or a non-overridable Platform security policy."

### Section 5, 6, 7. Behavioral Settings, Signal Use, Conflict-of-interest

**Feedback:** These three sections all use `SHOULD`, making them entirely optional recommendations. To be "binding shell law," they must be `SHALL`. Furthermore, Section 7's "meaningful conflicts" is another unenforceable, subjective term.

**Scores:** Legal Enforceability: 1

**Recommendation:**
1.  In Sections 5, 6, and 7, replace all instances of `SHOULD` with `SHALL`.
2.  In Section 7, replace "meaningful conflicts" with a more objective standard. For example: "The shell SHALL disclose conflicts of interest where a background process intended for platform benefit (such as telemetry or retention analysis) results in a user-facing action that is contrary to the user's active, resolved `Intent`."

### Section 8. Non-goals

**Feedback:** This section is clear and well-scoped. It correctly carves out what is not covered.

**Scores:** Clarity: 5

**Recommendation:** No changes.

### Final principle

**Feedback:** This is a good summary but does not carry legal weight. No issues.

**Scores:** N/A

**Recommendation:** No changes.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Global | Inconsistent use of `SHOULD` for binding requirements. | Change all instances of `SHOULD` to `SHALL` in Sections 2, 4, 5, 6, and 7 to make the document's rules mandatory and consistent with its stated purpose. | Critical | 3, 5, 8 |
| 2 | 3, 7 | Use of vague, legally unenforceable terms like "materially" and "meaningful." | Define these terms with objective, testable criteria, likely by tying them to other governed entities like `PolicyRecord` or `ExecutionPlan`. | Critical | 3, 7, 9 |
| 3 | Document | Missing consequences for non-compliance. | Add a new section defining the failure mode, e.g., "Failure to comply with the disclosure requirements herein SHALL be treated as a Tier 2 governance breach, requiring a documented remediation plan." | High | 3, 5 |
| 4 | 4, 6 | The "where policy permits" clause is ambiguous. | Clarify the policy hierarchy by specifying which policies can override these user controls (e.g., MPOA, Platform Security Policy). | High | 3, 6 |
| 5 | Document | Lacks an operationalization clause. | Add a requirement that these disclosures and controls must be implemented as components in `AIOS-SPEC-006` and be verifiable via a conformance test. | Medium | 7, 9 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has a strong and necessary purpose, but its legal foundation is critically flawed. The pervasive use of subjective terms and the inconsistent application of `SHALL` versus `SHOULD` render it unenforceable as "binding law" and closer to a list of suggestions.

**Top 3 Actions Required:**
1.  Conduct a full pass to replace all vague "weasel words" (`materially`, `meaningful`, etc.) with objective, `PolicyRecord`-backed, or otherwise testable definitions.
2.  Change all `SHOULD` statements that describe required behaviors (Sections 2, 4, 5, 6, 7) to `SHALL` to make the addendum's rules binding and unambiguous.
3.  Add a new section defining the consequences for non-compliance to give the document legal and operational teeth.
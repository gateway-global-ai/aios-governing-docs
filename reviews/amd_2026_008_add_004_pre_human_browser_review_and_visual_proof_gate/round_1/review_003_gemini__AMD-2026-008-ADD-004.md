---
review_id: REV-AMD-2026-008-ADD-004-003
document_reviewed: amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md
document_version: 0.2.0
reviewer: Gemini
review_date: 2026-04-08
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.6
---

# Peer Review: Pre-Human Browser Review and Visual Proof Gate

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document correctly references and builds upon the established framework, particularly ADD-001/002/003 and the acquisition process from AMD-2026-011. |
| 2 | Completeness | 4 | The document is thorough in its scope, triggers, and rules, but defers the critical `Review Target` schema definition to a future policy, leaving a gap. |
| 3 | Practical Operability | 4 | The rules are clear and actionable, with excellent remediation paths, but full implementation depends on external policies and schemas that are not yet defined. |
| 4 | Conflict Freedom | 5 | No conflicts with other governing documents were found; it logically extends the existing review and approval framework by adding a necessary verification layer. |
| 5 | Style & Clarity | 5 | The writing is exemplary—precise, unambiguous, and fully compliant with the Style Guide, making the rules easy to understand and enforce. |
| | **Composite Score** | **4.6** | |

---

## Overall Assessment

### Strengths

-   **Strong, Unambiguous Language:** The document's use of `SHALL` and `SHALL NOT` is precise and creates clear, enforceable obligations. Clauses like "The absence of time is not an exception" (§10.3) are models of legal clarity and would be highly defensible in any dispute.
-   **Robust Exception and Remediation Framework:** Sections 9.4 and 10 establish a governed, auditable path for handling blocked states and exceptions. This prevents ad-hoc overrides and ensures that any deviation from the standard process is a deliberate, recorded decision with clear acceptance of risk.
-   **Clear, Auditable States:** The definition of blocked approval states (§9.2) and the required audit posture (§11) create a traceable, enforceable process. This is critical for compliance and demonstrating procedural rigor.
-   **Excellent Definitions:** Section 0.1 clearly defines key terms like "Browser-visible evidence," "UI-affecting," and "Stale," which closes potential loopholes and prevents ambiguity in interpretation.

### Critical Gaps

-   **Deferred Schema Definition:** The core operational artifact, the `Review Target`, has its conceptual fields defined in §6.1, but the "canonical machine-readable schema" is deferred to "policy or product implementation." This creates a dependency risk and a potential enforceability gap. A contract with undefined terms is difficult to enforce.
-   **Potential "Proportionality" Loophole:** Section 4.1 introduces "Policy proportionality," allowing policy to "shape the minimum visual proof." This is a pragmatic concept, but as written, it could be exploited to weaken the core principle of the addendum. A malicious or poorly written policy could use this clause to render the gate meaningless for certain work items.

---

## Article-by-Article Review

### §4 Trigger conditions & §4.1 Policy proportionality

**Feedback:** The triggers in §4 are clear, and the default-to-review posture is strong. However, §4.1 introduces "proportionality," which could be interpreted as a weasel clause. It allows policy to "shape the minimum visual proof," which could be used to reduce the proof requirement to something trivial, thereby negating the addendum's core purpose for high-risk changes if the policy is not carefully written.

**Scores:** Legal Enforceability: 3, Practical Operability: 4

**Recommendation:** Add a clarifying sentence to §4.1 to create a floor for what policy can do.

**Proposed Text:**
> Such policy MAY define additional proof requirements or alternative approval paths for different risk classes, but **SHALL NOT** eliminate the core requirement for browser-visible evidence as defined in Section 7 for work items where this addendum applies.

### §6 Review target contract

**Feedback:** This section is legally critical as it defines the "contract" for each review. The deferral of the schema to "policy" is a significant legal gap. A process that relies on a contract with undefined or un-located terms is difficult to audit and enforce. While §14 *recommends* `REVIEW_TARGET.yaml`, a recommendation is not a binding requirement.

**Scores:** Legal Enforceability: 2, Practical Operability: 3

**Recommendation:** Strengthen the binding to a concrete, traceable schema artifact for the `Review Target` contract.

**Proposed Text:**
> The canonical machine-readable schema for this target **SHALL** be maintained in a governed operations artifact, with a default implementation provided as `REVIEW_TARGET.yaml` in product source control. Policy **MAY** reference a successor artifact but **SHALL NOT** leave the schema undefined.

### §9 Approval rule & §10 Exceptions

**Feedback:** These sections are legally very strong. The defined `blocked` states, the clear remediation paths in §9.4, and the robust exception rules in §10 are all excellent. The prohibition of implied exceptions in §10.3 is a particular highlight and demonstrates a mature approach to governance. No legal gaps were identified in these sections.

**Scores:** Legal Enforceability: 5, Practical Operability: 5

**Recommendation:** No changes recommended.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §4.1 | The "proportionality" clause could be used to waive the core requirement for visual proof. | Add language that establishes a floor, preventing policy from completely eliminating the visual proof requirement for in-scope work. | High | 3 (Legal Enforceability) |
| 2 | §6.1 | The binding `Review Target` contract schema is deferred to an undefined future policy, weakening enforceability. | Strengthen the language to require a canonical, governed schema artifact, such as the recommended `REVIEW_TARGET.yaml`. | High | 3 (Legal Enforceability), 7 (Practical Operability) |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document establishes a critically important and well-defined governance process. Its principles are sound, and its language is largely precise and enforceable. The recommended changes are necessary to close two key legal gaps related to the enforceability of the review contract and the integrity of the process under variable policies.

**Top 3 Actions Required:**
1.  Amend §6.1 to create a hard binding to a defined, governed schema for the `Review Target`.
2.  Amend §4.1 to clarify that "proportionality" cannot be used to entirely waive the visual proof requirement.
3.  (No third critical action, the first two are the most pressing for legal soundness).
review_id: REV-AMD-2026-008-ADD-001-001
document_reviewed: amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md
document_version: 0.1.0
reviewer: Gemini
review_date: 2024-05-15
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.2
---

# Peer Review: Base Shell Navigation Primitives and Start-Here Control

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document fits perfectly as the first axis of the control-plane model defined in ADD-002 and correctly separates its concerns. |
| 2 | Completeness | 4 | It provides a sufficient "base" set of primitives for its stated purpose, though it could eventually be expanded to cover error states more explicitly. |
| 3 | Practical Operability | 3 | A subjective "weasel word" clause in Section 5.1 ("when ambiguity would cause mis-routing") undermines the otherwise clear and enforceable obligations. |
| 4 | Conflict Freedom | 5 | Explicit non-goals and a tightly defined scope prevent any conflict with its parent or sibling governance documents. |
| 5 | Style & Clarity | 4 | The document is well-written and adheres to the Style Guide, but the ambiguity in one key obligation slightly reduces its overall clarity. |
| | **Composite Score** | **4.2** | |

---

## Overall Assessment

### Strengths

-   **Clear Scope and Separation of Concerns:** Sections 0, 2, and 6 do an exemplary job of defining what this document does (govern navigation) and what it does not do (govern output depth or packaging). This precision is critical for legal enforceability and prevents scope creep.
-   **Strong Cross-Document Alignment:** This addendum is perfectly harmonized with its sibling, AMD-2026-008-ADD-002, where it is explicitly cited as governing "Axis 1" of the twelve-axis control plane. This demonstrates mature and coherent governance architecture.
-   **Enforceable Primitives:** The definitions for navigation classes in Section 3 and the `SHALL NOT` constraints in Section 4 create a clear, auditable framework that can be implemented and verified.

### Critical Gaps

-   **Subjective Enforceability in Shell Obligations:** The document's primary weakness lies in Section 5.1. The obligation for the shell to make the navigation class "observable to the user when ambiguity would cause mis-routing" is legally problematic. This "ambiguity" trigger is not objectively defined, making the obligation difficult to enforce in a dispute. It relies on interpretation rather than a clear, measurable condition. This phrase constitutes a "weasel word" that must be replaced with a specific, auditable rule.

---

## Article-by-Article Review

### Section 0. Status and intent

**Feedback:** This section is excellent. It clearly situates the addendum within the broader governance framework of AMD-2026-008 and correctly delineates its responsibilities from the sibling ADD-002 document. This is a best practice for creating a coherent, multi-part governance package.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 5

**Recommendation:** No changes needed.

### Section 3. Navigation classes

**Feedback:** The five defined classes provide a solid, logical foundation for shell navigation. They are distinct and cover the primary modes of user interaction in a turn-based system. The definitions are concise and sufficient for a base specification.

**Scores:** Completeness: 4, Practical Operability: 5

**Recommendation:** No changes needed for this version. Future versions might consider an `ERROR` or `CLARIFY` class, but its absence does not render this base document incomplete.

### Section 5. Shell obligations (navigation)

**Feedback:** This section contains the document's most significant flaw. While 5.2 and 5.3 are well-defined, Section 5.1 introduces a subjective standard that is not enforceable as written. The phrase "when ambiguity would cause mis-routing" would be a point of contention in any compliance audit or arbitration. The platform could argue ambiguity did not exist, while a user could argue it did, with no objective standard to settle the dispute. This must be tied to a specific condition or a defined set of navigation classes.

**Scores:** Practical Operability: 2, Legal Enforceability: 2

**Recommendation:** Revise Section 5.1 to create an objective, non-discretionary rule. For example, tie the observability requirement to specific navigation classes where the user's input shape is constrained.

**Proposed Text Change:**
> **Old Text (5.1):** Make the **active navigation class** **observable** to the user when ambiguity would cause mis-routing (e.g. choose vs free-form).
>
> **New Text (5.1):** Make the **active navigation class** **observable** to the user (e.g., via visual chrome or voice preamble) whenever the active class is **CHOOSE** or **MULTI_INPUT**, to ensure the user is aware of the constrained input format.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 5.1 | The obligation to make the navigation class "observable" is triggered by a subjective condition ("when ambiguity would cause..."), making it legally unenforceable. | Replace the subjective trigger with an objective one, tying the obligation to specific, high-ambiguity navigation classes like `CHOOSE` and `MULTI_INPUT`. | Critical | 3, 5 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document provides a solid and well-architected framework for shell navigation primitives that is highly consistent with the surrounding governance. However, the legally unenforceable "weasel word" clause in Section 5.1 is a critical flaw that must be corrected before this document can be considered fully operable and binding.

**Top 3 Actions Required:**
1.  Revise Section 5.1 to replace the subjective ambiguity clause with a clear, objective trigger for when the navigation class must be made observable.
2.  Incorporate the proposed text change or a functionally equivalent alternative that removes the legal ambiguity.
3.  Proceed with ratification once the change is implemented.
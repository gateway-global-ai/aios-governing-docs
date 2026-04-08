---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.1
reviewer: Gemini
review_date: 2026-04-08
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.0
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document meticulously defines its seams with ADD-001 and ADD-002 and correctly cross-references all context documents. |
| 2 | Completeness | 4 | The document is exceptionally thorough in scope, but its operational effectiveness for §19 depends on a separate, deferred artifact (AIOS-OPS-020). |
| 3 | Practical Operability | 3 | While legally robust, the sheer number of interacting gates and contracts (§5, §9.4, §17, §18, §19, §20) presents a significant implementation and audit complexity risk. |
| 4 | Conflict Freedom | 5 | No conflicts were found; the document explicitly manages its relationship with parent and sibling documents, particularly in §2.1 and §16.7. |
| 5 | Style & Clarity | 3 | The document is precise but extraordinarily dense, which impairs clarity and increases the risk of misinterpretation by implementers. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

This document establishes a legally sophisticated and robust framework for governing AI-driven composition. Its strengths are significant:

-   **Liability Safe Harbors (§9.4, §19.9):** The Professional-use draft disclosure in §9.4 is exemplary. It provides clear, enforceable rules for marking drafts, including mandatory disclosure text and, critically, an obligation in §9.4.3(5) to block exports that would strip the disclosure. This creates a strong, defensible safe harbor.
-   **Fail-Closed Semantics (§5.9, §19):** The explicit `fail-closed` tables for the composition contract (§5.9) and originality gates (§19) are a cornerstone of its legal enforceability. This is not aspirational guidance; it is a set of binding, auditable rules that would hold up in arbitration.
-   **Precise Terminology (§20.3, §20.11):** The document wisely distinguishes between "template," "reference," and "authority," and explicitly forbids the use of the term "temperature" for "adherence" controls. This terminological discipline is crucial for avoiding legal ambiguity.
-   **Separation of Concerns:** The document correctly separates doctrinal requirements (this addendum) from implementation specifics (e.g., `AIOS-OPS-020` for originality scoring), which is a sound governance architecture.

### Critical Gaps

The primary issues stem from the document's immense complexity, which creates operational and legal risk.

-   **Implementation Complexity:** The document defines at least six distinct, interlocking "contracts" or gates (Composition §5, Professional-use §9.4, Language §16, Measurement §17, Knowledge §18, Originality §19, Reference §20). The sequential and parallel obligations described in §18.11 are legally sound but operationally daunting. There is a high risk that implementers will fail to apply all gates correctly, creating compliance gaps despite the well-written rules.
-   **Vague Enforcement Triggers:** While the rules themselves are often precise, the triggers for applying them sometimes rely on undefined policy. For example, §9.4 applies when an artifact is "classified or reasonably intended for" professional use. Without a clear policy on how "reasonably intended" is determined, this could be a point of contention.
-   **Density Impedes Clarity:** The document's density is its greatest weakness. Sections like §1, §5.9, and §18.11 are packed with cross-references and nested concepts. This makes the document difficult to parse and increases the risk of implementation errors. A less dense structure, perhaps by splitting some sections into annexes or separate documents as suggested by the R&D notes, would improve its practical utility.

---

## Article-by-Article Review

### §5. Composition contract requirements

**Feedback:** This section establishes a sound "role, intent, outcome" triad as a prerequisite for non-trivial composition. The `scaffold-only` boundary (§5.4) is a good fallback. The most critical component is the `fail-closed` enforcement table in §5.9, which is legally excellent—it translates principles into non-negotiable outcomes.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** No changes required. This section is a model for how to structure enforceable governance.

### §9.4. Professional-use draft disclosure

**Feedback:** This is the document's most important liability-limiting section. The mandatory disclosure text and the rule in §9.4.3(5) to preserve the disclosure on export are legally critical. The distinction between the three levels of assistance in §9.4.1 is sharp and defensible. The only weakness is the trigger, which relies on the artifact being "classified or reasonably intended" for professional use. This could be tightened.

**Scores:** Legal Enforceability: 5, Completeness: 4

**Recommendation:** Add a sentence to §9.4 to clarify how "reasonably intended" is determined.

*   **Proposed Text Change (in §9.4):** "The determination of whether an artifact is 'reasonably intended' for professional use SHALL be governed by policy, which SHALL consider, at a minimum, the document subclass (§9.2), the active composition contract (§5), and any explicit user declarations."

### §17. Measurement contract and quantified claims

**Feedback:** This is an excellent, and often overlooked, area of legal risk. Forcing confirmation of `method`, `unit`, and `basis` for material quantities is a powerful control against misrepresentation. The fallbacks in §17.5 (confirm, scaffold, disclose) are practical and reduce liability.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** No changes required.

### §19. Originality, source-boundary, and non-reproduction verification

**Feedback:** This section successfully navigates a legal minefield. It correctly frames the goal as risk reduction and policy enforcement, not a guarantee of non-infringement (§19.9). The `SHALL`/`MUST NOT` obligations for the release-time gate are binding and clear. The tension between the strong enforcement rules (§19.2, §19.4, §19.5) and the disclaimer (§19.9) is handled correctly; the disclaimer limits external promises without weakening internal governance. The handoff to `AIOS-OPS-020` is a proper separation of concerns, though it makes this document dependent on another artifact for full operational meaning.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5

**Recommendation:** Add a clarification in §19.1 to explicitly state that the §19.9 disclaimer does not create an exception to the §19.2 enforcement obligations. The current text in §19.2 does this, but reinforcing it at the start of the section would be beneficial.

*   **Proposed Text Change (add to the end of the first paragraph of §19.1):** "The disclaimer of absolute legal outcomes in §19.9 SHALL NOT be interpreted as a waiver of the explicit runtime enforcement obligations defined in this section."

### §20. Reference-guided composition

**Feedback:** This section is well-drafted from a legal perspective. The clear distinction between `template`, `reference`, and `authority` is crucial. The explicit disavowal of "temperature" for "adherence" controls is excellent legal hygiene. Most importantly, §20.14 provides a critical backstop by stating that maximum adherence does not bypass the §19 originality gate. This prevents the feature from being used as a loophole for high-fidelity copying.

**Scores:** Legal Enforceability: 5, Style & Clarity: 4

**Recommendation:** No changes required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §9.4 | The trigger for professional-use disclosure ("reasonably intended") is slightly ambiguous. | Add a sentence clarifying that this determination is governed by policy based on specific factors like document subclass and composition contract. | Medium | 3, 7 |
| 2 | §19.1 | The relationship between the enforcement rules (§19.2) and the legal disclaimer (§19.9) could be misinterpreted. | Add a sentence at the beginning of the section to reinforce that the disclaimer does not weaken the internal enforcement obligations. | Low | 3, 8 |
| 3 | General | The document's extreme density impairs readability and increases implementation risk. | For the next major revision, consider splitting the twelve axes (§6) into more manageable addenda or annexes, as suggested by `AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001`. | High | 7, 8 |

---

## Final Verdict

**Disposition:** **approved_with_changes**

**Rationale:** The document provides a legally sophisticated and defensible framework for a high-risk domain. Its strengths, particularly the fail-closed semantics and liability-limiting disclosures, are exemplary. The disposition is not "Approved" because the document's extreme complexity and density pose a significant risk to practical operability and clear implementation, which must be addressed.

**Top 3 Actions Required:**
1.  **Address Complexity:** In the next revision cycle, heed the advice of the architecture memos and consider breaking this monolithic document into more focused addenda. The current "twelve-axis" model is not sustainable.
2.  **Clarify Policy Triggers:** Implement the recommendation for §9.4 to ensure the triggers for applying mandatory disclosures are as unambiguous as the disclosures themselves.
3.  **Cross-reference Implementation:** Ensure that the dependent `AIOS-OPS-020` document is developed and versioned in lockstep with this one to avoid a situation where doctrine exists without a binding, testable implementation.
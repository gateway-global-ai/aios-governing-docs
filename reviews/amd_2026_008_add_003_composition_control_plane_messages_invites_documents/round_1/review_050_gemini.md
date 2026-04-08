review_id: REV-AMD-2026-008-ADD-003-002
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.5
reviewer: Gemini
review_date: 2026-04-11
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.4
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document demonstrates exemplary management of dependencies and seams, with clear, precise handoffs to ADD-001, ADD-002, MPOA, and AIOS-OPS-020. |
| 2 | Completeness | 5 | The twelve-axis control plane model provides a comprehensive framework that appears to cover all scoped aspects of artifact composition without obvious gaps. |
| 3 | Practical Operability | 3 | While legally and architecturally sound, the sheer density and complexity of the twelve interacting control axes present a significant implementation and audit challenge. |
| 4 | Conflict Freedom | 5 | The document is meticulously drafted to avoid conflict, correctly subordinating itself to the MPOA for liability and explicitly defining its seams with other addenda. |
| 5 | Style & Clarity | 4 | The writing is overwhelmingly precise, but the use of the word "SHOULD" in Section 20 introduces legal ambiguity where a binding obligation (SHALL) may be intended. |
| | **Composite Score** | **4.4** | |

---

## Overall Assessment

This is an exceptionally robust and legally sophisticated governance document. It demonstrates a profound understanding of the liability and intellectual property risks inherent in enterprise-grade generative AI. The systematic use of fail-closed defaults, explicit disclaimers, and clear procedural gates for high-risk areas like professional-use documents and source-derived content provides a strong, defensible framework.

### Strengths

-   **Liability Mitigation:** Sections 9.4 (Professional-use draft disclosure), 17.7 (Accuracy, reliance, and MPOA), and 19.9 (What this addendum does not claim) are exemplary. They create clear, enforceable boundaries that properly disclaim warranties and subordinate the document to the MPOA, which would be critical in any dispute resolution.
-   **Architectural Clarity:** The explicit definition of "addendum seams" (§2.1) and the clear handoff of implementation details to `AIOS-OPS-020` (§19.10) create a modular and internally consistent governance structure. This separation of concerns is a hallmark of mature legal and technical architecture.
-   **Precise Controls:** The distinction between "template," "reference," and "authority" (§20.3) and the replacement of "temperature" with a "reference adherence" scale (§20.11) replace ambiguous technical jargon with governable, specific controls. The rule in §20.14, which ensures maximum adherence does not bypass the §19 originality gate, is a crucial and well-conceived safeguard.

### Critical Gaps

-   **Legal Ambiguity via "SHOULD":** The document uses "SHOULD" in several places within Article 20, most notably §20.2 and §20.8. In a legal context, "SHOULD" is a recommendation, not a binding obligation like "SHALL." This creates potential loopholes where the system is not strictly required to perform critical pre-draft analysis on reference documents, undermining the section's intent.
-   **Operational Complexity:** The twelve-axis control plane (§6), while comprehensive, creates a highly complex operational environment. The document is so dense that it risks becoming difficult to implement and audit correctly, potentially leading to unintentional non-compliance. This "perfect is the enemy of good" scenario lowers the document's practical operability.

---

## Article-by-Article Review

### Section 5.9: Fail-closed rejection semantics

**Feedback:** This section provides a strong, enforceable backbone for the entire document. The mapping of specific failures to non-negotiable enforcement outcomes ("SHALL not proceed") is clear and auditable. The binding of these failures to specific DCP codes in `AIOS-OPS-020` is an excellent design choice, making the governance machine-readable and testable.

**Scores:** Legal Enforceability: 5, Practical Operability: 5

**Recommendation:** No changes. This section is a model for how to write enforceable governance.

### Section 9.4: Professional-use draft disclosure

**Feedback:** This is a masterfully drafted liability shield. It correctly identifies the risk, establishes a clear doctrine of producing "drafts for review," and mandates specific, persistent disclosures. The rule in §9.4.3(5) to block export or force user acknowledgment if the disclosure cannot be preserved is particularly strong and would hold up well in arbitration.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5

**Recommendation:** No changes.

### Section 19: Originality, source-boundary, and non-reproduction verification

**Feedback:** This section provides a robust, operational risk-control framework without over-promising legal outcomes it cannot guarantee. The disclaimer in §19.9 is essential and well-worded. The mandate for stricter thresholds on external-facing channels (§19.4) is a critical, common-sense control. The handoff of the implementation specifics to a versioned operations standard (`AIOS-OPS-020`) is a sound practice that allows the doctrine to remain stable while the technical methods evolve.

**Scores:** Legal Enforceability: 5, Cross-Document Consistency: 5

**Recommendation:** No changes.

### Section 20: Reference-guided composition

**Feedback:** This section provides an innovative and precise framework for a complex problem. However, its legal strength is weakened by the use of "SHOULD" instead of "SHALL" for key process steps. For example, §20.2 states the runtime "SHOULD determine whether it is used primarily for structure, tone, style..." and §20.8 states the runtime "SHOULD resolve" a list of critical pre-draft questions. This suggests these crucial analysis steps are optional, creating a gap in enforcement.

**Scores:** Legal Enforceability: 3, Style & Clarity: 3

**Recommendation:** To ensure these pre-draft analysis steps are binding obligations, replace "SHOULD" with "SHALL" or rephrase as a direct mandate.

-   **Change §20.2, last paragraph:**
    -   **Old Text:** "Where a reference is supplied, the runtime SHOULD determine whether it is used primarily for structure, tone, style, formatting, or authoritative conformity before substantive drafting proceeds (when policy or workflow requires disposition)."
    -   **New Text:** "Where a reference is supplied, the runtime SHALL determine whether it is used primarily for structure, tone, style, formatting, or authoritative conformity before substantive drafting proceeds (when policy or workflow requires disposition)."

-   **Change §20.8, opening sentence:**
    -   **Old Text:** "Before substantive drafting, the runtime SHOULD resolve (or surface for user confirmation) where references apply:"
    -   **New Text:** "Before substantive drafting, the runtime SHALL resolve (or surface for user confirmation) where references apply:"

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §20.2, §20.8 | Use of "SHOULD" creates a recommendation instead of a binding obligation, introducing a potential legal loophole. | Replace "SHOULD" with "SHALL" in §20.2 and §20.8 to make the pre-draft analysis of reference documents a mandatory step. | Critical | 3, 5 |
| 2 | §6, Overall | The high complexity of the twelve-axis control plane, while complete, may hinder practical implementation and auditing. | Consider authoring a supplementary, non-normative "Implementation Guide" or reference architecture that maps the twelve axes to a concrete state machine or data flow. This would improve operability without weakening the doctrine. | Medium | 7 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is legally and architecturally exemplary, providing a powerful framework for mitigating risk. However, the use of "SHOULD" in a critical section introduces an unacceptable level of legal ambiguity that must be corrected. The document's complexity also merits the creation of supporting materials to ensure it can be implemented as intended.

**Top 3 Actions Required:**
1.  Remediate the use of "SHOULD" in Article 20 to ensure pre-draft analysis is a binding `SHALL` requirement.
2.  Review the entire document for any other instances of "SHOULD" that may weaken intended obligations.
3.  Add the creation of a non-normative implementation guide to the product backlog to address the "Practical Operability" concerns stemming from the document's complexity.
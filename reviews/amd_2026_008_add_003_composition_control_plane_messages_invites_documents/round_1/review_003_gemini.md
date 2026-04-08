review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.10.0
reviewer: Gemini
review_date: 2024-06-11
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.6
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document expertly integrates with ADD-001 and ADD-002, clearly defining its orthogonal role and correctly cross-referencing concepts like packaging and BOOK workflows. |
| 2 | Completeness | 5 | This document is exceptionally thorough, defining a comprehensive twelve-axis control plane that addresses not just artifact types but also contracts, knowledge-basis, originality, and reference guidance. |
| 3 | Practical Operability | 4 | The principles are highly operable, but a few phrases like "where feasible" (§9.4.3) introduce ambiguity that could weaken enforcement in an auditable system. |
| 4 | Conflict Freedom | 4 | The document does an excellent job disclaiming liability (§9.4) and copyright guarantees (§19), but the phrase "reasonably intended" for professional-use documents could create a slight interpretive tension with the MPOA. |
| 5 | Style & Clarity | 5 | The document adheres to the Style Guide, using precise, unambiguous language to introduce complex but well-defined governance concepts that are critical for legal and operational clarity. |
| | **Composite Score** | **4.6** | |

---

## Overall Assessment

### Strengths

This is an exemplary governance document from a legal and compliance perspective. It demonstrates a mature understanding of the risks associated with AI-generated content and proactively establishes robust, enforceable controls to mitigate them.

-   **Section 5 (Composition Contract):** The `role, intent, outcome` triad is a powerful framework that moves governance from simple output formatting to a legally defensible model of intent-based creation. The scaffold-only fallback for ambiguity is a critical risk-reduction mechanism.
-   **Section 9.4 (Professional-use draft disclosure):** This section is outstanding. It creates a clear liability boundary by positioning the AI OS as a drafter's assistant, not a licensed professional. The mandatory disclosure text is strong and would be highly valuable in limiting liability.
-   **Sections 17-20 (Measurement, Knowledge, Originality, Reference):** These sections introduce sophisticated, first-class governance controls for concepts that are often left to chance. The `measurement contract` (§17), `discovery-before-creation` rule (§18), explicit non-guarantee of copyright safety (§19), and clear distinction between `reference`, `template`, and `authority` (§20) are legally robust and would stand up well to scrutiny. The clarification that `adherence` is not `temperature` is a model of precision.

### Critical Gaps

The document is very strong, with only minor gaps that should be tightened to remove any potential for misinterpretation or exploitation.

-   **Vague Enforcement Language:** In a few critical places, the language is softer than the rest of the document, creating potential loopholes. The most significant is in §9.4.3, where the obligation to preserve a legal disclosure in exports is qualified with "where feasible." This could be interpreted broadly to justify omitting the disclosure.
-   **Ambiguous Trigger for Professional-Use Disclosure:** Section 9.4 states it applies when an artifact is "classified or reasonably intended for... licensed-professional review or use." The term "reasonably intended" is a classic legal ambiguity. While difficult to eliminate entirely, it could be tightened by linking it more directly to the document subclasses defined in §9.2.

---

## Article-by-Article Review

### Section 9.4 Professional-use draft disclosure

**Feedback:** This is the most legally critical section and it is executed very well. The distinction between drafting assistance and a final professional instrument is a crucial liability shield. The mandatory disclosure text is clear and comprehensive. My only concern is with the implementation and enforcement clauses.

**Scores:** Legal Enforceability: 4, Practical Operability: 4

**Recommendation:** Strengthen the obligation to preserve the disclosure in exported documents.

*   **Current Text (§9.4.3, item 5):** "preserve that disclosure in exported versions **where feasible** (**MD**, **PDF**, **DOCX**, **HTML**, etc.)."
*   **Proposed Text:** "preserve that disclosure in exported versions. For formats that do not support embedded text (e.g., plain images), the export process **SHALL** require user acknowledgment of the disclosure before completion. The phrase 'where feasible' **SHALL NOT** be used to bypass this obligation for text-based formats."

This change closes a potential loophole and makes the obligation to warn the user much more explicit and auditable.

### Section 19 Originality, source-boundary, and non-reproduction verification

**Feedback:** The framing of this section is legally sound. Explicitly stating that it "SHALL NOT be read as a guarantee of copyright 'safety'" (§19) is paramount. The distinction between internal and external thresholds (§19.4) is a practical and defensible policy. The section correctly focuses on operational risk controls rather than making unenforceable legal promises. No changes are required, but this is a key strength.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5

**Recommendation:** No changes recommended. This section should be used as a model for how to govern high-risk AI behaviors.

### Section 20 Reference-guided composition

**Feedback:** This section successfully navigates the complex legal area of derivative works. The distinction between `template`, `reference`, and `authority` (§20.3) is legally precise and operationally valuable. The explicit rule in §20.14 that maximum adherence does not authorize reproduction of protected text is a critical safeguard that must be preserved.

**Scores:** Legal Enforceability: 5, Style & Clarity: 5

**Recommendation:** No changes recommended. The clarity in separating `adherence` from `temperature` (§20.11) is a prime example of the document's strength.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §9.4.3 | The phrase "where feasible" creates a loophole for preserving the mandatory professional-use disclosure in exports. | Replace "where feasible" with stronger language that makes disclosure preservation a firm requirement for all text-supporting formats. | Critical | 3, 7 |
| 2 | §9.4 | The trigger "reasonably intended" for professional-use classification is ambiguous. | Add a clause clarifying that this intent can be inferred from the document's `subclass` (per §9.2), e.g., "This intent **SHALL** be presumed for subclasses such as **CONTRACT_SUMMARY** and **POLICY**." | High | 3, 7 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is exemplary and establishes a new standard for AI composition governance. Its composite score of 4.6 is very high. The recommended changes are minor but critical for closing potential legal loopholes in an otherwise robust and enforceable framework.

**Top 3 Actions Required:**
1.  Strengthen the language in §9.4.3 to ensure the professional-use disclosure is preserved in exports without exception for text-based formats.
2.  Clarify the trigger for professional-use classification in §9.4 by linking it to the normative document subclasses in §9.2.
3.  Proceed with ratification after incorporating the above changes.
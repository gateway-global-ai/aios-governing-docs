---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.13.0
reviewer: Gemini
review_date: 2026-04-12
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 3.4
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document expertly defines its seams and dependencies with other addenda, especially ADD-001 and ADD-002. |
| 2 | Completeness | 3 | While incredibly comprehensive in scope, it has a critical gap in §19 where operational thresholds are left undefined. |
| 3 | Practical Operability | 2 | The originality/source-boundary gate (§19) is inoperable as specified because it lacks defined, auditable thresholds for enforcement. |
| 4 | Conflict Freedom | 4 | No direct contradictions with other governing documents were found; it correctly defers to the MPOA for liability and ADD-002 for its own scope. |
| 5 | Style & Clarity | 3 | The document adheres to the Style Guide, but its extreme density and length in a single addendum create a significant barrier to clarity. |
| | **Composite Score** | **3.4** | |

---

## Overall Assessment

### Strengths

This document is a remarkably thorough and mature piece of governance that demonstrates a deep understanding of the legal and operational risks inherent in advanced AI composition tools.

-   **Professional-Use Disclosures (§9.4):** This section is exemplary. The mandatory disclosure text, the rules for preserving it on export, and the "block or warn" protocol create a legally robust framework for managing liability in high-stakes use cases.
-   **Measurement Contracts (§17):** The requirement to govern quantified claims by defining their method, unit, and basis is a sophisticated control that proactively mitigates a common source of contractual and technical disputes.
-   **Authoritative Language (§16.5):** The mandate to identify an authoritative version in multilingual contexts is a critical and well-articulated rule for preventing legal ambiguity in contracts, policies, and other binding documents.
-   **Architectural Rigor (§2.1, §6):** The document shows excellent discipline in defining its scope and respecting the boundaries of other documents. The twelve-axis control-plane model provides a clear map of all governed concerns.

### Critical Gaps

The document's primary failure is that a key risk-mitigation control is functionally unenforceable as written.

-   **Inoperable Originality Gate (§19):** The entire non-reproduction and source-boundary verification framework is built on verification states (e.g., `overlap_review_required`, `high_reproduction_risk_blocked`) that are triggered by exceeding undefined thresholds. The document states that "Policy SHALL support different thresholds" but fails to specify them or normatively reference a document that does. This renders the entire section aspirational rather than operational and would not hold up to scrutiny, as the rules are too vague to be audited or enforced consistently.
-   **Excessive Density:** While comprehensive, the sheer volume of doctrine in this single addendum is overwhelming. It combines core artifact definitions with numerous complex, high-stakes gates (Knowledge Basis, Originality, Reference Guidance, etc.). This harms clarity and makes the document difficult to review, ratify, and implement as a single unit.

---

## Article-by-Article Review

### §9.4 Professional-use draft disclosure

**Feedback:** This is the strongest section of the document from a legal and compliance perspective. The distinction between levels of assistance, the mandatory disclosure text, and the export preservation rules (§9.4.3(5)) are clear, robust, and enforceable. The cross-reference to the MPOA in §9.4.6 correctly situates these operational rules within the platform's primary commercial and liability framework.

**Scores:** Practical Operability: 5, Completeness: 5

**Recommendation:** (Minor) In §9.4.3(5), consider specifying the minimum required content for the "blocking warning" to ensure the user's acknowledgment constitutes legally meaningful informed consent. For example: "The warning SHALL, at minimum, state that the chosen format cannot preserve the 'Draft for Professional Review' disclosure and that the user assumes all responsibility for its use without this context."

### §17. Measurement contract and quantified claims

**Feedback:** This is an excellent and sophisticated piece of governance. By forcing a distinction between a number and the *method* used to derive it, it closes a significant loophole that often leads to legal disputes. The rules are clear and the distinction between mandatory confirmation for high-stakes documents and lighter handling for casual use is practical.

**Scores:** Practical Operability: 5, Completeness: 5

**Recommendation:** No changes recommended. This section could serve as a model for other documents.

### §19. Originality, source-boundary, and non-reproduction verification

**Feedback:** This section has a critical, structural failure. While its intent is sound and the disclaimer in §19.9 is well-drafted, the core operational rules are unenforceable. The document mandates verification gates based on concepts like "high verbatim overlap" and "structurally excessive similarity" but provides no objective, numerical, or procedural definition of what constitutes these states.

**Scores:** Practical Operability: 1, Completeness: 2

**Recommendation:** **This section MUST be revised.** It must define the mechanism for its own enforcement.
-   **Proposed Change:** Amend §19.4 or add a new subsection to define the thresholds. Either include the thresholds directly (e.g., "An `overlap_review_required` state SHALL be triggered if an output shares more than a 15% verbatim token-sequence overlap with any single knowledge base source, excluding policy-defined quoted material.") or, preferably, add a normative requirement: "The specific methods, algorithms, and numerical thresholds for originality and source-boundary verification SHALL be defined in the governing specification AIOS-SPEC-014 (Content Originality Verification)." This would make the rule operational and auditable.

### §20. Reference-guided composition

**Feedback:** This section provides a strong framework for a complex feature. The distinction between `template`, `reference`, and `authority` (§20.3) is legally precise and useful. The `adherence` scale (§20.13) and its explicit separation from "temperature" (§20.11) provides a clear, governable control. The link back to the §19 originality gate in §20.14 is a sign of excellent internal consistency.

**Scores:** Cross-Document Consistency: 5, Practical Operability: 4

**Recommendation:** No major changes required, but operability would be improved by clarifying how the system should behave if a user provides contradictory references (e.g., one formal, one informal) for the same composition task.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19 | The entire section is rendered inoperable by the lack of defined, auditable thresholds for its verification gates. | Amend the section to either specify numerical thresholds for originality states or to normatively require their definition in a separate specification document. | **Critical** | 3 (Practical Operability), 2 (Completeness) |
| 2 | Document Structure | The document's extreme length and density harm clarity and make it difficult to review and implement effectively. | Consider splitting this addendum into two or three documents: e.g., ADD-003 for core composition classes/contracts, and a new ADD-004 for advanced gates (Knowledge, Originality, Reference). | High | 5 (Style & Clarity) |
| 3 | §9.4.3(5) | The "blocking warning" for exports that strip disclosures is not defined, creating ambiguity in what constitutes valid user consent. | Specify the minimum content of the warning to ensure the user's acknowledgment is legally informed and auditable. | Medium | 3 (Practical Operability) |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document receives this disposition because a critical risk-mitigation control—the originality and source-boundary gate in §19—is inoperable as written due to a failure to define its enforcement thresholds. This is a major issue that undermines a core purpose of the document. Additionally, its composite score of 3.4 is below the 3.5 threshold required for "Approved with Changes."

**Top 3 Actions Required:**
1.  **Fix §19:** Revise §19 to include specific, auditable thresholds for originality verification, or add a normative requirement for these thresholds to be defined in a new specification.
2.  **Improve Clarity:** Strongly consider splitting the document into more manageable, focused addenda to improve readability and implementation feasibility.
3.  **Refine §9.4:** Add language to §9.4.3(5) to specify the minimum content of the export warning, ensuring any user acknowledgment of risk is explicit and informed.
---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.0
reviewer: Gemini
review_date: 2026-04-08
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.4
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document meticulously defines and respects its boundaries with ADD-001 and ADD-002, ensuring a coherent and non-conflicting control plane. |
| 2 | Completeness | 4 | The document is exhaustive in scope but deliberately defers the critical operational parameters for originality verification (§19.10) to a separate document, leaving a normative gap. |
| 3 | Practical Operability | 3 | While most rules are highly operational, the critical originality gate in §19 cannot be implemented or audited without the scoring thresholds and methods deferred in §19.10. |
| 4 | Conflict Freedom | 5 | No conflicts were found; the document expertly manages its seams with other addenda and cross-references parent documents like the MPOA appropriately. |
| 5 | Style & Clarity | 5 | The document is a model of precise, unambiguous legal and technical writing, adhering perfectly to the Style Guide despite its considerable density. |
| | **Composite Score** | **4.4** | |

---

## Overall Assessment

This addendum represents an exceptionally mature and robust governance framework for AI-driven composition. From a legal and compliance standpoint, it is a fortress, built on precise definitions, clear separation of concerns, and enforceable, "fail-closed" operational rules. The drafters have demonstrated a profound understanding of the liability, intellectual property, and reputational risks inherent in enterprise-grade generative AI and have constructed specific, auditable controls to mitigate them.

### Strengths

-   **Sophisticated Risk Management (§9.4, §17, §19, §20):** The document contains some of the best-drafted risk controls for AI composition seen to date. The Professional-Use Disclosure (§9.4), Measurement Contract (§17), Originality/Source-Boundary Gate (§19), and Reference-Guided Composition framework (§20) are legally sound, operationally specific, and clearly define liability boundaries.
-   **Enforceable "Fail-Closed" Semantics (§5.9):** The explicit requirement for the runtime to block or downgrade outputs that fail to meet governance criteria (e.g., missing composition contract, failed originality check) is the document's greatest strength. It translates abstract principles into non-negotiable, auditable runtime behavior that would hold up in arbitration.
-   **Precision and Unambiguity:** The document avoids "weasel words" and vague requirements. Obligations are expressed in clear `SHALL` / `SHALL NOT` statements. The distinction between `template`, `reference`, and `authority` (§20.3) and the rejection of the term "temperature" in favor of "adherence" (§20.11) are prime examples of the legal precision that permeates the text.

### Critical Gaps

-   **Inoperable Originality Gate (§19.10):** The most significant issue is the "implementation handoff" in §19.10. The document mandates a sophisticated originality and source-boundary verification gate but defers the actual scoring algorithms, numeric thresholds, and transport bindings to a separate, unreferenced "governed specification or operations artifacts." Without this referenced document, the entire of §19 is legally and practically inoperable. An auditor cannot verify compliance, and a developer cannot implement the gate. This turns a critical, mandatory control into an unenforceable promise.

---

## Article-by-Article Review

### §5. Composition contract requirements

**Feedback:** This section provides a strong, enforceable foundation for the entire document. The `role, intent, outcome` triad is a clear and effective control. The addition of fail-closed rejection semantics in §5.9 elevates this from a good idea to a binding, auditable rule. The conditions are specific and cover the key risk-gating sections of the addendum. This section is exemplary.

**Scores:** Legal Enforceability: 5, Practical Operability: 5

**Recommendation:** No changes recommended.

### §9.4 Professional-use draft disclosure

**Feedback:** This is an outstanding example of proactive liability management. The mandatory disclosure text is clear and appropriately disclaims legal validity. The runtime obligations, particularly §9.4.3(5) which requires preserving the disclosure on export or blocking the export with a warning, are robust and close a common loophole. This section would significantly strengthen the platform's defense against claims of unauthorized professional advice.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5

**Recommendation:** No changes recommended.

### §19. Originality, source-boundary, and non-reproduction verification

**Feedback:** The principles and framework in this section are excellent. The distinction between internal and external thresholds (§19.4), the defined verification states (§19.5), and the carefully worded disclaimer (§19.9) create a sophisticated risk-mitigation strategy.

However, the section's operational effectiveness is completely undermined by §19.10. By deferring the "implementation-specific validation logic, overlap/similarity scoring, threshold tables," the document makes the enforceability of §19 purely theoretical. This is a critical gap that must be closed before this addendum can be considered fully operational. An otherwise 5-star section is rendered a 3 on operability because of this dependency.

**Scores:** Legal Enforceability: 4, Practical Operability: 2

**Recommendation:**
The following MUST be addressed before ratification:
1.  Create the initial draft of the "governed specification or operations artifact" referenced in §19.10.
2.  Add a direct, versioned cross-reference to that new document within §19.10.
3.  The new specification must, at a minimum, provide placeholder or initial values for the thresholds that distinguish `originality_clear` from `overlap_review_required` and `high_reproduction_risk_blocked` for both internal and external channels.

**Proposed Text (addition to §19.10):**
> "...such that §19 verification is auditable and not solely implementation-defined without a traceable home. **The normative thresholds and scoring methodologies are defined in AIOS-SPEC-014 (Composition Originality Verification).** Products SHALL document which artifact supplies release-time evaluation for each conformance claim tied to this addendum."

### §20. Reference-guided composition

**Feedback:** This section effectively navigates the complex IP issues surrounding the use of reference materials. The distinction between `template`, `reference`, and `authority` provides necessary clarity. The rejection of "temperature" for the more precise "adherence" is a legally sound choice that prevents misinterpretation. The safeguard in §20.14, which explicitly states that maximum adherence is to *shape* not *verbatim content*, correctly subordinates this feature to the master originality gate in §19.

**Scores:** Legal Enforceability: 5, Cross-Document Consistency: 5

**Recommendation:** No changes recommended.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.10 | The originality verification gate is inoperable without the concrete thresholds and methods, which are deferred to an undefined document. | Before ratification, create and reference a new specification (e.g., AIOS-SPEC-014) that defines the initial, auditable thresholds and scoring methods for originality verification. | Critical | 2, 3 |
| 2 | §1, §21 | The document's purpose statement and non-goals list are extremely dense and contain long, run-on sentences that can be difficult to parse. | For clarity, refactor the longest sentences in §1 and the list items in §21 into bullet points or shorter, more distinct statements. This is an editorial suggestion, not a normative gap. | Low | 5 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is exceptionally strong from a legal and governance perspective, setting a new standard for AI composition risk management. However, the critical gap in §19.10 renders the entire originality verification framework inoperable as written, preventing ratification until the dependent specification is created and referenced.

**Top 3 Actions Required:**
1.  **Resolve §19.10 Dependency:** Draft and formally reference the new specification containing the originality verification thresholds. This is the only critical blocker to approval.
2.  **Review Informative Context:** Ensure that the product and operations teams review the informative memos (RD-NOTES, ARCHITECTURE-MEMO, SHELL-SURFACE-MEMO) to prevent implementation drift from the clear architectural intent.
3.  **Conduct Implementer Read-Out:** Given the document's density, a formal read-out session with the development teams responsible for implementation is highly recommended to ensure the subtleties of the fail-closed logic and various gates are fully understood.
review_id: REV-AMD-2026-016-002
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.2.0
reviewer: Gemini
review_date: 2026-04-11
review_round: 2
review_type: legal
disposition: approved_with_changes
composite_score: 4.4
---

# Peer Review: Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The revision expertly links new concepts to existing law in AIOS-SPEC-002 and -009 without creating conflicts. |
| 2 | Business Model Alignment | 4 | Strongly supports the enterprise model by providing a clear, auditable framework for service accounts and applications, which is critical for adoption. |
| 3 | Legal Enforceability | 4 | Vastly improved; the addition of default liability, ownership, and economic attribution rules makes the framework defensible and clear. |
| 4 | Architectural Fidelity | 5 | Perfectly reflects policy supremacy by establishing an admission-style validation sequence that must pass before any authority-bearing action can occur. |
| 5 | Completeness | 4 | The addition of a full principal lifecycle (§4.13) and conformance records (§4.15) addresses the most critical gap from Round 1. |
| 6 | Conflict Freedom | 5 | The narrowed scope in §2 and explicit impact analysis in §5 successfully prevent conflicts with shell authority and intent execution law. |
| 7 | Practical Operability | 4 | Moved from aspirational to operational; the validation sequence, registry requirements, and examples provide a clear implementation path. |
| 8 | Style & Clarity | 5 | The document remains a model of clarity, precision, and adherence to the Style Guide, even with substantial new content. |
| 9 | Developer Synchrony | 4 | The examples in §8 are a crucial addition, providing developers with concrete JSON shapes to guide implementation. |
| 10 | Platform Economics Synchrony | 4 | The new requirement for an `economic_subject` (§4.5, §4.14) directly connects non-human actions to the platform's economic model. |
| 11 | Friction Factor | 4 | The added governance is substantial but necessary and proportional to the risk of ungoverned non-human actors. |
| | **Composite Score** | **4.4** | |

---

## Overall Assessment

This is an exemplary revision that systematically and comprehensively addresses every critical and high-priority issue raised in the Round 1 reviews. The document has been transformed from an abstract statement of principles into a legally sound, operationally clear, and enforceable piece of governance.

### Strengths

1.  **Direct Remediation of R1 Gaps:** The author has precisely targeted and fixed the key failures from Round 1. The addition of a complete Principal Lifecycle (`§4.13`), default Liability and Ownership rules (`§4.11`, `§4.14`), Economic Attribution (`§4.14`), and a clear Enforcement Mechanism (`§4.6`, `§4.12`) is a masterclass in responding to peer feedback.
2.  **Legally Sound Attribution:** The new sections on liability, ownership, and economic attribution (`§4.11`, `§4.14`) are legally robust. They establish clear, defensible default rules while allowing for contractual overrides, which is standard practice. This would hold up in arbitration.
3.  **Operational Clarity:** The introduction of the `Validation and admission rule` (`§4.6`) and the `Principal registry` (`§3`, `§4.7`) provides a concrete, step-by-step enforcement model. Paired with the examples in `§8`, the document is no longer aspirational; it provides a clear blueprint for implementation and conformance.
4.  **Excellent Cross-Document Integration:** The revised `§5` now provides a section-level impact analysis, showing a deep understanding of how this new law interacts with existing specifications for `PolicyRecord` (AIOS-SPEC-002) and Intent Execution (AIOS-SPEC-009). The solution for integrating with the `Actor` schema (by making principal facts available in the policy context) is elegant and non-disruptive.

### Critical Gaps

No critical gaps remain. The recommendations below are minor clarifications to further harden what is already a very strong document.

---

## Article-by-Article Review

### §3. Definitions

**Feedback:** The new definitions (`Route class`, `Authority-bearing action`, `Principal registry`, `Conformance record`) are excellent and provide the necessary vocabulary to make the rest of the document enforceable. The tightening of `Scope binding` is also a significant improvement.

**Scores:** Legal Enforceability: 5, Style & Clarity: 5

**Recommendation:** No changes needed.

### §4. Normative decisions

**Feedback:** This section has been substantially and successfully rebuilt. The new subsections directly address all major R1 concerns.
-   **§4.6 Validation and admission rule:** This is the cornerstone of the new enforceable model. It provides a clear, auditable sequence of checks that must pass. This is excellent.
-   **§4.13 Principal lifecycle management rule:** This single-handedly remedies the critical failure of completeness from R1. The stages are logical and comprehensive.
-   **§4.14 Liability and economic attribution rule:** This is a legally critical addition. The language is precise and correctly assigns responsibility to the entity that owns and configures the non-human principal. The mandate to record an economic subject for metered activity closes a major loophole.
-   **§4.15 Minimum conformance record rule:** This is a strong mechanism for ensuring that the law translates into verifiable implementation, directly improving Practical Operability and Developer Synchrony.

**Scores:** Completeness: 5, Legal Enforceability: 4, Practical Operability: 4

**Recommendation:** In `§4.13`, consider adding a `SHALL` statement that credentials or trust material must be invalidated or rotated upon revocation, to make the security implication explicit.

**Proposed addition to §4.13:**
> Revocation or suspension **SHALL** take effect before new authority-bearing action is allowed. Upon revocation, any associated credentials or trust material **SHALL** be invalidated.

### §5. Relationship to existing governance

**Feedback:** The new table is a significant improvement, providing specific implementation impact for each related document. The guidance for `AIOS-SPEC-002` (making principal facts available via `required_context_keys`) and `AIOS-SPEC-009` (joining principal identity to audit truth) is clear, actionable, and resolves the R1 concern about schema conflicts cleanly.

**Scores:** Cross-Document Consistency: 5, Conflict Freedom: 5

**Recommendation:** No changes needed.

### §8. Minimum conformance examples (informative)

**Feedback:** The addition of these JSON examples is immensely valuable. It transforms the document's principles into a concrete, developer-friendly format. The examples directly illustrate the new concepts of a registry record, policy context, and action envelope.

**Scores:** Developer Synchrony: 5, Practical Operability: 5

**Recommendation:** No changes needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §4.13 | Security implication of revocation is implicit. | Add a `SHALL` statement clarifying that upon revocation, associated credentials or trust material must be invalidated. | Medium | 3, 7 |
| 2 | §4.15 | The location of the conformance record is flexible but could be ambiguous. | Consider adding an informative note suggesting that the `Principal registry` is the preferred location for linking to or storing the conformance record for a given principal. | Low | 7, 9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document has been revised to an exemplary standard, addressing all critical failures from the previous round. The composite score of 4.4 and the fact that no dimension scores below 4 demonstrates its strength. The remaining recommendations are minor clarifications that can be incorporated without a full revision cycle. This document is ready to serve as binding law.

**Top 3 Actions Required:**
1.  **Action 1 (from Rec #1):** In `§4.13`, add the proposed sentence: "Upon revocation, any associated credentials or trust material **SHALL** be invalidated." This makes the security requirement explicit and non-negotiable.
2.  **Action 2 (from Rec #2):** In `§4.15`, add an informative note suggesting a link between the `Principal registry` and the `Conformance record` to guide implementers toward a sensible default.
3.  **Action 3 (Editorial):** Review and ratify. The document has met the bar for approval.
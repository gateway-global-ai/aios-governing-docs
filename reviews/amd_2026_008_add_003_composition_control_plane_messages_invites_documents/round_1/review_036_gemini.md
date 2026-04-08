review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.3
reviewer: Gemini
review_date: 2026-04-10
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.6
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document demonstrates exceptional awareness of its place within the governance framework, with precise cross-references and clear "seam" definitions. |
| 2 | Completeness | 5 | It comprehensively covers its stated purpose, defining a multi-axis control plane for composition with remarkable depth and foresight. |
| 3 | Practical Operability | 4 | The rules are highly specific and auditable, but their complexity presents a significant implementation challenge that could lead to operational gaps if not managed carefully. |
| 4 | Conflict Freedom | 5 | The document expertly avoids conflicts by explicitly deferring to the MPOA on liability/commercial terms and clearly delineating its scope relative to ADD-001/ADD-002. |
| 5 | Style & Clarity | 4 | The language is precise and adheres to the Style Guide, but the sheer density of the rules, particularly in §§18-20, can be challenging for a reader to fully integrate. |
| | **Composite Score** | **4.6** | |

---

## Overall Assessment

This is an exceptionally robust and well-architected governance document. From a legal and compliance perspective, it is a model of how to define enforceable, auditable rules for complex AI-driven composition while carefully managing platform liability. The consistent use of "fail-closed" semantics, clear definitions of liability boundaries, and specific, non-vague requirements would make this document highly defensible in a formal dispute resolution setting.

### Strengths

-   **Explicit Liability Boundaries:** Sections like §17.7 (Accuracy, reliance, and MPOA) and §19.9 (What this addendum does not claim) are perfectly drafted. They clearly delineate the platform's procedural obligations from any warranty of factual accuracy or legal non-infringement, correctly deferring ultimate liability to the MPOA. This is critical for risk management.
-   **Enforceable "Fail-Closed" Semantics:** The tables in §5.9 and the rules throughout §§18-20 establish a "fail-closed" posture. If a required check (e.g., originality verification, knowledge basis sufficiency) is not met, the system is mandated to block or downgrade the action, not proceed silently. This is a powerful and legally sound enforcement mechanism.
-   **Precise, Actionable Rules:** The document avoids "weasel words." Instead of vague requirements, it defines specific states (e.g., knowledge sufficiency states in §18.5), triggers (e.g., professional-use triggers in §9.4.0), and controls (e.g., reference adherence scale in §20.13). This precision makes compliance auditable.
-   **Strong Disclosure Obligations:** The professional-use disclosure requirements in §9.4 are exemplary. The mandatory text, the trigger logic, and especially the obligation in §9.4.3(5) to preserve the disclosure on export (or block/warn) represent a best-in-class approach to managing risk for high-stakes generated content.

### Critical Gaps

The document has no critical gaps from a legal/compliance perspective. The identified issues are minor and aimed at further hardening an already excellent document. The primary risk is not in the doctrine itself, but in the operational complexity of implementing it perfectly.

---

## Article-by-Article Review

### Section 5. Composition contract requirements

**Feedback:** This section establishes a strong foundation with the "role, intent, outcome" triad. The fail-closed semantics in §5.9 are the key enforcement mechanism and are very well-defined. The explicit blocking of "substantive drafting" without a satisfied contract is a clear, enforceable rule.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** No changes required. This section is a benchmark for quality.

### Section 9.4. Professional-use draft disclosure

**Feedback:** This is the most critical section from a direct liability standpoint, and it is handled masterfully. The trigger logic, the mandatory disclosure text, and the export-preservation rules create a defensible "safe harbor" for the platform. It correctly positions the AI as an assistant to, not a replacement for, a licensed professional.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5

**Recommendation:** No changes required. This section should be used as a template for other governance documents.

### Section 17. Measurement contract and quantified claims

**Feedback:** The requirement to confirm or declare the measurement method, unit, and basis is an excellent control against disputes arising from ambiguity. Section 17.7, which explicitly decouples these procedural requirements from MPOA-governed liability for reliance, is a perfect example of a clear liability boundary.

**Scores:** Legal Enforceability: 5, Cross-Document Consistency: 5

**Recommendation:** No changes required.

### Section 19. Originality, source-boundary, and non-reproduction verification

**Feedback:** This section successfully navigates the fine line between providing a meaningful operational control and making unsupportable legal guarantees about copyright. The disclaimer in §19.9 is crucial and well-written. The binding of implementation details to a separate, governed operations document (AIOS-OPS-020) is a sound architectural choice that keeps this amendment focused on high-level law.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** To further strengthen the "fail-closed" principle, consider a minor addition to the introduction of §19.2.

-   **Section:** 19.2
-   **Issue:** The phrase "when policy or artifact class requires it" could be read as permissive, potentially allowing new artifact classes to bypass this gate by default if no policy is explicitly attached. While §5.9 closes this loop, reinforcement here would add clarity.
-   **Recommendation:**
    -   **Current Text:** "For **composed artifacts** **derived** from **knowledge-base** or **other** **source** materials, the runtime **SHALL** apply an **originality** and **source-boundary** verification **gate** before **publish**, **send**, or **formal export** actions when **policy** or **artifact class** requires it."
    -   **Proposed Text:** "For **composed artifacts** **derived** from **knowledge-base** or **other** **source** materials, the runtime **SHALL** apply an **originality** and **source-boundary** verification **gate** before **publish**, **send**, or **formal export** actions. **Policy** **SHALL** define the **thresholds** for this gate; in the absence of an explicit policy permitting release, the gate **SHALL** fail closed per **§5.9**."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 19.2 | The conditional phrasing "when policy...requires it" could be misinterpreted as an opt-in system. | Strengthen the language to clarify that the verification gate is default-on for derived artifacts, with policy defining the thresholds, reinforcing the fail-closed principle from §5.9. | Medium | 3, 7 |
| 2 | 21 | The title "Non-goals" is informal. | Rename the section to "Scope Exclusions" to align with the formal, legalistic tone of the rest of the document. | Low | 5, 8 |

---

## Final Verdict

**Disposition:** Approved with Changes

**Rationale:** The document is exemplary and fundamentally sound, setting a new standard for AI composition governance. The disposition of "Approved with Changes" is chosen because the minor recommended clarifications, while not critical, would further harden its legal enforceability and remove any potential for misinterpretation.

**Top 3 Actions Required:**
1.  **Accept Recommendation #1:** Fortify the language in §19.2 to make the originality gate an unambiguous default-on requirement for derived works.
2.  **Accept Recommendation #2:** Retitle §21 to "Scope Exclusions" for stylistic and tonal consistency.
3.  **Conduct an Implementation Complexity Review:** While not a flaw in the document, its density and the interconnectedness of its rules pose a significant implementation risk. A separate review focused on creating an auditable implementation plan is highly recommended before this doctrine is considered fully operational.
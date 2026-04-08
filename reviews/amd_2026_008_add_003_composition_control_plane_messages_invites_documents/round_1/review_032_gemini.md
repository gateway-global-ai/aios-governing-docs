review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.2
reviewer: Gemini
review_date: 2026-04-10
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The document effectively establishes "seams" and handoffs, particularly to ADD-002 and the new OPS standard for originality. |
| 2 | Completeness | 4 | The twelve-axis control plane is exceptionally comprehensive, covering a vast range of composition-related governance concerns. |
| 3 | Practical Operability | 4 | The strong fail-closed semantics and clear gating sequences provide a robust framework for implementation, though its complexity is high. |
| 4 | Conflict Freedom | 4 | The document diligently avoids conflict by explicitly defining its scope relative to other addenda and deferring to the MPOA for liability. |
| 5 | Style & Clarity | 3 | While precise, the document's reliance on extremely long, dense sentences with heavy inline cross-referencing impairs readability and clarity. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

This document establishes a remarkably thorough and legally robust framework for governing AI-driven composition. Its key strengths are:

1.  **Strong Fail-Closed Semantics (§5.9, §19.1):** The principle of failing closed when required gates (Composition Contract, Originality Verification, etc.) are not met is a cornerstone of sound legal and operational risk management. This shifts the burden to proving a "good state" before proceeding, which is highly defensible.
2.  **Excellent Liability Partitioning (§9.4, §19.9):** The document does an exemplary job of setting operational guardrails while explicitly disclaiming legal guarantees. The professional-use disclosure (§9.4) and the originality disclaimer (§19.9) are well-drafted to manage platform liability by clearly defining the system's role as an assistant, not a final authority.
3.  **Clear Separation of Concerns (§2.1, §19.10):** The explicit definition of "seams" with ADD-001/ADD-002 and the architectural decision to hand off implementation details (like scoring thresholds in §19) to a separate, versioned Operations Standard is best practice. This makes the governance framework both modular and maintainable.

### Critical Gaps

Despite its strengths, the document has several gaps that introduce legal ambiguity or risk:

1.  **Use of Vague or Undefined Legal Terms:** The document uses terms like "reasonably intended" (§9.4) and "substantial protected expression" (§19.2) without providing a specific, contractually-binding definition within the AIOS framework. These terms are subject to external legal interpretation, creating ambiguity that could be exploited in a dispute.
2.  **Implicit Liability for Factual Accuracy:** While §17 (Measurement Contract) defines a strong process for handling quantified claims, it does not explicitly state where liability falls if the system generates a factually incorrect measurement that passes all procedural checks. The document relies on a general deferral to the MPOA, but a specific disclaimer within this highly relevant section would strengthen the platform's position.
3.  **Clarity Impeded by Density:** The document's style, particularly in Section 1, uses extraordinarily long and complex sentences. While technically precise, this density makes the document difficult to parse, increasing the risk of misinterpretation by implementers, operators, and potentially arbitrators.

---

## Article-by-Article Review

### Section 5. Composition contract requirements

**Feedback:** The triad of "role, intent, outcome" is a strong foundation. The most powerful feature here is the set of "Fail-closed rejection semantics" in §5.9. This section provides clear, non-negotiable enforcement actions for contract failures, which is excellent from a compliance standpoint. It turns governance from a suggestion into a machine-enforceable rule.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** No changes recommended. This section is a model for how to write enforceable governance.

### Section 9.4. Professional-use draft disclosure

**Feedback:** This is a critical liability-limiting section and is very well-drafted. The mandatory disclosure text (§9.4.4) is clear and appropriately cautious. The runtime obligation in §9.4.3(5) to preserve the disclosure on export, and to block/warn if preservation is not possible, is a powerful and legally prudent control. However, the trigger for this entire section hinges on when an artifact is "classified or **reasonably intended** for... use." This is a potential weak point. Who determines what is "reasonably intended"? A user might argue they did not intend for a document to be for professional use, while the platform's classification model might disagree.

**Scores:** Legal Enforceability: 4, Conflict Freedom: 4

**Recommendation:** Add a definition or clarification for the trigger mechanism. For example:
"For the purposes of this section, an artifact's intended use SHALL be determined by a combination of its explicit classification by the user, its document subclass (e.g., `CONTRACT_SUMMARY`), and platform-level analysis of its content. In cases of ambiguity, the system SHALL default to applying the disclosure requirements."

### Section 17. Measurement contract and quantified claims

**Feedback:** This section correctly identifies that measurements are a high-risk area. The focus on process—confirming method, unit, and basis—is sound. However, it is silent on liability for errors. An AI could generate a perfectly-formatted measurement claim that is factually wrong. While the MPOA is the ultimate home for liability, the absence of any mention here feels like a gap. A user who suffers a loss from an incorrect measurement in a generated contract will point to this section, and its silence on liability could be problematic.

**Scores:** Legal Enforceability: 3, Completeness: 3

**Recommendation:** Add a new subsection to clarify the liability boundary, explicitly cross-referencing the MPOA.
**Proposed Text (for a new §17.7):**
"**17.7 Liability for accuracy**
The obligations in this Section 17 define the procedural requirements for generating quantified claims. They do not constitute a warranty or guarantee of the factual accuracy of any measurement produced by the system. Liability for damages arising from reliance on inaccurate information generated by the platform is governed exclusively by the Master Platform Operating Agreement (MPOA)."

### Section 19. Originality, source-boundary, and non-reproduction verification

**Feedback:** This section masterfully balances imposing strict operational controls while disclaiming any guarantee of a specific legal outcome. The non-waiver language in §19.2 and the disclaimer in §19.9 are crucial and well-integrated. The handoff to a separate OPS standard for the "how" (metrics, thresholds) is the correct architecture. The use of "substantial protected expression" (§19.2) is a direct import from copyright law. While contextually understandable, it's safer for a governance document to define its own operational, measurable standard and state that this standard is intended to reduce the *risk* of infringing on "substantial protected expression," rather than using the legal term of art itself as the standard. The current structure, which hands off to the numeric thresholds in AIOS-OPS-020, effectively does this, but the language could be tighter.

**Scores:** Legal Enforceability: 4, Cross-Document Consistency: 5

**Recommendation:** Consider replacing the legal term of art with an operational one.
**Proposed Text (revised §19.2, first paragraph):**
"For composed artifacts derived from knowledge-base or other source materials, the runtime SHALL apply an originality and source-boundary verification gate before publish, send, or formal export actions when policy or artifact class requires it. The system SHALL prefer transformed, purpose-built composition over source reproduction and SHALL NOT treat source retrieval as permission to reproduce source material beyond policy-defined quantitative thresholds (per §19.4 and §19.10). This gate is designed to reduce the risk of reproducing substantial protected expression."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §9.4 | The term "reasonably intended" is ambiguous and could be a point of legal contention regarding when disclosure rules apply. | Add a clarifying sentence that defines how "intended use" is determined by the platform, defaulting to applying the rules in cases of ambiguity. | High | 3 (Legal Enforceability) |
| 2 | §17 | The document is silent on liability for factually incorrect measurements, creating a potential gap if a user relies on a generated number to their detriment. | Add a new subsection explicitly disclaiming any warranty of factual accuracy and pointing directly to the MPOA as the sole arbiter of liability. | High | 3 (Legal Enforceability), 5 (Completeness) |
| 3 | §1, §16.1, etc. | Several key sections, especially the introduction, are written as single, extremely long and dense sentences, harming clarity. | Break down complex sentences into shorter, more digestible ones. For example, rewrite the single sentence of Section 1 into 3-4 separate sentences. | Medium | 8 (Style & Clarity) |
| 4 | §19.2 | Use of the legal term of art "substantial protected expression" as an operational standard can create ambiguity. | Rephrase to state that the operational gates (defined by quantitative thresholds in the OPS standard) are designed to *reduce the risk* of reproducing substantial protected expression. | Low | 3 (Legal Enforceability) |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document provides a sophisticated and legally sound framework for a very complex domain. Its strengths in fail-closed semantics and liability partitioning are exemplary. However, the ambiguities in key legal terms and the lack of clarity from stylistic density require revision before it can be considered fully ratifiable.

**Top 3 Actions Required:**
1.  **Clarify Ambiguous Triggers:** In §9.4, define how "reasonably intended" use is determined to make the professional-use disclosure rules non-ambiguous.
2.  **Add Explicit Liability Disclaimer:** In §17, add a subsection that disclaims warranty for the factual accuracy of measurements and explicitly defers liability to the MPOA.
3.  **Improve Readability:** Revise the entire document, with a focus on §1, to break down excessively long sentences to improve clarity and reduce the risk of misinterpretation.
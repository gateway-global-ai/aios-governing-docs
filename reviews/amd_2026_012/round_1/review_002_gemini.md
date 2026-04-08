---
review_id: REV-AMD-2026-012-001
document_reviewed: AMD-2026-012
document_version: 0.1.1
reviewer: Gemini
review_date: 2026-04-08
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.2
---

# Peer Review: Shell Authority and Voice-First Entry

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document expertly synthesizes and strengthens concepts from related specs without introducing contradictions. |
| 2 | Business Model Alignment | 4 | Aligns well with the intent-driven user experience but misses an opportunity to connect Shell authority to Kit discovery. |
| 3 | Legal Enforceability | 3 | While sections like the "finite family" of outcomes are strong, the use of subjective "weasel words" weakens enforceability. |
| 4 | Architectural Fidelity | 5 | Perfectly reinforces the Technical Manifesto's principles of UI sovereignty and the separation of presentation from execution. |
| 5 | Completeness | 4 | The amendment is comprehensive in defining the Shell's role but should specify how its subjective rules will be measured. |
| 6 | Conflict Freedom | 5 | No conflicts found; it serves as a clarifying capstone for the concepts of Shell, Intent, and subordinate Skills. |
| 7 | Practical Operability | 4 | Provides a clear operational model, though subjective UX requirements will require further interpretation by implementers. |
| 8 | Style & Clarity | 4 | The document is well-structured and mostly clear, with minor ambiguity introduced by the same subjective terms affecting legality. |
| 9 | Developer Synchrony | 4 | Gives developers clear boundaries about the subordinate role of their Kits, but lacks concrete metrics for UX rules. |
| 10 | Platform Economics Synchrony | 3 | The document does not address or connect to the platform's economic model, a notable omission for a core UX document. |
| 11 | Friction Factor | 5 | The proposed rules reduce end-user friction and clarify developer constraints, adding value without unnecessary bureaucracy. |
| | **Composite Score** | **4.2** | |

---

## Overall Assessment

### Strengths

This amendment provides a crucial and well-articulated definition of the AI OS Shell's authority. Its greatest strengths are:

1.  **Architectural Clarity (§4):** It unambiguously establishes the Shell as the single point of entry and session authority, preventing architectural drift towards a fragmented, dashboard-like experience. This is critical for maintaining the platform's core "voice-first" and "intent-driven" value proposition.
2.  **Enforceable Boundaries (§7, §12):** The concept of a "finite family" of governed outcomes (§7) is exemplary governance. It creates a closed, auditable set of states that is highly enforceable. Similarly, the list of "Prohibited patterns" (§12) provides clear, binary rules for compliance.
3.  **Cross-Document Cohesion:** The amendment does an excellent job of building upon `AIOS-SPEC-009` and `AMD-2026-007`, formalizing the Shell's role and its relationship to subordinate skills and integrations like the Google Workspace pack.

### Critical Gaps

The primary weakness of the document lies in its legal enforceability, stemming from the use of subjective and undefined terms.

1.  **Use of "Weasel Words" (§5, §8):** The document uses terms like "relevant," "likely," "briefly," and "concisely" without providing objective, measurable criteria. In a dispute (e.g., a Vendor Kit being rejected for a "non-concise" UI), these terms are legally weak and would be difficult to defend in arbitration. They create ambiguity where precision is required for governance.
2.  **Missing Economic Link (§10):** The document defines the core user experience but is silent on how this model connects to the platform's economics. It does not address how the "guided discovery" mode, for example, impacts Kit discovery or potential monetization within the marketplace, which is a significant strategic omission.

---

## Article-by-Article Review

### §5. User Entry Classification

**Feedback:** The distinction between "new" and "returning" users is a strong starting point. However, the requirements for a returning user's experience in §5.2 rely on subjective terms. "Restoration of **relevant** context" and "return to **likely** intent" are not defined. What makes context "relevant"? How is "likely" intent determined? This ambiguity could lead to inconsistent implementations and disputes.

**Scores:** Legal Enforceability: 2, Practical Operability: 3

**Recommendation:** Tie these subjective terms to governed, and potentially user-configurable, mechanisms.
*   **Proposed Change (to §5.2):** "For a **returning** user, the Shell **SHALL** prioritize: continuity; restoration of context as defined by the active `SessionContext` and applicable `PolicyRecord`; lowest-friction return to the most recent or pinned intent; and **less** scaffolding than for a new user."

### §7. Shell-owned governed outcomes (finite family)

**Feedback:** This section is excellent. By defining a "finite family" of outcomes, the document creates a clear, enforceable standard for system behavior. This approach is legally sound, as it provides a closed set of valid states that can be audited for compliance. It is the strongest section of the amendment.

**Scores:** Legal Enforceability: 5, Architectural Fidelity: 5

**Recommendation:** No changes. This section should be used as a model for other governance documents.

### §8. Voice-first Interaction Standard

**Feedback:** This section correctly captures the product's intended interaction model. However, like §5, it relies on unenforceable language. Terms such as "**briefly**," "**concisely**," and "**minimize** persistent explanatory text" lack objective metrics. This could lead to compliance arguments over UX design choices.

**Scores:** Legal Enforceability: 2, Style & Clarity: 3

**Recommendation:** Mandate that these qualitative terms be defined with quantitative thresholds in a subordinate, versioned policy or specification document.
*   **Proposed Addition (as a new normative statement in this section):** "The qualitative standards in this section (e.g., 'brief,' 'concise,' 'minimal') **SHALL** be given specific, measurable thresholds in a subordinate UI/UX Policy document (e.g., `POL-UX-001`). Implementations **MUST** adhere to these documented thresholds to be considered conformant."

### §13. Governance and Admin Separation

**Feedback:** This is a critical and well-defined rule. Explicitly separating the end-user Shell from admin/governance surfaces is essential for security, stability, and user experience. The rule preventing admin identities from becoming default fallbacks is a crucial safeguard.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 5

**Recommendation:** No changes needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §5.2 | Use of subjective terms "relevant" and "likely" for returning user experience. | Replace subjective terms with references to governed state objects like `SessionContext` and `PolicyRecord` to create a deterministic rule. | Critical | 3, 7, 8 |
| 2 | §8 | Use of unenforceable qualitative terms like "briefly," "concisely," and "minimize." | Add a normative statement requiring these terms to be defined by measurable thresholds in a subordinate UI/UX Policy document. | Critical | 3, 5, 7, 8 |
| 3 | General | The document is disconnected from the platform's economic model. | Add a section or subsection (e.g., under §9 or §11) clarifying the relationship between Shell-led discovery and the Kit marketplace/economics. | High | 2, 10 |
| 4 | §6 | The order of the "Shell journey model" stages is stated to be compressible. | Add a clause stating that while stages may compress, the logical dependencies (e.g., Entry before Execution) MUST be preserved. | Medium | 4, 7 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document provides an essential architectural definition for the AI OS Shell that aligns with core platform principles. However, its reliance on several subjective, legally unenforceable terms requires remediation before it can be considered a binding and robust governance standard.

**Top 3 Actions Required:**
1.  **Eliminate Subjectivity in §8:** Add a requirement for a subordinate policy document to provide measurable thresholds for all qualitative UX terms (e.g., "briefly," "concisely").
2.  **Harden §5.2:** Rephrase the requirements for the "returning user" experience to reference specific, governed state objects instead of ambiguous terms like "relevant" and "likely."
3.  **Integrate Economics:** Draft a new section or add to an existing one to clarify how this Shell-first model intersects with the platform's marketplace economics and Kit discovery mechanisms.
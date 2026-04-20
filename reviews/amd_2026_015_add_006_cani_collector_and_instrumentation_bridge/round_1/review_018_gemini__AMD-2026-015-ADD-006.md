---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.5
reviewer: Gemini
review_date: 2026-04-10
review_round: 1
review_type: legal
disposition: approved
composite_score: 4.6
---

# Peer Review: CANI Collector and Instrumentation Bridge

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document meticulously defines its subordinate relationship to parent and sibling documents, ensuring perfect consistency. |
| 2 | Completeness | 4 | The document is comprehensive within its narrow scope, though a concrete example of "bounded reviewable evidence" could add minor clarity. |
| 3 | Practical Operability | 4 | The rules are specific and the process is clearly defined, but the distinction between provisional and final statuses requires careful implementation. |
| 4 | Conflict Freedom | 5 | The document demonstrates exceptional awareness of the governance hierarchy, explicitly avoiding any conflict with parent doctrines. |
| 5 | Style & Clarity | 5 | The document is a model of clarity and precision, perfectly adhering to the style guide and leaving no room for ambiguity. |
| | **Composite Score** | **4.6** | |

---

## Overall Assessment

This document is an exceptionally well-drafted piece of governance that serves as a critical liability and authority control boundary for the CANI Experience Loop. It successfully closes the final gap in the process chain, defining how raw signals are captured and handled *before* they even enter the formal intake and validation process. Its primary focus on creating governance-preserving seams, rather than implementation authority, is its greatest strength.

### Strengths

-   **Legal Precision:** The document uses strong, enforceable language (`SHALL`, `MUST NOT`, `SHALL NOT`) throughout, leaving no doubt as to its binding nature. Sections 5 and 6, in particular, establish a legally robust, fail-closed handoff process.
-   **Clear Authority Boundaries:** Section 2's establishment of this amendment's doctrinal control over its technical support contract is a crucial legal protection against scope creep. The repeated emphasis on the non-authoritative nature of collectors, the writer lane, and the bridge itself (Section 7) is exemplary.
-   **Robust Fail-Closed Design:** The rules for handling an `unknown` surface (Section 3), the minimum requirements for pre-normalization (Section 4), and the distinction between provisional normalization statuses and authoritative validator outcomes (Section 6) create a system that defaults to safety and requires human review for ambiguity.

### Critical Gaps

There are no critical gaps in this document. The legal and compliance posture is outstanding. The recommendations below are minor clarifications to further harden an already strong document.

---

## Article-by-Article Review

### Section 0. Status & Section 1. Purpose and problem statement

**Feedback:** Excellent. The scope posture is clearly defined as a "narrow doctrine bridge." The problem statement correctly identifies the specific gap this addendum fills in the CANI family. Citing the corresponding technical support contract upfront is good practice.

**Scores:** N/A (Preamble)

**Recommendation:** No changes needed.

### Section 2. Relationship to AMD-2026-015

**Feedback:** This is a legally critical section, and it is executed perfectly. The statement "If this amendment and `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` are read in tension, this amendment controls at the doctrine layer" is an essential supremacy clause that protects the integrity of the governance framework. The explicit subordination to `ADD-004` and `ADD-005` is also correct.

**Scores:** Conflict Freedom: 5, Cross-Document Consistency: 5

**Recommendation:** No changes needed.

### Section 3. Governed capture-surface bridge rule

**Feedback:** The rule is clear and enforceable. By defining a whitelist of five allowed surface classes and explicitly making `unknown` ineligible for automatic processing, it establishes a strong control gate. This forces ambiguous signals into a manual review lane, which is appropriate for a governed system.

**Scores:** Practical Operability: 5, Legal Enforceability: 5

**Recommendation:** No changes needed.

### Section 4. Raw-capture and normalization rule

**Feedback:** This section provides a robust legal distinction between "raw capture" (mere evidence) and "normalized intake" (a governed artifact). The list of minimum pre-envelope requirements creates a clear, auditable checklist before a signal can be admitted into the system. The final paragraph, which specifies the fate of a failed signal, is a crucial control that prevents failed signals from lingering in an undefined state.

**Scores:** Completeness: 4, Practical Operability: 4

**Recommendation:** To slightly improve clarity, consider adding a single, non-normative example to the support contract (`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`) illustrating what "non-normalized repo-local reviewable evidence" might look like (e.g., a simple text file with a timestamp and a note).

### Section 5. Validator and writer handoff rule

**Feedback:** This is the document's operational core and its strongest section from a legal standpoint. It defines the "writer lane" as explicitly non-authoritative and subordinate. The sequential, four-step handoff is unambiguous. The rule that only a validator outcome of `pass` permits entry to the writer lane—and that `advisory_warning` does *not*—is a critical loophole closure that prevents ambiguous data from being persisted as if it were valid.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5

**Recommendation:** No changes needed.

### Section 6. Fail-closed outcome rule before validator handoff

**Feedback:** The creation of a separate, *provisional* set of normalization statuses is a sophisticated and necessary distinction. It allows the normalization bridge to perform its own integrity checks without co-opting the language or authority of the formal validator. This clean separation of concerns is vital for auditability and dispute resolution.

**Scores:** Architectural Fidelity: 5, Practical Operability: 4

**Recommendation:** No changes needed.

### Sections 7-10. Non-authority, Implementation, Out of scope, Summary

**Feedback:** These closing sections are clear, concise, and effectively reinforce the document's narrow, non-implementation-authorizing scope. They serve as a final, unambiguous statement of intent that would be invaluable in any legal review or arbitration.

**Scores:** Style & Clarity: 5

**Recommendation:** No changes needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 4 | Minor Clarity Gap | To aid implementers, consider adding a non-normative example of "non-normalized repo-local reviewable evidence" to the referenced support contract, `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`. | Low | 7 (Practical Operability) |

---

## Final Verdict

**Disposition:** **approved**

**Rationale:** The document is exemplary. It demonstrates a masterful understanding of governance architecture and legal hardening. It achieves its narrow purpose with precision, clarity, and a robust, fail-closed design that protects the integrity of the entire CANI framework.

**Top 3 Actions Required:**
1. No critical actions are required. The document is ready for the next stage.
2. The single, low-priority recommendation to add an example in the support contract can be addressed at the author's discretion.
3. This document should be used as a model for future "bridge" amendments that connect different stages of a governed process.
---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.1
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
| 1 | Cross-Document Consistency | 4 | The document meticulously defines its seams with other addenda, but its sheer scope creates a high cognitive load for ensuring consistency. |
| 2 | Completeness | 5 | This document is exhaustive, defining a comprehensive 12-axis control plane that appears to cover all intended aspects of composition. |
| 3 | Practical Operability | 3 | While the rules are specific, the cumulative complexity of the stacked gates (§18.11) presents a significant implementation and usability challenge. |
| 4 | Conflict Freedom | 4 | Strong effort is made to de-conflict with parent documents, particularly in §2.1, and no direct contradictions were found. |
| 5 | Style & Clarity | 3 | The document is stylistically correct but its density is extreme; merging so many complex domains into a single addendum harms overall clarity. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

This document excels in establishing robust, legally-sound controls for high-risk AI generation tasks. Its greatest strengths are the clear and enforceable liability boundaries it creates.

-   **Section 9.4 (Professional-use draft disclosure):** The mandatory disclosure text and runtime obligations for handling professional-use drafts are exceptionally well-defined. The principle of positioning the AI as a draft assistant, not a licensed professional, is legally sound and consistently enforced. The export preservation rule (§9.4.3(5)) is a critical and well-thought-out control.
-   **Section 19 (Originality, source-boundary...):** This section provides a strong, defensible risk-management framework. The legal disclaimer in §19.9, which clarifies that the feature is for risk reduction and is not a guarantee of non-infringement, is crucial and would be highly valuable in any dispute. The explicit requirement for stricter thresholds on external-facing channels (§19.4) is a key compliance control.
-   **Section 5.9 (Fail-closed rejection semantics):** The document's default posture to "fail closed" when required gates or contracts are not satisfied is a fundamental strength. It makes the system safer and more auditable by default, which is a legally conservative and appropriate stance.

### Critical Gaps

The primary weakness of the document is not a lack of rules, but its overwhelming complexity and density. This complexity creates a significant risk that the controls will be implemented incorrectly, incompletely, or in a way that is unusable, thereby negating their legal benefit.

-   **Extreme Density:** The document bundles at least five major, distinct governance domains (Language, Measurement, Knowledge Basis, Originality, Reference Guidance) into a single addendum. This makes the document difficult to review, comprehend, and, most importantly, implement with high fidelity. An implementer is likely to miss nuances when faced with such a large and interconnected set of rules.
-   **High Implementation Friction:** The prescribed sequence of gates in §18.11 (contract -> knowledge check -> discovery -> reference disposition -> creation mode -> originality check) is logically sound but operationally complex. Translating this sequence into an intuitive user experience without creating unacceptable friction will be a major challenge. If the UX is poor, users will find ways to bypass the controls, defeating their purpose.

---

## Article-by-Article Review

### Section 5: Composition contract requirements

**Feedback:** This section is well-drafted. Mandating the `role`, `intent`, and `outcome` triad is a strong way to reduce ambiguity and subsequent liability for outputs that miss the mark. The `fail-closed` semantics in §5.9 are legally robust and provide a clear, enforceable standard.
**Scores:** Practical Operability: 4, Style & Clarity: 4
**Recommendation:** No changes recommended. This section is a model of good governance design.

### Section 9.4: Professional-use draft disclosure

**Feedback:** This is the strongest section of the document from a legal and compliance perspective. It provides clear, specific, and actionable rules for a high-risk use case. The mandatory disclosure text is excellent. The distinction between the three levels of assistance (§9.4.1) is a critical liability boundary. The requirement to preserve the disclosure on export (§9.4.3(5)) is a standout feature that demonstrates mature governance thinking.
**Scores:** Completeness: 5, Practical Operability: 5
**Recommendation:** No changes recommended. This section should be considered a gold standard for other documents dealing with high-stakes generated content.

### Section 18: Knowledge basis and discovery gating

**Feedback:** The principle of "Discover before create" is sound. This section correctly identifies that generating content without a sufficient factual basis is a major risk. The state machine (`sufficient`, `partial`, `insufficient`, etc.) in §18.5 is implementable. However, the operational complexity of automatically determining the "knowledge sufficiency state" for any given request is immense and is largely hand-waved. The document mandates the "what" but provides little guidance on the "how," which could lead to inconsistent implementation.
**Scores:** Practical Operability: 3
**Recommendation:** Add an informative subsection or reference to an operations document that provides guidance or examples on how `knowledge_state` might be determined in practice. For instance, "Policy MAY define that a `RESEARCH_REPORT` requires at least two `governing_docs` sources to be considered `sufficient`." This would make the requirement less abstract.

### Section 19: Originality, source-boundary, and non-reproduction verification

**Feedback:** Legally, this section is excellent. It creates a robust internal control mechanism while masterfully disclaiming any external guarantee of non-infringement in §19.9. This manages both platform risk and user expectations. The handoff to a separate, detailed operations standard (`AIOS-OPS-020`) in §19.10 is the correct architectural choice, separating high-level doctrine from low-level implementation constants like numeric thresholds. The distinction between internal and external channel sensitivity (§19.4) is critical for practical risk management.
**Scores:** Completeness: 5, Conflict Freedom: 5
**Recommendation:** No substantive changes recommended. The structure is sound.

### Section 20: Reference-guided composition

**Feedback:** This section correctly identifies the need to govern the use of examples to guide generation, which touches upon complex IP issues like derivative works. The distinction between `Template`, `Reference`, and `Authority` (§20.3) is legally precise and useful. The explicit rule in §20.14 that maximum adherence does not bypass the §19 originality gate is the most important sentence in this section, correctly subordinating form-matching to non-reproduction.
**Scores:** Practical Operability: 3
**Recommendation:** The adherence scale (1-10) is specific, but the difference between a '6' and a '7' is highly subjective. Recommend adding a simpler 3- or 4-tier model (e.g., `Loose`, `Guided`, `Strict`) as the primary shell control, while retaining the 1-10 scale for API/policy use. This would improve usability and reduce ambiguity for end-users.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | All | Document Density & Complexity | Split the document. Promote §18 (Knowledge Basis), §19 (Originality), and §20 (Reference Guidance) into their own distinct addenda. Their complexity and importance merit standalone treatment, improving clarity and implementation focus. | High | 3, 5 |
| 2 | §18 | Abstract Requirement | Add an informative subsection with concrete examples of policy rules for determining `knowledge_state` to make the concept more tangible for implementers. | Medium | 3 |
| 3 | §20.13 | User Interface Ambiguity | Recommend the user-facing shell control for `reference_adherence` be a simpler, labeled preset (e.g., Loose/Guided/Strict) that maps to the underlying 1-10 scale, rather than exposing a raw numeric slider. | Low | 3 |

---

## Final Verdict

**Disposition:** **Approved with Changes**

**Rationale:** The document establishes an exceptionally strong and well-considered legal and compliance framework, particularly around professional-use drafts and originality verification. However, its extreme density and the resulting implementation complexity present a material risk to its own objectives. The proposed changes focus on modularizing the document to improve clarity and ensure its robust controls can be implemented correctly and effectively.

**Top 3 Actions Required:**
1.  Develop a plan to split this monolithic addendum into several more focused documents (Recommendation #1). The current scope is too large for a single review-and-implement cycle.
2.  While the document split is being planned, create an implementation guide for developers that translates the complex gate sequencing in §18.11 into a clear, step-by-step process with concrete examples.
3.  Ensure the `ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD` (AIOS-OPS-020) is ratified alongside or immediately after this addendum, as this document is critically dependent on it for operability.
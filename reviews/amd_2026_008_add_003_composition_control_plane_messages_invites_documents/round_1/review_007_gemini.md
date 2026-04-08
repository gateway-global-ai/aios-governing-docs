review_id: REV-AMD-2026-008-ADD-003-002
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.12.0
reviewer: Gemini
review_date: 2026-04-11
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 4.0
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | The document meticulously defines its seams with other addenda (§2.1, §16.7) and consistently cross-references them, avoiding redefinition of terms. |
| 2 | Completeness | 4 | The document is exceptionally comprehensive in its defined scope, but the sheer number of new, complex governance domains (§16-§20) introduced in one addendum is a potential structural issue. |
| 3 | Practical Operability | 3 | While concepts are broken down into implementable states and scales, the combined complexity of seven distinct, high-stakes control planes (§5, §9.4, §16-§20) creates a significant implementation and audit burden. |
| 4 | Conflict Freedom | 5 | The document shows excellent discipline in respecting the boundaries of other documents, explicitly stating what it does and does not own, which prevents internal contradictions. |
| 5 | Style & Clarity | 3 | The document adheres to the formal style guide's rules, but its extreme density and length, covering seven major concepts, make it difficult to parse and review, impairing overall clarity. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

- **Liability-Aware Disclaimers:** The document contains several well-drafted sections designed to manage legal risk. Section 9.4 (Professional-use draft disclosure), Section 19 (Originality/Non-reproduction), and Section 20 (Reference-guided composition) all include precise language and disclaimers that clarify the system's role as a tool, not a licensed professional or a guarantor of copyright compliance. The distinction in §20.3 between "Template," "Reference," and "Authority" is particularly strong from a risk management perspective.
- **Clear Separation of Concerns:** The document excels at defining its own boundaries. Section 2.1 explicitly states which concepts are owned by ADD-001 and ADD-002 and normatively binds this document to respect those seams. This discipline prevents contradictions and creates a coherent, albeit complex, governance framework.
- **Operational Precision:** The principles are translated into potentially enforceable rules. The definition of the "Composition Contract" (§5), the "Knowledge Sufficiency States" (§18.5), and the "Reference Adherence Scale" (§20.13) provide a basis for implementation and audit, moving beyond abstract principles to governable states.

### Critical Gaps

- **Overwhelming Complexity and Density:** The single most significant issue is the document's scope. It attempts to define and govern at least seven major, distinct control planes (Composition Contracts, Professional Disclosures, Language, Measurement, Knowledge Basis, Originality, and Reference Guidance) in a single addendum. This density makes the document incredibly difficult to review, implement, and audit, which in itself is a compliance risk. A failure to correctly implement any one of the dozens of `SHALL` clauses constitutes a governance breach.
- **Weak Enforceability on Exported Disclosures:** Section 9.4.3(5) mandates that the professional-use disclosure be preserved in exported versions "where feasible." The phrase "where feasible" is a weasel word that significantly weakens the obligation. For a critical disclosure intended to shield the platform from liability, this should be a much stronger mandate.
- **Potential for Ambiguous Policy Thresholds:** Sections like §19.4 state that policy "SHALL support" different thresholds for internal vs. external use. While good, the document doesn't mandate that such distinct thresholds *must exist*, creating a potential gap where a weak policy could apply internal-use standards to external publishing, defeating the purpose of the control.

---

## Article-by-Article Review

### Section 5. Composition contract requirements

**Feedback:** This section provides a solid foundation for the entire document, correctly identifying that composed artifacts require a different governance posture than simple responses. The "triad" of Role, Intent, and Outcome is clear and legally sound, as it forces a record of purpose that can be audited.
**Scores:** Practical Operability: 4, Legal Enforceability: 5
**Recommendation:** No changes recommended. This section is strong.

### Section 9.4 Professional-use draft disclosure

**Feedback:** This is the most critical section from a legal and liability standpoint. The doctrine, principles, and disclosure text are generally well-drafted and correctly position the AI OS as a drafting tool, not a source of professional advice. However, the obligation to preserve the disclosure on export is weak.
**Scores:** Legal Enforceability: 3, Practical Operability: 4
**Recommendation:** Strengthen the language in §9.4.3(5).

**Old Text:**
> 5. **preserve** that disclosure in **exported** versions **where feasible** (**MD**, **PDF**, **DOCX**, **HTML**, etc.).

**New Text:**
> 5. **preserve** that disclosure in **exported** versions. For formats where embedding is technically impossible, the export workflow **SHALL** present a blocking warning to the user stating that the disclosure could not be included and that the user assumes responsibility for adding it.

### Section 16. Language, localization, and authoritative version control

**Feedback:** This section correctly identifies that language is not merely a cosmetic feature, especially in legal or professional contexts. The requirement in §16.5 to identify an "authoritative_language" is a crucial risk control for multilingual documents that could have binding force. This is a mature and well-considered control.
**Scores:** Legal Enforceability: 5
**Recommendation:** No changes recommended.

### Section 17. Measurement contract and quantified claims

**Feedback:** This is an excellent and often-overlooked area of risk. Forcing confirmation of measurement method, unit, and basis (§17.2) before asserting a quantity as fact is a powerful control against misrepresentation. It turns an implicit assumption into an explicit, auditable contract.
**Scores:** Legal Enforceability: 5, Practical Operability: 4
**Recommendation:** No changes recommended.

### Section 18. Knowledge basis and discovery gating

**Feedback:** The principle of "Discover before create" is sound. This section provides a strong operational framework for preventing the system from "hallucinating" a polished artifact based on incomplete information. The sufficiency states in §18.5 are logical and provide clear gates for the runtime to enforce.
**Scores:** Practical Operability: 4
**Recommendation:** No changes recommended.

### Section 19. Originality, source-boundary, and non-reproduction verification

**Feedback:** This section correctly frames its purpose as risk reduction, not a legal guarantee of non-infringement (§19.9). This is a critical liability boundary. The distinction between internal and external thresholds is also key. However, the link between the control and the policy layer could be stronger.
**Scores:** Legal Enforceability: 4
**Recommendation:** Add a clarifying sentence to §19.4 to ensure policies *must* differentiate thresholds where appropriate.

**Proposed addition to §19.4:**
> **Policy** **SHALL** support **different** **thresholds** by **channel**. For any artifact class that can be distributed externally, policy **SHALL** define a stricter originality and source-boundary gate than for artifacts intended solely for internal review.

### Section 20. Reference-guided composition

**Feedback:** This is a sophisticated and well-designed control. The distinction between guidance and copying (§20.1) and the taxonomy of Template/Reference/Authority (§20.3) provide a robust framework for managing the risk of using external materials. The explicit disavowal of "temperature" as a label (§20.11) is also a mark of precision. The rule in §20.14, which subjects even maximum-adherence outputs to the §19 originality gate, is a critical and correctly-placed backstop.
**Scores:** Legal Enforceability: 5
**Recommendation:** No changes recommended.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Overall | Document is overly dense, combining ~7 major governance planes. This complexity increases implementation and audit risk. | Consider splitting §§16-20 into a separate addendum (e.g., ADD-004 "Advanced Composition Controls") to improve readability and modularity. | Medium | 3, 5 |
| 2 | §9.4.3(5) | The phrase "where feasible" weakens the mandatory disclosure requirement for professional-use documents on export. | Replace "where feasible" with a stronger `SHALL` clause that requires preservation, or a blocking warning if preservation is technically impossible. | High | 3 |
| 3 | §19.4 | The document allows policy to support different originality thresholds but doesn't mandate their use for external-facing documents. | Add a sentence requiring policy to define stricter originality gates for any artifact class that can be distributed externally. | High | 3 |

---

## Final Verdict

**Disposition:** Approved with Changes

**Rationale:** The document is substantively excellent, demonstrating deep thought on managing the complex risks of AI-driven composition. However, its extreme density impairs clarity and increases operational risk, and two critical `SHALL` clauses related to liability and IP risk are weakened by imprecise language. The recommended changes are necessary to ensure the document is as enforceable and protective as it intends to be.

**Top 3 Actions Required:**
1. Strengthen the professional-use disclosure export requirement in §9.4.3(5) to remove the "where feasible" loophole.
2. Mandate in §19.4 that policies *must* define stricter originality thresholds for external-facing documents.
3. Consider a strategic split of the document to reduce its complexity, which is a latent risk to both implementation and compliance.
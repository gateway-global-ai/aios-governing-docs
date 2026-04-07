---
review_id: REV-AIOS-SPEC-009-002
document_reviewed: AIOS-SPEC-009
document_version: 0.5.2
reviewer: Gemini
review_date: 2026-04-08
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 2.9
---

# Peer Review: Intent Primitive and Execution Model

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The front matter's cross-references are improperly formatted and inconsistent with the binding Style Guide. |
| 2 | Business Model Alignment | 4 | The concept of promoting verified playbooks strongly supports the ecosystem model by creating reusable, low-friction value. |
| 3 | Legal Enforceability | 2 | Critical terms like "materially broad" are undefined, creating legal ambiguity, and liability for user-approved plans is not explicitly assigned. |
| 4 | Architectural Fidelity | 4 | The specification correctly models the intent lifecycle and separation of concerns (e.g., local interpretation) outlined in the Manifesto. |
| 5 | Completeness | 4 | The document is comprehensive, covering lifecycle, state, UI, compilation, and sovereign runtimes, including forward-looking conformance tests. |
| 6 | Conflict Freedom | 3 | The term "verified playbook" creates potential tension with the MPOA's liability caps by implying a Platform warranty that may not exist. |
| 7 | Practical Operability | 3 | The core model is operable, but the lack of defined thresholds for vague terms like "large result set" will lead to implementation ambiguity. |
| 8 | Style & Clarity | 2 | While the body is mostly clear, the document violates the Style Guide on cross-referencing and section notation, undermining its formality. |
| 9 | Developer Synchrony | 4 | The inclusion of TypeScript interfaces, policy references, and an implementation alignment section provides clear guidance for developers. |
| 10 | Platform Economics Synchrony | 1 | The "Proposal Requirement" in §15.4 critically fails to mandate cost disclosure for actions that debit the Funded Data Account. |
| 11 | Friction Factor | 3 | The balance between proposal requirements for new plans and auto-approval for verified ones is sound, though fallback proposals could be noisy. |
| | **Composite Score** | **2.9** | |

**Reviewer Note:** The disposition is `major_revision_required` due to a dimension score of 1 (Platform Economics Synchrony) and multiple scores of 2, per the Disposition Rules. The composite score does not override this.

---

## Overall Assessment

### Strengths

-   **Architectural Soundness:** The document provides a robust, comprehensive definition of the core `Intent` primitive. The lifecycle (§6), compilation model (§15), and separation of concerns for local runtimes (§16, §17) are well-defined and align perfectly with the architectural principles of the Technical Manifesto.
-   **Developer Clarity:** The inclusion of TypeScript schemas (§5, §15.3) and an implementation alignment guide (§19) makes the specification highly actionable for engineering teams.
-   **Governance Integration:** The model correctly subordinates execution to policy at every stage, explicitly referencing policy numbers and establishing a clear governance chain from intent to outcome (§9, §14).

### Critical Gaps

-   **Economic Transparency Failure:** Section 15.4 mandates a user proposal for new execution plans but critically omits the requirement to disclose potential costs. Any plan that utilizes external intelligence *must* inform the user that it will debit their Funded Data Account, per the MPOA. This is a fatal flaw that undermines the platform's billing transparency promise.
-   **Legal Ambiguity and Weasel Words:** The specification relies on legally unenforceable terms like "materially broad" (§6.3.2), "large," and "operationally non-actionable" (§6.3.1) without defining them. In arbitration, these terms are subjective and create risk. They must be replaced with specific, policy-driven thresholds.
-   **Implied Liability and Warranty:** The use of "verified playbook" (§15.6, §15.7) implies a level of warranty from the Platform that may conflict with the liability caps in the MPOA. If a "verified" plan fails, it creates a direct line of argument against the Platform. This language must be softened.
-   **Gross Style Guide Violations:** The front matter completely disregards the Style Guide's rules for cross-referencing, using internal identifiers instead of full document titles and article citations. This is unacceptable for a ratified governance document.

---

## Article-by-Article Review

### Section 0: Status and ratification & Front Matter

**Feedback:** The cross-references section is non-compliant with the AIOS Style Guide. The guide mandates citing by "full document title and specific Article/Section," but this document uses a list of internal document IDs and external standards without context. This sloppiness undermines the document's authority and creates ambiguity.

**Scores:** Cross-Document Consistency: 2, Style & Clarity: 2

**Recommendation:** Rewrite the `cross_references` front matter to be fully compliant. For example:
`cross_references:`
`- { doc_id: "AIOS-SPEC-006", relationship: "references", citation: "UI Component Specification" }`
`- { doc_id: "AIOS-CORE-003", relationship: "constrained_by", citation: "Master Platform Operating Agreement (Article II)" }`

### Section 6: Intent lifecycle (normative)

**Feedback:** The lifecycle is well-defined, but subsections 6.3.1 and 6.3.2 introduce legally ambiguous "weasel words." Terms like "materially over-broad," "large," and "materially broad result set" are not defined. What constitutes "materially broad"? 100 results? 1000? This must be defined in policy, not left to interpretation, to be enforceable and to protect the Platform from claims of failing to disclose properly.

**Scores:** Legal Enforceability: 2, Practical Operability: 3

**Recommendation:** Add a requirement that these thresholds are defined in a `PolicyRecord` and are configurable by the Tenant or Platform.
**Proposed Text Change (for §6.3.1):** "…a materially over-broad time range, **as defined by thresholds in the active Tenant Policy,** would return a large or operationally non-actionable result set…"

### Section 15: Intent compilation and approval model (REQUIRED)

**Feedback:** This is the most critical section and contains the most severe gaps.

1.  **Economic Disconnect (§15.4):** The `Proposal requirement` list is missing the single most important element for the business model: cost. Failure to disclose that an action will draw from the Funded Data Account is a breach of the MPOA's transparency principle (Article V) and a major legal risk.
2.  **Liability Gap (§15.5):** The document does not explicitly state that user approval of a proposed plan transfers liability for the business outcome to the Tenant. This should be explicitly linked to the "Tenant Configuration Liability" clause in the MPOA (Article III).
3.  **Implied Warranty (§15.6, §15.7):** The term "verified playbook" is problematic. "Verified" implies it is guaranteed to work by the Platform. A better term would be "Promoted Playbook" or "Established Playbook" to indicate it has worked successfully before without implying a forward-looking warranty. This reduces the risk of legal claims that would try to pierce the MPOA's liability cap.

**Scores:** Platform Economics Synchrony: 1, Legal Enforceability: 2, Conflict Freedom: 3

**Recommendation:**
1.  **(Critical)** Add cost disclosure to the proposal requirements in §15.4.
    **Proposed Text Change:** "The proposal MUST include: ... **A clear statement if any step will debit the Tenant's Funded Data Account, including an estimate of the cost where feasible.**"
2.  Add a subsection clarifying liability for approved plans.
    **Proposed Text:** "§15.5.1 Liability for Approved Plans: Consistent with the Master Platform Operating Agreement (Article III), the Tenant's explicit approval of a proposed execution plan renders the Tenant liable for the business outcomes resulting from that execution."
3.  Replace all instances of "verified playbook" with "promoted playbook."

### Sections 16 & 17: Local Interpretation and Sovereign Voice

**Feedback:** These sections are well-drafted from a legal and compliance perspective. They make strong, specific promises about data sovereignty ("sovereign voice") and correctly link them to auditable controls. The requirement for explicit policy and disclosure before falling back to a remote model (§16.1, §17.1) is exactly what is needed to make these promises legally defensible. This is a strength of the document.

**Scores:** Legal Enforceability: 5, Architectural Fidelity: 5

**Recommendation:** No changes required. These sections should be used as a model for how to write legally defensible specifications.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §15.4 | The proposal model critically fails to require disclosure of costs that debit the Funded Data Account. | Add a mandatory requirement to the proposal flow to disclose any potential costs to the Tenant before execution. | Critical | 10, 3, 2 |
| 2 | §6.3.1, §6.3.2 | Vague, unenforceable terms like "materially broad" and "large" create legal risk and implementation ambiguity. | Replace vague quantifiers with language requiring these thresholds to be defined in a `PolicyRecord` or system constant. | High | 3, 7 |
| 3 | §15.6, §15.7 | The term "verified playbook" implies a Platform warranty that conflicts with the MPOA's liability limitations. | Replace all instances of "verified playbook" with "promoted playbook" or "established playbook" to reduce implied liability. | High | 6, 3 |
| 4 | §15.5 | Liability for user-approved, system-proposed plans is not explicitly assigned to the Tenant. | Add a clause explicitly stating that user approval of a plan assigns liability for the business outcome to the Tenant, citing the MPOA. | High | 3 |
| 5 | Front Matter | The `cross_references` section is non-compliant with the mandatory Style Guide. | Rewrite the entire `cross_references` block to use full document titles and citations as required by the Style Guide. | Medium | 1, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The disposition is driven by the critical failure in Platform Economics Synchrony (Score: 1) and major issues in Legal Enforceability and Style & Clarity (Score: 2). The lack of cost disclosure in the core execution proposal flow is a fundamental violation of the platform's economic model and creates unacceptable legal risk.

**Top 3 Actions Required:**
1.  **Integrate Economics into Proposals:** Amend §15.4 to make disclosure of potential costs from the Funded Data Account a mandatory part of any execution plan proposal.
2.  **Eliminate Legal Ambiguity:** Replace all "weasel words" (§6) with references to policy-defined thresholds and explicitly assign liability for user-approved plans (§15), citing the MPOA.
3.  **Soften Warranty Language:** Change "verified playbook" to "promoted playbook" throughout §15 to avoid creating an implied warranty that conflicts with the MPOA.
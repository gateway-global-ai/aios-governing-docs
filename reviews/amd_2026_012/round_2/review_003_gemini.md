---
review_id: REV-AMD-2026-012-008
document_reviewed: AMD-2026-012
document_version: 0.1.2
reviewer: Gemini
review_date: 2026-04-10
review_round: 2
review_type: legal
disposition: major_revision_required
composite_score: 3.5
---

# Peer Review: Shell Authority and Voice-First Entry

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The revision successfully ties "governed session state" in §5.2 to ratified documents like AIOS-SPEC-009, improving consistency. |
| 2 | Business Model Alignment | 4 | The new informative note in §9.4 correctly delineates this amendment's authority from commercial marketplace terms, strengthening alignment. |
| 3 | Legal Enforceability | 2 | The critical enforceability gap in §8.4, identified in Round 1, remains unaddressed; the section is still a legally weak "promise to agree." |
| 4 | Architectural Fidelity | 4 | The document strongly defines the Shell's authority and its subordinate relationship to skills, aligning well with the Technical Manifesto. |
| 5 | Completeness | 3 | The Shell's mandate as "session authority" in §4.2 remains incomplete, as it omits governance over audit trail initiation and economic disclosure. |
| 6 | Conflict Freedom | 4 | The strict hierarchy established in §9 successfully prevents conflict with integration specifications like AIOS-SPEC-007. |
| 7 | Practical Operability | 3 | The continued reliance on undefined qualitative terms in §8 (e.g., "brief," "concise") makes day-one implementation a matter of subjective interpretation. |
| 8 | Style & Clarity | 4 | The document is well-written and structured, but the legal ambiguity in §8 creates a lack of clarity in a core section. |
| 9 | Developer Synchrony | 3 | While the subordination rules are clear, the lack of measurable thresholds in §8 means developers cannot know if their UX implementation is compliant. |
| 10 | Platform Economics Synchrony | 3 | The document fails to grant the Shell authority over the *presentation* of economic information (§4.2), a key aspect of the user session. |
| 11 | Friction Factor | 4 | The rules are intentionally strict to enforce the product vision and do not introduce unnecessary procedural friction. |
| | **Composite Score** | **3.5** | |

---

## Overall Assessment

This is a Round 2 review of a revised document. While the author successfully incorporated several key recommendations from Round 1, two critical gaps related to legal enforceability and completeness were not addressed, preventing this document from being ready for ratification.

### Strengths

The revisions have strengthened the document in several areas. The explicit linking of "governed session state" to `AIOS-SPEC-009` and `PolicyRecord` in §5.2 is a significant improvement in legal precision. Likewise, the new informative note in §9.4 clarifying the boundary with commercial marketplace documents successfully resolves an ambiguity identified in Round 1. The document's core strengths remain its clear establishment of the Shell/tool hierarchy (§9) and the legally robust "finite family" of outcomes (§7).

### Critical Gaps

Despite the improvements, the document fails on two key points raised in the previous review round:

1.  **Unenforceable Qualitative Standards (§8.4):** The most critical flaw from Round 1 remains. The document mandates a "voice-first" interaction standard using subjective terms like "brief" and "concise." The revision in §8.4 continues to defer the definition of these terms to a future document. This is a "promise to agree" and is legally unenforceable. The Round 1 recommendation to include binding, *interim* numerical thresholds was not adopted, leaving this core section without a defensible standard.
2.  **Incomplete Session Authority (§4.2):** The Round 1 review noted that a true "session authority" must govern all key aspects of the session. The list of Shell authorities in §4.2 still omits the power to govern `Audit trail initiation` and `Economic disclosure` presentation. This is a major completeness gap that undermines the Shell's stated role.

The failure to address these fundamental issues, particularly the direct feedback on legal enforceability, means the document cannot be approved.

---

## Article-by-Article Review

### §4. Normative shell authority

**Feedback:** The revision to §4.4, which ties fallback behavior directly to the finite outcome family in §7, is a significant improvement in enforceability. However, the table in §4.2 remains unchanged from Round 1 and is critically incomplete. As the "session authority," the Shell must have governance over the presentation of all key session events, including the initiation of an audit trail and the disclosure of potential costs to the user (per `AIOS-SPEC-009 §15.4`).

**Scores:** Legal Enforceability: 3, Completeness: 3

**Recommendation:** The recommendation from Round 1 is restated: Add `Audit trail initiation` and `Economic disclosure` to the table in §4.2, granting the Shell authority over their presentation and timing. This is essential for the claim of "session authority" to be credible and complete.

### §8. Voice-first interaction standard

**Feedback:** This section remains the document's greatest weakness. The revision to §8.4 acknowledges the problem of subjective terms but its solution—punting the definitions to a future, unratified document—is the same flawed approach from the previous version. It fails to create a binding, enforceable standard for day-one operations. The critical Round 1 recommendation to add interim, numerical defaults was ignored.

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** The recommendation from Round 1 is restated with emphasis: Amend §8.4 to include binding, conservative defaults that apply *until* the subordinate policy is ratified. For example:
"Until such a subordinate document is ratified, implementations claiming conformance **SHALL** operate under the following interim thresholds: 'brief' and 'concise' acknowledgments **SHALL NOT** exceed 15 words or 5 seconds of generated speech; 'minimal' clarification **SHALL NOT** present more than two distinct choices."

### §9. Skills and tools are subordinate

**Feedback:** The addition of the informative note in §9.4 is an excellent revision that directly addresses Round 1 feedback. It successfully clarifies that while the Shell is a discovery gatekeeper, the economic rules for that marketplace function are governed by separate commercial documents. This cleanly separates architectural governance from commercial policy.

**Scores:** Business Model Alignment: 4, Cross-Document Consistency: 4

**Recommendation:** No further changes required for this section. The revision is successful.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §8.4 | Qualitative UX terms ("brief", "minimal") remain legally unenforceable as they are defined by a future document. | **Restated from R1:** Add a clause that defines conservative, numeric, interim thresholds for these terms, which remain binding until a formal subordinate policy is ratified. | Critical | 3, 7, 9 |
| 2 | §4.2 | The list of Shell authorities is incomplete, omitting its role in presenting audit and economic disclosures. | **Restated from R1:** Add `Audit trail initiation` and `Economic disclosure` to the table of Shell authorities to make its session-governing role complete. | High | 5, 10 |
| 3 | General | The disposition rules in the rubric template have a logical gap for a document with a single score of 2. | Advise the governance coordinator to review the disposition rules. This is non-binding on the document itself but is a process-level finding. | Low | N/A |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document fails to incorporate critical Round 1 feedback regarding legal enforceability in §8. A core standard based on subjective terms defined in a non-existent future document is legally untenable. This, combined with the incomplete definition of the Shell's authority in §4, requires a major revision before this amendment can proceed. The disposition is driven by the low score in the primary review dimension (Legal Enforceability) and the failure to remediate a known critical issue from a prior review round.

**Top 3 Actions Required:**
1.  Implement the recommendation for §8.4 to add binding, interim numerical thresholds for all qualitative UX terms. This is non-negotiable for legal enforceability.
2.  Amend the table in §4.2 to expand the definition of Shell authority to include its role in presenting audit and economic information.
3.  Conduct a thorough review to ensure all critical feedback from Round 1 has now been fully incorporated.
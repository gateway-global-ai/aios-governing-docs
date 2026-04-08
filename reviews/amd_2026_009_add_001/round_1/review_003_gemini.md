---
review_id: REV-AMD-2026-009-ADD-001-001
document_reviewed: amendments/AMD-2026-009-ADD-001
document_version: 1.0.1
reviewer: Gemini 2.5 Pro
review_date: 2026-04-08
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 3.6
---

# Peer Review: Retrieval backend neutrality (beyond Google PSE / Custom Search)

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The addendum aligns well with its parent and sibling documents, correctly identifying necessary deltas. |
| 2 | Completeness | 3 | The document is conceptually complete but lacks specificity on the legal and compliance verification process for new backends. |
| 3 | Practical Operability | 3 | While it enables flexibility, the criteria for backend approval are too subjective, risking inconsistent application or legal exposure. |
| 4 | Conflict Freedom | 4 | No direct conflicts are created, as it correctly frames the change as an extension rather than a replacement of core principles. |
| 5 | Style & Clarity | 4 | The document is well-written and follows the style guide, clearly stating its purpose and non-goals. |
| | **Composite Score** | **3.6** | |

---

## Overall Assessment

### Strengths

- **Clear Problem Statement (§1):** The document effectively articulates the operational need for backend neutrality, moving beyond a mandatory PSE implementation. This addresses a valid real-world constraint.
- **Preservation of Core Governance (§0, §1):** It correctly emphasizes that all parent governance from AMD-2026-009 (scope classes, SPEC-010 binding, audit) remains in force. This is critical for preventing the dilution of standards.
- **Explicit Non-Goals (§5):** The non-goals section is crucial and well-defined, explicitly prohibiting unbounded browsing or prompt-only web access, which prevents misinterpretation of the addendum's intent.

### Critical Gaps

- **Undefined Liability and Diligence Process (§2):** The document introduces the possibility of using various third-party APIs but fails to define who is responsible for conducting the legal and commercial due diligence (e.g., ToS review, data privacy compliance). Phrases like "where product and vendor terms allow" are legally insufficient as they do not assign the duty of verification.
- **Ambiguous Backend Approval Criteria (§2):** The criteria for an acceptable alternative backend—such as requiring a "documented API" that returns "citable result lists"—are too vague. This could lead to operators approving risky backends (e.g., based on unofficial, reverse-engineered APIs) under a loose interpretation of "documented."
- **Insufficient Guardrails on High-Risk Integrations (§2.1):** The document correctly identifies "HTML scraping" as a high-risk activity but frames its prohibition too weakly. Stating it "MUST NOT" be treated as governed "without legal review and explicit risk acceptance" leaves a dangerous door open. For a governing document, such practices should be explicitly forbidden by default, requiring a formal, high-bar exemption process akin to a constitutional override.

---

## Article-by-Article Review

### Section 2: Normative effect

**Feedback:** This section is the legal and functional core of the addendum. While its intent is sound, its language introduces significant legal ambiguity. Item 3's list of providers is correctly marked as informative, but the criteria for *any* provider are too loose. The phrase "where product and vendor terms allow" is a "weasel word" that offloads compliance responsibility without specifying to whom. Furthermore, the criteria for what constitutes a "documented API" and "citable result lists" are not precise enough to be uniformly enforced.

Section 2.1 is particularly concerning from a legal perspective. It correctly identifies the risk of scraping but provides a weak, conditional prohibition. In any legal dispute, this conditional language could be interpreted as tacit approval as long as some form of "review" was performed, regardless of its quality. This creates an unacceptable liability risk for the platform.

**Scores:** Practical Operability: 2, Completeness: 3

**Recommendation:**
1.  Replace the phrase in §2 item 3, "...where product and vendor terms allow..." with:
    > "...provided that the proposed backend has undergone a formal compliance review, approved by the Governance Council or its delegate, which confirms its alignment with the platform's data privacy, security, and commercial terms. The responsibility for initiating and presenting this review rests with the Operator proposing the new backend."
2.  Strengthen the definition of an acceptable API in §2 item 3 from "documented API" to:
    > "...provider's officially published and commercially supported API..."
3.  Strengthen the prohibition in §2.1. The final sentence should be replaced with:
    > "**MUST NOT** treat **HTML scraping** or **unofficial** reverse-engineered endpoints as governed retrieval backends. Use of such methods is a direct violation of this policy. A formal exemption may only be sought through the emergency override process defined in Governance Constitution Article IV."

### Section 4: Deltas to sibling artifacts

**Feedback:** This section provides a clear and useful checklist for ensuring the changes proposed in the addendum are propagated correctly across the governance framework. It demonstrates good cross-document awareness. No issues.

**Scores:** Cross-Document Consistency: 5

**Recommendation:** No change required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §2.1 | The prohibition on web scraping and unofficial APIs is too weak and conditional, creating a significant legal and compliance risk. | Replace the conditional prohibition with an explicit, default-deny rule that requires a high-bar constitutional exemption process for any consideration of such methods. | Critical | 3, 7 |
| 2 | §2 | The document fails to assign the specific responsibility for conducting legal and commercial due diligence (e.g., ToS review) on new backends. | Explicitly assign the duty of initiating and presenting a formal compliance review to the Operator, with final approval required from the Governance Council. | High | 2, 7 |
| 3 | §2 | The term "documented API" is ambiguous and could be misinterpreted to include unofficial or unstable endpoints. | Refine the requirement to specify "a provider's officially published and commercially supported API" to ensure stability and legal clarity. | Medium | 7 |

---

## Final Verdict

**Disposition:** **approved_with_changes**

**Rationale:** The document addresses a valid operational need for flexibility in retrieval backends and correctly maintains the supremacy of the parent amendment's governance principles. However, it introduces significant legal and operational risk by failing to establish a sufficiently rigorous and enforceable process for approving and managing these backends. The recommended changes are required to close these compliance gaps before ratification.

**Top 3 Actions Required:**
1.  Strengthen §2.1 to explicitly prohibit scraping and use of unofficial APIs by default.
2.  Amend §2 to define a clear due diligence process and assign responsibility for the legal/commercial review of new backends to the Operator, with Council approval.
3.  Refine the definition of an acceptable API in §2 to require official, commercially supported endpoints.

---
review_id: REV-shell-authority-surfaces-001
document_reviewed: reviews/aios_shell_governing_document_and_artifact_plan_001/phase_packets_2026-04-10/PHASE_1_SHELL_AUTHORITY_SURFACES.md
document_version: 1
reviewer: Gemini
review_date: 2026-04-10
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 3.2
---

# Peer Review: Phase 1 shell authority surfaces

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The document aligns well with the shell/workspace separation in other specs but lacks formal structure. |
| 2 | Business Model Alignment | 4 | Differentiating user/dev/operator roles supports the ecosystem model by enabling trusted development. |
| 3 | Legal Enforceability | 2 | The document correctly identifies a critical liability (interim authority) but proposes a plan rather than enacting enforceable rules. |
| 4 | Architectural Fidelity | 5 | The separation of shell-state control (`app.shell.*`) from domain execution (`workspace.*`) perfectly reflects the Manifesto's architecture. |
| 5 | Completeness | 4 | As a planning document, it is comprehensive in defining the problem, scope, and required outputs for the next phase. |
| 6 | Conflict Freedom | 4 | No conflicts are introduced; it reinforces the principle of a supreme shell governing subordinate integrations. |
| 7 | Practical Operability | 3 | The *described interim system* is operable but dangerously insecure; the document is a good operational plan but lacks specific rules. |
| 8 | Style & Clarity | 2 | The document uses an informal, free-form structure that violates the Style Guide's rules for governing documents. |
| 9 | Developer Synchrony | 4 | It provides excellent clarity for developers by directly referencing implementation files and architectural boundaries. |
| 10 | Platform Economics Synchrony | 3 | The document is neutral on economics, which is acceptable but misses an opportunity to link operator-mode access to a commercial tier. |
| 11 | Friction Factor | 4 | The proposed review gates and transition to identity-bound access create necessary friction that is proportional to the security risk. |
| | **Composite Score** | **3.5** | |

---

## Overall Assessment

### Strengths

-   **Architectural Clarity:** The document does an exemplary job of defining and defending the architectural boundary between the sovereign shell and subordinate "Workspace" integrations. The distinction between `app.shell.*` intents for shell state and `workspace.*` intents for domain execution is perfectly aligned with the *Technical Manifesto*.
-   **Problem Identification:** It correctly identifies the current "interim device-local authority" mechanism (URL parameters, local storage) as a critical security and legal liability. Its focus on creating a clear remediation path is a significant strength.
-   **Scope Definition:** The document is very clear about what it is and is not. The "Required phase outputs" and "Acceptance criteria" sections provide a complete and actionable plan for creating a formal, governable specification.

### Critical Gaps

-   **Lack of Enforceable Rules:** The primary gap is that this document is a plan *about* governance, not a governance document itself. It describes a system that relies on insecure mechanisms like URL flags (`?aios_operator=1`), which are legally indefensible for controlling access to privileged functions. While it correctly flags this for remediation, the document contains no binding, legally enforceable rules to replace it.
-   **Style Guide Non-compliance:** The document is written as an internal memo or design document, not a piece of formal AIOS governance. It uses an informal heading structure, lacks Article/Section divisions, and does not adhere to the voice, tone, and formatting conventions required by the *AIOS Governing Documents: Writing Style Guide*. This makes it ambiguous whether its statements are findings, proposals, or binding rules.
-   **Undefined Liability:** By discussing `operator` and `developer` surfaces without defining the liability associated with actions taken in those modes, the document leaves a major legal question unanswered. If an operator's action causes a data breach, is the liability cap in the MPOA still applicable, or does a higher standard of care apply? This must be clarified.

---

## Article-by-Article Review

The document is not structured with formal Articles. The review will follow its main H2 sections.

### Current baseline / Runtime evidence snapshot

**Feedback:** This section is effective at grounding the discussion in the current implementation. However, by confirming that the platform currently uses "interim device-local authority," it documents a major compliance and security failure. From a legal perspective, admitting that privileged access is controlled by a URL flag is a significant finding that increases the urgency of remediation.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 1

**Recommendation:** Frame the "Current baseline" as a "Statement of Deficiency." This reframes the section from a neutral description to a formal acknowledgement of a gap that must be closed, strengthening the mandate for the "Immediate remediation direction."

### Authority matrix / Transition and denial rules

**Feedback:** These tables are clear and provide a good foundation for a formal policy. However, the term "interim eligibility" is a weasel word. It has no legal meaning. For a rule to be enforceable, the condition for eligibility must be specific (e.g., "session is authenticated as a user assigned the 'Operator' role in the Tenant's identity provider").

**Scores:** Practical Operability: 4, Legal Enforceability: 2

**Recommendation:** Replace all instances of "interim eligibility" and "eligible session" with a forward-looking reference to a defined, identity-bound role. For example: "Requires `operatorEligible`" should be "Requires the session to be authenticated under an identity-bound 'Operator' role."

### Disclosure obligations

**Feedback:** This section correctly identifies the need for explicit user disclosure, which is critical for compliance and mitigating liability. However, it lacks specificity. Stating the shell "must require explicit disclosure" is not enough; a governing document must specify the *content* of that disclosure (or a direct pointer to the required text).

**Scores:** Legal Enforceability: 3, Completeness: 3

**Recommendation:** Add a requirement that the specific legal/compliance-approved text for each disclosure (e.g., entering operator mode, denial of elevation) must be stored in a canonical, versioned artifact (e.g., a `PolicyRecord` or a content registry) and referenced by the shell implementation. This prevents developers from inventing their own legally inadequate disclosure messages.

### Immediate remediation direction / Required phase outputs

**Feedback:** These sections form a strong, actionable plan. The call to define an "identity-bound administrator posture" is the correct path forward. The document correctly positions itself as the foundational work for a future, formal specification. My primary legal concern is ensuring this transition happens immediately and is not deferred.

**Scores:** Completeness: 5, Practical Operability: 5

**Recommendation:** Add a timeline or urgency statement. For example: "The interim device-local authority model presents a critical security risk and must be replaced with an identity-bound mechanism within the next development cycle. No new features leveraging elevated privileges may be built until this remediation is complete."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Entire Document | This is a plan, not an enforceable governing document. The "interim authority" it describes is a critical liability. | **Major Revision Required:** Convert this plan into a formal, binding AIOS Specification document. Replace the entire "interim device-local authority" system with specific rules for an identity-bound model, even if it's a minimal V1. | Critical | 3, 8 |
| 2 | Disclosure obligations | Disclosure requirements are stated but the specific, legally-binding content of the disclosures is not defined. | Mandate that all user-facing disclosure text for authority changes must be sourced from a version-controlled, compliance-approved registry, not hard-coded by developers. | High | 3, 7 |
| 3 | Authority matrix | The term "interim eligibility" is vague and legally meaningless, creating an unenforceable rule. | Replace all references to "eligibility" with the specific condition required, such as "authentication with an identity-bound role of 'Operator'." | High | 3, 8 |
| 4 | Entire Document | The document's structure, voice, and tone do not comply with the binding *AIOS Style Guide*. | Reformat the new specification using the standard Article/Section structure. Use formal, third-person, present-tense language for all rules. | Medium | 1, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The composite score of 3.5 normally suggests "Approved with Changes," but a score of 2 in Legal Enforceability triggers a "Major Revision" under the disposition rules. The document correctly identifies a critical security and legal flaw in the platform's core authority model but fails to provide the enforceable rules needed to fix it, presenting a plan instead. This gap is too significant to approve, even with changes.

**Top 3 Actions Required:**
1.  **Draft a Formal Specification:** Immediately begin converting the contents of this plan into a new, formal AIOS Specification document that defines the V1 identity-bound authority model.
2.  **Eliminate "Interim Authority":** The new specification must define rules that completely supersede and prohibit the use of URL parameters or local storage for privilege escalation.
3.  **Define Liability for Privileged Roles:** The new specification must cross-reference the MPOA and clarify the liability boundaries and standards of care for users acting in `developer` or `operator` roles.
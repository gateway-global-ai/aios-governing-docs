review_id: REV-AMD-2026-006-001
document_reviewed: AMD-2026-006
document_version: 0.1.0
reviewer: Gemini
review_date: 2026-04-07
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 1.8
---

# Peer Review: Google Workspace Governed Integration Plane

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 1 | The amendment is in a temporal conflict with the documents it claims to amend, which already contain the proposed changes. |
| 2 | Business Model Alignment | 3 | Enabling a key enterprise integration is aligned with the business model, but the legal gaps would deter adoption. |
| 3 | Legal Enforceability | 1 | The amendment and the specification it ratifies (AIOS-SPEC-007) are critically lacking in liability boundaries, consequences for breach, and specific obligations. |
| 4 | Architectural Fidelity | 3 | The proposed architecture is sound and aligns with the Manifesto, but the document fails to codify it in a non-conflicting, coherent manner. |
| 5 | Completeness | 1 | This amendment omits essential components for governance, including liability terms, a phased rollout plan, and specific versioning for the ratified document. |
| 6 | Conflict Freedom | 1 | The document creates a circular dependency and logical paradox, as AIOS-SPEC-003 and -006 already reference this draft amendment and include its content. |
| 7 | Practical Operability | 2 | The profound inconsistencies and missing details make the governance unactionable for developers and compliance teams. |
| 8 | Style & Clarity | 2 | The amendment is overly terse, failing to provide the necessary context or specific changes required for a formal legislative act. |
| 9 | Developer Synchrony | 1 | The circular references between this amendment and the specifications make it impossible for a developer to determine the source of truth. |
| 10 | Platform Economics Synchrony | 3 | It fails to address the economic implications of Workspace actions, such as whether they constitute "external intelligence" subject to a billing multiplier. |
| 11 | Friction Factor | 1 | The document's state of confusion introduces maximum friction, blocking rather than enabling governed development. |
| | **Composite Score** | **1.8** | |

---

## Overall Assessment

### Strengths

- **Rationale (§1):** The document correctly identifies a critical architectural risk: the need to prevent unbounded execution by exposing a broad tool surface like Google Workspace directly to conversational layers. The proposed architectural pattern (`Intent Layer → Router → Control Plane → Adapter`) is consistent with AIOS principles of governed execution.

### Critical Gaps

- **Temporal/Logical Conflict:** The amendment is fundamentally broken from a process standpoint. It proposes to "extend" `AIOS-SPEC-003` and `AIOS-SPEC-006`, but the provided versions of those documents (v1.3.0) already include the Google Workspace sections (Sec. 11 and Sec. 13, respectively). Those sections, in turn, reference `AMD-2026-006` as the enabling amendment. This creates an impossible circular reference and suggests a severe version control or governance process failure.
- **Missing Liability Framework:** The amendment, and more importantly the `AIOS-SPEC-007` it seeks to ratify, completely omits any discussion of liability. If an AI agent, operating through this governed plane, incorrectly deletes a user's files or sends a sensitive email to the wrong recipient, where does the liability lie? This is a non-negotiable requirement for any enterprise-grade integration and its absence is a critical failure.
- **Vagueness and Incompleteness:** The amendment is a "thin" legislative act that lacks necessary substance. It does not specify the exact version of `AIOS-SPEC-007` it ratifies, fails to provide a phased migration and rollback plan (unlike its predecessor `AMD-2026-005`), and does not define the consequences of non-compliance. It is not specific enough to be enforceable.

---

## Article-by-Article Review

### Section 1. Rationale

**Feedback:** The rationale is architecturally sound but legally insufficient. It correctly identifies the risk but fails to frame it in terms of legal or commercial obligations (e.g., "to mitigate operational risk and enforce data handling policies as required by the MPOA..."). The statement is dense with technical jargon without connecting it back to the governing principles of liability and compliance.

**Scores:** Architectural Fidelity: 4, Legal Enforceability: 2

**Recommendation:** Expand the rationale to connect the technical architecture to the legal and business imperatives.

**Proposed Text:**
> Google Workspace MCP servers expose a broad tool surface with significant potential for data modification and exfiltration. Exposing this surface directly to conversational or voice layers creates **unbounded execution risk and unacceptable legal liability** for both the Tenant and the Platform. This amendment ratifies **AIOS-SPEC-007** as the binding contract to mitigate this risk by enforcing a governed execution path: **Intent Layer → Workspace Intent Router → Integration Control Plane → MCP Adapter → Google APIs**. This model ensures all Workspace actions are subject to policy, audit, and scope limitations defined in policy packs POL-WORKSPACE-001–006, thereby satisfying the Platform's duties under the MPOA.

### Section 2. Proposed Changes

**Feedback:** This section is the source of the critical process failure. It describes actions that appear to have already been taken in the source documents. Furthermore, as an amendment, it should be more explicit. Simply stating the "Effect" is insufficient for a binding legal document. It should specify *how* the documents are extended, for instance, by stating "Insert new Section 11 into AIOS-SPEC-003 as defined in Annex A of this amendment."

**Scores:** Completeness: 1, Cross-Document Consistency: 1

**Recommendation:** Halt this amendment. First, revert the premature changes in `AIOS-SPEC-003` and `AIOS-SPEC-006` to a prior version. Then, rewrite this amendment to include the full text of the proposed new sections as an Annex, making the amendment a self-contained, auditable change.

### Section 4. Ratification Requirements

**Feedback:** This section is incomplete. The third bullet point, "SPEC-007 aligned with AMD-2026-005 governed surfaces and deterministic failure," is a vague statement, not a verifiable checklist item. It should also include requirements for a legal review of liability and a clear migration plan.

**Scores:** Practical Operability: 2, Legal Enforceability: 2

**Recommendation:** Add specific, auditable checklist items.

**Proposed Additions:**
> - [ ] Legal review of AIOS-SPEC-007 completed, confirming explicit liability boundaries for integration failures.
> - [ ] Annex B (Phased Migration & Rollback Plan) drafted and approved by the Governance Council.
> - [ ] AIOS-SPEC-007 (version 0.1.1 or higher) confirmed to contain no "weasel words" (e.g., "generally," "reasonable efforts") in normative sections.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Global | Circular/Temporal Conflict | **Halt ratification.** Revert the target documents (`AIOS-SPEC-003`, `AIOS-SPEC-006`) to a state preceding the addition of the Google Workspace sections. The amendment must *introduce* the change, not ratify a change that has already been merged. | Critical | 1, 5, 6, 7, 9, 11 |
| 2 | Global | Missing Liability Framework | Add a new section to `AIOS-SPEC-007` (and reference it in this amendment) that explicitly defines the liability model for actions taken through the Workspace integration, including errors, data loss, and security incidents. | Critical | 3, 2, 5, 7 |
| 3 | Sec 2 | Insufficient Detail | Rewrite the amendment to be a self-contained legislative act. It should include the full text of the new sections being added to `AIOS-SPEC-003` and `AIOS-SPEC-006` within an Annex. | High | 3, 5, 8 |
| 4 | Global | Missing Migration Plan | Add a "Phased Migration & Rollback" Annex, similar to the one in `AMD-2026-005`, detailing the steps, acceptance criteria, and rollback triggers for activating the governed integration plane. | High | 5, 7 |
| 5 | Global | Vague Ratification Target | Change "Ratify AIOS-SPEC-007" to "Ratify **AIOS-SPEC-007 version 0.1.1**". All ratified documents must have their version explicitly pinned. | Medium | 3, 5, 7 |
| 6 | Global | Unaddressed Economic Impact | Add a section to `AIOS-SPEC-007` clarifying the economic treatment of Workspace API calls. State explicitly whether they are considered "external intelligence" subject to the 2.0x billing multiplier under the MPOA. | Medium | 10, 2 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is fundamentally non-ratifiable in its current state due to a critical temporal conflict with the documents it purports to amend. This process failure, combined with a complete lack of a liability framework for a high-risk integration, renders the amendment legally unsound and operationally incoherent.

**Top 3 Actions Required:**
1.  **Resolve Document State Conflict:** Halt this amendment and execute a version control reset. Revert `AIOS-SPEC-003` and `AIOS-SPEC-006` to a clean state, then redraft this amendment to properly *introduce* the new sections.
2.  **Draft Liability & Indemnity Clauses:** Add a comprehensive liability section to `AIOS-SPEC-007` that addresses incorrect AI actions, data loss, and security breaches, clearly delineating platform, tenant, and user responsibilities.
3.  **Make the Amendment Self-Contained:** Rewrite `AMD-2026-006` to include the full text of proposed changes and a detailed, actionable migration plan, making it a complete and auditable record of the governance decision.
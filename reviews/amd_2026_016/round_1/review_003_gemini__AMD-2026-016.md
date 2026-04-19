---
review_id: REV-AMD-2026-016-001
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.1.0
reviewer: Gemini
review_date: 2026-04-10
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 2.9
---

# Peer Review: Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Introduces a `principal class` concept without reconciling it with the existing `Actor` schema in AIOS-SPEC-009 and AMD-2026-007. |
| 2 | Business Model Alignment | 4 | The document strongly supports enterprise and vendor integration by creating a clear, governable framework for service and application accounts. |
| 3 | Legal Enforceability | 2 | The principles are strong, but the document critically lacks explicit clauses for liability, dispute resolution, and artifact ownership when a non-human principal acts. |
| 4 | Architectural Fidelity | 4 | Aligns well with the core principles of Policy Supremacy and routed authority, correctly treating non-human actors as subjects of governance, not as trusted infrastructure. |
| 5 | Completeness | 1 | Critically omits the entire lifecycle management for non-human principals, including their creation, credentialing, management, and revocation. |
| 6 | Conflict Freedom | 4 | No direct conflicts with other governing documents are present; it extends the existing authority model by filling a significant gap. |
| 7 | Practical Operability | 2 | A developer or operator cannot act on this document because the mechanism for registering and managing these new principal types is undefined. |
| 8 | Style & Clarity | 5 | The document is exceptionally well-written, precise, unambiguous, and adheres perfectly to the AIOS Style Guide. |
| 9 | Developer Synchrony | 2 | Developers would be blocked, as the document defines the rules for principals but provides no API, schema, or process for creating or managing them. |
| 10 | Platform Economics Synchrony | 2 | Fails to address how actions initiated by non-human principals are metered, billed, or debited against a Funded Data Account. |
| 11 | Friction Factor | 3 | The principles themselves are necessary governance, but the document's incompleteness creates significant friction by leaving the implementation path undefined. |
| | **Composite Score** | **2.9** | |

---

## Overall Assessment

### Strengths

This amendment addresses a critical and previously undefined area of the AIOS governance framework. Its greatest strengths are:

1.  **Conceptual Clarity (Section 3, 4):** The document does an excellent job of defining and separating the distinct classes of non-human principals (Service Account, Agent, Application). This separation is vital for creating granular, enforceable policies.
2.  **Principle of No Ambient Authority (Section 4.2):** The prohibition of undeclared or implicit power is a cornerstone of good security and governance. By mandating explicit identity, role, scope, and routing, the amendment closes significant potential backdoors.
3.  **Adherence to Style & Clarity (Overall):** The writing is precise, authoritative, and perfectly aligned with the AIOS Style Guide, making its normative requirements clear and unambiguous.

### Critical Gaps

Despite its strong foundation, the document suffers from several critical omissions that render it incomplete and inoperable as-is.

1.  **Missing Lifecycle Management:** The document provides no mechanism for the creation, credentialing, management, or revocation of non-human principals. This is a critical failure of completeness (Dimension 5) and makes the document practically inoperable (Dimension 7).
2.  **Undefined Liability and Ownership:** The document does not specify who is liable for the actions of a non-human principal, nor does it define the ownership of artifacts created by one. This is a major legal enforceability gap (Dimension 3) that would create significant disputes.
3.  **Lack of Economic Attribution:** There is no mention of how actions taken by non-human principals are billed or tied to the platform's economic model (e.g., Funded Data Accounts). This is a critical gap in Platform Economics Synchrony (Dimension 10).
4.  **Schema Inconsistency:** The concept of `principal class` is not integrated with the existing `Actor` schema defined in AIOS-SPEC-009, creating a cross-document consistency issue (Dimension 1).

---

## Article-by-Article Review

### Section 3. Definitions

**Feedback:** The definitions are clear and well-scoped. The distinction between a `Service account` (deterministic) and an `Agent principal` (interpretive) is particularly strong and useful for policy creation.

**Scores:** Style & Clarity: 5

**Recommendation:** No changes needed for this section. It is a model of clarity.

### Section 4. Normative decisions

**Feedback:** This section establishes excellent, legally-sound principles. However, many of the `SHALL` statements require a corresponding mechanism for enforcement that is currently missing from the AIOS framework.

-   **Section 4.5 Required action-carriage fields:** This is an excellent, concrete requirement that makes auditing possible.
-   **Section 4.10 Ownership and mutation boundary:** This section correctly identifies a critical issue but punts on the solution. Stating "the system SHALL define" is insufficient. This amendment is the place where the *default* rules for that definition must be established.
-   **Section 4.9 Non-substitution rule:** This is a critical rule for maintaining audit integrity and preventing privilege escalation.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 2

**Recommendation:** Add a new subsection to address liability and ownership directly.

**Proposed Text for Section 4.12 (New):**
> ### 4.12 Liability and Ownership Attribution
>
> Unless superseded by an explicit Tenant agreement or a `PolicyRecord` governing a specific transaction, the following default rules of attribution **SHALL** apply:
>
> 1.  **Service Account:** Actions and created artifacts are attributed to the Tenant or Platform entity that owns and configured the service account. Liability for its actions rests with the owning entity.
> 2.  **Agent Principal:** Actions and created artifacts are attributed to the session and `Actor` (human or application) that invoked the agent. Liability flows back to the invoker, subject to the MPOA.
> 3.  **Application Principal:** Actions and created artifacts are attributed to the Tenant that registered and deployed the application. The Tenant **SHALL** be liable for the actions of its registered applications per the MPOA.

### Section 5. Relationship to existing governance

**Feedback:** The analysis of relationships is accurate. However, it fails to identify the direct schema conflict with AIOS-SPEC-009's `Actor` interface. The `Actor` has an `id` and `role`, but this document implies a third critical field: `principal_class`.

**Scores:** Cross-Document Consistency: 3

**Recommendation:** Explicitly state the need to amend the `Actor` schema in AIOS-SPEC-009.

**Proposed Text Addition to the table, AIOS-SPEC-009 row:**
> **Relationship:** [...] This amendment necessitates an update to the `Actor` interface in AIOS-SPEC-009 to include a `principal_class` field, ensuring that policy evaluation can distinguish between human, service, agent, and application principals.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | N/A (New Section) | The document is critically missing the entire lifecycle for non-human principals (creation, credentialing, revocation). | Add a new top-level section (e.g., "Section 5: Principal Lifecycle Management") that defines the normative process or API for registering and decommissioning non-human principals. This section should specify that principals are registered within a Kit or via a governed control plane API. | Critical | 5, 7, 9 |
| 2 | 4.10 | Liability and ownership are undefined, creating a massive legal gap. | Add a new subsection (e.g., 4.12) that defines the default liability and ownership attribution rules for each class of non-human principal, linking them back to the MPOA and the invoking actor or owning Tenant. | Critical | 3, 10 |
| 3 | 5 | The document introduces `principal class` but does not reconcile this with the existing `Actor` schema in AIOS-SPEC-009. | Update Section 5 to explicitly state that the `Actor` schema in AIOS-SPEC-009 must be amended to include a `principal_class` field to support policy evaluation. | High | 1, 9 |
| 4 | N/A (New Section) | The economic impact of non-human principal actions is not addressed. | Add a new subsection or reference that clarifies how actions by non-human principals are metered and attributed for billing (e.g., tied to the owning Tenant's Funded Data Account or the invoking user's session). | High | 10 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document establishes an excellent and necessary set of principles for governing non-human actors, but it is critically incomplete. The complete absence of a principal lifecycle management framework (how principals are created/destroyed) and the lack of specific clauses for liability and ownership make it inoperable and legally unsound.

**Top 3 Actions Required:**
1.  **Define the Principal Lifecycle:** Add a new section detailing the normative process for registering, credentialing, and revoking non-human principals.
2.  **Specify Liability and Ownership:** Add a new subsection explicitly defining the default attribution of liability and artifact ownership for actions taken by each principal class.
3.  **Reconcile Actor Schema:** Explicitly call for the amendment of the `Actor` schema in AIOS-SPEC-009 to include the `principal_class` concept introduced here.
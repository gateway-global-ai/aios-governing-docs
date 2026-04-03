---
review_id: REV-AIOS-SPEC-007-001
document_reviewed: AIOS-SPEC-007
document_version: 0.1.0
reviewer: Gemini
review_date: 2026-04-03
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: Google Workspace Integration Governance

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The document aligns well with core principles and references other specifications correctly, but some terminology could be tighter. |
| 2 | Completeness | 2 | Critical implementation details, particularly for the policy framework and liability boundaries, are missing or merely placeholders. |
| 3 | Practical Operability | 2 | The pervasive use of "SHOULD" for critical governance and transport requirements makes key sections unenforceable as written. |
| 4 | Conflict Freedom | 3 | While not in direct conflict, the document's weak language on governance logging creates procedural tension with the Constitution's transparency mandates. |
| 5 | Style & Clarity | 3 | The document generally follows the style guide but has inconsistencies in capitalization and uses ambiguous terms. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

-   **Strong Architectural Foundation (Section 1 & 2):** The document correctly establishes a governance model that respects the AIOS separation of powers, mandating that all operations pass through a governed Integration Control Plane. The prohibition on direct MCP calls is clear and architecturally sound.
-   **Clear Capability Classification (Section 4):** The distinction between Layer 1 (governance scope classes) and Layer 2 (intent identifiers) is excellent. The "Hard rule — one-to-one resolution" provides exactly the kind of deterministic, legally unambiguous mapping required for policy enforcement.
-   **Deterministic Failure (Section 7):** The specification correctly incorporates the deterministic failure policy from `AMD-2026-005`, preventing silent degradation and ensuring system transparency, which is critical for auditability and liability.

### Critical Gaps

-   **Unenforceable Weasel Words (Sections 2, 8, 12):** The document uses "SHOULD" for critical requirements like production transport protocols and the recording of governance decisions. This language is legally weak and makes these core rules practically optional, undermining the entire framework.
-   **Placeholder Policy Framework (Section 9):** The policy framework consists of titles, not enforceable rules. A developer cannot implement `POL-WORKSPACE-002` without knowing the specific conditions, exceptions, and parameters. This section is incomplete to the point of being non-functional.
-   **Missing Liability and SLA Terms:** The document defines a critical integration but is silent on liability for failures, data breaches via the integration, or performance SLAs for the Control Plane. While the MPOA is the ultimate authority, this specification must define its operational relationship to the MPOA's terms.

---

## Article-by-Article Review

### Section 2: Integration Model

**Feedback:** The architectural model is strong, but the technical requirements are too weak for a binding specification. Section 2.3 states production transport "SHOULD" use streamable HTTP and that single-user mode is "NOT permitted" but then allows it for testing under "explicit policy," without defining that policy. This creates a loophole.
**Scores:** Practical Operability: 2
**Recommendation:** Change "SHOULD use" to "MUST use" for production environments.

> **Proposed Change (Section 2.3):**
> **Old Text:** The integration SHOULD use: streamable HTTP transport...
> **New Text:** The integration **MUST** use: streamable HTTP transport...
>
> **Old Text:** It MAY be used only for local development or sandboxed testing under explicit policy.
> **New Text:** It MAY be used only for local development. Use in any shared sandbox environment requires an explicit, auditable policy exception granted by the Governance Council.

### Section 4: Capability Classification

**Feedback:** This section is a highlight. The one-to-one mapping rule is precise and enforceable. The only minor issue is that the text defines the taxonomy as "canonical authority," but the document itself is a `draft`. The status should be reflected.
**Scores:** Practical Operability: 5, Style & Clarity: 4
**Recommendation:** No text changes required, but the document's `draft` status must be considered when relying on this as a canonical source.

### Section 9: Policy Framework

**Feedback:** This section is critically incomplete. It lists policy names but provides no actual policy logic, thresholds, or evaluation criteria. As written, it is inoperable and unauditable. A developer has no guidance on how to implement `POL-WORKSPACE-003 — Share and permission hard gate`. What confirmation is required? What does a "full audit" entail?
**Scores:** Completeness: 1, Practical Operability: 1
**Recommendation:** Each policy must be defined with explicit, testable rules. At a minimum, each policy requires its own subsection detailing the conditions, required inputs, and deny/allow/confirm logic.

> **Example for POL-WORKSPACE-003:**
> ### POL-WORKSPACE-003: Share and Permission Hard Gate
> 1. Any intent resolving to the `workspace.google.share` scope class MUST trigger a `CONFIRM` state in the Stateful Shell before execution.
> 2. The confirmation UI (`aios-confirmation-dialog`) MUST display the target resource name, the identity being granted access, and the permission level.
> 3. Creating a "public" or "anyone with the link" permission MUST require two-factor authentication from the user if their `authority_level` is `user`.

### Section 12: Deployment Phases

**Feedback:** Stating that advancement "SHOULD be recorded as a governance decision" is a severe legal and governance flaw. Per the Constitution (Article II, Section 3), all such changes *must* be logged. This weak language creates a direct conflict with the spirit, if not the letter, of the parent governing document.
**Scores:** Conflict Freedom: 2, Practical Operability: 1
**Recommendation:** Change "SHOULD" to "MUST".

> **Proposed Change (Section 12):**
> **Old Text:** Advancement to a higher phase SHOULD be recorded as a governance decision (Council or delegated authority per Constitution).
> **New Text:** Advancement to a higher phase **MUST** be ratified and recorded as a formal governance decision, consistent with the legislative process defined in the Governance Constitution (Article II).

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---|---|---|---|---|
| 1 | 9 | Policy Framework is Incomplete | Expand Section 9 to include specific, enforceable rules for each listed policy. | Critical | 2, 3 |
| 2 | 2, 8, 12 | Pervasive use of "SHOULD" | Replace "SHOULD" with "MUST" for all non-negotiable requirements, especially production transport, governance logging, and error handling. | Critical | 3, 4 |
| 3 | N/A | Missing Liability & SLAs | Add a new section clarifying the liability boundaries for this integration and referencing the MPOA. Define operational SLAs for the Control Plane. | High | 2, 3 |
| 4 | 2.3 | Ambiguous Test Environment Rules | Clarify the exact policy required to use single-user mode in any non-local environment. | Medium | 3 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document establishes a sound architectural direction but is critically undermined by unenforceable language and incomplete sections. The placeholder policy framework and the use of "SHOULD" for mandatory governance actions render the document unfit for ratification as a binding specification.

**Top 3 Actions Required:**
1.  Rewrite Section 9 to define the actual rules for each policy, not just their titles.
2.  Perform a document-wide search for "SHOULD" and replace it with "MUST" for all binding technical and procedural requirements.
3.  Add a section defining the liability model and performance SLAs as they relate to the Master Platform Operating Agreement (MPOA).
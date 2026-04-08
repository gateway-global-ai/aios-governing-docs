---
review_id: REV-AIOS-SPEC-007-002
document_reviewed: AIOS-SPEC-007
document_version: 0.2.0
reviewer: DeepSeek R3
review_date: 2026-04-08
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.7
---

# Peer Review: Google Workspace Integration Governance

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with AIOS-SPEC-009 and AMD-2026-009, but some references to WORKSPACE.md create ambiguity about normative vs informative status. |
| 2 | Business Model Alignment | 4 | Correctly positions integration as governed capability layer, not product factory, though vendor ecosystem implications could be more explicit. |
| 3 | Legal Enforceability | 3 | Uses "SHALL" consistently but lacks specific liability boundaries and SLA numbers for control plane operations. |
| 4 | Architectural Fidelity | 5 | Perfectly implements SPEC-009 intent primitive and DCP pipeline; enforces separation of powers through mandatory routing chain. |
| 5 | Completeness | 3 | Missing concrete policy definitions (POL-WEB-*), detailed failure modes, and explicit audit requirements for the control plane. |
| 6 | Conflict Freedom | 4 | No direct conflicts, but §3 references "policy register" that doesn't exist in current governing corpus. |
| 7 | Practical Operability | 3 | Routing envelope is well-defined but lacks JSON schema; MCP tool resolution process needs more implementation detail. |
| 8 | Style & Clarity | 4 | Follows Style Guide well, but some sections mix normative and informative content without clear demarcation. |
| 9 | Developer Synchrony | 4 | Good reference to implementation pointers, but missing concrete CLI commands and validation steps. |
| 10 | Platform Economics Synchrony | 4 | Correctly references MPOA for liability, but doesn't address token economics for web retrieval operations. |
| 11 | Friction Factor | 4 | Minimal friction for compliant implementations, though scope validation could add overhead. |
| | **Composite Score** | **3.7** | |

---

## Overall Assessment

### Strengths

- **Architectural Rigor (§2.1):** The mandatory integration chain perfectly implements AIOS-SPEC-009's intent primitive and enforces the separation of powers between UI layer and MCP execution.
- **Execution Scope Integration (§8):** Strong binding to AIOS-SPEC-010 ensures deterministic scope validation before MCP dispatch, preventing context bounding violations.
- **Web Search Governance (§3):** Correctly incorporates AMD-2026-009 requirements and establishes PSE as one permitted backend with proper credential handling.

### Critical Gaps

- **Missing Policy Definitions (§3):** References POL-WEB-SCOPE-001 but provides no concrete policy logic, thresholds, or evaluation criteria.
- **Incomplete Failure Modes (§6):** Lists error codes but lacks specific recovery procedures and audit requirements for each failure type.
- **Ambiguous Informative References:** Frequent references to WORKSPACE.md blur the line between normative requirements and implementation notes.

---

## Article-by-Article Review

### Section 2: Normative Routing Model

**Feedback:** The integration chain is architecturally sound and enforces SPEC-009 principles. The one-to-one mapping rule (2.1.3) is precise and enforceable. However, the MCP tool resolution process (2.3) needs more detail about how intent parameters map to MCP arguments.

**Scores:** Architectural Fidelity: 5, Practical Operability: 3

**Recommendation:** Add a subsection detailing the parameter mapping contract between intent fields and MCP tool arguments, with validation rules.

> **Proposed Addition (Section 2.4):**
> ### 2.4 Intent Parameter Validation
> 1. Each intent in the workspace.* registry **SHALL** define required and optional parameters in a machine-readable schema.
> 2. The Integration Control Plane **SHALL** validate all required parameters are present before MCP dispatch.
> 3. Parameter validation failures **SHALL** return `invalid_intent` with specific field-level error messages.

### Section 3: Web Search and External Retrieval (PSE)

**Feedback:** Correctly incorporates AMD-2026-009 but references a policy register that doesn't exist in the current governing corpus. The PSE credential handling is security-conscious but lacks implementation verification steps.

**Scores:** Cross-Document Consistency: 3, Completeness: 2

**Recommendation:** Either define POL-WEB-SCOPE-001 inline or create a concrete reference to where it will be defined. Add credential verification requirements.

> **Proposed Change (Section 3.2):**
> **Old Text:** Implementations **SHALL** reference **POL-WEB-SCOPE-001** (or successor in the organization policy register) for which **search scope classes** are allowed per tenant or intent.
> **New Text:** Implementations **SHALL** enforce search scope classes as defined in **[AMD-2026-009 §4](../amendments/AMD-2026-009.md)**. The policy engine **SHALL** maintain tenant-specific allowlists for `web.search.broad_public` usage.

### Section 5: Workspace Routing Envelope

**Feedback:** The envelope structure is well-defined but lacks a formal JSON schema. The `execution_scope` field correctly references SPEC-010 but doesn't specify validation timing.

**Scores:** Practical Operability: 3, Developer Synchrony: 4

**Recommendation:** Add a normative JSON schema appendix and clarify validation sequence.

> **Proposed Addition (Appendix B):**
> ```json
> {
>   "$schema": "http://json-schema.org/draft-07/schema#",
>   "title": "WorkspaceRoutingEnvelope",
>   "type": "object",
>   "required": ["intent", "actor_type", "tenant_id", "user_binding", "execution_mode", "policy_context"],
>   "properties": {
>     "intent": { "type": "string", "pattern": "^workspace\\.[a-z]+\\.[a-z0-9_]+$" },
>     "actor_type": { "type": "string" },
>     "tenant_id": { "type": "string" },
>     "user_binding": { "type": "string" },
>     "execution_mode": { "enum": ["observe", "prepare", "execute", "automate"] },
>     "policy_context": {
>       "type": "object",
>       "required": ["scope_class"],
>       "properties": {
>         "scope_class": { "type": "string" },
>         "requires_confirmation": { "type": "boolean" }
>       }
>     },
>     "execution_scope": { "$ref": "#/definitions/ExecutionScopeEnvelope" }
>   }
> }
> ```

### Section 6: Integration Control Plane — Deterministic Outcomes

**Feedback:** Error codes are well-defined but lack specific audit requirements and recovery procedures. The `adapter_error` code needs sub-classification for different MCP failure modes.

**Scores:** Completeness: 3, Practical Operability: 3

**Recommendation:** Expand with audit requirements and failure recovery procedures.

> **Proposed Addition (Section 6.1):**
> ### 6.1 Audit Requirements
> 1. All control plane outcomes (success and failure) **SHALL** generate an audit record with at minimum: timestamp, intent, scope_class, outcome_code, and correlation_id.
> 2. Audit records for `policy_denied` outcomes **SHALL** include the specific policy identifier and denial reason.
> 3. `adapter_error` outcomes **SHALL** be sub-classified as: `mcp_transport_failure`, `mcp_tool_error`, or `mcp_timeout`.

### Section 8: Execution Scope Envelope

**Feedback:** Perfect implementation of SPEC-010 requirements. The validation timing is implied but should be explicit.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5

**Recommendation:** Make validation timing explicit and reference SPEC-010 validation rules.

> **Proposed Change:**
> **Old Text:** When **`execution_scope`** is present on the **Workspace routing envelope**, the Integration Control Plane **SHALL** validate the resolved MCP operation against that envelope **before** calling the MCP adapter.
> **New Text:** When **`execution_scope`** is present, the Integration Control Plane **SHALL** validate the operation per **AIOS-SPEC-010 §5.2** before MCP dispatch. Validation failures **SHALL** return `scope_denied` with the specific validation error.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 3 | Missing policy definitions | Define POL-WEB-SCOPE-001 inline or create concrete reference | High | 5, 6 |
| 2 | 5 | No JSON schema | Add normative JSON schema in Appendix | Medium | 7, 9 |
| 3 | 6 | Incomplete failure handling | Add audit requirements and failure recovery procedures | High | 5, 7 |
| 4 | 2 | Missing parameter validation | Add intent parameter validation subsection | Medium | 7, 9 |
| 5 | Throughout | Ambiguous informative references | Clearly demarcate normative vs informative content | Low | 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document establishes a technically sound integration architecture with strong alignment to governing principles, but requires concrete policy definitions and implementation details before ratification.

**Top 3 Actions Required:**
1. Define concrete search scope policies or create explicit references to where they will be defined.
2. Add JSON schema for the routing envelope and clarify parameter validation requirements.
3. Expand failure handling with specific audit requirements and recovery procedures.
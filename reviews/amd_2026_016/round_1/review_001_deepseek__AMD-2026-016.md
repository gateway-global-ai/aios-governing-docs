---
review_id: REV-AMD-2026-016-001
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.1.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.7
---

# Peer Review: AMD-2026-016 — Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Uses consistent terminology but lacks explicit mapping to PolicyRecord schema and AIOS-SPEC-009 intent lifecycle. |
| 2 | Business Model Alignment | 4 | Supports marketplace model by governing non-human actors that vendors and tenants would deploy. |
| 3 | Legal Enforceability | 2 | Definitions are clear but lack binding schema or concrete enforcement mechanisms; "SHALL" statements need PolicyRecord hooks. |
| 4 | Architectural Fidelity | 3 | Aligns with policy supremacy but misses integration with DCP pipeline and stateless compute principles. |
| 5 | Completeness | 2 | Missing annexes: JSON schema for principal binding, audit field specifications, and conformance test criteria. |
| 6 | Conflict Freedom | 4 | No direct contradictions with existing documents; respects supremacy clause boundaries. |
| 7 | Practical Operability | 2 | Lacks implementation guidance: no examples of role binding in PolicyRecord, no routing examples, no migration path. |
| 8 | Style & Clarity | 4 | Clear, authoritative voice; follows Style Guide; definitions are precise and well-structured. |
| 9 | Developer Synchrony | 2 | Developers cannot implement from this alone; missing schemas, CLI references, and integration with existing developer docs. |
| 10 | Platform Economics Synchrony | 3 | Implicitly supports BYOK and tenant-scoped principals but lacks explicit economic mechanics for service account billing. |
| 11 | Friction Factor | 3 | Introduces necessary governance for non-human actors without excessive bureaucracy; scope is appropriately narrow. |
| | **Composite Score** | **2.7** | |

---

## Overall Assessment

### Strengths

1. **Clear Problem Statement** (§1): Articulates the "ambient authority" problem precisely—non-human actors must not operate as hidden infrastructure.
2. **Precise Definitions** (§3): Terms like "service account," "agent principal," and "routed communication" are well-defined and distinguish principal classes.
3. **Strong Normative Foundation** (§4): The "no ambient authority" and "role-binding and scope" rules establish essential governance boundaries.

### Critical Gaps

1. **Missing Technical Schemas**: No JSON schema for principal binding, audit fields, or routed communication envelopes—developers cannot implement.
2. **No Integration with PolicyRecord**: The amendment does not specify how non-human principals map to PolicyRecord `actor` fields or `required_context_keys`.
3. **Incomplete Execution Model Alignment**: Fails to define how non-human principals participate in AIOS-SPEC-009 intent lifecycle (expression → resolution → validation → execution).
4. **Lacks Conformance Criteria**: No annex defining how implementations prove compliance; no testable thresholds.

---

## Article-by-Article Review

### §3 Definitions

**Feedback:** Definitions are precise but isolated. Missing: mapping to existing glossary (Technical Manifesto Appendix) and cross-reference to AIOS-SPEC-009 §3 (Actor definition). "Deterministic non-human action" should explicitly reference PolicyRecord evaluation.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 2

**Recommendation:** Add a table mapping each defined term to existing glossary entries. Add: "**Actor** (as defined in AIOS-SPEC-009 §3) includes non-human principals governed by this amendment."

### §4 Normative decisions

**Feedback:** Rules are conceptually sound but lack enforcement mechanisms. §4.5 "Required action-carriage fields" lists minimum facts but does not provide a schema or specify where these fields appear (PolicyRecord? audit log? intent envelope?).

**Scores:** Architectural Fidelity: 3, Practical Operability: 2, Legal Enforceability: 2

**Recommendation:** Add Annex A: "Non-Human Principal Binding Schema" with JSON schema defining `principal_identity`, `principal_class`, `role_binding`, `scope_binding`, etc. Reference AIOS-SPEC-002 (PolicyRecord) and specify that these fields must appear in `SessionContext` for policy evaluation.

### §4.6 Service-account rule

**Feedback:** Correctly distinguishes service accounts as deterministic but misses integration with DCP pipeline. Service accounts should be registered in a governed registry (like capability registry) with versioned binding.

**Scores:** Architectural Fidelity: 3, Developer Synchrony: 2

**Recommendation:** Add: "Service accounts **SHALL** be registered in the Platform Principal Registry with versioned binding metadata. Registration **SHALL** follow DCP compilation and Tier 2 governance review."

### §4.7 Agent-principal rule

**Feedback:** Does not address how agent principals interact with intent compilation and approval model (AIOS-SPEC-009 §15). Agent principals may propose execution plans; need rules for plan attribution and audit.

**Scores:** Cross-Document Consistency: 3, Completeness: 2

**Recommendation:** Add subsection: "Agent principals proposing execution plans **SHALL** include `principal_identity` and `principal_class` in plan metadata. Plan approval gates **SHALL** evaluate agent authority per PolicyRecord."

### §5 Relationship to existing governance

**Feedback:** Table is helpful but superficial. Missing: explicit mapping to AIOS-SPEC-002 (PolicyRecord schema needs new `principal_class` field), AIOS-SPEC-009 (intent lifecycle), and DCP pipeline.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 2

**Recommendation:** Expand table with "Implementation Impact" column. Add row for DCP pipeline: "Non-human principal registration must pass DCP schema validation."

### Missing: Annexes and Implementation

**Feedback:** Critical omission. Amendment cannot be ratified without:
1. JSON schema for principal binding
2. Audit field specification
3. Conformance test suite (like AIOS-SPEC-009-CONFORMANCE-TEST-V1)
4. Example PolicyRecord with non-human principal

**Scores:** Completeness: 1, Practical Operability: 1, Developer Synchrony: 1

**Recommendation:** Add:
- **Annex A**: Principal Binding Schema (JSON)
- **Annex B**: Audit Field Specification (mapping to AIOS-SPEC-009 §12.4)
- **Annex C**: Conformance Test Cases (P0/P1/P2)
- **Annex D**: Example PolicyRecord with `actor` field containing non-human principal

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §3 Definitions | Isolated from existing glossary | Add mapping table to Technical Manifesto Appendix; cross-reference AIOS-SPEC-009 Actor. | High | 1, 9 |
| 2 | §4 Normative decisions | Lacks enforcement schemas | Add Annex A: Principal Binding Schema (JSON); integrate with PolicyRecord `SessionContext`. | Critical | 3, 4, 5, 7, 9 |
| 3 | §4.6 Service-account rule | No registry or DCP integration | Require registration in Platform Principal Registry with DCP validation. | High | 4, 7, 9 |
| 4 | §4.7 Agent-principal rule | No intent compilation alignment | Add rules for agent principals in execution plans (AIOS-SPEC-009 §15). | High | 1, 5 |
| 5 | §5 Relationship table | Superficial | Add "Implementation Impact" column; include DCP pipeline and PolicyRecord schema changes. | Medium | 1, 9 |
| 6 | Missing annexes | No implementable artifacts | Add Annexes A-D: schemas, audit fields, conformance tests, example PolicyRecord. | Critical | 5, 7, 9 |
| 7 | Overall | No integration with DCP | State that non-human principal bindings must pass DCP compilation (like PolicyRecord). | High | 4, 7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The amendment establishes crucial doctrine but lacks the technical schemas, PolicyRecord integration, and conformance artifacts required for implementation. Multiple dimensions score ≤2 (Completeness, Practical Operability, Developer Synchrony), and the composite score (2.7) is below the 3.0 threshold.

**Top 3 Actions Required:**
1. **Add Annex A (Principal Binding Schema)** – JSON schema defining non-human principal fields for PolicyRecord `SessionContext` and audit logs.
2. **Integrate with PolicyRecord and DCP** – Explicitly require that non-human principal bindings pass DCP validation and appear in PolicyRecord evaluation.
3. **Add Conformance Test Suite** – Define P0/P1/P2 test cases (like AIOS-SPEC-009-CONFORMANCE-TEST-V1) to prove implementations comply.
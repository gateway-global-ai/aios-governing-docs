---
review_id: REV-AMD-2026-016-002
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.2.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 2
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-016 — Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Introduces "route class" and "principal registry" concepts without reconciling with existing shell routing (AMD-2026-007 §11.9) and PolicyRecord validation (AIOS-SPEC-002 §5). |
| 2 | Business Model Alignment | 4 | Supports marketplace by governing non-human actors but lacks explicit vendor/tenant differentiation in principal classes. |
| 3 | Legal Enforceability | 2 | Many SHALL statements but missing concrete enforcement mechanisms, failure modes, and remediation procedures for violations. |
| 4 | Architectural Fidelity | 3 | Aligns with policy supremacy but creates parallel validation path that could conflict with PolicyRecord evaluation chain. |
| 5 | Completeness | 2 | Missing critical sections on implementation requirements, migration from existing systems, and concrete failure scenarios. |
| 6 | Conflict Freedom | 3 | Creates potential tension with shell authority (AMD-2026-012) and intent execution (AIOS-SPEC-009) without explicit reconciliation. |
| 7 | Practical Operability | 1 | Rules are aspirational without actionable implementation guidance, specific thresholds, or step-by-step processes. |
| 8 | Style & Clarity | 4 | Generally follows style guide with clear structure, though §4 has 15 sub-rules causing cognitive load. |
| 9 | Developer Synchrony | 2 | Lacks schemas, CLI references, or concrete implementation guidance that developers would need to build compliant systems. |
| 10 | Platform Economics Synchrony | 3 | Doesn't contradict economic model but fails to address cost implications of audit requirements and routing overhead. |
| 11 | Friction Factor | 2 | Introduces significant new compliance burden without clear risk justification or graduated implementation path. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

This revision addresses critical Round 1 gaps by adding lifecycle management (§4.13), liability attribution (§4.14), and conformance records (§4.15). The principal registry concept (§3) and route class definitions (§4.4) provide necessary structure for governing non-human actors. The amendment correctly identifies that non-human principals must not operate with ambient authority and establishes explicit binding requirements.

### Critical Gaps

Despite improvements, the document remains primarily doctrinal rather than operational. The most critical issue is **Practical Operability (score 1)** - developers cannot implement from this document alone. There are no concrete validation mechanisms, no integration with existing PolicyRecord evaluation, and no failure mode definitions. The amendment creates a parallel validation path (§4.6) that could conflict with PolicyRecord supremacy (AIOS-SPEC-002). Additionally, the relationship to shell authority (AMD-2026-012) and intent execution (AIOS-SPEC-009) is described but not operationally defined.

---

## Article-by-Article Review

### §0. Status

**Feedback:** Correctly identifies as narrow authority amendment. Missing ratification_target suggests this is still early draft.

**Scores:** Style & Clarity: 4

**Recommendation:** Add ratification_target date or mark as "pending committee review."

### §2. Scope

**Feedback:** Scope boundaries are well-defined but overly restrictive in stating "does not redesign peer review, ratification, UI styling" - this creates tension when non-human principals inevitably interact with these systems.

**Scores:** Conflict Freedom: 3, Completeness: 3

**Recommendation:** Clarify that while amendment doesn't redesign these systems, it governs non-human interaction WITH them.

### §3. Definitions

**Feedback:** Definitions are comprehensive but introduce new concepts ("route class", "principal registry") without integration points to existing systems. "Authority-bearing action" is circularly defined.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 2

**Recommendation:** Add references to where these concepts integrate with PolicyRecord validation and shell routing. Provide concrete examples of what constitutes "authority-bearing" vs routine background activity.

### §4. Normative Decisions

**Feedback:** The 15 sub-rules create significant cognitive load. While each rule is conceptually sound, they lack enforcement mechanisms:

- §4.4 "Permitted route classes MAY include" is too permissive for governance
- §4.6 creates parallel validation path that could bypass PolicyRecord
- §4.12 references "default-deny, fail-closed" but doesn't define specific failure modes
- §4.13 lifecycle management lacks concrete states and transitions

**Scores:** Architectural Fidelity: 3, Practical Operability: 1, Legal Enforceability: 2

**Recommendation:** 
1. Consolidate related rules (e.g., 4.1-4.3 could be one rule)
2. Define specific enforcement mechanisms for each SHALL
3. Integrate validation (§4.6) with PolicyRecord evaluation chain
4. Add concrete failure scenarios and remediation procedures

### §4.4 Routed Communication Rule

**Feedback:** The list of permitted route classes is illustrative rather than normative. Missing criteria for what makes a route class "approved."

**Scores:** Legal Enforceability: 2, Developer Synchrony: 2

**Recommendation:** Replace "MAY include" with "SHALL be limited to" and reference existing authority structures (shell intent routes from AMD-2026-007, control-plane calls from AIOS-SPEC-009).

**Proposed Text:**
> Permitted route classes **SHALL** be limited to those explicitly defined in ratified specifications: shell intent routes (AMD-2026-007 §11.9), control-plane calls (AIOS-SPEC-009 §15), policy-evaluated service interfaces (AIOS-SPEC-002 §5), and application interfaces explicitly governed in tenant agreements.

### §4.6 Validation and Admission Rule

**Feedback:** Creates parallel validation path that could conflict with PolicyRecord evaluation. Missing integration with existing PolicyRecord context keys.

**Scores:** Architectural Fidelity: 2, Conflict Freedom: 3

**Recommendation:** Integrate with PolicyRecord validation rather than creating parallel path.

**Proposed Text:**
> Before a non-human principal may perform an authority-bearing action, the system **SHALL** evaluate the action through the PolicyRecord validation chain (AIOS-SPEC-002 §5). The PolicyRecord evaluation **SHALL** have access to, at minimum, the following `required_context_keys`: `principal.id`, `principal.class`, `principal.role_binding`, `principal.scope_binding`, `route.class`. If any required context is missing or invalid, the PolicyEngine **SHALL** deny execution per its fail-closed posture.

### §5. Relationship to Existing Governance

**Feedback:** Table is comprehensive but lacks specific implementation guidance. "Implementation impact" column is descriptive rather than prescriptive.

**Scores:** Cross-Document Consistency: 4, Developer Synchrony: 2

**Recommendation:** Add specific integration requirements for each referenced document.

### §8. Minimum Conformance Examples

**Feedback:** Examples are informative but not normative. JSON schemas lack validation rules and don't reference existing schemas.

**Scores:** Developer Synchrony: 2, Practical Operability: 2

**Recommendation:** Make examples normative or reference them from normative sections. Add schema validation rules.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §4.4 | Permissive route class definition | Define specific permitted route classes referencing existing authority structures | Critical | 3, 7, 9 |
| 2 | §4.6 | Parallel validation path conflicts with PolicyRecord | Integrate validation with PolicyRecord evaluation chain | Critical | 4, 6, 7 |
| 3 | §4 | Missing enforcement mechanisms | Add enforcement subsection with specific failure modes and remediation | Critical | 3, 5, 7 |
| 4 | §3 | New concepts lack integration points | Add references to PolicyRecord context keys and shell routing | High | 1, 9 |
| 5 | §8 | Examples are informative not normative | Make examples normative or reference from normative sections | High | 7, 9 |
| 6 | §4.13 | Lifecycle lacks concrete states | Define specific lifecycle states and transitions | Medium | 5, 7 |
| 7 | Document | No migration guidance | Add section on migrating existing systems to compliance | Medium | 7, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** Multiple dimensions score below 3, including critical failure in Practical Operability (1) and significant gaps in Legal Enforceability (2) and Completeness (2). The amendment establishes sound doctrine but lacks operational specificity.

**Top 3 Actions Required:**
1. Integrate validation with PolicyRecord evaluation chain rather than creating parallel path
2. Define specific enforcement mechanisms and failure modes for all SHALL statements
3. Make conformance examples normative with proper schema validation rules
---
review_id: REV-AMD-2026-016-002
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.2.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.6
---

# Peer Review: Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Uses canonical terminology correctly and properly references existing governance instruments, though some integration points with AIOS-SPEC-009 Actor schema could be more explicit. |
| 2 | Business Model Alignment | 4 | Supports marketplace model by creating clear governance for service accounts and applications without creating vendor barriers, though Kit implications could be clearer. |
| 3 | Legal Enforceability | 4 | Contains specific SHALL statements with clear enforcement mechanisms and failure modes, though some liability edge cases remain unaddressed. |
| 4 | Architectural Fidelity | 4 | Aligns well with policy supremacy and separation of powers, correctly treating non-human actors as governed subjects rather than trusted infrastructure. |
| 5 | Completeness | 4 | Addresses all major lifecycle aspects and provides concrete examples, though some edge cases around principal migration and emergency revocation need clarification. |
| 6 | Conflict Freedom | 4 | No direct contradictions found and explicitly respects existing document boundaries, though potential tension with shell authority delegation needs minor clarification. |
| 7 | Practical Operability | 3 | Provides concrete examples and schemas but lacks specific implementation guidance for principal registry and route class validation mechanisms. |
| 8 | Style & Clarity | 4 | Generally follows style guide with clear structure, though some definitions in §3 are dense and could benefit from simplification. |
| 9 | Developer Synchrony | 3 | Includes useful JSON examples and conformance probes but lacks CLI integration examples and specific API guidance for principal management. |
| 10 | Platform Economics Synchrony | 3 | Addresses economic attribution correctly but doesn't specify how metered usage by non-human principals affects billing thresholds or cost controls. |
| 11 | Friction Factor | 3 | Introduces necessary governance overhead that is proportional to risk, though the validation sequence in §4.6 could create performance bottlenecks without optimization guidance. |
| | **Composite Score** | **3.6** | |

---

## Overall Assessment

### Strengths

This revision successfully addresses the major gaps identified in Round 1 reviews. The document now provides:

1. **Complete Lifecycle Management (§4.13):** The amendment now defines creation, credentialing, suspension, revocation, and decommissioning processes, filling a critical gap from the previous version.

2. **Concrete Implementation Examples (§8):** The JSON examples for principal registry records, policy context, and action envelopes provide developers with actionable guidance for implementation.

3. **Clear Liability Attribution (§4.11, §4.14):** Default attribution rules resolve the legal enforceability concerns by explicitly defining ownership and liability for each principal class.

4. **Robust Validation Framework (§4.6):** The six-step validation sequence provides a clear admission control mechanism that prevents under-governed principals from exercising authority.

5. **Conformance Requirements (§4.15, §9):** The minimum conformance record requirements and conformance probes provide measurable compliance criteria.

### Critical Gaps

Despite significant improvements, several areas need refinement:

1. **Implementation Mechanism Gaps:** While the document defines what must be validated, it doesn't specify how principal registries should be implemented or how route class validation should occur in practice.

2. **Performance Considerations:** The six-step validation sequence in §4.6 could create latency issues for high-frequency service account operations without caching or optimization guidance.

3. **Emergency Procedures:** The document lacks guidance for emergency revocation scenarios or what happens when a principal registry becomes unavailable.

---

## Article-by-Article Review

### Section 3: Definitions

**Feedback:** The definitions are comprehensive and legally precise, but some are quite dense. The definition of "scope binding" is particularly complex and could benefit from simplification or examples.

**Scores:** Legal Enforceability: 4, Style & Clarity: 3

**Recommendation:** Simplify the scope binding definition and add a brief example. Replace the current definition with: "**Scope binding** means the governed boundary within which a principal's authority is valid, expressed through documented scope dimensions such as tenant scope, session scope, and resource scope. Example: a service account bound to tenant 'acme-corp' with resource scope 'documents/finance/*'."

### Section 4.6: Validation and admission rule

**Feedback:** The six-step validation sequence is architecturally sound but could create performance bottlenecks for high-frequency operations. The document should acknowledge this and provide guidance.

**Scores:** Practical Operability: 3, Architectural Fidelity: 4

**Recommendation:** Add a performance note: "Implementations MAY optimize this validation sequence through caching, pre-computed validation tokens, or batched evaluation, provided the logical validation requirements are preserved and audit trails remain complete."

### Section 4.7: Service-account rule

**Feedback:** This section is well-structured and provides clear requirements for service account registration. However, it doesn't specify what happens if the principal registry is unavailable during validation.

**Scores:** Completeness: 3, Practical Operability: 3

**Recommendation:** Add a failure mode clause: "If the principal registry is unavailable during validation, the system SHALL deny authority-bearing action and MAY provide a degraded read-only mode for non-authority-bearing operations, subject to policy configuration."

### Section 4.11: Ownership and mutation boundary

**Feedback:** The default attribution rules are clear and legally sound. However, the interaction with existing tenant agreements could be clearer.

**Scores:** Legal Enforceability: 4, Conflict Freedom: 4

**Recommendation:** Add clarification: "These default rules apply in the absence of more specific agreements. Tenant agreements or PolicyRecords MAY override these defaults for specific transaction types, provided such overrides are explicitly documented and auditable."

### Section 8: Minimum conformance examples

**Feedback:** The JSON examples are helpful and provide concrete implementation guidance. However, they could benefit from additional context about how these records are maintained and validated.

**Scores:** Developer Synchrony: 4, Practical Operability: 3

**Recommendation:** Add a brief explanation before each example describing when and how it would be used in practice.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §3 | Scope binding definition is overly complex | Simplify definition and add concrete example | Medium | 8, 9 |
| 2 | §4.6 | Validation sequence could create performance bottlenecks | Add performance optimization guidance | High | 7, 11 |
| 3 | §4.7 | Missing failure mode for registry unavailability | Add registry unavailability handling clause | High | 5, 7 |
| 4 | §4.11 | Interaction with tenant agreements needs clarification | Clarify override precedence for tenant agreements | Medium | 3, 6 |
| 5 | §8 | Examples lack implementation context | Add explanatory context for each JSON example | Medium | 7, 9 |
| 6 | Document | Missing CLI integration examples | Add section showing how principals are managed via CLI | Low | 9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document successfully addresses the major gaps from Round 1 and provides a solid governance framework for non-human principals, but needs refinements in practical operability and performance considerations.

**Top 3 Actions Required:**
1. Add performance optimization guidance for the validation sequence in §4.6 to prevent bottlenecks in high-frequency operations
2. Define failure modes for principal registry unavailability in §4.7 to ensure system resilience
3. Simplify the scope binding definition in §3 and add concrete examples to improve clarity for implementers
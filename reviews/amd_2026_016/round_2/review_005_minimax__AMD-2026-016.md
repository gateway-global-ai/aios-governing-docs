<think>This is a peer review task for AMD-2026-016, a governance document about non-human principals in the AI OS system. Let me analyze this document following the grading rubric and produce a structured review.

The document under review is AMD-2026-016 version 0.2.0, a draft amendment about "Governed Non-Human Principals and Deterministic Routed Authority."

Let me understand the document:
- It defines how non-human actors (service accounts, agent principals, application principals) participate in AI OS authority
- It establishes rules for principal identity, role binding, scope binding, routed communication, and audit
- It has lifecycle management, liability attribution, and economic attribution rules

Now let me score each dimension according to the rubric:

1. **Cross-Document Consistency**: Need to check terminology consistency with existing documents like AIOS-SPEC-009 (Actor schema), AMD-2026-007, AMD-2026-012, AIOS-SPEC-002. The document does reference these appropriately. However, it introduces "principal class" which needs to align with "Actor" in SPEC-009.

2. **Business Model Alignment**: Does this support marketplace, vendor ecosystem, enterprise adoption? The document seems to support enterprise by creating clear governance for non-human actors. It could help vendors understand how their agents/apps are governed.

3. **Legal Enforceability**: Are rules specific enough? Many SHALL statements but lacks explicit consequence definitions in some areas. However, it does define deny-and-audit consequences.

4. **Architectural Fidelity**: Does it align with Technical Manifesto principles? Yes - policy supremacy, separation of powers, deterministic execution are respected.

5. **Completeness**: Does it cover everything promised? It covers definitions, lifecycle, validation, audit, liability, conformance. Missing some edge cases perhaps.
 
I'll evaluate the remaining dimensions systematically. The document appears to have minimal conflicts with existing governance documents, maintaining a clear separation from shell-state routing and domain intent lifecycle. Practical operability seems solid, with concrete examples for policy evaluation and authority-bearing action. Style and clarity are strong, with well-structured sections and defined terms. Developer synchronization looks promising, with JSON examples provided. Platform economics are addressed through economic attribution rules. The friction factor seems low, introducing necessary governance without significant barriers.</think>

```
review_id: REV-AMD-2026-016-001
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.2.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---
```

# Peer Review: AMD-2026-016 — Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Correctly references AMD-2026-007 §11.9, AMD-2026-012 §4.2 and §7, AIOS-SPEC-002, AIOS-SPEC-009; minor alignment needed with SPEC-009 Actor schema for principal_class field |
| 2 | Business Model Alignment | 4 | Supports enterprise and vendor ecosystem by creating clear, governable framework for service accounts, agents, and applications |
| 3 | Legal Enforceability | 4 | Specific SHALL statements with defined consequences; liability attribution rules in §4.14 are explicit |
| 4 | Architectural Fidelity | 5 | Aligns with policy supremacy, separation of powers, deterministic execution; correctly respects shell vs domain intent boundaries |
| 5 | Completeness | 4 | Covers lifecycle, validation, audit, liability, conformance; edge cases addressed in §4.6-4.15; minor gap in failure scenario examples |
| 6 | Conflict Freedom | 4 | No contradictions with referenced documents; correctly defers to existing shell-state and domain intent law |
| 7 | Practical Operability | 3 | Provides JSON examples in §8 but lacks step-by-step implementation guidance for validation sequence |
| 8 | Style & Clarity | 5 | Follows Style Guide precisely; clear structure with well-organized normative subsections |
| 9 | Developer Synchrony | 3 | Provides schema examples but lacks CLI references, conformance test guidance, or integration test patterns |
| 10 | Platform Economics Synchrony | 4 | Explicitly addresses economic attribution in §4.14; links to FDA and metering concepts correctly |
| 11 | Friction Factor | 4 | Governance additions are proportional to risk; lifecycle requirements are necessary, not bureaucratic |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

This amendment successfully addresses a critical governance gap in the AI OS framework. Its primary strengths are:

1. **Conceptual Clarity (§3, §4)**: The definitions of service accounts, agent principals, and application principals are precise and well-differentiated. The separation into distinct principal classes prevents the "undifferentiated power source" problem identified in Round 1.

2. **Comprehensive Normative Framework (§4)**: The 15 normative subsections provide a complete governance framework covering role binding, scope binding, routed communication, validation, lifecycle, liability, and conformance. This directly addresses the Round 1 criticism about missing lifecycle management and enforcement mechanisms.

3. **Architectural Integration**: The document correctly respects existing authority boundaries—AMD-2026-007 §11.9 for shell-state routing and AIOS-SPEC-009 for domain intent lifecycle. It augments rather than contradicts these instruments.

4. **Practical Examples (§8)**: The JSON examples for principal registry records, policy-evaluable context, and authority-bearing action envelopes provide implementable reference material.

5. **Liability Attribution (§4.14)**: The explicit default attribution rules for service, agent, and application principals resolve the Round 1 gap around legal ownership.

### Critical Gaps

While substantially improved from Round 1, the document still hasoperability and developer-synchrony gaps:

1. **Validation Sequence Implementation**: §4.6 defines a 6-step validation sequence but doesn't provide guidance on how to implement this in practice—whether as a single control-plane stage or distributed checks.

2. **Conformance Testing**: §4.15 requires conformance records but doesn't specify how implementations demonstrate compliance or what test patterns validate conformance.

3. **Failure Scenario Documentation**: While §4.12 defines deny-and-audit consequences, concrete failure scenarios (what happens when each validation step fails) are referenced but not fully illustrated.

---

## Article-by-Article Review

### §0. Status

**Feedback:** The status section correctly identifies this as a narrow authority amendment and notes the scope boundaries. The version is properly incremented to 0.2.0.

**Scores:** Completeness: 4

**Recommendation:** No changes needed.

---

### §1. Purpose

**Feedback:** The problem statement is clear and well-framed. The formulation "authority drifts into hidden infrastructure" directly addresses the governance gap. The solution statement correctly captures the five pillars (identity, role binding, scope, routing, audit).

**Scores:** Style & Clarity: 5, Architectural Fidelity: 5

**Recommendation:** No changes needed.

---

### §2. Scope

**Feedback:** The in-scope/out-of-scope boundary is well-drawn. Importantly, this amendment correctly excludes shell-state routing (AMD-2026-007 §11.9) and domain intent lifecycle (AIOS-SPEC-009) from its scope, preventing authority conflict.

**Scores:** Completeness: 4, Conflict Freedom: 5

**Recommendation:** No changes needed.

---

### §3. Definitions

**Feedback:** Definitions are comprehensive and precise. Key additions from Round 1 include "route class," "authority-bearing action," "principal registry," and "conformance record." The definitions of "scope binding" now include explicit dimension requirements (tenant, session, resource/route).

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 5

**Recommendation:** Minor addition—add a cross-reference to where permission families and scope classes are registered (AIOS-POLICY-INDEX) for implementers.

---

### §4. Normative Decisions (Subsections 4.1-4.15)

**Feedback:** This is the substantive core. The 15 subsections provide comprehensive governance:

- **§4.1-4.3 (Foundation)**: Establish the governed principle, no-ambient-authority rule, and binding requirements. Sound foundation.
- **§4.4 (Routed Communication)**: Now includes documented route classes with specific examples—shell intent routes, control-plane calls, policy-evaluated service interfaces. This addresses Round 1's ambiguity about "approved surfaces."
- **§4.5 (Action-Carriage Fields)**: The minimum 10 audit fields are well-specified. The joinable records provision is pragmatic.
- **§4.6 (Validation Sequence)**: The 6-step sequence is clear but lacks implementation guidance.
- **§4.7-4.9 (Principal Class Rules)**: Well-differentiated rules for service, agent, and application principals. The registry requirement in §4.7 is a critical improvement.
- **§4.10 (Non-Substitution)**: The five-class separation is clear and prevents class collision.
- **§4.11 (Ownership Boundary)**: Default attribution rules are explicit—directly addresses Round 1's legal gap.
- **§4.12 (Audit/Policy Consequence)**: Fail-closed, deny-and-audit posture is clear.
- **§4.13 (Lifecycle)**: Lifecycle rules for registration, credentialing, suspension, revocation, and decommissioning directly address Round 1's completeness gap.
- **§4.14 (Liability/Economic Attribution)**: Explicit liability attribution linked to economic subjects—addresses Round 1's economics gap.
- **§4.15 (Conformance Records)**: Minimum conformance record requirements are specified.

**Scores:** Legal Enforceability: 4, Architectural Fidelity: 5, Completeness: 4, Practical Operability: 3

**Recommendation:** Add an informative subsection showing the validation sequence as a decision flow or pseudocode:

> **Informative: Validation Sequence Flow**
> ```
> 1. Receive authority-bearing action request
> 2. Validate principal identity exists in registry → if fail, deny + audit
> 3. Determine principal class → if indeterminate, deny + audit
> 4. Validate role binding exists and is active → if fail, deny + audit
> 5. Validate scope binding permits action → if fail, deny + audit
> 6. Validate route class is permitted → if fail, deny + audit
> 7. Evaluate PolicyRecord → if deny, deny + audit
> 8. Execute action with audit correlation
> ```

---

### §5. Relationship to Existing Governance

**Feedback:** The cross-reference table is accurate and complete. It correctly identifies the implementation impact for each governing instrument. The relationship descriptions are precise.

**Scores:** Cross-Document Consistency: 5, Conflict Freedom: 4

**Recommendation:** No changes needed.

---

### §6. Cross-Document Impact

**Feedback:** The follow-up requirements table is helpful for governance maintenance. It identifies the necessary spec updates without creating obligations.

**Scores:** Completeness: 4

**Recommendation:** No changes needed.

---

### §7. Non-Goals

**Feedback:** The non-goals prevent scope creep and clarify the amendment's boundaries. The explicit exclusion of vendor-specific models is important.

**Scores:** Architectural Fidelity: 4

**Recommendation:** No changes needed.

---

### §8. Minimum Conformance Examples

**Feedback:** The JSON examples in §8.1-8.3 are well-constructed and provide implementable reference material. They correctly use the concepts defined earlier (principal_class, role_bindings, scope_bindings, route_class).

**Scores:** Developer Synchrony: 3, Practical Operability: 3

**Recommendation:** Add one more example showing a validation failure scenario—how the deny-and-audit consequence manifests in the audit record:

> **§8.4 Validation Failure Example (Informative)**
> ```json
> {
>   "principal_id": "svc.shell.voice-router",
>   "principal_class": "service_account",
>   "validation_stage": "scope_binding",
>   "failure_reason": "scope_binding.action_family 'document_write' not in permitted scope",
>   "consequence": "denied",
>   "audit_correlation_id": "aud-20260410-002",
>   "policy_record_ref": "POL-SCOPE-001"
> }
> ```

---

### §9. Conformance Probes

**Feedback:** The five conformance probes provide testable cases. They cover success, scope exceedance, under-governed action, revocation, and economic attribution.

**Scores:** Practical Operability: 3

**Recommendation:** No changes needed, but note that these probes would benefit from automation guidance in a future implementation note.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §4.6 | Validation sequence lacks implementation flow | Add decision flow or pseudocode showing 6-step validation | Medium | 7, 9 |
| 2 | §8 | Missing validation failure example | Add §8.4 example showing deny-and-audit audit record | Medium | 7, 9 |
| 3 | §3 | Permission families reference location unclear | Add cross-reference to AIOS-POLICY-INDEX for registered permission families and scope classes | Low | 1, 9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document has substantially improved from Round 1 (composite rose from 2.9 to 3.8). No dimensions score below 3. The key improvements—lifecycle management, validation sequence, liability attribution, and conformance records—directly addressed Round 1's critical gaps. Remaining gaps (implementation flow guidance, failure scenarios) are informatively addressable without normative changes. The document is ready for ratification consideration with the recommended informative additions.

**Top 3 Actions Required:**
1. Add validation sequence decision flow as informative content (improves Practical Operability and Developer Synchrony)
2. Add validation failure example in §8 (demonstrates deny-and-audit consequence in practice)
3. Consider adding AIOS-POLICY-INDEX cross-reference for permission families registration location (improves Developer Synchrony)
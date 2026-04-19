---
review_id: REV-AMD-2026-016-001
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.1.0
reviewer: Claude
review_date: 2026-04-10
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 2.5
---

# Peer Review: Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Uses canonical terms correctly but lacks specific cross-references to existing authority structures in AMD-2026-012 and AIOS-SPEC-009. |
| 2 | Business Model Alignment | 4 | Supports marketplace model by governing non-human actors without creating vendor barriers, though could be clearer on Kit implications. |
| 3 | Legal Enforceability | 2 | Contains many SHALL statements but lacks specific enforcement mechanisms, failure modes, and remediation procedures. |
| 4 | Architectural Fidelity | 3 | Generally aligns with policy supremacy and separation of powers but doesn't clearly map to existing control plane structures. |
| 5 | Completeness | 2 | Missing critical sections on implementation requirements, failure modes, migration from existing systems, and concrete examples. |
| 6 | Conflict Freedom | 3 | No direct contradictions found but creates potential tension with existing shell authority without explicit reconciliation. |
| 7 | Practical Operability | 1 | Rules are aspirational without actionable implementation guidance, specific thresholds, or step-by-step processes. |
| 8 | Style & Clarity | 4 | Generally follows style guide with clear structure and appropriate voice, minor formatting inconsistencies. |
| 9 | Developer Synchrony | 2 | Lacks schemas, CLI references, or concrete implementation guidance that developers would need to build compliant systems. |
| 10 | Platform Economics Synchrony | 3 | Doesn't contradict economic model but fails to address cost implications of audit requirements and routing overhead. |
| 11 | Friction Factor | 2 | Introduces significant new compliance burden without clear risk justification or graduated implementation path. |
| | **Composite Score** | **2.5** | |

---

## Overall Assessment

### Strengths

This amendment addresses a genuine governance gap by establishing explicit authority rules for non-human actors in AI OS. The core insight that non-human principals should not operate with ambient authority is architecturally sound and aligns with the policy supremacy principle from the Technical Manifesto. The document correctly identifies that service accounts, agent principals, and application principals need distinct governance rather than being treated as undifferentiated infrastructure.

### Critical Gaps

The document is primarily aspirational rather than operational. It lacks concrete implementation requirements, enforcement mechanisms, failure mode definitions, and migration guidance. The audit requirements in §4.5 are extensive but provide no guidance on implementation cost or performance impact. There are no schemas, no CLI integration, and no specific thresholds that would allow a developer to build a compliant system.

---

## Article-by-Article Review

### Section 1: Purpose

**Feedback:** Clearly articulates the problem and need. The framing of "authority drifts into hidden infrastructure" is compelling and aligns with architectural principles.

**Scores:** Style & Clarity: 5, Architectural Fidelity: 4

**Recommendation:** No changes needed for this section.

### Section 3: Definitions

**Feedback:** Definitions are comprehensive but some are circular. "Deterministic non-human action" definition is particularly unclear about what constitutes "pre-bound permissions" in practice.

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Add concrete examples for each principal type and define "pre-bound permissions" with reference to PolicyRecord or similar existing mechanisms.

### Section 4: Normative Decisions

**Feedback:** Contains the core governance rules but lacks enforcement mechanisms. §4.5 requires nine audit fields but provides no guidance on implementation, storage, or performance implications.

**Scores:** Legal Enforceability: 2, Practical Operability: 1, Completeness: 2

**Recommendation:** Add subsections defining:
- Specific enforcement mechanisms for each SHALL statement
- Failure modes and remediation procedures  
- Implementation requirements with reference to existing control plane structures
- Performance and cost considerations for audit requirements

### Section 4.4: Routed Communication Rule

**Feedback:** The prohibition on "hidden backdoors" is important but vague. What constitutes an "approved routed surface" needs concrete definition.

**Scores:** Legal Enforceability: 2, Developer Synchrony: 2

**Recommendation:** Replace "Approved routed surfaces MAY include" with "Approved routed surfaces SHALL be limited to" and provide specific technical criteria for approval, referencing existing shell authority from AMD-2026-012.

### Section 5: Relationship to Existing Governance

**Feedback:** Good attempt to position the amendment but lacks specific integration points. The relationship to AIOS-SPEC-002 PolicyRecord is mentioned but not operationalized.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 3

**Recommendation:** Add specific references to how non-human principals integrate with existing PolicyRecord evaluation, shell outcome families from AMD-2026-012 §7, and intent execution from AIOS-SPEC-009.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §4 | Missing enforcement mechanisms | Add enforcement subsection with specific failure modes and remediation | Critical | 3, 5, 7 |
| 2 | §4.5 | Audit requirements lack implementation guidance | Define audit storage, performance impact, and cost considerations | Critical | 7, 9, 10 |
| 3 | §3 | Circular definitions | Add concrete examples and reference existing PolicyRecord mechanisms | High | 3, 7, 9 |
| 4 | §4.4 | Vague routing approval criteria | Define specific technical criteria for approved routes | High | 3, 7, 9 |
| 5 | §5 | Missing integration specifications | Add specific PolicyRecord and shell authority integration points | High | 1, 6, 9 |
| 6 | Document | No schemas or CLI guidance | Add implementation schemas and CLI integration examples | Medium | 9 |
| 7 | Document | No migration guidance | Add section on migrating existing systems to compliance | Medium | 7, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** Multiple dimensions score below 3, including critical failures in Practical Operability (1) and significant gaps in Legal Enforceability (2) and Completeness (2).

**Top 3 Actions Required:**
1. Add concrete enforcement mechanisms and failure mode definitions for all SHALL statements
2. Provide implementation guidance for audit requirements including cost and performance considerations  
3. Define specific integration points with existing PolicyRecord, shell authority, and intent execution systems
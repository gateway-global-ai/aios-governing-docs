---
review_id: REV-AMD-2026-016-001
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.1.0
reviewer: MiniMax
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: approved_with_changes
composite_score: 3.4
---

# Peer Review: AMD-2026-016 — Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Terminology references existing AMDs correctly; minor glossary alignment needed for "deterministic non-human action" |
| 2 | Business Model Alignment | 4 | Indirectly supports marketplace by preventing ambient authority, but doesn't address vendor ecosystem directly |
| 3 | Legal Enforceability | 3 | Binding "SHALL" language used, but consequence framework for violations is incomplete |
| 4 | Architectural Fidelity | 5 | Aligns with shell authority (AMD-2026-012), PolicyRecord (AIOS-SPEC-002), and intent primitive (AIOS-SPEC-009) |
| 5 | Completeness | 3 | Core principals defined, but missing concrete examples and edge case handling |
| 6 | Conflict Freedom | 4 | No contradictions with referenced documents; scope boundaries are clear |
| 7 | Practical Operability | 2 | Document is too abstract; developers need implementation pathways |
| 8 | Style & Clarity | 4 | Follows Style Guide; clear section structure but §4 has 11 sub-rules causing cognitive load |
| 9 | Developer Synchrony | 2 | Definitions provided without actionable schemas, CLI examples, or implementation guidance |
| 10 | Platform Economics Synchrony | 3 | Silent on economic implications of service account usage; could affect billing models |
| 11 | Friction Factor | 3 | Additional governance steps are proportional but could be burdensome without tooling |
| | **Composite Score** | **3.4** | |

---

## Overall Assessment

### Strengths

This amendment correctly identifies the governance gap where non-human principals (service accounts, agents, applications) operate without explicit authority boundaries. The core principles in §4.1–§4.3 establish a sound doctrine: non-human principals require explicit role binding, explicit scope, and routed communication. The document integrates well with existing shell authority (AMD-2026-012) and the PolicyRecord framework (AIOS-SPEC-002), creating a layered authority model. The explicit prohibition of ambient authority (§4.2) and the ownership/mutation boundary (§4.10) are particularly valuable additions to the governance set.

### Critical Gaps

The most significant issue is **Practical Operability**: the document provides doctrine without a path for developers to implement it. There are no JSON schema examples for non-human principal declarations, no CLI reference examples, and no implementation guidance for how role binding and scope binding should be expressed in code. Additionally, §4.5 defines required action-carriage fields but doesn't provide a conformance validation method. The document also lacks concrete failure scenarios—what happens when a service account exceeds its bound scope, and what the audit consequence looks like in practice.

---

## Article-by-Article Review

### §0. Status

**Feedback:** The status section correctly identifies this as a "narrow authority amendment" which sets appropriate expectations. However, the "ratification_target" field is null, which may need to be populated before Round 2.

**Scores:** Clarity: 4

**Recommendation:** No change needed for Round 1.

---

### §1. Purpose

**Feedback:** The problem statement is clear and well-framed. It correctly identifies that AI OS depends on non-human actors that can observe, route, invoke, and mutate—making governance essential. The solution (explicit role binding, scope, routing, audit) is logically sound.

**Scores:** Clarity: 5, Architectural Fidelity: 5

**Recommendation:** No change needed.

---

### §2. Scope

**Feedback:** The in-scope/out-of-scope boundary is well-drawn. Notably, this amendment correctly avoids overreaching into UI design or replacing PolicyRecord, instead complementing those documents.

**Scores:** Completeness: 4

**Recommendation:** No change needed.

---

### §3. Definitions

**Feedback:** Core definitions are clear: non-human principal, service account, agent principal, application principal. However, "deterministic non-human action" appears only in definitions without a formal schema or example. The key gap is that role binding and scope binding are defined but not illustrated in practice.

The definitions rely on terms like "permission families" and "scope classes" without pointing to where those are formally registered (presumably AIOS-POLICY-INDEX).

**Scores:** Cross-Document Consistency: 4, Completeness: 3

**Recommendation:** Add a reference to where permission families and scope classes are registered (e.g., AIOS-POLICY-INDEX). Add an example showing how a service account declaration would look in practice.

---

### §4. Normative Decisions (Sub-sections 4.1–4.11)

**Feedback:** This is the substantive core with 11 separate rules. The structure is clear but creates cognitive load because each "rule" reads as a mini-policy. Key observations:

**§4.1–§4.3 (Governed principal, No ambient authority, Role-binding/scope):** These are the foundation and well-stated. The three-way requirement (principal + role + scope) is sound.

**§4.4 (Routed communication):** Approved surfaces are listed but the document doesn't specify who certifies a surface as "approved routed." This could create ambiguity.

**§4.5 (Required action-carriage fields):** This is the audit requirement. It's well-specified but lacks a conformance test or schema.

**§4.6–§4.8 (Service/Agent/Application rules):** The separation is clear. The agent-principal rule (§4.7) is particularly important as it prevents "undifferentiated power source" drift.

**§4.9 (Non-substitution):** This is a critical anti-drift rule. The five-class separation (human, group, service, agent, application) should be registered in AIOS-POLICY-INDEX.

**§4.10 (Ownership/mutation boundary):** This is valuable but needs more specificity—what does "the system SHALL define" mean operationally?

**§4.11 (Audit/policy consequence):** Links to default-deny/post-evaluated posture correctly but needs failure scenario examples.

**Scores:** Legal Enforceability: 3, Practical Operability: 2, Completeness: 3

**Recommendation:** 
1. Add an appendix or expanded section showing concrete examples of each principal class with sample role binding and scope declarations.
2. Clarify who certifies surfaces as "approved routed" — this could reference an AIOS-SPEC or policy index entry.
3. Add a failure scenario example: what happens when a service account exceeds scope (deny, audit log, notification).

---

### §5. Relationship to Existing Governance

**Feedback:** This cross-reference table is valuable and correctly maps the amendment to existing instruments. The relationship descriptions are accurate.

**Scores:** Cross-Document Consistency: 5

**Recommendation:** No change needed.

---

### §6. Immediate Shell-Program Implications

**Feedback:** This section is important—it tells readers how this amendment connects to planning artifacts. The phrasing "SHOULD cite this amendment" is appropriate as it doesn't create a mandatory requirement.

**Scores:** Clarity: 4

**Recommendation:** No change needed.

---

### §7. Non-Goals

**Feedback:** The non-goals are well-considered and prevent scope creep. Particularly good is "Treating service accounts as a Kubernetes-specific borrowing exercise" — this anchors the amendment as general governance law.

**Scores:** Completeness: 4

**Recommendation:** No change needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §3 Definitions | "deterministic non-human action" lacks example; permission families reference missing | Add reference to AIOS-POLICY-INDEX and brief example | Medium | 1, 9 |
| 2 | §4.4 Routed communication | Who certifies surfaces as "approved routed" is ambiguous | Add note stating certification authority or reference to spec | Medium | 7 |
| 3 | §4.5 Action-carriage fields | No conformance validation method defined | Add statement describing how validation occurs (e.g., "DCP validates" or "PolicyRecord schema includes") | High | 3, 7 |
| 4 | §4.10 Ownership boundary | "system SHALL define" is vague operationally | Add example: artifact ownership metadata schema | High | 7, 9 |
| 5 | General | Document lacks concrete examples throughout | Add an appendix with principal declaration examples for each class (service, agent, application) | High | 7, 9 |
| 6 | §4.11 | Failure scenarios not illustrated | Add failure scenario: service account exceeds scope | Medium | 3, 7 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document establishes sound doctrine for governing non-human principals and integrates well with existing governance instruments. However, the Practical Operability (score 2) and Developer Synchrony (score 2) scores pull the composite below 4.0. The amendment needs concrete examples, implementation guidance, and clarity on certification authorities before it can serve as fully actionable law.

**Top 3 Actions Required:**
1. Add concrete principal declaration examples (service account, agent principal, application principal) showing role binding and scope in practice
2. Clarify who certifies surfaces as "approved routed" in §4.4 — add a reference or define certification authority
3. Expand §4.11 with at least one concrete failure scenario (service account exceeds scope) to illustrate the audit/policy consequence
---
review_id: REV-AMD-2026-009-ADD-001-001
document_reviewed: AMD-2026-009-ADD-001
document_version: 1.0.1
reviewer: DeepSeek R3
review_date: 2026-04-08
review_round: 1
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: AMD-2026-009-ADD-001 — Retrieval backend neutrality

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with parent AMD-2026-009 and SPEC-010, but §2.1 informative examples create potential ambiguity about governance boundaries. |
| 2 | Business Model Alignment | 4 | Correctly addresses operational constraints of PSE while maintaining vendor-neutral posture, though commercial terms for alternative backends need clearer policy hooks. |
| 3 | Legal Enforceability | 3 | Lacks specific liability allocation for backend failures and doesn't define ToS compliance verification mechanisms for registered backends. |
| 4 | Architectural Fidelity | 5 | Perfectly implements the separation of concerns: policy registration, logical resource keys, and SPEC-010 integration without weakening parent amendment's architectural guarantees. |
| 5 | Completeness | 4 | Covers core requirements but omits implementation schema for policy registration and audit format standardization across heterogeneous backends. |
| 6 | Conflict Freedom | 5 | No contradictions with parent amendment or other governing documents; properly scoped as implementation detail expansion. |
| 7 | Practical Operability | 3 | Missing concrete JSON schema for backend registration and lacks failure mode definitions for backend-specific errors. |
| 8 | Style & Clarity | 4 | Follows Style Guide conventions with precise terminology, though §2.1 table mixes normative and informative content confusingly. |
| 9 | Developer Synchrony | 4 | Provides clear integration points for MCP and product teams, but needs explicit versioning strategy for backend API changes. |
| 10 | Platform Economics Synchrony | 4 | Acknowledges cost implications but doesn't define how different backends map to token policy tiers or SLA differentials. |
| 11 | Friction Factor | 4 | Low implementation friction for existing deployments, though backend validation requirements could increase operator overhead. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

1. **Architectural purity**: The addendum correctly maintains AMD-2026-009's core governance model while expanding implementation flexibility. The SPEC-010 logical key pattern (`web:retrieval:{backend_id}:...`) in §3 is technically elegant and preserves envelope-based execution boundaries.

2. **Clear scope boundaries**: §5 "Non-goals" effectively prevents scope creep and ensures the addendum doesn't weaken parent amendment's safety guarantees against unbounded browsing.

3. **Operational realism**: §1 accurately identifies the PSE configuration limitations that motivate this addendum, grounding the technical change in real deployment constraints.

### Critical Gaps

1. **Missing policy registration schema**: §2 requires backend registration but provides no normative JSON schema or validation rules, leaving implementations to invent incompatible formats.

2. **Inadequate failure mode definitions**: No specification of how different backend failure types (quota exceeded, API deprecation, ToS violation) should be handled in the control plane or audit trail.

3. **Ambiguous commercial terms handling**: §2.1's "informative only" examples create confusion about governance requirements for third-party API compliance verification.

---

## Article-by-Article Review

### §0. Status and intent

**Feedback:** Clear framing that this is an implementation detail expansion, not a replacement of parent governance. The "Does not replace" table effectively prevents misinterpretation.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 5

**Recommendation:** Add explicit version dependency: "This addendum requires AMD-2026-009 version ≥ 0.1.6."

### §1. Problem statement (operational)

**Feedback:** Accurately captures the PSE configuration limitations. However, it misses the broader architectural principle: retrieval backend as a pluggable component in the governed execution pipeline.

**Scores:** Practical Operability: 4, Architectural Fidelity: 4

**Recommendation:** Add architectural rationale: "This enables retrieval backend as a stateless, policy-governed component that can be swapped without affecting the deterministic execution guarantees of the parent amendment."

### §2. Normative effect

**Feedback:** §2 correctly establishes policy registration as the control mechanism. However, the requirements for backend registration lack specificity. What constitutes a "citable result list"? What validation must the policy engine perform?

**Scores:** Legal Enforceability: 3, Practical Operability: 3

**Recommendation:** Add normative requirements for backend registration:
```
2.1.1 Backend registration SHALL include:
  - `backend_id`: string (regex: `[a-z0-9_]+`)
  - `api_endpoint`: URL template with {query} placeholder
  - `result_schema`: JSON Schema defining required fields (title, snippet, url, source_domain)
  - `auth_method`: enum (api_key, oauth2, none)
  - `quota_class`: mapping to POL-WEB token tiers
  - `tos_compliance_url`: required URL to current terms
```

### §2.1 Privacy-first and independent index providers

**Feedback:** This section dangerously mixes normative requirements ("MUST NOT treat HTML scraping...") with informative examples. The DuckDuckGo caveats are important but belong in operator documentation, not a normative addendum.

**Scores:** Style & Clarity: 2, Legal Enforceability: 2

**Recommendation:** Move the entire table to an informative appendix or WORKSPACE.md. Replace with normative requirement: "Alternative backends SHALL provide documented, stable HTTP/REST APIs with versioned contracts. Scraping-based implementations SHALL NOT be registered without explicit Council risk acceptance recorded in policy."

### §3. SPEC-010 logical keys

**Feedback:** Technically perfect. The `web:retrieval:{backend_id}:{query_fingerprint}` pattern cleanly extends the parent amendment's logical resource model without breaking existing implementations.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5

**Recommendation:** Add validation rule: "The `backend_id` component SHALL match a registered backend in the active policy version at envelope validation time."

### §4. Deltas to sibling artifacts

**Feedback:** Useful checklist but lacks specificity about what changes are required. "Optional wording tweaks" is too vague for a governing document.

**Scores:** Practical Operability: 3, Completeness: 3

**Recommendation:** For each artifact, specify exact text changes:
- AMD-2026-009 §1.3: "Add 'See AMD-2026-009-ADD-001 for policy-registered alternative backends.'"
- AIOS-SPEC-007 §3: "Replace 'PSE credentials' with 'retrieval backend credentials' and add 'as registered in POL-WEB-RETRIEVAL-BACKEND-001'"

### §5. Non-goals

**Feedback:** Excellent boundary definition. Prevents misinterpretation that this addendum authorizes prompt-only access or weakens safety guarantees.

**Scores:** Conflict Freedom: 5, Architectural Fidelity: 5

**Recommendation:** No changes needed.

### §6. Ratification checklist

**Feedback:** Missing critical implementation dependency: product capability registry updates to support backend-specific skill bindings.

**Scores:** Completeness: 3, Practical Operability: 3

**Recommendation:** Add checklist item: "Update product capability registry to accept `backend_id` parameter in `web.*` skill definitions and route to appropriate MCP adapter."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §2 | Missing backend registration schema | Add normative JSON Schema with required fields (backend_id, api_endpoint, result_schema, auth_method, quota_class, tos_compliance_url) | Critical | 3, 5, 7 |
| 2 | §2.1 | Normative/informative confusion | Move provider examples table to appendix; replace with clear "SHALL provide documented stable API" requirement | High | 2, 8 |
| 3 | §4 | Vague delta specifications | Specify exact text changes for each sibling artifact with before/after examples | Medium | 5, 7 |
| 4 | §6 | Missing implementation dependency | Add checklist item for product capability registry updates to support backend_id parameter | Medium | 5, 9 |
| 5 | §1 | Missing architectural rationale | Add sentence explaining backend as pluggable stateless component in governed pipeline | Low | 4, 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The addendum correctly extends parent amendment architecture with necessary implementation flexibility, but requires normative schema definitions and clearer separation of informative examples from requirements before ratification.

**Top 3 Actions Required:**
1. Add normative JSON Schema for backend registration in §2 with validation rules
2. Move §2.1 provider examples to informative appendix and clarify API stability requirements
3. Specify exact text deltas for sibling artifacts in §4 with before/after examples

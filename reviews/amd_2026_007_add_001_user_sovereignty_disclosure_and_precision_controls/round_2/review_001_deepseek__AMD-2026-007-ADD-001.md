---
review_id: REV-AMD-2026-007-ADD-001-002
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.2.0
reviewer: DeepSeek
review_date: 2026-04-17
review_round: 2
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: User Sovereignty Disclosure and Precision Controls

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Aligns with parent AMD-2026-007 but fails to properly reference AIOS-SPEC-009's execution model and PolicyRecord mechanisms for operationalizing thresholds. |
| 2 | Business Model Alignment | 4 | Supports enterprise trust model by providing transparency, but lacks clear boundaries for mandatory platform functions. |
| 3 | Legal Enforceability | 2 | Uses undefined qualifiers like "materially" and "where policy permits" without tying them to PolicyRecord thresholds, making enforcement ambiguous. |
| 4 | Architectural Fidelity | 3 | Extends shell disclosure duties but doesn't integrate with the governed execution model or specify how user preferences affect PolicyRecord evaluation. |
| 5 | Completeness | 2 | Missing critical operational details: no schemas for disclosure surfaces, no failure modes, no integration with capability registry or execution plans. |
| 6 | Conflict Freedom | 2 | Creates potential conflicts with AIOS-SPEC-009's audit requirements and deterministic execution model without clear resolution mechanisms. |
| 7 | Practical Operability | 2 | Requirements are too abstract for implementation; lacks concrete UI component references, data models, or integration points. |
| 8 | Style & Clarity | 4 | Follows Style Guide structure but uses inconsistent terminology between "shell disclosure surface" and "documented shell disclosure surface." |
| 9 | Developer Synchrony | 2 | No developer can implement from this document alone; missing schemas, event models, and references to UI component specifications. |
| 10 | Platform Economics Synchrony | 3 | Doesn't address how disabling logging affects usage-based billing or platform analytics, relying on undefined "policy" exceptions. |
| 11 | Friction Factor | 3 | Adds necessary transparency friction but implementation complexity is high without clear architectural integration. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- **Clear Principles:** Section 2 establishes a strong governing principle for user sovereignty that correctly identifies the failure mode of hidden platform state.
- **Good Categorization:** Section 3 provides a comprehensive list of disclosure classes that need transparency, aligning with the shell's disclosure duties in AMD-2026-007.
- **Architectural Extension:** The addendum correctly extends the shell's responsibilities without violating core architectural principles of separation of powers.

### Critical Gaps

1. **Lack of Technical Integration:** The document fails to specify how user sovereignty controls integrate with the governed execution model in AIOS-SPEC-009. There's no mention of how user preferences affect PolicyRecord evaluation or execution plan compilation.
2. **Undefined Technical Boundaries:** Terms like "materially" and "where policy permits" are not tied to PolicyRecord thresholds or capability registry states, making them unenforceable in the technical architecture.
3. **Missing Implementation Details:** No schemas for disclosure surfaces, no event models for state changes, no references to UI components in AIOS-SPEC-006, and no integration with the capability registry.

---

## Article-by-Article Review

### Section 0. Status and intent

**Feedback:** Clear purpose statement but lacks technical specificity about how this integrates with the execution model.

**Scores:** Style & Clarity: 4, Architectural Fidelity: 3

**Recommendation:** Add a technical integration statement: "This addendum extends shell disclosure requirements defined in AMD-2026-007 §11.6 and must be implemented in coordination with PolicyRecord evaluation and capability registry states per AIOS-SPEC-009."

### Section 2. Governing principle

**Feedback:** The principle is sound but uses "materially" without technical definition. In AIOS-SPEC-009, materiality is defined through PolicyRecord thresholds.

**Scores:** Legal Enforceability: 2, Architectural Fidelity: 2

**Recommendation:** Replace subjective definition with PolicyRecord reference: "For this addendum, a state materially affects behavior when its presence or absence would alter PolicyRecord evaluation, change resolved ExecutionPlan composition, or trigger disclosure requirements defined in the active tenant policy."

### Section 3. Required disclosure classes

**Feedback:** Good list but "documented shell disclosure surface" is vague. Should reference specific UI components in AIOS-SPEC-006.

**Scores:** Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Specify implementation: "The shell SHALL disclose these classes through components registered in AIOS-SPEC-006 (e.g., ShellIdentityBar, SessionSummaryPanel) with stable component IDs and data binding schemas."

### Section 4. Precision controls

**Feedback:** Critical architectural gap: doesn't specify how user logging preferences interact with mandatory audit requirements in AIOS-SPEC-009's deterministic execution model.

**Scores:** Conflict Freedom: 1, Architectural Fidelity: 2

**Recommendation:** Add technical integration: "User-configurable logging controls SHALL be implemented as PolicyRecord overrides that cannot disable audit fields required for execution traceability per AIOS-SPEC-009 §12.4. The system SHALL maintain separate audit and user-preference logging streams with clear metadata differentiation."

### Section 5. Behavioral and guardrail settings

**Feedback:** Missing technical implementation: how do these settings affect PolicyRecord evaluation? No reference to capability registry or execution plan compilation.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2

**Recommendation:** Add technical binding: "Behavioral settings SHALL be stored as user preference PolicyRecords that influence but do not override mandatory policy constraints. These preferences SHALL be available to the intent resolver during plan compilation per AIOS-SPEC-009 §15."

### Section 6. Inspectable signal use

**Feedback:** No technical specification for how signal families are defined, registered, or exposed. Should reference capability registry patterns.

**Scores:** Developer Synchrony: 1, Completeness: 2

**Recommendation:** Add registry requirement: "Signal families SHALL be registered in the capability registry with metadata including: signal_id, influence_domains, default_thresholds, and user_override_policy. The shell SHALL read from this registry to populate disclosure surfaces."

### Section 7. Conflict-of-interest disclosure

**Feedback:** Too abstract for technical implementation. Needs concrete examples tied to specific platform behaviors.

**Scores:** Practical Operability: 2, Legal Enforceability: 2

**Recommendation:** Provide technical examples: "Examples requiring disclosure include: retention policies that extend beyond session boundaries for platform analytics, behavioral adaptation that increases interaction frequency without user benefit, and routing decisions that prioritize platform engagement metrics over user intent completion."

### Section 8. Non-goals

**Feedback:** Good scoping but misses technical non-goals like "does not define PolicyRecord schema extensions" or "does not modify execution plan compilation algorithm."

**Scores:** Style & Clarity: 4

**Recommendation:** Add technical non-goals: "This addendum does not define PolicyRecord schema extensions for user preferences, modify the execution plan compilation algorithm in AIOS-SPEC-009 §15, or specify audit stream implementation details."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 2, 3, 4 | Undefined technical terms | Replace "materially" and "where policy permits" with PolicyRecord and capability registry references | Critical | 3, 4, 7 |
| 2 | 4 | Conflict with audit requirements | Explicitly separate user-preference logging from mandatory audit streams and reference AIOS-SPEC-009 §12.4 | Critical | 6, 4 |
| 3 | 5, 6 | Missing technical implementation | Add requirements for PolicyRecord storage, registry registration, and integration with intent compilation | High | 5, 7, 9 |
| 4 | 3 | Vague UI references | Specify implementation through AIOS-SPEC-006 components with stable IDs and data schemas | Medium | 7, 9 |
| 5 | 7 | Abstract conflict examples | Provide concrete technical examples tied to specific platform behaviors | Medium | 3, 7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document establishes important principles for user sovereignty but lacks the technical specificity required for implementation in the AIOS governed execution environment. Critical gaps in architectural integration, undefined technical boundaries, and missing implementation details prevent it from being actionable.

**Top 3 Actions Required:**
1. Integrate all user sovereignty controls with the PolicyRecord and execution model defined in AIOS-SPEC-009, specifying how preferences affect policy evaluation and plan compilation.
2. Resolve the conflict between user-configurable logging and mandatory audit requirements by defining separate logging streams with clear technical boundaries.
3. Add concrete implementation details including UI component references (AIOS-SPEC-006), data schemas, and registry integration patterns to make the requirements developer-actionable.
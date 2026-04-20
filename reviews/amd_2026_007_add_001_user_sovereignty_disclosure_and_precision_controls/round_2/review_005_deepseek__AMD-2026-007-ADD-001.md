---
review_id: REV-AMD-2026-007-ADD-001-002
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.3.0
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
| 1 | Cross-Document Consistency | 3 | References correct parent documents but fails to integrate with SPEC-009's execution-readiness thresholds and PolicyRecord evaluation model. |
| 2 | Business Model Alignment | 4 | Supports enterprise trust model by providing transparency, but lacks clear boundaries for mandatory platform functions. |
| 3 | Legal Enforceability | 2 | Uses "SHALL" consistently but relies on undefined terms like "materially affects behavior" without PolicyRecord-backed thresholds. |
| 4 | Architectural Fidelity | 2 | Creates parallel disclosure system that conflicts with SPEC-009's transparency model and doesn't integrate with intent-driven UI contract. |
| 5 | Completeness | 2 | Lacks implementation schemas, failure modes, and clear integration points with existing capability registry and UI component standards. |
| 6 | Conflict Freedom | 2 | Directly conflicts with SPEC-009's deterministic execution model by allowing user logging controls without clear auditability preservation. |
| 7 | Practical Operability | 2 | Requirements are too abstract; no schemas, no component references, no testable thresholds for implementation. |
| 8 | Style & Clarity | 4 | Follows Style Guide conventions with consistent "SHALL" usage and clear structure, though some sections remain vague. |
| 9 | Developer Synchrony | 2 | No actionable implementation guidance; missing schemas, component references, and integration patterns with existing systems. |
| 10 | Platform Economics Synchrony | 3 | Doesn't address how disabling telemetry affects usage-based billing or platform analytics for product improvement. |
| 11 | Friction Factor | 3 | Adds necessary transparency friction but implementation complexity is high without clear architectural integration. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- **Clear Purpose:** Section 1 articulates a strong need for user sovereignty against hidden platform state.
- **Consistent Language:** Uses "SHALL" consistently throughout, addressing Round 1's major criticism.
- **Good Categorization:** Sections 3-6 provide comprehensive categories of state that should be disclosed and controlled.

### Critical Gaps

1. **Architectural Conflict:** Creates a parallel disclosure system that doesn't integrate with SPEC-009's transparency model (§12) and intent-driven UI contract (§10-11).
2. **Undefined Thresholds:** Relies on "materially affects behavior" without PolicyRecord-backed operationalization, making requirements unenforceable.
3. **Missing Implementation:** No schemas, no component references to AIOS-SPEC-006, no integration with capability registry or PolicyRecord evaluation.
4. **Auditability Conflict:** Section 4's logging controls directly threaten SPEC-009's deterministic execution model without clear preservation of mandatory audit trails.

---

## Article-by-Article Review

### Section 2: Governing principle

**Feedback:** The definition of "materially affects behavior" is circular and not operationalized. It references PolicyRecord evaluation but doesn't require PolicyRecord definitions for these thresholds.

**Scores:** Legal Enforceability: 2, Architectural Fidelity: 2

**Recommendation:** Replace with PolicyRecord-backed definition:
"Materially affects behavior SHALL be defined by numeric or enumerated thresholds in the active PolicyRecord for each state class in Section 3. When no PolicyRecord threshold exists, the state SHALL be considered material if it alters any visible shell behavior, UI rendering, or execution path."

### Section 3: Required disclosure classes

**Feedback:** References "documented shell disclosure surface" but doesn't cite AIOS-SPEC-006 components. Creates parallel system to SPEC-009's transparency model (§12) without integration.

**Scores:** Cross-Document Consistency: 2, Developer Synchrony: 2

**Recommendation:** Integrate with SPEC-009:
"The shell SHALL disclose these classes through the transparency model defined in AIOS-SPEC-009 §12, extending the system state disclosure with additional user-sovereignty dimensions. Disclosure components SHALL be registered in AIOS-SPEC-006 with stable identifiers."

### Section 4: Precision controls

**Feedback:** Direct conflict with SPEC-009's deterministic execution model. The clause about non-discretionary auditability is insufficient - it needs explicit reference to SPEC-009's audit requirements.

**Scores:** Conflict Freedom: 1, Architectural Fidelity: 1

**Recommendation:** Explicitly subordinate to SPEC-009:
"User-configurable logging controls SHALL NOT override audit logging required by AIOS-SPEC-009 §6.7 (state update), §15 (intent compilation audit), and the product audit model. The system SHALL maintain separate audit and user-preference logging streams with clear metadata separation."

### Section 5: Behavioral and guardrail settings

**Feedback:** Mentions PolicyRecord influence but doesn't define how settings map to PolicyRecord inputs. No schema for user preference storage or validation.

**Scores:** Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Add schema reference:
"User-governable behavior settings SHALL be stored as structured preferences with schema defined in the Workspace Domain Pack v1 or equivalent. These preferences SHALL influence PolicyRecord evaluation through documented policy input fields."

### Section 6: Inspectable signal use

**Feedback:** Requires signal registration but doesn't reference existing capability registry patterns from AMD-2026-007 §7.

**Scores:** Cross-Document Consistency: 3, Completeness: 2

**Recommendation:** Integrate with existing registry:
"Signal families SHALL be registered in the capability registry defined in AMD-2026-007 §7 with additional metadata fields for influence domains, default thresholds, and user-override posture."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 2, 3, 4 | Architectural conflict with SPEC-009 | Integrate disclosure requirements with SPEC-009's transparency model and subordinate logging controls to SPEC-009's audit requirements. | Critical | 4, 6, 1 |
| 2 | 2, 3 | Undefined thresholds | Require PolicyRecord definitions for "materially affects behavior" and all disclosure class thresholds. | Critical | 3, 7 |
| 3 | 3, 5, 6 | Missing implementation schemas | Add references to AIOS-SPEC-006 components, Workspace Domain Pack schemas, and capability registry extensions. | High | 5, 9, 7 |
| 4 | 4 | Auditability conflict | Explicitly reference SPEC-009 audit requirements and define separate audit/user-preference logging streams. | High | 6, 4 |
| 5 | Document | No failure modes | Add section defining consequences for non-compliance (Tier 2 governance breach requiring remediation). | Medium | 5, 3 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document addresses important user sovereignty concerns but creates architectural conflicts with SPEC-009's transparency and audit models while lacking operational definitions and implementation schemas.

**Top 3 Actions Required:**
1. Resolve architectural conflicts by integrating disclosure requirements with SPEC-009's transparency model and explicitly subordinating logging controls to SPEC-009's audit requirements.
2. Define all qualitative thresholds through PolicyRecord-backed operational definitions to make requirements enforceable.
3. Add implementation schemas, component references to AIOS-SPEC-006, and integration patterns with existing capability registry and PolicyRecord systems.
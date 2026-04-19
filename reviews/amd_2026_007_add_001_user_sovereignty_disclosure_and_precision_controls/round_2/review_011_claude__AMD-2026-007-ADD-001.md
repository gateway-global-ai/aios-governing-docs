---
review_id: REV-AMD-2026-007-ADD-001-002
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.4.0
reviewer: DeepSeek
review_date: 2026-04-17
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.6
---

# Peer Review: User Sovereignty Disclosure and Precision Controls

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with AMD-2026-007 and AIOS-SPEC-009, but lacks explicit cross-reference to AIOS-SPEC-006 component registry requirements. |
| 2 | Business Model Alignment | 4 | Supports enterprise trust model effectively by providing transparency controls, though implementation complexity may create vendor friction. |
| 3 | Legal Enforceability | 4 | Significant improvement from Round 1 with consistent SHALL usage and PolicyRecord-backed thresholds, but "materially affects behavior" still needs more precision. |
| 4 | Architectural Fidelity | 4 | Correctly implements separation of powers with user preferences as policy inputs, maintains stateless compute principles, and respects audit boundaries. |
| 5 | Completeness | 3 | Covers core disclosure and control requirements but lacks failure mode definitions and specific schema references for structured preferences. |
| 6 | Conflict Freedom | 4 | Well-resolved potential conflicts with audit requirements through explicit non-override clauses, though signal registry integration needs clarification. |
| 7 | Practical Operability | 3 | Provides clear requirements but lacks specific thresholds, component identifiers, and implementation guidance for developers. |
| 8 | Style & Clarity | 4 | Follows Style Guide well with consistent SHALL usage and proper structure, minor issues with some undefined terms. |
| 9 | Developer Synchrony | 3 | References appropriate specs but lacks concrete schemas, component IDs, or implementation examples that developers need. |
| 10 | Platform Economics Synchrony | 4 | Properly preserves audit logging for billing integrity while allowing user control over discretionary logging. |
| 11 | Friction Factor | 3 | Introduces necessary complexity for user sovereignty but may create implementation burden without clear prioritization guidance. |
| | **Composite Score** | **3.6** | |

---

## Overall Assessment

### Strengths

- **Strong Legal Foundation:** The revision successfully addresses Round 1 feedback by converting recommendations to binding requirements with consistent SHALL usage throughout (Sections 2-7).
- **Architectural Alignment:** Excellent integration with the governed execution model, properly treating user preferences as policy inputs while preserving mandatory audit boundaries (Section 4).
- **Conflict Resolution:** Well-handled potential conflicts with AIOS-SPEC-009 audit requirements through explicit non-override clauses and separate logging stream requirements (Section 4).
- **Principled Approach:** Clear governing principle with operationalized materiality thresholds tied to PolicyRecord evaluation (Section 2).

### Critical Gaps

- **Implementation Specificity:** While the document references appropriate specs, it lacks concrete component identifiers, schema definitions, or threshold examples that developers need for implementation (Sections 3, 5, 6).
- **Signal Registry Integration:** Section 6 references capability registry integration for signal families but doesn't specify how this maps to existing AMD-2026-007 §7 capability registry structure.
- **Failure Mode Operationalization:** Section 9 defines failure posture but lacks specific remediation procedures or conformance testing requirements.

---

## Article-by-Article Review

### Section 0.1: Integration posture

**Feedback:** Excellent architectural positioning that properly subordinates this addendum to existing specs while defining clear integration points. The PolicyRecord-backed approach is sound.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 4

**Recommendation:** Add explicit reference to AIOS-SPEC-006 component registration requirements: "disclosure surfaces registered under AIOS-SPEC-006 with stable component identifiers as defined in that specification's UI Component Registry Standard."

### Section 2: Governing principle

**Feedback:** Strong improvement from Round 1 with PolicyRecord-backed materiality thresholds. However, "materially affects behavior" remains somewhat subjective and could benefit from more specific criteria.

**Scores:** Legal Enforceability: 4, Architectural Fidelity: 4

**Recommendation:** Add specific behavioral change examples: "changes visible shell behavior, registered UI state, execution-readiness thresholds, resolved ExecutionPlan composition, **intent routing decisions**, **capability availability**, retention, routing, pacing, escalation, safety posture, or exit ability..."

### Section 3: Required disclosure classes

**Feedback:** Good list of disclosure classes with proper reference to AIOS-SPEC-009 §12. The requirement for machine-readable bindings is architecturally sound.

**Scores:** Completeness: 4, Developer Synchrony: 3

**Recommendation:** Specify component registration requirements: "The disclosure surface SHALL be implemented through components registered in AIOS-SPEC-006 with component IDs following the pattern `shell.disclosure.{class_name}` and machine-readable bindings to the underlying state..."

### Section 4: Precision controls

**Feedback:** Excellent handling of the audit logging conflict with clear separation requirements. The distinction between user-configurable and non-discretionary logging is well-defined.

**Scores:** Conflict Freedom: 5, Legal Enforceability: 4

**Recommendation:** Add schema reference for user preferences: "User-configurable logging or retention controls SHALL be implemented as structured user-preference policy inputs conforming to the Workspace Domain Pack v1 schema defined in AMD-2026-007 §7."

### Section 5: Behavioral and guardrail settings

**Feedback:** Good coverage of behavioral settings with proper policy integration. The prohibition against invisible behavioral management is well-stated.

**Scores:** Architectural Fidelity: 4, Completeness: 3

**Recommendation:** Specify storage schema: "User-governable behavior settings SHALL be stored as structured preferences under the `user_behavior_config` schema defined in Workspace Domain Pack v1, with fields for each setting class listed above."

### Section 6: Inspectable signal use

**Feedback:** Important requirement for signal transparency, but the capability registry integration needs clarification given AMD-2026-007's existing registry structure.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 3

**Recommendation:** Clarify registry integration: "Signal families SHALL be registered in the typed capability registry defined by AMD-2026-007 §7 under the domain `shell.signals` with capability IDs following the pattern `shell.signals.{family_name}` and metadata including influence domains, default thresholds, and user-override posture."

### Section 9: Failure posture

**Feedback:** Good principle for handling non-conformant disclosure, but lacks specific remediation procedures or testing requirements.

**Scores:** Practical Operability: 3, Completeness: 3

**Recommendation:** Add remediation specifics: "Remediation SHALL include: (1) registering missing disclosure components per AIOS-SPEC-006, (2) updating PolicyRecord thresholds to reflect actual system behavior, and (3) passing conformance tests defined in the User Sovereignty Conformance Suite (to be developed)."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 3, 5, 6 | Missing implementation specifics | Add concrete component IDs, schema references, and registry patterns for developers to implement | High | 7, 9 |
| 2 | 6 | Unclear capability registry integration | Specify how signal families map to AMD-2026-007 §7 capability registry structure with domain and ID patterns | High | 1, 9 |
| 3 | 9 | Vague remediation procedures | Define specific remediation steps and conformance testing requirements for non-conformant disclosure | Medium | 5, 7 |
| 4 | 2 | Behavioral change criteria could be more specific | Add intent routing and capability availability to the list of behavioral changes that trigger materiality | Medium | 3, 7 |
| 5 | 0.1 | Missing AIOS-SPEC-006 reference | Explicitly reference component registration requirements from AIOS-SPEC-006 | Low | 1 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document successfully addresses Round 1 legal enforceability issues and provides a solid architectural foundation, but needs implementation specifics and clearer integration guidance for developers.

**Top 3 Actions Required:**
1. Add concrete component identifiers, schema references, and registry patterns throughout Sections 3, 5, and 6 to make the requirements implementable by developers.
2. Clarify how signal families integrate with the existing AMD-2026-007 §7 capability registry structure, including domain assignments and ID patterns.
3. Define specific remediation procedures and conformance testing requirements in Section 9 to operationalize the failure posture.
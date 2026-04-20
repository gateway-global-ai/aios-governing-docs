<think>The user wants me to conduct a peer review of AMD-2026-007-ADD-001 (User Sovereignty Disclosure and Precision Controls). This is an addendum to AMD-2026-007, which is already ratified.

Let me analyze the document:

1. **Document**: AMD-2026-007-ADD-001 - User Sovereignty Disclosure and Precision Controls
2. **Parent**: AMD-2026-007 (ratified v0.2.1)
3. **Status**: Draft v0.4.0
4. **Purpose**: Extend shell disclosure law for user sovereignty

Looking at the prior reviews:
- There were Round 1 reviews (two from different models) that gave composite scores of 2.7 and 3.1
- Both called for "major_revision_required"
- Key issues identified:
  - Inconsistent use of SHOULD vs SHALL (weak legal enforceability)
  - Undefined qualifiers like "materially"
  - Missing definitions for key terms
  - Conflict with audit logging requirements
  - Lack of operationalization

This is Round 2, so I need to check if these issues were addressed in the revision.

Let me read through the current version:

**Section 0**: Status and intent - Good, clearly states it's an addendum to AMD-2026-007

**Section 1**: Purpose - Clear statement about preventing hidden state failure mode

**Section 2**: Governing principle - Uses "SHALL" which is good. Has defined "materially" with operationalization through PolicyRecord. This addresses some prior concerns.

**Section 3**: Required disclosure classes - Lists 7 classes. Uses "materially exist" but refers back to Section 2's materiality definition.

**Section 4**: Precision controls - Uses "SHALL" for requirements. Addresses the conflict with audit logging by saying user controls SHALL NOT override mandatory audit logging. This is improved.

**Section 5**: Behavioral and guardrail settings - Uses "SHALL" for requirements. 

**Section 6**: Inspectable signal use - Uses "SHALL" requirements and references capability registry.

**Section 7**: Conflict-of-interest disclosure - Uses "SHALL" requirements.

**Section 8**: Non-goals - Clear.

**Section 9**: Failure posture - Added a new section defining failure behavior.

The document has been significantly improved from the prior reviews. Key improvements:
1. Changed most "SHOULD" to "SHALL" for binding requirements
2. Added operationalization of "materially" through PolicyRecord in Section 2
3. Added explicit conflict resolution with audit logging in Section 4
4. Added Section 9 for failure handling

I need to evaluate this against the 11 dimensions and check for any remaining issues.

Looking more carefully at the style and enforceability, the document now employs proper binding language with "SHALL" throughout. The materiality concept is tied to PolicyRecord thresholds. The conflict between user controls and audit requirements is explicitly resolved. Section 9 provides concrete failure definitions. The definitions anchor to existing specifications like AIOS-SPEC-009 and AIOS-SPEC-006. Some terminology could still use further clarification—"user-comprehensible surface" lacks a precise definition, and the policy references could be more explicit. The integration with existing governance structures appears solid, and the specification alignment is mostly complete. Section 4's override language is appropriately bounded, and Section 5 correctly distinguishes between user preferences and mandatory constraints. The overall structure seems sound, with good alignment across the relevant specifications.</think>

---
review_id: REV-AMD-2026-007-ADD-001-002
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.4.0
reviewer: DeepSeek
review_date: 2026-04-17
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: AMD-2026-007-ADD-001 — User Sovereignty Disclosure and Precision Controls

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | References AMD-2026-007, AIOS-SPEC-009, AIOS-SPEC-006 correctly by title and section; policy ID references align with parent AMD. |
| 2 | Business Model Alignment | 4 | Strengthens enterprise trust model by providing transparency and control; aligns with governed platform positioning. |
| 3 | Legal Enforceability | 4 | Uses consistent "SHALL" for binding requirements; defines "materiality" through PolicyRecord thresholds; resolves audit logging conflict in §4. |
| 4 | Architectural Fidelity | 4 | Extends AIOS-SPEC-009 §12 transparency model correctly; shell-state vs domain intent boundary respected per AMD-2026-007 §11.9. |
| 5 | Completeness | 4 | Covers all disclosure classes, precision controls, behavioral settings, signal transparency, and conflict disclosure; added §9 failure posture. |
| 6 | Conflict Freedom | 4 | Explicitly addresses audit logging conflict in §4; user controls subordinate to non-discretionary logging with disclosure requirement. |
| 7 | Practical Operability | 3 | Requires PolicyRecord thresholds and SPEC-006 component registration but leaves operationalization to downstream implementation; acceptable for amendment-level spec. |
| 8 | Style & Clarity | 4 | Consistent SHALL/SHOULD usage; proper reference format; follows Style Guide for governance documents. |
| 9 | Developer Synchrony | 3 | References capability registry and PolicyRecord but lacks concrete schema examples or CLI references; developers need implementation guidance. |
| 10 | Platform Economics Synchrony | 4 | Does not create economic conflicts; logging controls properly subordinated to billing integrity requirements. |
| 11 | Friction Factor | 4 | Adds necessary disclosure friction with clear justification; user controls balanced against mandatory audit requirements. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

*   **Strong Legal Foundation:** The revision successfully addressed the critical "SHOULD vs SHALL" issue from Round 1. All binding requirements now use "SHALL," giving the document enforceable authority.
*   **Materiality Defined:** Section 2 now properly operationalizes "materiality" through PolicyRecord-backed thresholds, resolving the undefined qualifier problem from prior reviews.
*   **Audit Conflict Resolved:** Section 4 explicitly subordinates user-configurable logging to mandatory audit logging while requiring disclosure of that boundary — a well-designed compromise.
*   **Failure Posture Added:** New Section 9 defines remediation requirements for non-conformant disclosure, giving the addendum operational teeth.
*   **Policy Integration:** The document correctly integrates with AIOS-SPEC-009 execution-readiness thresholds, capability registry, and Workspace Domain Pack v1.

### Critical Gaps

*   **Missing Policy IDs:** Section 4 references audit logging requirements but doesn't cite specific policy IDs (e.g., `POL-AUDIT-001` mentioned in Round 1 review). Should be added for traceability.
*   **Operational Detail Gap:** While the document is legally sound, developers still lack concrete schema examples for the disclosure surface or preference storage format.
*   **Incomplete Cross-References:** Section 0.1 mentions "AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001" in cross_references but the document doesn't explicitly invoke or align with its provisions.

---

## Article-by-Article Review

### Section 0: Status and Intent

**Feedback:** Clear integration posture statement. References parent AMD-2026-007 correctly. The statement that it "extends, and SHALL NOT replace, the transparency model in AIOS-SPEC-009 §12" is architecturally important and well-stated.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5

**Recommendation:** No changes required.

### Section 1: Purpose

**Feedback:** Well-articulated failure mode. The statement that this prevents "hidden platform state" management is a strong governance principle.

**Scores:** Style & Clarity: 5

**Recommendation:** No changes required.

### Section 2: Governing Principle

**Feedback:** Excellent revision. Changed from "SHOULD" to "SHALL" as required. The materiality operationalization through PolicyRecord thresholds directly addresses the Round 1 critique about undefined qualifiers.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** Minor editorial — add the specific policy ID reference:
> "operationalized through numeric, enumerated, or PolicyRecord-backed thresholds (per active PolicyRecord for the session or tenant)"

### Section 3: Required Disclosure Classes

**Feedback:** Comprehensive list of 7 disclosure classes. References AIOS-SPEC-009 §12 transparency model correctly. The requirement for "stable identifiers and machine-readable bindings" is a strong operationalization requirement.

**Scores:** Completeness: 4, Developer Synchrony: 3

**Recommendation:** No changes required, though developers will need SPEC-006 component examples to implement.

### Section 4: Precision Controls

**Feedback:** This section shows the most improvement. Resolves the audit logging conflict that was the top concern in Round 1. The three-sentence paragraph at the end (lines 44-48) is well-crafted:
- User controls SHALL NOT override mandatory audit
- Shell SHALL disclose the boundary
- Separate audit and user-preference streams preserved

**Scores:** Conflict Freedom: 5, Legal Enforceability: 4

**Recommendation:** Add specific policy ID for audit requirements:
> "User-configurable logging or retention controls SHALL NOT override audit logging required by AIOS-SPEC-009 §12.4, AIOS-SPEC-009 §15, or the active product audit model (per POL-AUDIT-001 or equivalent)..."

### Section 5: Behavioral and Guardrail Settings

**Feedback:** Uses binding "SHALL" throughout. The distinction between user-governable settings and mandatory policy constraints is correctly handled — user settings "SHALL NOT override mandatory policy constraints."

**Scores:** Legal Enforceability: 4

**Recommendation:** No changes required.

### Section 6: Inspectable Signal Use

**Feedback:** Correctly references capability registry posture from AMD-2026-007 §7. The requirement to register signal families with "influence domains, default thresholds, and user-override posture" provides necessary governance metadata.

**Scores:** Completeness: 4, Cross-Document Consistency: 4

**Recommendation:** No changes required.

### Section 7: Conflict-of-Interest Disclosure

**Feedback:** Strong governing principle. Uses "SHALL" binding language. However, "meaningful" is still somewhat vague — consider whether this needs the same PolicyRecord-backed operationalization as "materiality" in Section 2.

**Scores:** Legal Enforceability: 3

**Recommendation:** Consider adding operationalization note similar to Section 2, or rely on existing PolicyRecord thresholds to define what constitutes a "conflict" for governance purposes.

### Section 8: Non-Goals

**Feedback:** Clear and appropriate scope limitation. Correctly excludes internal reasoning traces and exact UI tokens.

**Scores:** Style & Clarity: 5

**Recommendation:** No changes required.

### Section 9: Failure Posture

**Feedback:** This is a valuable addition not present in Round 1 versions. Defines remediation requirement for non-conformant disclosure. Prevents "fake compliance" where incomplete disclosure is presented as complete.

**Scores:** Practical Operability: 4, Completeness: 4

**Recommendation:** No changes required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 4 | Missing policy ID reference for audit logging | Add "(per POL-AUDIT-001 or equivalent)" after "active product audit model" | Medium | 3, 9 |
| 2 | 7 | "Meaningful" qualifier may need operationalization | Consider adding note: "defined as conflict per active PolicyRecord evaluation" or accept as implicitly covered by §2 materiality definition | Low | 3 |
| 3 | General | AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001 in cross-references but not invoked | Explicitly state alignment with that standard's provisions or note that this AMD addendum satisfies its disclosure requirements | Low | 1 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document has substantially improved from Round 1, addressing the critical enforceability issues (SHOULD→SHALL, undefined materiality). The audit logging conflict is resolved with appropriate disclosure requirements. Only minor policy ID references and optional operationalization details remain. The composite score of 3.8 reflects a legally sound, architecturally aligned addendum that requires only minor polish before ratification.

**Top 3 Actions Required:**
1. Add specific policy ID reference (POL-AUDIT-001) in Section 4 for audit logging requirements.
2. Clarify whether "meaningful conflicts" in Section 7 inherits the Section 2 materiality operationalization or needs separate definition.
3. Verify that AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001 provisions are satisfied by this addendum or explicitly scoped.
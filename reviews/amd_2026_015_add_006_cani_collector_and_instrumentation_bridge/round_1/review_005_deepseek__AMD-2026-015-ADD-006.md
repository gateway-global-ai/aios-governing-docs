---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.1
reviewer: DeepSeek
review_date: 2026-04-09
review_round: 1
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Correctly references all CANI family documents but has minor terminology drift in §4 regarding "raw capture" vs. "intake envelope" boundaries. |
| 2 | Business Model Alignment | 5 | Maintains strict non-authority boundary, preventing unauthorized collector implementation or economic bypass. |
| 3 | Legal Enforceability | 4 | Clear liability boundaries but §5's "writer lane" reference lacks explicit governance lane citation for materialization decisions. |
| 4 | Architectural Fidelity | 4 | Correctly separates capture, normalization, and handoff layers but §6's pre-validator outcome model creates potential overlap with ADD-005 validator contract. |
| 5 | Completeness | 3 | Missing explicit mapping of "writer lane" to ADD-003 persisted artifact contract and lacks concrete examples of blocked vs. failed capture scenarios. |
| 6 | Conflict Freedom | 5 | No contradictions with parent AMD-2026-015 or other CANI addenda; respects supremacy of existing governance lanes. |
| 7 | Practical Operability | 3 | Abstract about "capture surfaces" without defining how they emit signals or how normalization bridge is implemented; lacks concrete failure modes. |
| 8 | Style & Clarity | 4 | Follows style guide but §4 is overly dense with nested conditionals; could benefit from a visual flow diagram. |
| 9 | Developer Synchrony | 4 | Aligns with existing CANI technical standards but doesn't provide implementation hooks or API sketches for future developers. |
| 10 | Platform Economics Synchrony | 5 | Explicitly prohibits autonomous routing decisions and execution authority, preserving economic control planes. |
| 11 | Friction Factor | 4 | Maintains fail-closed posture but adds complexity with pre-validator and validator dual outcome models. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

1. **Clear Governance Boundary (§7):** Explicitly enumerates what this addendum does NOT authorize (collector implementation, browser instrumentation, database work), preventing scope creep.
2. **Architectural Layering (§3-5):** Correctly separates capture surfaces, normalization, validator handoff, and writer lanes, maintaining the CANI family's separation of concerns.
3. **Fail-Closed Discipline (§6):** Establishes `fail`, `blocked`, `advisory_warning`, `pass` outcomes before validator handoff, ensuring boundary violations don't propagate.
4. **Cross-Reference Integrity (§2):** Properly subordinates to AMD-2026-015 and references all relevant CANI addenda and support contracts.

### Critical Gaps

1. **Ambiguous "Writer Lane" Definition (§5):** References "writer lane for persisted artifacts" without explicitly citing ADD-003's storage contract or defining what authorization is needed for materialization.
2. **Overlapping Outcome Models (§6):** Creates a pre-validator outcome family that conceptually overlaps with ADD-005's validator outcomes, risking confusion about which layer makes final blocking decisions.
3. **Abstract Capture Surface Implementation (§3):** Lists allowed surface classes but doesn't define how they "emit" signals or what interfaces they must implement, leaving implementation undefined.
4. **Missing Failure Mode Examples (§6):** Lacks concrete examples of what constitutes a `fail` vs. `blocked` vs. `advisory_warning` outcome, reducing operational clarity.

---

## Article-by-Article Review

### §0. Status

**Feedback:** Clear status table with correct parent relationship. The footnote about writer lane being subordinate to ADD-003 is good but should be elevated to the main body.

**Scores:** Cross-Document Consistency: 5, Completeness: 4

**Recommendation:** Move the footnote about writer lane subordination to ADD-003 into the main Status table or add it as a separate row: "Storage Authority: Subordinate to AMD-2026-015-ADD-003 for persisted artifact materialization."

### §1. Purpose and Problem Statement

**Feedback:** Correctly identifies the gap between ADD-004/ADD-005 and capture surfaces. References the support contract (AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001) appropriately.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5

**Recommendation:** Add a brief sentence clarifying that this addendum provides the governing bridge while the support contract provides operational details, maintaining the pattern used in other CANI addenda.

### §2. Relationship to AMD-2026-015

**Feedback:** Properly subordinates to parent amendment. The note about the support contract supplying detailed operational crosswalk is correct but could be more explicit about division of responsibilities.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 4

**Recommendation:** Add a bullet list: "This addendum governs: (1) capture-surface eligibility principles; (2) normalization boundary rules; (3) handoff sequencing. The support contract defines: (1) specific surface classes; (2) minimum pre-envelope requirements; (3) fail-closed handling details."

### §3. Governed Capture-Surface Bridge Rule

**Feedback:** Correctly lists allowed surface classes and establishes `unknown` as a boundary classification. However, doesn't define what makes a surface "governed and reviewable."

**Scores:** Architectural Fidelity: 4, Practical Operability: 3

**Recommendation:** Add criteria for "governed and reviewable": "(a) has stable repo path; (b) produces evidence artifacts with stable references; (c) preserves provenance metadata; (d) is documented in registry or equivalent discovery surface."

### §4. Raw-Capture and Normalization Rule

**Feedback:** Dense but technically correct. Establishes important distinction between raw capture and normalized intake. The minimum requirements list is comprehensive but could be organized as a checklist.

**Scores:** Architectural Fidelity: 4, Style & Clarity: 3

**Recommendation:** Reformat as a checklist table:
| Requirement | Purpose | Failure Consequence |
|-------------|---------|---------------------|
| Source-surface classification | Map to allowed class | `blocked` if `unknown` |
| Signal-family candidate | Determine envelope type | `blocked` if indeterminate |
| Repo-local payload reference | Provide reviewable evidence | `fail` if external or hidden |
| Sequence context | Derive stream_key/sequence_id | `blocked` if unprovable |

### §5. Validator and Writer Handoff Rule

**Feedback:** Establishes correct sequence but "writer lane" is undefined. The prohibition list is good but misses the critical point about who authorizes materialization.

**Scores:** Legal Enforceability: 3, Architectural Fidelity: 3

**Recommendation:** Replace "writer lane for persisted artifacts" with "writer lane governed by AMD-2026-015-ADD-003 for persisted artifact materialization, subject to that addendum's routing and acceptance rules." Add: "Materialization requires explicit routing acceptance per ADD-003 §6, not automatic validator pass."

### §6. Fail-Closed Outcome Rule Before Validator Handoff

**Feedback:** Creates a pre-validator outcome model that conceptually overlaps with ADD-005. The distinctions between `fail`, `blocked`, and `advisory_warning` are logical but need examples.

**Scores:** Practical Operability: 2, Architectural Fidelity: 3

**Recommendation:** Add concrete examples:
- `fail`: "Signal depends on external API not declared in repo"
- `blocked`: "Source surface classification is `unknown` after resolution attempts"
- `advisory_warning`: "Sequence context exists but confidence is `low`"
- `pass`: "All minimum requirements satisfied with `high` confidence"

Also clarify relationship to ADD-005: "These pre-validator outcomes determine whether an intake envelope can be constructed for validator input; they do not replace validator authority over persisted artifact integrity."

### §7. Non-Authority Boundary

**Feedback:** Excellent comprehensive list of what is NOT authorized. This should be the model for other bridge addenda.

**Scores:** Legal Enforceability: 5, Business Model Alignment: 5

**Recommendation:** No changes needed. This section is exemplary.

### §8. Implementation Follow-Through and Affected Surfaces

**Feedback:** Correctly identifies affected surfaces but misses the opportunity to specify what implementation packages would need to comply with.

**Scores:** Completeness: 4, Developer Synchrony: 3

**Recommendation:** Add: "Future collector implementation packages must: (1) declare which capture surface class they implement; (2) document their normalization bridge compliance; (3) provide test cases for fail-closed outcomes; (4) preserve handoff sequencing without bypass."

### §9. Out of Scope

**Feedback:** Comprehensive list matching §7. Good mirroring.

**Scores:** Completeness: 5, Conflict Freedom: 5

**Recommendation:** No changes needed.

### §10. Addendum Intent Summary

**Feedback:** Concise and accurate summary.

**Scores:** Style & Clarity: 5, Cross-Document Consistency: 5

**Recommendation:** No changes needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §0 | Writer lane authority undefined | Add explicit subordination to ADD-003 in status table | High | 3, 5 |
| 2 | §5 | "Writer lane" ambiguous | Replace with "writer lane governed by ADD-003" and add materialization authority note | High | 3, 4, 7 |
| 3 | §6 | Pre-validator outcome overlap with ADD-005 | Add examples and clarify relationship to validator authority | High | 4, 7 |
| 4 | §3 | "Governed and reviewable" undefined | Add criteria checklist | Medium | 4, 7 |
| 5 | §4 | Dense requirements list | Reformat as checklist table | Medium | 8 |
| 6 | §8 | Missing implementation compliance requirements | Add bullet list of what future packages must demonstrate | Medium | 5, 9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The addendum correctly establishes the architectural bridge between capture surfaces and the existing CANI intake/validator/persistence stack but requires clarification on writer lane authority, pre-validator outcome definitions, and implementation compliance criteria before ratification.

**Top 3 Actions Required:**
1. Explicitly define "writer lane" as subordinate to ADD-003 and specify that materialization requires routing acceptance per ADD-003 §6.
2. Clarify the relationship between pre-validator outcomes (§6) and validator outcomes (ADD-005) with concrete examples.
3. Add criteria for what makes a capture surface "governed and reviewable" to ensure operational clarity.
---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.6
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
| 1 | Cross-Document Consistency | 4 | Strong alignment with CANI family but some mapping language could be more explicit. |
| 2 | Business Model Alignment | 5 | Correctly maintains advisory-only posture without creating revenue or liability exposure. |
| 3 | Legal Enforceability | 3 | Clear boundaries but some terms like "writer lane" need stronger definition. |
| 4 | Architectural Fidelity | 4 | Properly separates capture, normalization, validation, and persistence layers. |
| 5 | Completeness | 4 | Covers all required bridge elements but lacks explicit error handling for normalization failures. |
| 6 | Conflict Freedom | 5 | No contradictions with parent amendments or support contracts. |
| 7 | Practical Operability | 3 | Defines clear handoff sequence but lacks concrete examples of normalization failure scenarios. |
| 8 | Style & Clarity | 4 | Well-structured with clear section boundaries, though some technical mapping is verbose. |
| 9 | Developer Synchrony | 4 | Aligns with existing CANI support contracts and provides clear implementation boundaries. |
| 10 | Platform Economics Synchrony | 5 | Maintains zero-cost advisory posture without creating implementation obligations. |
| 11 | Friction Factor | 4 | Minimal governance overhead for future implementation while preserving strict boundaries. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

1. **Excellent architectural separation** (Section 3-5): Clearly distinguishes capture surfaces, raw capture, normalized intake, and handoff lanes without creating implementation authority.
2. **Strong boundary preservation** (Section 7): Explicitly enumerates what this addendum does NOT authorize, preventing scope creep.
3. **Proper dependency hierarchy** (Section 2): Correctly subordinates to ADD-004 and ADD-005 while maintaining amendment precedence over support contracts.
4. **Clear fail-closed design** (Section 6): Provisional normalization statuses provide proper pre-validator gating without bypassing governance.

### Critical Gaps

1. **Missing error handling specification**: No explicit guidance on what happens to `normalization_fail` or `normalization_blocked` signals after classification.
2. **"Writer lane" definition ambiguity**: The locally defined term in Section 5 lacks clear ownership and accountability boundaries.
3. **Insufficient mapping validation**: Section 3's mapping to support contract values needs explicit validation requirements to prevent drift.

---

## Article-by-Article Review

### Section 3: Governed capture-surface bridge rule

**Feedback:** Strong classification of allowed surfaces with proper mapping to support contract values. The `unknown` handling is appropriately strict. However, the mapping language ("shell/operator flow -> `shell`") creates a maintenance dependency that should include validation requirements.

**Scores:** Architectural Fidelity: 5, Practical Operability: 3, Developer Synchrony: 4

**Recommendation:** Add validation requirement: "Any implementation of this mapping MUST validate that capture-surface classifications correspond exactly to the controlled values defined in AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001 §2. Mismatches SHALL be treated as `normalization_fail`."

### Section 4: Raw-capture and normalization rule

**Feedback:** Comprehensive minimum requirements for pre-envelope construction. The distinction between raw capture and normalized intake is architecturally sound. However, the handling of failed requirements needs explicit error pathways.

**Scores:** Architectural Fidelity: 4, Completeness: 3, Practical Operability: 3

**Recommendation:** Add explicit error handling: "Signals classified as `normalization_fail` or `normalization_blocked` SHALL be retained only as non-governed review evidence under `reviews/cani/intake_errors/` with timestamp and classification metadata, and SHALL NOT be referenced by any governed intake envelope."

### Section 5: Validator and writer handoff rule

**Feedback:** Clear sequential handoff with proper validator gating. The "writer lane" definition is functional but lacks accountability boundaries. The prohibition against treating `advisory_warning` as writer-lane admission is correct.

**Scores:** Architectural Fidelity: 4, Legal Enforceability: 3, Practical Operability: 4

**Recommendation:** Strengthen "writer lane" definition: "For purposes of this addendum, 'writer lane' means the governed materialization surface owned by the builder role under AMD-2026-013 §6.1, which writes persisted CANI artifacts only when authorized by validator outcome `pass` and remains subordinate to architecture review."

### Section 6: Fail-closed outcome rule before validator handoff

**Feedback:** Excellent provisional status design that prevents validator bypass. The distinction between pre-validator normalization statuses and authoritative validator outcomes is architecturally correct. However, the transition mechanism needs specification.

**Scores:** Architectural Fidelity: 5, Practical Operability: 3, Conflict Freedom: 5

**Recommendation:** Add transition specification: "The normalization bridge MUST convert provisional normalization statuses to validator input metadata as follows: `normalization_pass` -> validator input with full envelope; `normalization_fail`/`normalization_blocked` -> validator input marked `pre_validator_rejection` with classification reason; `normalization_advisory_warning` -> validator input with warning annotations."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §3 | Mapping validation gap | Add explicit validation requirement for capture-surface classification mapping. | High | 4,7,9 |
| 2 | §4 | Missing error handling | Specify retention path for failed/blocked signals as non-governed review evidence. | Critical | 5,7 |
| 3 | §5 | "Writer lane" ambiguity | Strengthen definition with role ownership and accountability boundaries. | High | 3,4 |
| 4 | §6 | Status transition gap | Specify how provisional normalization statuses convert to validator input metadata. | Medium | 4,7 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The addendum establishes architecturally sound bridges for capture surfaces and normalization handoff with strong governance boundaries, but requires clarification on error handling and role accountability before ratification.

**Top 3 Actions Required:**
1. Add explicit error handling specification for `normalization_fail` and `normalization_blocked` signals (Section 4).
2. Strengthen "writer lane" definition with clear role ownership and accountability (Section 5).
3. Add validation requirement for capture-surface classification mapping to prevent support contract drift (Section 3).
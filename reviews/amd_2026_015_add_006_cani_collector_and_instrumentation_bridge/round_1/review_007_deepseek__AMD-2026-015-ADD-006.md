---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.2
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
| 1 | Cross-Document Consistency | 4 | Correctly references all parent and sibling addenda but fails to explicitly bind to the capture-surface support contract's schema version. |
| 2 | Business Model Alignment | 5 | Maintains strict non-authority boundaries and does not authorize any commercial or runtime implementation. |
| 3 | Legal Enforceability | 4 | Clear prohibitions and fail-closed rules, but some outcome classifications are provisional and could create ambiguity in enforcement. |
| 4 | Architectural Fidelity | 4 | Correctly positions the bridge between capture surfaces, intake envelopes, and validator/writer lanes with proper separation of concerns. |
| 5 | Completeness | 3 | Defines the bridge rule but lacks explicit schema version references and concrete examples of the handoff sequence. |
| 6 | Conflict Freedom | 5 | No contradictions with parent amendment or sibling addenda; respects all existing authority boundaries. |
| 7 | Practical Operability | 3 | While conceptually sound, the pre-validator outcome model creates a parallel classification system that could conflict with authoritative validator outcomes. |
| 8 | Style & Clarity | 4 | Follows AIOS style conventions with precise terminology, though some sections are overly abstract. |
| 9 | Developer Synchrony | 4 | Aligns with existing CANI family patterns but doesn't provide concrete implementation guidance for future developers. |
| 10 | Platform Economics Synchrony | 5 | Maintains zero-cost governance posture without authorizing any infrastructure or runtime expenses. |
| 11 | Friction Factor | 4 | Adds necessary governance seams without creating unnecessary process overhead for future implementation. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

1. **Architectural Precision**: Section 3 correctly defines the governed capture-surface classes with explicit eligibility rules, maintaining the separation between `unknown` (boundary) and allowed surfaces.
2. **Non-Authority Boundary Clarity**: Section 7 provides comprehensive prohibitions that prevent scope creep into implementation, browser instrumentation, or autonomous execution.
3. **Handoff Sequence Integrity**: Section 5 establishes the correct sequential flow (capture → normalization → validator → writer) with explicit dependencies on prior addenda.
4. **Fail-Closed Discipline**: Section 6 mandates closed failure handling with specific classification rules that prevent silent downgrades of boundary violations.

### Critical Gaps

1. **Schema Version Ambiguity**: The addendum references `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` but doesn't bind to a specific schema version, creating potential drift.
2. **Pre-Validator Outcome Conflict**: The normalization bridge's `pass/fail/blocked/advisory_warning` classifications in Section 6 could conflict with the authoritative validator outcomes defined in `AMD-2026-015-ADD-005`.
3. **Missing Concrete Examples**: The document lacks illustrative examples of the handoff sequence, making it difficult for future implementers to understand the practical flow.
4. **Writer Lane Authority Ambiguity**: Section 5 defines the writer lane but doesn't explicitly subordinate it to the persisted-artifact contract's versioned schema.

---

## Article-by-Article Review

### Section 3: Governed capture-surface bridge rule

**Feedback:** This section correctly enumerates the five allowed capture surface classes and establishes the critical rule that `unknown` is a boundary classification only. The requirement that signals with unresolved source classification must be `blocked` is architecturally sound. However, the section doesn't reference the specific schema version from `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` that defines these classes, creating potential version drift.

**Scores:** Architectural Fidelity: 5, Completeness: 3, Practical Operability: 4

**Recommendation:** Add explicit schema version binding: "The allowed surface classes are those defined in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version 0.1.0 or later, specifically: 1. shell/operator flow, 2. UI surface observation, 3. planning artifacts, 4. review artifacts, 5. operator note."

### Section 4: Raw-capture and normalization rule

**Feedback:** The distinction between raw capture and normalized intake is architecturally correct and maintains the separation established in `ADD-004`. The minimum requirements list is comprehensive but abstract. The rule that missing required elements must result in `blocked` or `fail` classification is appropriate. However, the section doesn't specify how these requirements map to the intake-envelope contract's fields from `ADD-004`.

**Scores:** Architectural Fidelity: 4, Completeness: 3, Practical Operability: 3

**Recommendation:** Add a mapping table showing how each pre-envelope requirement corresponds to specific fields in the `ADD-004` intake envelope contract. For example: "source-surface classification → `source_surface` field; repo-local reviewable payload reference → `payload_ref` field; sequence context → `stream_key` and `sequence_id` fields."

### Section 5: Validator and writer handoff rule

**Feedback:** The sequential handoff rule is architecturally sound and maintains proper dependencies. The clarification that the writer lane is subordinate to validator outcomes and the persisted-artifact contract is correct. However, the definition of the writer lane as "the downstream governed materialization step" is too abstract and doesn't explicitly reference the schema version from `ADD-003`.

**Scores:** Architectural Fidelity: 4, Completeness: 3, Conflict Freedom: 5

**Recommendation:** Explicitly bind the writer lane to the specific version: "For purposes of this addendum, the writer lane means the materialization step that writes persisted CANI artifacts under the storage contract defined by `AMD-2026-015-ADD-003` version 0.1.0 or later and its corresponding technical support document `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`."

### Section 6: Fail-closed outcome rule before validator handoff

**Feedback:** This section creates a parallel classification system (`pass/fail/blocked/advisory_warning`) that exists "before validator handoff." While the intent to fail closed is correct, this creates potential conflict with the authoritative validator outcomes defined in `ADD-005`. The distinction between pre-validator and authoritative outcomes is conceptually valid but operationally ambiguous.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2, Conflict Freedom: 3

**Recommendation:** Clarify that these are provisional normalization statuses, not authoritative outcomes, and explicitly map them to validator input states: "These pre-validator classifications represent the normalization bridge's assessment of whether an intake envelope can be constructed. They must be converted to the authoritative outcome model defined in `AMD-2026-015-ADD-005` Section 5 before any routing or persistence decisions."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Missing schema version binding | Add explicit reference to `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version 0.1.0 | High | 1, 5, 7 |
| 2 | Section 4 | Abstract requirements mapping | Add table mapping pre-envelope requirements to `ADD-004` intake envelope fields | Medium | 5, 7, 9 |
| 3 | Section 5 | Writer lane definition ambiguity | Explicitly bind writer lane to `ADD-003` versioned schema | High | 1, 5, 7 |
| 4 | Section 6 | Pre-validator outcome conflict | Clarify provisional status and mapping to authoritative validator outcomes | Critical | 3, 6, 7 |
| 5 | Document-wide | Lack of concrete examples | Add an appendix with a handoff sequence example | Medium | 5, 7, 9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The addendum establishes architecturally sound bridge rules with proper non-authority boundaries, but requires clarification on schema version binding, outcome classification hierarchy, and concrete implementation guidance before ratification.

**Top 3 Actions Required:**
1. Resolve the pre-validator outcome conflict in Section 6 by explicitly mapping provisional classifications to authoritative validator outcomes.
2. Add explicit schema version references to all technical support documents (capture-surface contract, intake-envelope contract, persisted-artifact contract).
3. Clarify the writer lane definition with explicit subordination to the versioned persisted-artifact contract from `ADD-003`.
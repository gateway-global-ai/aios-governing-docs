---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.4
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
| 1 | Cross-Document Consistency | 4 | The document correctly references the entire CANI family and its support contracts, but Section 2's crosswalk language is overly complex and risks misinterpretation. |
| 2 | Business Model Alignment | 5 | The document correctly maintains the non-authority boundary and does not authorize any revenue-impacting or liability-creating activities. |
| 3 | Legal Enforceability | 4 | The "SHALL" and "SHALL NOT" language is precise, but Section 5's definition of the "writer lane" as "non-authoritative" creates a potential enforcement ambiguity. |
| 4 | Architectural Fidelity | 4 | The document correctly separates capture, normalization, validation, and writing lanes, preserving the DCP pipeline separation of powers. |
| 5 | Completeness | 3 | The document defines the bridge but lacks explicit JSON schema references for the provisional normalization statuses and does not define the handoff mechanism between provisional and authoritative validator states. |
| 6 | Conflict Freedom | 5 | No direct contradictions with the parent amendment or other CANI addenda; the non-authority boundaries are consistently reinforced. |
| 7 | Practical Operability | 3 | While the conceptual pipeline is clear, the document does not specify how the provisional normalization statuses map to validator outcomes or how a "normalization_pass" envelope is handed to the validator. |
| 8 | Style & Clarity | 4 | The writing is precise and follows the Style Guide, but Section 2 is overly verbose and could be simplified for clarity. |
| 9 | Developer Synchrony | 4 | The document correctly defers implementation to future packages and maintains stateless compute principles. |
| 10 | Platform Economics Synchrony | 5 | The document explicitly does not authorize any collector implementation, preserving the current economic model. |
| 11 | Friction Factor | 4 | The bridge is narrowly scoped and should not introduce significant operational friction, but the provisional status model adds cognitive overhead. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

1.  **Clear Separation of Powers:** The document meticulously defines a pipeline (capture → normalization → validation → writing) that respects the DCP's separation of powers. It correctly prohibits collectors from writing persisted artifacts directly (Section 5).
2.  **Strong Non-Authority Boundary:** Sections 3, 5, and 7 consistently reinforce that this is a governance bridge, not an implementation authorization. The list of prohibited activities is comprehensive.
3.  **Fail-Closed Design:** Section 6 correctly mandates a fail-closed approach using provisional normalization statuses (`normalization_fail`, `normalization_blocked`) before validator handoff, preventing boundary violations from proceeding.
4.  **Correct Subordination:** The document correctly positions itself as subordinate to `AMD-2026-015`, `ADD-004`, and `ADD-005`, and references the correct technical support contract (`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`).

### Critical Gaps

1.  **Handoff Mechanism Undefined:** The document states that provisional normalization statuses "must be superseded by the outcome model governed by `AMD-2026-015-ADD-005`" but does not specify the mechanism (e.g., a field in the intake envelope, a separate handoff artifact). This creates an operational gap.
2.  **Schema Omission:** The provisional normalization statuses (`normalization_pass`, `normalization_fail`, etc.) are not defined in a referenced JSON schema. They should be added as controlled values to the intake envelope schema in `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`.
3.  **Ambiguous Writer Lane Authority:** Section 5 defines the writer lane as "non-authoritative" but also states it writes "persisted CANI artifacts." This creates a tension; the writer's authority is derived solely from the validator's `pass` outcome, which should be stated more explicitly.

---

## Article-by-Article Review

### Section 0: Status

**Feedback:** The status table is clear and correctly identifies the document's subordinate relationship and narrow scope. The "Scope posture" accurately summarizes the document's intent.

**Scores:** Completeness: 5, Style & Clarity: 5

**Recommendation:** No change needed.

### Section 1: Purpose and problem statement

**Feedback:** Effectively states the problem and the bridge's purpose. Correctly references the technical support contract (`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` v0.1.2). The final sentence correctly limits the addendum's authority.

**Scores:** Completeness: 4, Cross-Document Consistency: 5

**Recommendation:** No change needed.

### Section 2: Relationship to AMD-2026-015

**Feedback:** This section is overly complex and verbose. It correctly states subordination but repeats the same point multiple times. The long sentence detailing the contents of the support contract is better placed in a footnote or removed, as it's descriptive, not normative.

**Scores:** Style & Clarity: 2, Architectural Fidelity: 4

**Recommendation:** Simplify. Proposed text:
> "This addendum is narrower. It binds governed capture-surface eligibility, normalization into intake envelopes, and handoff from normalized intake into validator and writer lanes. It remains subordinate to `AMD-2026-015-ADD-004` for intake-envelope behavior and to `AMD-2026-015-ADD-005` for validator behavior. Detailed capture-surface classification, pre-envelope requirements, and handoff expectations are specified in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`."

### Section 3: Governed capture-surface bridge rule

**Feedback:** Correctly lists the five allowed surface classes and mandates a fail-closed approach for `unknown`. The note distinguishing provisional normalization statuses from authoritative validator outcomes is crucial for architectural clarity.

**Scores:** Architectural Fidelity: 5, Practical Operability: 4

**Recommendation:** No change needed.

### Section 4: Raw-capture and normalization rule

**Feedback:** Clearly distinguishes raw capture from normalized intake. The list of minimum pre-envelope requirements is comprehensive and ensures the intake envelope contract can be satisfied. The rule against inventing fields is architecturally sound.

**Scores:** Architectural Fidelity: 5, Completeness: 4

**Recommendation:** Add a cross-reference to the specific section of `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001` that defines the intake envelope fields, to reinforce the contract boundary. E.g., "These elements correspond to the required fields defined in `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001` Section 3."

### Section 5: Validator and writer handoff rule

**Feedback:** The handoff sequence is correct. The prohibitions on collectors are essential. However, the definition of the "writer lane" as "non-authoritative" is problematic. The writer lane's authority is *derived* from the validator's `pass` outcome and the governing storage contract (`ADD-003`). It is authoritative *for the act of materialization* under those constraints.

**Scores:** Architectural Fidelity: 3, Legal Enforceability: 3

**Recommendation:** Revise the first paragraph for precision. Proposed text:
> "For purposes of this addendum, the **writer lane** is the downstream materialization surface that writes persisted CANI artifacts under the storage contract defined by `AMD-2026-015-ADD-003`. The writer lane's authority to materialize artifacts is **contingent and derived** from a validator outcome of `pass` and remains subordinate to the storage contract and downstream governance rules."

### Section 6: Fail-closed outcome rule before validator handoff

**Feedback:** Correctly defines four provisional statuses and mandates their use for fail-closed control. The critical rule that they "must not be emitted as final validator outcomes" is correct. However, the mechanism for superseding them is not defined (see Critical Gap #1).

**Scores:** Architectural Fidelity: 4, Practical Operability: 2

**Recommendation:** Add a sentence specifying the handoff mechanism. Proposed text:
> "The normalized intake envelope **SHALL** contain a field (e.g., `provisional_normalization_status`) reflecting this provisional outcome. Upon handoff to the validator, this field serves as input, and the validator **SHALL** emit its authoritative outcome (e.g., `validator_outcome`), superseding the provisional status in the review record."

### Section 7: Non-authority boundary

**Feedback:** Comprehensive and correctly scoped. No issues.

**Scores:** Business Model Alignment: 5, Conflict Freedom: 5

**Recommendation:** No change needed.

### Sections 8-10: Implementation, Out of Scope, Intent Summary

**Feedback:** These sections are clear, correct, and reinforce the document's limited scope. Section 8 correctly lists the affected surfaces.

**Scores:** Completeness: 5, Style & Clarity: 5

**Recommendation:** No change needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 2 | Overly complex and verbose crosswalk language. | Simplify the prose as proposed. | Medium | 8 (Style & Clarity) |
| 2 | Section 5 | Ambiguous definition of "writer lane" authority. | Clarify that writer authority is contingent and derived from validator `pass` and the storage contract. | High | 3 (Legal Enforceability), 4 (Architectural Fidelity) |
| 3 | Section 6 | Missing mechanism for handing off provisional normalization status to validator. | Specify that the provisional status is a field in the intake envelope that is superseded by the validator's authoritative outcome field. | High | 5 (Completeness), 7 (Practical Operability) |
| 4 | General | Provisional normalization statuses not defined in a governed schema. | **Action for `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`:** Add `provisional_normalization_status` as a controlled-value field to the intake envelope schema. | Critical | 5 (Completeness), 7 (Practical Operability) |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document establishes a sound architectural bridge for the CANI capture pipeline with strong governance boundaries. However, the lack of a defined handoff mechanism between provisional and authoritative validation states, and an ambiguous definition of writer-lane authority, require resolution before ratification.

**Top 3 Actions Required:**
1.  Define the mechanism for handing off the provisional normalization status to the validator and specify the resulting authoritative outcome field (Section 6).
2.  Clarify the derived and contingent nature of the writer lane's authority in Section 5.
3.  Update the intake envelope schema (`AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`) to include the `provisional_normalization_status` field as a controlled value.
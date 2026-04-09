---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.5
reviewer: DeepSeek
review_date: 2026-04-09
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The document correctly references the CANI family but creates terminological drift between "provisional normalization statuses" and validator outcomes, and its relationship to the support contract is ambiguous. |
| 2 | Business Model Alignment | 4 | The document maintains the non-authority boundary and does not authorize revenue-generating features or create economic liabilities. |
| 3 | Legal Enforceability | 2 | The document uses "SHALL" for technical normalization rules but lacks clear accountability surfaces and enforcement mechanisms for the bridge rules. |
| 4 | Architectural Fidelity | 2 | The document describes a pipeline but lacks concrete JSON schemas, DCP integration points, and fails to define the "writer lane" as a governed execution surface. |
| 5 | Completeness | 3 | The document covers capture surfaces and handoff but omits critical implementation details like error handling, retry logic, and concrete examples of the normalization bridge. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other CANI documents, but the "writer lane" concept creates tension with the stateless compute principle. |
| 7 | Practical Operability | 2 | The rules are too abstract for implementation; missing concrete examples, schemas, and step-by-step procedures for normalization. |
| 8 | Style & Clarity | 3 | Generally follows style guide but has overly complex sentence structures and repetitive disclaimers that obscure the core rules. |
| 9 | Developer Synchrony | 3 | References support contracts but doesn't provide clear guidance for developers on how to implement the bridge. |
| 10 | Platform Economics Synchrony | 4 | Maintains the non-commercial nature of the CANI family and doesn't create economic dependencies. |
| 11 | Friction Factor | 3 | The bridge adds complexity but is necessary for the CANI architecture; however, the current formulation creates implementation friction. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Clear non-authority boundary** (Section 7): Explicitly states what the addendum does NOT authorize, maintaining governance hygiene.
2. **Proper cross-referencing** (Section 0, 2): Correctly positions itself within the CANI family hierarchy and references support contracts.
3. **Fail-closed approach** (Section 6): Establishes important safety boundaries for normalization failures.

### Critical Gaps

1. **Missing architectural concretization**: No JSON schemas for the normalization bridge, no DCP integration points, and the "writer lane" is undefined as a governed execution surface.
2. **Ambiguous relationship with support contract**: Section 2 creates confusion about whether the amendment or support contract controls implementation details.
3. **Incomplete operational procedures**: Missing error handling, retry logic, and concrete examples of how normalization actually works.
4. **Terminological drift**: Creates "provisional normalization statuses" that overlap with but don't cleanly map to validator outcomes.

---

## Article-by-Article Review

### Section 0: Status

**Feedback:** The status table correctly identifies the document's subordinate relationship but the "Scope posture" is overly verbose and mixes implementation concerns with doctrinal statements.

**Scores:** Style & Clarity: 3, Cross-Document Consistency: 4

**Recommendation:** Simplify the scope posture to: "Narrow doctrine bridge establishing governed capture surfaces, normalization discipline, and validator-to-writer handoff boundaries for the CANI family. Does not authorize implementation."

### Section 2: Relationship to AMD-2026-015

**Feedback:** This section creates significant ambiguity about the relationship between the amendment and the support contract. The phrase "If this amendment and AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001 are read in tension, this amendment controls at the doctrine layer" creates implementation uncertainty.

**Scores:** Legal Enforceability: 2, Architectural Fidelity: 2, Cross-Document Consistency: 2

**Recommendation:** Replace the entire second paragraph with: "This amendment establishes the governing doctrine for capture surfaces and normalization handoff. AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001 provides the technical implementation contract that MUST conform to this amendment's rules. Any conflict MUST be resolved by bringing the support contract into alignment with this amendment."

### Section 3: Governed capture-surface bridge rule

**Feedback:** The rule correctly identifies allowed capture surfaces but creates implementation ambiguity by referencing "implementation-facing controlled values" without defining them. The relationship between amendment-layer names and implementation values is unclear.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2

**Recommendation:** Add a table mapping amendment-layer names to implementation values:
```
| Amendment Name | Implementation Value | Notes |
|----------------|---------------------|-------|
| shell/operator flow | `shell` | |
| UI surface observation | `ui_surface` | |
| planning artifacts | `planning_artifact` | |
| review artifacts | `review_artifact` | |
| operator note | `operator_note` | |
```

### Section 4: Raw-capture and normalization rule

**Feedback:** This section describes the conceptual flow but lacks concrete implementation details. The minimum pre-envelope requirements are listed but not structured as a verifiable schema. Missing: how sequence context is "sufficient to derive stream_key and sequence_id."

**Scores:** Architectural Fidelity: 2, Practical Operability: 1, Completeness: 2

**Recommendation:** Add a JSON schema example for the minimum pre-envelope structure:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CANI Pre-Envelope Capture Candidate",
  "type": "object",
  "required": [
    "source_surface",
    "signal_family_candidate",
    "signal_type_candidate",
    "payload_ref",
    "evidence_basis",
    "admitted_by"
  ],
  "properties": {
    "source_surface": {
      "type": "string",
      "enum": ["shell", "ui_surface", "planning_artifact", "review_artifact", "operator_note"]
    },
    "sequence_context": {
      "type": "object",
      "required": ["stream_key", "sequence_id"],
      "properties": {
        "stream_key": {"type": "string"},
        "sequence_id": {"type": "integer", "minimum": 0}
      }
    }
  }
}
```

### Section 5: Validator and writer handoff rule

**Feedback:** The "writer lane" concept is critically underspecified. It's described as a "non-authoritative downstream materialization surface" but lacks architectural placement. How does it integrate with DCP? What are its inputs/outputs? What happens if writer lane fails?

**Scores:** Architectural Fidelity: 1, Practical Operability: 1, Completeness: 2

**Recommendation:** Define the writer lane as a governed DCP pipeline stage with explicit inputs, outputs, and failure modes:
1. Add: "The writer lane SHALL be implemented as a DCP pipeline stage that consumes validator-outcome='pass' envelopes and produces persisted artifacts according to ADD-003."
2. Add: "Writer lane failures SHALL be recorded as governance events and SHALL NOT silently drop envelopes."
3. Add: "The writer lane SHALL be stateless and idempotent, replaying from the last successful write on failure recovery."

### Section 6: Fail-closed outcome rule before validator handoff

**Feedback:** Creates terminological drift by introducing "provisional normalization statuses" that don't cleanly map to validator outcomes. The relationship between these statuses and the validator's authoritative outcomes is unclear.

**Scores:** Cross-Document Consistency: 2, Architectural Fidelity: 2

**Recommendation:** Align the provisional statuses with validator outcomes or remove them entirely. Better approach: "The normalization bridge SHALL classify signals into categories that map directly to validator input states: 'ready_for_validation', 'blocked_requires_manual_review', 'rejected_invalid'. These classifications are pre-validator only and SHALL be superseded by authoritative validator outcomes."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 2 | Ambiguous relationship with support contract | Clarify that amendment controls doctrine, support contract implements it | Critical | 1, 3, 4 |
| 2 | Section 5 | Underspecified "writer lane" | Define as DCP pipeline stage with explicit failure handling | Critical | 4, 5, 7 |
| 3 | Section 4 | Missing concrete schemas | Add JSON schema for pre-envelope structure | High | 4, 5, 7 |
| 4 | Section 3 | Unclear mapping to implementation values | Add table mapping amendment names to implementation values | High | 4, 7 |
| 5 | Section 6 | Terminological drift with validator outcomes | Align provisional statuses with validator input states | Medium | 1, 4 |
| 6 | Section 0 | Overly verbose scope posture | Simplify to clear doctrinal statement | Low | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has critical architectural gaps, particularly the underspecified "writer lane" and missing concrete schemas, combined with ambiguous relationships with support contracts that create implementation uncertainty.

**Top 3 Actions Required:**
1. Define the "writer lane" as a governed DCP pipeline stage with explicit failure handling and integration points.
2. Clarify the amendment's controlling relationship over the support contract to eliminate implementation ambiguity.
3. Add concrete JSON schemas for the pre-envelope structure and normalization bridge interfaces.
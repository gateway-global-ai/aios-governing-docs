---
review_id: REV-AIOS-SPEC-009-R2-001
document_reviewed: AIOS-SPEC-009
document_version: 0.5.4
reviewer: DeepSeek R3
review_date: 2026-04-17
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 4.5
---

# Peer Review: Intent Primitive and Execution Model

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 5 | Perfect alignment with referenced documents, especially AMD-2026-007 §11 and operational runtime standards. |
| 2 | Business Model Alignment | 5 | Strong support for marketplace model through playbook promotion and explicit economic disclosure. |
| 3 | Legal Enforceability | 4 | Most rules are enforceable, but §12.2's "when material" clause creates minor ambiguity. |
| 4 | Architectural Fidelity | 5 | Perfectly embodies Technical Manifesto principles with clear separation of concerns and deterministic execution. |
| 5 | Completeness | 5 | Comprehensive coverage from intent schema through compilation, execution, and sovereign runtime lanes. |
| 6 | Conflict Freedom | 5 | No conflicts with other documents; clear boundaries established with shell state controls. |
| 7 | Practical Operability | 4 | Highly actionable with specific schemas, but some temporal grounding thresholds need clearer definition. |
| 8 | Style & Clarity | 5 | Exemplary adherence to Style Guide with precise, unambiguous language throughout. |
| 9 | Developer Synchrony | 5 | Clear TypeScript interfaces, implementation alignment section, and conformance test suite provide excellent guidance. |
| 10 | Platform Economics Synchrony | 5 | Strong economic disclosure requirements with explicit Funded Data Account linkage. |
| 11 | Friction Factor | 5 | Well-balanced governance with auto-approval rules that maintain safety while enabling velocity. |
| | **Composite Score** | **4.5** | |

---

## Overall Assessment

### Strengths

- **Architectural Rigor (§4-6):** The intent schema and lifecycle are precisely defined with clear separation between shell state and domain intent (§2.1), preventing architectural drift.
- **Sovereign Runtime Lanes (§16-17):** Excellent separation of speech-input, interpretation, and speech-output lanes with clear linkage to operational standards (OLLAMA, WHISPER, LOCAL_TTS).
- **Execution Model (§15):** Comprehensive compilation, proposal, and promotion framework that bridges intent to capability execution while maintaining auditability.
- **Cross-Document Alignment (§18):** Explicit requirements for SPEC-006, SPEC-007, SPEC-008, and AMD-2026-009 ensure consistent implementation across the platform.

### Critical Gaps

- **Temporal Grounding Thresholds (§6.3.1):** While the requirement for policy-defined thresholds is stated, the document doesn't specify what happens when thresholds aren't configured, creating implementation ambiguity.
- **Materiality Ambiguity (§12.2):** The "when material" clause for system state disclosure is subjective and could lead to inconsistent implementations.
- **ExecutionPlan Schema (§15.3):** The `temporalScope` field in `ExecutionPlan` should reference the same `TemporalScope` interface from §5 for consistency.

---

## Article-by-Article Review

### §2.1 Shell state vs domain intent (normative boundary)

**Feedback:** Excellent clarification that prevents misreading of SPEC-009 as governing shell-state semantics. The explicit reference to AMD-2026-007 §11.9 and POL-SHELL-004-006 ensures proper routing plane separation.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5

**Recommendation:** No changes needed. This section perfectly establishes the boundary.

### §5 Intent schema (required)

**Feedback:** The schema is well-structured with clear TypeScript interfaces. The `TemporalScope` interface with `isExplicit` and `isDefaulted` flags provides excellent audit trail for temporal grounding provenance.

**Scores:** Developer Synchrony: 5, Legal Enforceability: 5

**Recommendation:** No changes needed. The schema provides a solid foundation for implementation.

### §6.3.1 Temporal grounding for time-indexed domains (REQUIRED)

**Feedback:** The requirement for policy-defined thresholds is correct, but the document should specify what "conservative grounding" means when thresholds aren't configured. This creates implementation ambiguity.

**Scores:** Practical Operability: 3, Legal Enforceability: 4

**Recommendation:** Add specific default behavior for when thresholds aren't configured.
**Proposed Text Change:** After "Where thresholds are not yet configured, the system SHALL apply conservative grounding (§6.3.1 paths 1–4) before executing broad reads." add: "For mail and calendar domains, conservative grounding SHALL default to 'today' or 'last_7_days' unless policy specifies otherwise."

### §12.2 System state (primary-appropriate)

**Feedback:** The "when material" clause is subjective and could lead to inconsistent disclosure. This should be tied to objective policy conditions.

**Scores:** Legal Enforceability: 3, Practical Operability: 4

**Recommendation:** Replace subjective "when material" with policy-defined conditions.
**Proposed Text Change:** Replace "when material to whether the declared intent can execute" with "when system state readiness, as defined by the governing PolicyRecord for the resolved intent, is degraded or unavailable such that execution is blocked or would produce an incomplete result."

### §15.3 Plan structure (normative shape)

**Feedback:** The `ExecutionPlan` interface references `TemporalScope` but doesn't explicitly import the interface from §5. This could lead to schema drift.

**Scores:** Developer Synchrony: 4, Cross-Document Consistency: 4

**Recommendation:** Add explicit reference to the §5 `TemporalScope` interface.
**Proposed Text Change:** In the `ExecutionPlan` interface comment, add: "`temporalScope`: TemporalScope — see §5 for interface definition."

### §16.1 Normative requirements

**Feedback:** Excellent separation of retrieval from interpretation. The readiness state requirements align perfectly with OLLAMA_RUNTIME_STANDARD.

**Scores:** Architectural Fidelity: 5, Practical Operability: 5

**Recommendation:** No changes needed. This section correctly implements the DCP pipeline separation.

### §17 Sovereign voice and local runtime lanes (REQUIRED)

**Feedback:** Perfect three-lane separation with clear linkage to operational standards. The "block or proposal — never silent substitute" rule is architecturally sound.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 5

**Recommendation:** No changes needed. This section provides a robust framework for sovereign voice claims.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §6.3.1 | Unclear "conservative grounding" behavior when thresholds aren't configured | Specify default temporal grounding (e.g., "today" or "last_7_days") for mail/calendar when no policy thresholds exist | High | 7, 3 |
| 2 | §12.2 | Subjective "when material" clause for system state disclosure | Replace with policy-defined conditions based on system readiness state | High | 3, 7 |
| 3 | §15.3 | `ExecutionPlan.temporalScope` lacks explicit interface reference | Add comment referencing §5 `TemporalScope` interface definition | Medium | 9, 1 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is architecturally sound and nearly ratification-ready, with only minor clarifications needed for temporal grounding thresholds and system state disclosure criteria.

**Top 3 Actions Required:**
1. Specify default temporal grounding behavior in §6.3.1 for when policy thresholds aren't configured.
2. Replace the subjective "when material" clause in §12.2 with policy-defined conditions.
3. Add explicit interface reference for `ExecutionPlan.temporalScope` to the §5 `TemporalScope` interface.
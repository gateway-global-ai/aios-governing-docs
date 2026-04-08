---
review_id: REV-AMD-2026-012-009
document_reviewed: AMD-2026-012
document_version: 0.1.3
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: Shell Authority and Voice-First Entry

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with AMD-2026-007 and AIOS-SPEC-009, but §7 mapping to control-plane state needs explicit schema references. |
| 2 | Business Model Alignment | 4 | Clearly subordinates skills/tools to Shell authority, preserving marketplace model, though §9.4 could better articulate economic governance boundaries. |
| 3 | Legal Enforceability | 4 | §8.4.1 interim numeric defaults significantly improve enforceability, but some qualitative terms in §3 and §8 remain undefined. |
| 4 | Architectural Fidelity | 5 | Perfectly reinforces Technical Manifesto's UI sovereignty and separation of powers; Shell as single entry point aligns with stateless compute model. |
| 5 | Completeness | 3 | Missing explicit failure modes for control-plane mapping failures and edge cases for multi-modal continuity across voice/chat transitions. |
| 6 | Conflict Freedom | 4 | No direct contradictions, but §7 normative mapping creates implicit dependency on AIOS-SPEC-009 that should be made explicit. |
| 7 | Practical Operability | 3 | §7 mapping requirement is abstract; needs concrete examples of control-plane field mappings for each outcome. |
| 8 | Style & Clarity | 4 | Well-structured with clear normative language, though some sections (especially §7) are technically dense without illustrative examples. |
| 9 | Developer Synchrony | 3 | Lacks concrete schemas or API contracts for implementing the finite outcome family and its control-plane mappings. |
| 10 | Platform Economics Synchrony | 4 | §9.4 correctly acknowledges marketplace boundary, but doesn't specify how Shell-led discovery interacts with Funded Data Account disclosures. |
| 11 | Friction Factor | 4 | Voice-first model intentionally adds friction for dashboard drift prevention; §8.4.1 defaults are reasonable for developer implementation. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

- **Architectural Precision (§4):** Establishes Shell as single governed entry point with clear authority boundaries, perfectly aligning with Technical Manifesto's UI sovereignty principle.
- **Finite Outcome Family (§7):** The concept of a finite, auditable set of primary outcomes is architecturally sound and prevents implementation drift.
- **Interim Numeric Defaults (§8.4.1):** Provides concrete, enforceable thresholds for qualitative UX terms, addressing Round 1's critical legal enforceability gap.
- **Control-Plane Integration (§14):** Correctly positions Shell as presentation layer over authoritative control-plane state, maintaining separation of concerns.

### Critical Gaps

- **Abstract Control-Plane Mapping (§7):** The normative mapping requirement lacks concrete examples or schema references, making implementation ambiguous.
- **Missing Failure Modes:** No specification for what happens when control-plane state doesn't map cleanly to Shell outcomes or when multi-modal continuity breaks.
- **Incomplete Developer Contracts:** Lacks explicit API or schema definitions for implementing the finite outcome family in real systems.

---

## Article-by-Article Review

### §4. Normative shell authority

**Feedback:** This section is architecturally precise. The addition of audit trail initiation and economic disclosure presentation to §4.2 addresses Round 1's completeness gap. The separation between Shell presentation authority and underlying commercial rules is correctly maintained.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 4

**Recommendation:** Add a note clarifying that while Shell governs presentation timing, the actual economic calculations remain in the control plane per AIOS-SPEC-009 §15.4.

### §7. Shell-owned governed outcomes (finite family)

**Feedback:** The finite outcome family concept is excellent governance. However, the normative mapping requirement in the final paragraph is too abstract. "At least one of session summary, SessionContext, or PolicyRecord fields" doesn't specify which fields or how they should be structured.

**Scores:** Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Add an informative table mapping each outcome to example control-plane field references:
```
| Outcome | Example Control-Plane Field | AIOS-SPEC-009 Reference |
|---------|----------------------------|--------------------------|
| ready_for_intent | session.state.intent_resolution_status | §6.2 |
| needs_clarification | session.clarification.required_fields | §6.3 |
| needs_auth | policy.auth_required | §12.2 |
```
Or reference a specific schema file in the repository that defines these mappings.

### §8.4.1 Interim defaults (normative, binding until superseded)

**Feedback:** This addition successfully addresses Round 1's critical legal enforceability gap. The numeric thresholds are reasonable and testable. The supersession mechanism in §8.4.2 is clear and governed.

**Scores:** Legal Enforceability: 5, Practical Operability: 4

**Recommendation:** Consider adding a conformance test example: "Implementations MUST provide a test that verifies default opening surface word count ≤ 200 when no user expansion has occurred."

### §14. Control-plane implications

**Feedback:** Correctly establishes the control plane as authoritative runtime layer. However, it doesn't specify what happens when control-plane signals are missing or contradictory (e.g., session identity present but PolicyRecord missing).

**Scores:** Completeness: 3, Architectural Fidelity: 4

**Recommendation:** Add a failure mode: "If control-plane state is incomplete or contradictory for a required Shell outcome, the Shell SHALL present `execution_failed` with disclosure of the specific missing signal."

### §15. Conformance

**Feedback:** The conformance criteria are clear but some are subjective ("materially differs", "materially displace"). Item 7 references §8.4.1 defaults correctly.

**Scores:** Legal Enforceability: 4, Practical Operability: 3

**Recommendation:** For item 5, add a measurable threshold: "dashboard-first is defined as >50% of opening surface area occupied by non-conversational UI elements before first user intent."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §7 | Abstract control-plane mapping | Add informative table mapping outcomes to concrete control-plane field references or reference a schema file. | High | 7, 9 |
| 2 | §14 | Missing failure modes for incomplete control-plane state | Add failure mode requiring `execution_failed` outcome when required control-plane signals are missing. | Medium | 5, 7 |
| 3 | §15 | Subjective conformance criteria | Add measurable thresholds for "materially differs" and "materially displace" in items 5 and 6. | Medium | 3, 7 |
| 4 | §3 | Undefined qualitative terms in definitions | Add numeric defaults for "brief" and "minimal" in voice-first definition, referencing §8.4.1. | Low | 3, 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document successfully addresses Round 1's critical legal enforceability gap with §8.4.1 interim defaults and demonstrates strong architectural alignment. However, it requires concrete implementation guidance for the control-plane mappings in §7 to be fully operable.

**Top 3 Actions Required:**
1. Add concrete examples or schema references for the §7 control-plane outcome mappings.
2. Specify failure modes for incomplete or contradictory control-plane state in §14.
3. Add measurable thresholds for subjective terms in §15 conformance criteria.
---
review_id: REV-AMD-2026-012-006
document_reviewed: AMD-2026-012
document_version: 0.1.2
reviewer: DeepSeek
review_date: 2026-04-09
review_round: 2
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: Shell Authority and Voice-First Entry

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with AMD-2026-007 and AIOS-SPEC-009 concepts, but some terminology could be more explicitly linked to ratified schemas. |
| 2 | Business Model Alignment | 4 | Supports marketplace model by clearly subordinating Kits/tools, but could better articulate economic implications of Shell-led discovery. |
| 3 | Legal Enforceability | 3 | §8.4's dependency on future thresholds creates enforceability gap; some provisions use subjective terms without interim definitions. |
| 4 | Architectural Fidelity | 5 | Perfectly reinforces Technical Manifesto's UI sovereignty and separation of powers; Shell as single entry point aligns with stateless compute model. |
| 5 | Completeness | 3 | Missing explicit mapping between §7 outcomes and control-plane state; lacks failure mode specifications for edge cases. |
| 6 | Conflict Freedom | 4 | No direct conflicts, but §7 outcome family needs clearer boundary with AIOS-SPEC-009 §12 disclosure requirements. |
| 7 | Practical Operability | 3 | §7 outcomes are conceptually sound but lack concrete implementation schemas; §8.4 dependency delays day-one conformance. |
| 8 | Style & Clarity | 4 | Well-structured and follows Style Guide, but some sections are verbose and could be more concise. |
| 9 | Developer Synchrony | 3 | Provides conceptual framework but lacks specific schemas, CLI references, or control-plane contracts for implementation. |
| 10 | Platform Economics Synchrony | 3 | Acknowledges marketplace boundary but doesn't address how Shell authority affects Kit discovery economics or Funded Data Account implications. |
| 11 | Friction Factor | 4 | Voice-first model is intentionally high-friction for product vision; rules themselves add minimal unnecessary bureaucracy. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

- **Architectural Precision (§4):** Establishes Shell as single governed entry point with clear authority boundaries, perfectly aligning with Technical Manifesto's UI sovereignty principle.
- **Finite Outcome Family (§7):** Defines a discrete, auditable set of Shell outcomes that prevents ambiguity and enables deterministic execution paths.
- **Clear Hierarchy (§9):** Explicitly subordinates skills/tools/Kits to Shell authority, preventing dashboard drift and maintaining platform integrity.
- **Prohibited Patterns (§12):** Provides concrete, enforceable negative covenants that prevent common anti-patterns.

### Critical Gaps

- **Enforceability Gap (§8.4):** Dependency on future thresholds document creates legal void; qualitative terms need interim definitions for day-one conformance.
- **Missing Implementation Contracts:** No explicit mapping between §7 outcomes and control-plane state schemas, leaving implementation ambiguous.
- **Economic Blind Spot:** Doesn't address how Shell authority interacts with platform economics, particularly Kit discovery and Funded Data Account implications.

---

## Article-by-Article Review

### §4. Normative shell authority

**Feedback:** Excellent architectural definition. §4.4's "auditable fallback" requirement is particularly strong, ensuring all fallbacks map to §7 outcomes. However, the table in §4.2 should explicitly include audit trail initiation and economic disclosure presentation as Shell authorities.

**Scores:** Architectural Fidelity: 5, Completeness: 3

**Recommendation:** Add to §4.2 table: "Audit trail initiation" and "Economic disclosure presentation" with Shell authority "Yes — timing and presentation". This completes the session authority model.

### §7. Shell-owned governed outcomes (finite family)

**Feedback:** Conceptually excellent governance pattern. The finite family enables deterministic auditing. However, needs explicit mapping to control-plane state objects (e.g., SessionContext, PolicyRecord) and should reference AIOS-SPEC-009 §12 for disclosure alignment.

**Scores:** Architectural Fidelity: 5, Developer Synchrony: 3

**Recommendation:** Add normative statement: "Each outcome in this family SHALL map to a defined control-plane state code in the SessionContext schema (see AIOS-SPEC-009). Implementations SHALL maintain this mapping in versioned registry."

### §8. Voice-first interaction standard

**Feedback:** §8.4 creates significant enforceability gap by deferring thresholds to future document. Without interim definitions, §8.1-8.3 are legally unenforceable. This was noted in Round 1 but not fully addressed.

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Add interim thresholds clause: "Until subordinate thresholds document is ratified, implementations SHALL use: 'brief' ≤ 15 words/5s speech; 'one clarifying question' means exactly one before execution decision; 'minimal persistent text' ≤ 40 words initial entry."

### §9.4 Shell-led discovery, Kits, and marketplace boundary

**Feedback:** Correctly establishes hierarchy but misses economic implications. Shell's gatekeeping role in Kit discovery has significant economic consequences that should be acknowledged.

**Scores:** Business Model Alignment: 4, Platform Economics Synchrony: 2

**Recommendation:** Add to informative note: "The economic rules governing Shell-led Kit discovery, including any impact on Funded Data Account or marketplace placement economics, SHALL be defined in the Marketplace Terms document."

### §14. Control-plane implications

**Feedback:** Correctly identifies control-plane responsibilities but lacks concrete schema references. Should explicitly tie to AIOS-SPEC-009 execution model and SessionContext schema.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 3

**Recommendation:** Add specific references: "Control plane SHALL implement the intent resolution and validation lifecycle per AIOS-SPEC-009 §6, and SHALL expose session state via SessionContext schema including §7 outcome mapping."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §8.4 | Qualitative terms unenforceable without thresholds | Add interim numeric thresholds binding until subordinate document ratified | Critical | 3, 7, 9 |
| 2 | §7 | Missing mapping to control-plane state | Add requirement to map outcomes to SessionContext schema with versioned registry | High | 5, 9 |
| 3 | §4.2 | Incomplete session authority definition | Add audit trail initiation and economic disclosure presentation to authority table | High | 5, 7 |
| 4 | §9.4 | Economic implications of Shell-led discovery unaddressed | Add reference to Marketplace Terms for economic rules | Medium | 2, 10 |
| 5 | §14 | Lack of concrete schema references | Explicitly reference AIOS-SPEC-009 §6 and SessionContext schema | Medium | 9, 4 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document provides essential architectural definition for Shell authority that aligns perfectly with platform principles, but requires concrete implementation details and interim thresholds to be fully enforceable.

**Top 3 Actions Required:**
1. Add interim numeric thresholds for §8 qualitative terms to close enforceability gap.
2. Define explicit mapping between §7 outcomes and control-plane state schemas.
3. Complete §4.2 authority table with audit and economic disclosure responsibilities.
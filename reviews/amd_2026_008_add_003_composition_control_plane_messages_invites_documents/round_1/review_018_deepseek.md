---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.1
reviewer: DeepSeek
review_date: 2026-04-08
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Most terms match the glossary, but §19.10 references a placeholder operations standard (AIOS-OPS-020) that lacks substantive thresholds, creating an implementation gap. |
| 2 | Business Model Alignment | 4 | Clear alignment with MPOA for premium BOOK workflows (§10.11) and professional-use disclosure (§9.4), but lacks specific SLA numbers for verification processes. |
| 3 | Legal Enforceability | 2 | §19 originality gate lacks concrete thresholds and relies on a placeholder standard; §5.9 fail-closed rules are stated but lack DCP binding schemas for enforcement. |
| 4 | Architectural Fidelity | 3 | Correctly separates composition plane from ADD-001/ADD-002, but §18 knowledge basis lacks clear DCP pipeline integration points and JSON schemas for state transport. |
| 5 | Completeness | 2 | Missing critical implementation schemas for originality verification (§19), knowledge basis states (§18), and reference adherence controls (§20); relies on external placeholders. |
| 6 | Conflict Freedom | 4 | No direct contradictions with AMD-2026-008 or ADD-002; respects supremacy clause and bounded domains from architecture memo. |
| 7 | Practical Operability | 2 | Many rules are abstract (e.g., "high-overlap paraphrase risk" in §19.3) without actionable thresholds; developers cannot implement without filling gaps. |
| 8 | Style & Clarity | 4 | Follows Style Guide well; precise terminology; clear heading hierarchy; some sections overly verbose but structurally sound. |
| 9 | Developer Synchrony | 3 | Identifies needed fields (e.g., §5.9 table) but lacks JSON schemas and DCP transport bindings; developers must infer implementation details. |
| 10 | Platform Economics Synchrony | 4 | Aligns with MPOA for premium BOOK gates (§10.11) and professional-use liability; clear separation of base vs. premium workflows. |
| 11 | Friction Factor | 3 | Adds necessary governance gates but risks over-constraining casual use; §18 discovery-before-creation may slow responsive outputs if misapplied. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- **Clear architectural separation** (§2.1) correctly delegates navigation, depth, and VC to ADD-001/ADD-002, preventing conflation.
- **Comprehensive control-plane model** (§6 twelve-axis table) provides excellent conceptual mapping for developers.
- **Professional-use disclosure** (§9.4) is well-defined with mandatory text and export preservation rules.
- **Reference-guided composition** (§20) properly distinguishes template vs. reference vs. authority, avoiding copyright pitfalls.

### Critical Gaps

1. **§19 originality verification is unimplementable** — references placeholder AIOS-OPS-020 without thresholds, scoring algorithms, or DCP bindings.
2. **Missing JSON schemas** for composition contract (§5), knowledge basis states (§18), and reference adherence (§20) prevents DCP integration.
3. **§18 knowledge basis lacks pipeline integration** — no clear hooks to retrieval systems or state machine for discovery-before-creation.
4. **§5.9 fail-closed rules lack error codes** — normative intent stated but no transport schemas for DCP rejection.

---

## Article-by-Article Review

### §0 Status and intent

**Feedback:** Clear separation from ADD-001/ADD-002 is correct. Informative grounding references are appropriate but should be marked as non-normative more prominently.

**Scores:** Cross-Document Consistency: 5, Architectural Fidelity: 5

**Recommendation:** Add explicit "(non-normative)" after each informative reference in the table to prevent confusion.

### §5 Composition contract requirements

**Feedback:** The triad (role, intent, outcome) is architecturally sound. §5.9 table identifies minimum fields but lacks JSON schema. Fail-closed semantics are stated but without DCP error codes.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 2

**Recommendation:** Add Annex B with normative JSON Schema for composition contract, including required fields and validation error codes for DCP transport.

### §18 Knowledge basis and discovery gating

**Feedback:** Conceptually strong but lacks implementation hooks. §18.5 states sufficiency states but no state machine or retrieval system integration points. §18.11 sequence is informative but not binding.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2

**Recommendation:** Add §18.12 "DCP Integration" defining required API endpoints for knowledge basis checks, state transitions, and discovery triggers with example payloads.

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** Critical governance gap. §19.4 references AIOS-OPS-020 which is a placeholder without thresholds. §19.10 acknowledges implementation handoff but doesn't require concrete schemas. Developers cannot implement without filling these gaps.

**Scores:** Legal Enforceability: 1, Completeness: 1, Practical Operability: 1

**Recommendation:** Either embed minimum thresholds in §19.4 (e.g., "external publish requires <15% verbatim overlap") or require AIOS-OPS-020 to be populated before ratification. Add normative JSON Schema for verification metadata in Annex C.

### §20 Reference-guided composition

**Feedback:** Well-architected distinction between template/reference/authority. §20.13 adherence scale is clear but lacks binding to model parameters. No schema for reference_documents field.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 3

**Recommendation:** Add §20.16 "Implementation Schema" defining JSON structure for reference_documents array, adherence values, and innovation_mode enumeration.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.4, §19.10 | Originality verification unimplementable | Embed minimum thresholds or require AIOS-OPS-020 to be substantive before ratification | Critical | 3, 5, 7 |
| 2 | §5.9, §18, §20 | Missing JSON schemas | Add Annex B (composition contract), Annex C (originality), Annex D (reference) with normative schemas | High | 4, 5, 9 |
| 3 | §18 | No DCP integration points | Add §18.12 defining API endpoints for knowledge basis checks and discovery triggers | High | 4, 7 |
| 4 | §5.9 | Fail-closed rules lack error codes | Add table of DCP error codes (e.g., "COMPOSITION_CONTRACT_INCOMPLETE", "KNOWLEDGE_BASIS_INSUFFICIENT") | Medium | 3, 7 |
| 5 | §0 | Informative references not clearly marked | Add "(non-normative)" after each informative reference in §0 table | Low | 1, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** While architecturally sound, the document lacks critical implementation schemas and thresholds, particularly for originality verification (§19), making it unimplementable in its current form. The composite score of 3.0 and critical gaps in dimensions 3, 5, and 7 require substantial revision.

**Top 3 Actions Required:**
1. Resolve §19 originality verification by either embedding minimum thresholds or requiring AIOS-OPS-020 to be substantive before ratification.
2. Add normative JSON schemas for composition contract, knowledge basis states, and reference adherence controls.
3. Define DCP integration points for knowledge basis checks and fail-closed error codes.
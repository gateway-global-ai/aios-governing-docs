---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.1
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 3.2
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with ADD-001/ADD-002 but some terminology drift in §20.11-§20.15. |
| 2 | Business Model Alignment | 3 | Premium gates referenced but not fully integrated with composition classes. |
| 3 | Legal Enforceability | 3 | Professional disclosure well-defined but originality verification lacks concrete thresholds. |
| 4 | Architectural Fidelity | 2 | Control plane axes defined but implementation seams between §18, §19, §20 create overlapping responsibilities. |
| 5 | Completeness | 4 | Covers all promised areas but §19.10 implementation handoff creates ambiguity. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other documents. |
| 7 | Practical Operability | 3 | Many conceptual fields but missing JSON schemas and DCP bindings for critical gates. |
| 8 | Style & Clarity | 3 | Dense prose with repetitive normative language makes parsing difficult. |
| 9 | Developer Synchrony | 3 | Control-plane concepts clear but implementation mapping requires significant interpretation. |
| 10 | Platform Economics Synchrony | 3 | References MPOA and premium gates but lacks clear entitlement mapping tables. |
| 11 | Friction Factor | 3 | Multiple overlapping gates could create user friction without clear sequencing guidance. |
| | **Composite Score** | **3.2** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane definition** (§6 twelve-axis table) provides clear separation of concerns between ADD-001, ADD-002, and ADD-003.
2. **Professional-use disclosure** (§9.4) establishes clear governance posture for licensed-professional documents with mandatory disclosure text.
3. **Reference-guided composition** (§20) correctly distinguishes template vs reference vs authority roles, avoiding conflation with model temperature.
4. **Knowledge basis gating** (§18) establishes important "discover before create" principle with clear sufficiency states.

### Critical Gaps

1. **Architectural seam confusion** between §18 (knowledge basis), §19 (originality), and §20 (reference guidance) creates overlapping responsibilities without clear precedence rules.
2. **Missing implementation schemas** for critical control-plane objects (composition contract, originality evaluation record, reference adherence controls).
3. **Incomplete DCP pipeline integration** - §19.10 references ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD but doesn't define how gates integrate with DCP.
4. **Overly dense normative language** makes the document difficult to parse and implement.

---

## Article-by-Article Review

### §5 Composition contract requirements

**Feedback:** The triad (role, intent, outcome) is architecturally sound but §5.9's "normative fields and validation posture" table creates confusion. The table mixes composition contract fields (§5) with professional-use disclosure (§9.4.5) and reference-guided composition (§20) fields without clear separation. The "fail-closed rejection semantics" are valuable but should be in a dedicated enforcement section, not buried in a table.

**Scores:** Architectural Fidelity: 3, Practical Operability: 3

**Recommendation:** Move §5.9 to a new §21 "Enforcement and Validation" section. Create separate JSON schemas for each control-plane object in an annex. Clarify that composition contract validation occurs before knowledge basis check (§18), not after.

### §18 Knowledge basis and discovery gating

**Feedback:** The "sufficiency states" (sufficient, partial, insufficient, stale, conflicted, unverified) are well-defined. However, §18.11 "Recommended sequence" creates architectural confusion by mixing A (before drafting) and B (before publish/send) steps. The sequence should be mandatory, not recommended, and should clearly define precedence between §18, §19, and §20.

**Scores:** Architectural Fidelity: 2, Practical Operability: 3

**Recommendation:** Replace §18.11 with a mandatory gate sequence table:
1. Composition contract (§5) validation
2. Knowledge basis check (§18) - if insufficient → scaffold-only
3. Reference disposition (§20) when references apply
4. Originality verification (§19) before external release
Each gate should have defined DCP outcome codes and JSON schemas.

### §19 Originality and source-boundary verification

**Feedback:** §19 correctly establishes channel-based thresholds (internal vs external) but §19.10's implementation handoff to ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD creates architectural ambiguity. The document should define the minimum DCP interface required, not defer all implementation details.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2

**Recommendation:** Add a DCP integration section defining:
- Required evaluation triggers (publish, send, formal_export, shared_surface)
- Minimum evaluation record schema (artifact_id, channel_class, originality_verification_state, evaluated_at)
- DCP outcome codes mapping to §19.5 states
- Fail-closed behavior when evaluation missing

### §20 Reference-guided composition

**Feedback:** The R1-R3 roles and 1-10 adherence scale are architecturally sound. However, §20.11-§20.15 contains repetitive normative language that could be condensed. The innovation_mode (preserve/improve/reimagine) concept is valuable but needs clearer mapping to adherence levels.

**Scores:** Architectural Fidelity: 4, Style & Clarity: 2

**Recommendation:** Consolidate §20.11-§20.15 into a single "Adherence Controls" subsection. Add a table mapping adherence levels to expected structural changes. Define JSON schema for reference_documents array with required fields (document_id, reference_role, reference_mode).

### §6 Control-plane axes (twelve axes summary)

**Feedback:** The table correctly maps governance responsibilities but should include implementation artifact references. For example, Axis 11 (Originality) should reference both §19 and ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.

**Scores:** Cross-Document Consistency: 5, Developer Synchrony: 3

**Recommendation:** Add a "Implementation Artifact" column to the table:
- Axis 5-6: Composition class registry (product-specific)
- Axis 7: Composition contract schema (Annex B)
- Axis 11: ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD
- Axis 12: Reference adherence schema (Annex C)

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §5.9 | Mixed validation table creates confusion | Move to new §21 "Enforcement and Validation"; create separate JSON schemas | Critical | 4, 7, 9 |
| 2 | §18.11 | Recommended sequence should be mandatory | Replace with mandatory gate sequence table with DCP integration | High | 4, 7, 11 |
| 3 | §19.10 | Implementation handoff creates ambiguity | Add DCP integration section with minimum interface definition | Critical | 4, 7, 9 |
| 4 | §20.11-§20.15 | Repetitive normative language | Consolidate into "Adherence Controls" subsection with clear tables | Medium | 8, 9 |
| 5 | §6 | Missing implementation artifact references | Add "Implementation Artifact" column to twelve-axis table | Medium | 9, 10 |
| 6 | Throughout | Missing JSON schemas | Add Annex B (composition contract), Annex C (reference adherence), Annex D (gate outcomes) | High | 7, 9 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** While the document establishes comprehensive composition control-plane concepts, critical architectural gaps in gate sequencing, DCP integration, and implementation schemas prevent practical operability. The composite score of 3.2 and Architectural Fidelity score of 2 mandate major revision.

**Top 3 Actions Required:**
1. Define clear mandatory gate sequence with DCP integration points (§18.11, §19.10)
2. Create implementation JSON schemas for all control-plane objects (composition contract, originality evaluation, reference adherence)
3. Consolidate repetitive normative language and improve document structure for implementer clarity
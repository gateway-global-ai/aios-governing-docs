---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.3
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Multiple cross-references are correct, but §16.7 creates confusion by attempting to govern ADD-002 concepts. |
| 2 | Business Model Alignment | 4 | Clear premium gates and MPOA alignment, but lacks specific enforcement mechanisms for entitlement checks. |
| 3 | Legal Enforceability | 3 | Professional-use disclosure is strong, but originality verification lacks concrete thresholds and fails to define "materially significant" measurements. |
| 4 | Architectural Fidelity | 2 | Control-plane model is conceptually sound but lacks JSON schemas, DCP bindings, and clear separation between §18 and §19 scopes. |
| 5 | Completeness | 3 | Covers all promised axes but §19 implementation handoff to AIOS-OPS-020 is incomplete without specifying required conformance fields. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other documents, but §16.7 creates tension with ADD-002's ownership of depth/VC semantics. |
| 7 | Practical Operability | 2 | Missing concrete JSON schemas, DCP outcome codes, and implementation mappings for composition contract fields. |
| 8 | Style & Clarity | 3 | Structure is logical but document is excessively long (21 sections) with redundant explanatory text that obscures normative requirements. |
| 9 | Developer Synchrony | 2 | No product binding examples or implementation guidance for mapping conceptual fields to actual identifiers. |
| 10 | Platform Economics Synchrony | 4 | Clear premium gates and MPOA references, but lacks specific SLA numbers for verification processes. |
| 11 | Friction Factor | 3 | Multiple mandatory gates could create workflow friction without clear user experience guidance. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane model** (§6 twelve-axis table) provides clear separation of concerns across the addendum family.
2. **Professional-use disclosure** (§9.4) is well-defined with mandatory text and export preservation requirements.
3. **Reference-guided composition** (§20) correctly distinguishes structure adherence from model temperature.
4. **Clear premium gate separation** (§14) aligns with ADD-002 §10.11 and MPOA economics.
5. **Fail-closed semantics** (§5.9) provide clear enforcement postures for missing required fields.

### Critical Gaps

1. **Missing implementation schemas**: No JSON schemas for composition contract, knowledge basis, or measurement fields despite normative requirements.
2. **Incomplete originality verification**: §19 delegates to AIOS-OPS-020 but doesn't specify which fields must be implemented for conformance.
3. **Architectural boundary violations**: §16.7 attempts to govern ADD-002 concepts (depth/VC semantics) creating cross-document inconsistency.
4. **Unclear scope separation**: §18 vs §19 distinction is theoretically sound but lacks concrete procedural mapping for implementers.
5. **Excessive length and redundancy**: 21 sections with repetitive explanatory text obscures normative requirements.

---

## Article-by-Article Review

### §2.1 Addendum seams

**Feedback:** This section correctly establishes boundaries but §16.7 violates these principles by attempting to govern ADD-002 depth/VC semantics. The statement "§16 SHALL require the shell to apply ADD-002 depth and VC" creates architectural confusion about which document owns the enforcement.

**Scores:** Architectural Fidelity: 2, Cross-Document Consistency: 2

**Recommendation:** Remove the problematic language in §16.7 and replace with: "Language controls SHALL NOT alter the active output depth or VC class definitions as governed by ADD-002. The shell SHALL apply the current depth and VC settings to content in the active output_language."

### §5.9 Normative fields and validation posture

**Feedback:** The table correctly identifies minimum conceptual fields but lacks JSON schema definitions. The fail-closed rejection semantics are clear but missing DCP outcome codes for each rejection condition.

**Scores:** Practical Operability: 2, Architectural Fidelity: 2

**Recommendation:** Add Appendix B with JSON schemas for:
1. CompositionContractV1 (role, intent, outcome, optional fields)
2. ProfessionalUseMetadataV1 (professional_review_required, professional_domain, artifact_status)
3. ReferenceGuidanceV1 (reference_documents, reference_mode, reference_role, adherence fields)

### §16.7 Shell and voice-first behavior

**Feedback:** This section violates architectural boundaries by attempting to govern ADD-002 concepts. The language "§16 SHALL require the shell to apply ADD-002 depth and VC" creates confusion about enforcement ownership.

**Scores:** Architectural Fidelity: 1, Cross-Document Consistency: 1

**Recommendation:** Replace entire §16.7 with: "Language selection SHALL NOT alter the active output depth class (RESPONSE through BOOK) or VC class (VC0 through VC5) as defined in ADD-002. The shell SHALL track active output_language for editing and voice delivery, applying the current depth and VC settings to content in that language."

### §18.11 Recommended sequence

**Feedback:** The A/B sequence is conceptually sound but lacks concrete implementation mapping. Step 6 references §19 but doesn't specify how the originality verification integrates with the knowledge basis check.

**Scores:** Practical Operability: 2, Completeness: 3

**Recommendation:** Add implementation note: "Products SHALL implement §18.11 as a state machine with explicit transitions between states. The originality verification in step 6 SHALL consume the knowledge basis established in steps 2-3 and SHALL produce an OriginalityEvaluationRecordV1 per AIOS-OPS-020 §9."

### §19.10 Implementation handoff

**Feedback:** Correctly delegates to AIOS-OPS-020 but doesn't specify which fields from that standard must be implemented for conformance claims. The statement "Algorithm IDs and concrete scorers remain deferred" creates implementation uncertainty.

**Scores:** Practical Operability: 2, Completeness: 2

**Recommendation:** Add requirement: "Products claiming conformance to §19 SHALL implement at minimum: (a) the metric names in AIOS-OPS-020 §6.1, (b) the severity mapping in §6.2, (c) the evaluation record schema in Appendix A, and (d) the DCP outcome codes in §10. The policy_pack_id field SHALL be recorded in all evaluation records."

### §20.4 First-class inputs

**Feedback:** The conceptual fields are well-defined but lack schema definitions. The adherence controls (1-10) need specific mapping to implementation parameters.

**Scores:** Developer Synchrony: 2, Architectural Fidelity: 3

**Recommendation:** Add JSON schema for ReferenceGuidanceV1 including:
- reference_documents: array of document handles with source attribution
- reference_mode: enum with allowed values
- reference_adherence: integer 1-10 with default 5
- structure_adherence and style_adherence: optional integers 1-10
- innovation_mode: enum preserve|improve|reimagine

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §16.7 | Violates ADD-002 architectural boundaries | Replace with language respecting ADD-002 ownership of depth/VC | Critical | 1, 4, 6 |
| 2 | §5.9, §20.4 | Missing JSON schemas | Add Appendix B with CompositionContractV1, ProfessionalUseMetadataV1, ReferenceGuidanceV1 schemas | High | 4, 7, 9 |
| 3 | §19.10 | Incomplete conformance requirements | Specify minimum AIOS-OPS-020 fields that must be implemented | High | 4, 5, 7 |
| 4 | Document structure | Excessive length and redundancy | Move informative examples to Annex A, trim explanatory text | Medium | 8, 11 |
| 5 | §18.11 | Missing implementation mapping | Add state machine guidance and originality integration note | Medium | 4, 7 |
| 6 | §17.3 | Vague "materially significant" threshold | Define concrete artifact classes that trigger measurement confirmation | Low | 3, 7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has strong conceptual foundations but lacks the concrete implementation schemas, clear architectural boundaries, and specific conformance requirements needed for practical operability. Multiple dimensions score below 3, with Architectural Fidelity and Practical Operability at critical levels.

**Top 3 Actions Required:**
1. Fix §16.7 to respect ADD-002 ownership of depth/VC semantics (architectural boundary violation)
2. Add JSON schemas for all normative field definitions (composition contract, professional metadata, reference guidance)
3. Specify complete conformance requirements for §19 originality verification including which AIOS-OPS-020 fields must be implemented
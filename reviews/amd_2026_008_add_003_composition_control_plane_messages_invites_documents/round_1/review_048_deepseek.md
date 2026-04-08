---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.5
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Multiple cross-references to ADD-002 but fails to properly separate domains, creating confusion about ownership of depth/VC concepts. |
| 2 | Business Model Alignment | 4 | Properly references MPOA for commercial tiers and liability, though some economic implications are underspecified. |
| 3 | Legal Enforceability | 2 | Contains contradictory "SHALL NOT" statements in §19 that undermine enforcement posture. |
| 4 | Architectural Fidelity | 2 | Attempts to govern composition plane but lacks clear DCP pipeline description and JSON schema validation. |
| 5 | Completeness | 3 | Covers many axes but missing critical implementation schemas and fails to properly separate §18 and §19 scopes. |
| 6 | Conflict Freedom | 2 | Direct contradictions within §19 between enforcement obligations and disclaimer language. |
| 7 | Practical Operability | 3 | Defines conceptual fields but lacks concrete JSON schemas and DCP transport bindings for implementation. |
| 8 | Style & Clarity | 3 | Overly dense with repetitive cross-references; structure makes it difficult to parse governance boundaries. |
| 9 | Developer Synchrony | 2 | References AIOS-OPS-020 but doesn't provide clear mapping between composition plane and DCP codes. |
| 10 | Platform Economics Synchrony | 4 | Properly defers to MPOA for liability and commercial terms. |
| 11 | Friction Factor | 3 | Creates complex gating requirements but some gates lack clear implementation paths. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive coverage** of composition control plane with 12-axis model (§6) provides thorough conceptual framework.
2. **Proper separation of concerns** in referencing ADD-001 for navigation and ADD-002 for depth/VC/packaging (§2.1).
3. **Strong business model alignment** with proper MPOA references for commercial tiers and liability (§9.4.6, §17.7).
4. **Detailed originality verification framework** (§19) with proper channel-based thresholds and reference to AIOS-OPS-020.

### Critical Gaps

1. **Architectural contradiction** in §19 between enforcement obligations ("SHALL block") and disclaimer language that could be interpreted as waiving those obligations.
2. **Missing DCP pipeline description** - no clear mapping from composition contract to DCP transport codes for fail-closed scenarios.
3. **Incomplete JSON schema validation** - references AIOS-OPS-020 but doesn't provide schemas for composition contract fields.
4. **Confused scope separation** between §18 (knowledge basis) and §19 (originality) with unclear handoff points.

---

## Article-by-Article Review

### §2.1 Addendum seams

**Feedback:** While this section correctly references ADD-001/ADD-002 boundaries, it fails to establish clear ownership of the composition plane's DCP transport layer. The document references AIOS-OPS-020 for originality codes but doesn't define the composition-plane DCP namespace or transport envelope.

**Scores:** Architectural Fidelity: 2, Developer Synchrony: 2

**Recommendation:** Add explicit DCP transport requirements: "The composition control plane SHALL emit DCP codes in the `aios.dcp.composition` namespace for fail-closed scenarios defined in §5.9. Implementations SHALL use the transport envelope format defined in AIOS-OPS-020 §14."

### §5.9 Normative fields and validation posture

**Feedback:** The fail-closed table is conceptually sound but lacks concrete DCP code mappings. While it references AIOS-OPS-020 §13, it doesn't require implementations to actually emit these codes or define what happens when they're missing.

**Scores:** Practical Operability: 2, Architectural Fidelity: 2

**Recommendation:** Replace the current table with explicit DCP code requirements:
```
| Condition | DCP Code (namespace: aios.dcp.composition) | Enforcement Outcome |
|-----------|--------------------------------------------|---------------------|
| Mandatory composition contract fields missing | COMP_CONTRACT_INCOMPLETE | SHALL NOT proceed to substantive drafting except via explicit §5.4 scaffold path |
| Professional-use disclosure missing | COMP_PROF_DISCLOSURE_MISSING | SHALL NOT send/publish/export without remediation |
| Knowledge basis insufficiency | COMP_KNOWLEDGE_INSUFFICIENT | SHALL remain scaffold-only or blocked |
```

### §18.11 Recommended sequence

**Feedback:** The sequence mentions §19 in step B6 but doesn't define the handoff mechanism between knowledge basis states and originality verification. There's no clear data flow from §18 creation mode to §19 evaluation record.

**Scores:** Architectural Fidelity: 2, Completeness: 2

**Recommendation:** Add explicit handoff requirement: "When §19 applies, the `OriginalityEvaluationRecordV1` (per AIOS-OPS-020 §9) SHALL reference the same artifact identifier used in §18 knowledge basis metadata. The evaluation record SHALL include a `knowledge_basis_state` field mapping to §18.5 states."

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** Critical architectural flaw: §19.2 contains strong enforcement obligations ("SHALL block", "SHALL NOT treat source retrieval as permission to reproduce") but §19.9 contains language that could be interpreted as waiving these obligations. This creates a contradiction in the deterministic execution model.

**Scores:** Conflict Freedom: 1, Legal Enforceability: 1, Architectural Fidelity: 1

**Recommendation:** Rewrite §19.9 to clarify that disclaimer language applies only to marketing claims, not enforcement obligations: "§19.9 Marketing Claims Limitation: The runtime SHALL NOT market or represent the system as ensuring absolute copyright compliance or guaranteed non-infringement. This marketing limitation SHALL NOT weaken the enforcement obligations in §19.2-§19.5, which remain binding product requirements."

### §19.10 Implementation handoff

**Feedback:** Properly references AIOS-OPS-020 but doesn't define the composition-plane specific requirements for DCP transport. The "minimum surface" list is good but incomplete without transport envelope requirements.

**Scores:** Developer Synchrony: 3, Practical Operability: 3

**Recommendation:** Add transport requirement: "Products emitting DCP for §5.9 composition fail-closed scenarios SHALL use the envelope format defined in AIOS-OPS-020 §14 with `dcp_namespace: 'aios.dcp.composition'`."

### §20 Reference-guided composition

**Feedback:** The adherence scale (§20.13) is well-defined but lacks architectural integration with the DCP pipeline. There's no specification for how adherence levels affect the composition process or how they're validated.

**Scores:** Architectural Fidelity: 3, Practical Operability: 3

**Recommendation:** Add validation requirement: "Reference adherence controls SHALL be validated during composition contract establishment (§5). When `reference_adherence` ≥ 8, the runtime SHALL perform structural similarity validation against reference documents and SHALL emit `COMP_REFERENCE_ADHERENCE_HIGH` warning if structural conformity cannot be achieved."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.2 vs §19.9 | Contradiction between enforcement and disclaimer | Rewrite §19.9 to clarify marketing vs enforcement separation | Critical | 3, 4, 6 |
| 2 | §5.9 | Missing DCP code specifications | Add explicit DCP code table with namespace mapping | High | 4, 7, 9 |
| 3 | §2.1 | Missing DCP transport requirements | Add composition-plane DCP namespace and envelope requirements | High | 4, 7, 9 |
| 4 | §18.11 | Unclear handoff to §19 | Add explicit artifact identifier and state field mapping | Medium | 4, 5 |
| 5 | §20.13 | Missing architectural integration | Add adherence validation and DCP warning requirements | Medium | 4, 7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document contains critical architectural contradictions in §19 that undermine enforcement posture, lacks essential DCP pipeline specifications, and has incomplete implementation schemas despite comprehensive conceptual coverage.

**Top 3 Actions Required:**
1. Resolve the contradiction between §19.2 enforcement obligations and §19.9 disclaimer language.
2. Add explicit DCP code specifications and transport requirements for the composition plane.
3. Provide clear JSON schema validation requirements for composition contract fields.
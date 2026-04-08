---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.0
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
| 1 | Cross-Document Consistency | 3 | Most terms match the glossary, but §19.10 creates an ambiguous handoff that conflicts with DCP determinism principles. |
| 2 | Business Model Alignment | 4 | Clear alignment with MPOA for professional-use drafts and premium BOOK gates, though some enforcement mechanisms are deferred. |
| 3 | Legal Enforceability | 2 | §19.9 disclaimer directly contradicts §19.2 normative rules, creating an unenforceable conflict within the same document. |
| 4 | Architectural Fidelity | 2 | §19.10 implementation handoff violates DCP's stateless compute principle by deferring critical validation logic to unspecified artifacts. |
| 5 | Completeness | 4 | Covers all twelve axes comprehensively with detailed normative requirements for each control plane dimension. |
| 6 | Conflict Freedom | 1 | Direct internal contradiction between §19.2 (SHALL apply verification) and §19.9 (does not claim to enforce §19.2). |
| 7 | Practical Operability | 3 | Detailed conceptual fields defined but §5.9 fail-closed semantics lack concrete JSON schemas or DCP transport bindings. |
| 8 | Style & Clarity | 4 | Follows Style Guide conventions with clear section hierarchy, though some sections are excessively verbose. |
| 9 | Developer Synchrony | 3 | Control-plane axes are well-defined but §19.10 creates uncertainty about where implementation logic should reside. |
| 10 | Platform Economics Synchrony | 4 | Properly references ADD-002 §10.11 for premium BOOK gates and MPOA for professional-use liability. |
| 11 | Friction Factor | 3 | Comprehensive gating creates necessary friction for high-stakes artifacts but may be overly complex for simple compositions. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive Control-Plane Definition** (§6): The twelve-axis model properly separates navigation, depth, composition classes, and specialized controls like measurement contracts and reference adherence.
2. **Clear Addendum Seams** (§2.1): Explicitly defines boundaries with ADD-001 and ADD-002, preventing definitional overlap.
3. **Detailed Composition Contract** (§5): The role/intent/outcome triad provides a solid foundation for deterministic artifact generation.
4. **Professional-Use Disclosure** (§9.4): Well-structured with mandatory disclosure text and clear runtime obligations.

### Critical Gaps

1. **Internal Contradiction in §19**: §19.2 establishes normative SHALL rules for originality verification, but §19.9 states "No waiver of §19.2... The runtime SHALL/MUST NOT rules above remain binding" while simultaneously claiming "this subsection limits only what may be promised to users." This creates an unenforceable paradox.
2. **Architectural Violation in §19.10**: Deferring implementation-specific validation logic, scoring algorithms, and threshold tables to unspecified "governed specification or operations artifacts" violates the DCP principle of stateless compute with deterministic validation.
3. **Missing JSON Schemas**: While §5.9 mentions "normative fields and validation posture," it lacks concrete JSON schemas that would enable DCP pipeline validation.
4. **Overly Complex Gate Stacking**: §18.11 recommends a 6-step sequence before substantive drafting, which may create excessive friction for simple compositions.

---

## Article-by-Article Review

### §0 Status and Intent

**Feedback:** Properly establishes addendum relationship to AMD-2026-008 and references informative grounding documents. The "Does not replace" table clearly separates concerns from ADD-001 and ADD-002.

**Scores:** Cross-Document Consistency: 5, Architectural Fidelity: 5

**Recommendation:** No changes needed for this section.

### §2.1 Addendum Seams

**Feedback:** Excellent boundary definition that prevents definitional overlap. Explicitly states that ADD-003 shall not redefine ADD-002 labels or ladder semantics.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5

**Recommendation:** No changes needed. This should serve as a model for other addendum boundary definitions.

### §5 Composition Contract Requirements

**Feedback:** The role/intent/outcome triad is architecturally sound. §5.9 provides a good summary table but lacks the concrete JSON schemas needed for DCP validation. The "fail-closed rejection semantics" table is conceptually correct but needs implementation binding.

**Scores:** Architectural Fidelity: 4, Practical Operability: 3

**Recommendation:** Add a normative annex with JSON schemas for composition contract validation. The schemas should be referenced in §5.9 with a note: "See Annex B for normative JSON schemas implementing these validation postures."

### §19 Originality, Source-Boundary, and Non-Reproduction Verification

**Feedback:** This section contains a critical architectural flaw and internal contradiction. §19.2 establishes strong normative rules ("SHALL apply... SHALL prefer... SHALL flag... SHALL block"). §19.4 properly distinguishes internal vs external thresholds. However, §19.9 creates an unenforceable paradox by stating "No waiver of §19.2... The runtime SHALL/MUST NOT rules above remain binding" while also stating "this subsection limits only what may be promised to users about third-party legal outcomes."

**Scores:** Conflict Freedom: 1, Architectural Fidelity: 1, Legal Enforceability: 1

**Recommendation:** Rewrite §19.9 to eliminate the contradiction. Proposed text:
```
### 19.9 Legal Outcome Disclaimer

The originality verification and source-boundary controls defined in §§19.2-19.5 are operational risk-reduction mechanisms implemented as product behavior. They do not constitute legal advice or guarantee specific legal outcomes regarding copyright infringement, fair use determinations, or licensing compliance in any jurisdiction.

The runtime SHALL implement the verification states (§19.5), channel thresholds (§19.4), and enforcement outcomes (§19.2) as binding product obligations. Legal determinations of infringement, fair use, or licensing compliance remain outside the scope of this addendum and require consultation with qualified legal counsel.
```

### §19.10 Implementation Handoff

**Feedback:** This violates core DCP architecture principles. The DCP requires deterministic, stateless validation with clearly defined schemas. Deferring "implementation-specific validation logic, overlap/similarity scoring, threshold tables, serialized contract schemas, and control-plane transport bindings" to unspecified artifacts creates architectural ambiguity.

**Scores:** Architectural Fidelity: 1, Developer Synchrony: 2

**Recommendation:** Replace §19.10 with a requirement for concrete schemas and algorithms. Proposed text:
```
### 19.10 Implementation Specification

The originality verification mechanism SHALL be implemented as a deterministic validation function with the following characteristics:

1. **Input Schema**: Defined in Annex C, including required fields: `source_materials[]`, `output_text`, `target_channel`, `policy_thresholds`.
2. **Validation Algorithm**: The overlap detection algorithm SHALL be specified in AIOS-SPEC-XXX (Originality Verification Standard) with version 1.0.0 or later.
3. **Output States**: Exactly the five states defined in §19.5, serialized as defined in Annex C.
4. **Threshold Tables**: Policy thresholds for internal vs external channels SHALL be defined in AIOS-POL-XXX (Originality Policy) with version 1.0.0 or later.

Products SHALL implement the validation function as a stateless DCP component that can be audited and tested independently.
```

### §20.11-20.15 Reference Adherence Controls

**Feedback:** Properly distinguishes reference adherence from model temperature. The 1-10 scale with clear definitions is architecturally sound. The warning about maximum adherence not authorizing verbatim reproduction aligns with §19.

**Scores:** Architectural Fidelity: 5, Practical Operability: 4

**Recommendation:** Add a cross-reference to §19.4 in §20.14: "Maximum layout/reference adherence authorizes close conformity to structure, but SHALL NOT authorize wholesale reproduction of protected text (§19.2) and SHALL apply external channel thresholds (§19.4) when the artifact targets external distribution."

### §18.11 Recommended Sequence

**Feedback:** The A/B sequence is conceptually correct but may create excessive friction. The "Before substantive drafting" 5-step sequence could block simple compositions unnecessarily.

**Scores:** Practical Operability: 3, Friction Factor: 2

**Recommendation:** Add policy-based gating exceptions. Proposed addition to §18.11:
```
**Policy Exceptions**: For artifact classes with low grounding tier (§18.10) or when policy explicitly permits streamlined composition, steps 2-4 MAY be condensed or bypassed, provided the composition contract (§5) is satisfied and the artifact is marked as `streamlined_composition` in audit trails.
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.9 | Internal contradiction between normative rules and disclaimer | Rewrite to eliminate paradox while maintaining legal disclaimer | Critical | 3, 4, 6 |
| 2 | §19.10 | Violates DCP stateless compute principle | Replace with requirement for concrete schemas and algorithms | Critical | 4, 7, 9 |
| 3 | §5.9 | Lacks concrete JSON schemas for DCP validation | Add normative annex with JSON schemas | High | 4, 7 |
| 4 | §18.11 | Excessive friction for simple compositions | Add policy-based exceptions for low-stakes artifacts | Medium | 7, 11 |
| 5 | §20.14 | Missing cross-reference to originality controls | Add explicit reference to §19.2 and §19.4 | Low | 1, 6 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document contains a critical internal contradiction in §19 that makes it legally unenforceable, and §19.10 violates core DCP architectural principles by deferring implementation logic to unspecified artifacts.

**Top 3 Actions Required:**
1. Fix the §19.9 contradiction to create a legally enforceable document while maintaining appropriate disclaimers.
2. Replace §19.10 with concrete architectural requirements for deterministic validation.
3. Add normative JSON schemas for composition contract validation in §5.9.
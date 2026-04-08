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

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Multiple cross-references to ADD-002 are correct, but §16.7 creates confusion about ownership of depth/VC semantics. |
| 2 | Business Model Alignment | 4 | Clear alignment with MPOA for professional-use disclosure and premium BOOK workflows. |
| 3 | Legal Enforceability | 2 | §19.9 disclaimer creates tension with §19.2-§19.5 enforcement obligations, potentially weakening legal standing. |
| 4 | Architectural Fidelity | 2 | Control-plane model is overly complex (12 axes), lacks clear DCP transport mapping, and §5.9 fail-closed semantics are incomplete. |
| 5 | Completeness | 3 | Covers required domains but lacks implementation schemas, state machine diagrams, and concrete DCP message formats. |
| 6 | Conflict Freedom | 4 | No direct contradictions with parent AMD-2026-008 or referenced documents. |
| 7 | Practical Operability | 2 | Too abstract for implementation; missing JSON schemas, validation rules, and concrete state transitions. |
| 8 | Style & Clarity | 3 | Generally follows Style Guide but suffers from excessive conceptual density and repetitive phrasing. |
| 9 | Developer Synchrony | 2 | No product implementation mapping; abstract concepts without concrete API or schema definitions. |
| 10 | Platform Economics Synchrony | 4 | Clear premium BOOK gating and professional-use disclosure align with MPOA commercial terms. |
| 11 | Friction Factor | 3 | Complex control-plane model creates implementation friction but necessary for governance. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive scope coverage** (§1-§20) addresses all major composition control-plane concerns including professional-use disclosure, measurement contracts, and originality verification.
2. **Clear premium gating** (§10.11 references to ADD-002) properly separates base authoring from enhancement/publishing workflows.
3. **Strong cross-document alignment** with ADD-001/ADD-002 seams documented in §2.1 and architecture memo references.

### Critical Gaps

1. **Architectural over-complexity**: The 12-axis control-plane model (§6) creates unnecessary implementation friction without clear DCP transport mapping.
2. **Incomplete fail-closed semantics**: §5.9 references AIOS-OPS-020 §13 but lacks concrete DCP message schemas and state transition validation.
3. **Legal tension**: §19.9 disclaimer weakens the enforcement obligations in §19.2-§19.5, creating potential liability gaps.
4. **Missing implementation artifacts**: No JSON schemas for composition contracts, no state machine diagrams, and no concrete API definitions.

---

## Article-by-Article Review

### §5.9 Normative fields and validation posture

**Feedback:** The fail-closed table references AIOS-OPS-020 §13 DCP codes but provides no guidance on how these codes integrate with the composition control plane. Missing: DCP message schema, error response format, retry semantics, and audit logging requirements. The "SHALL not proceed to substantive drafting" language is too vague - what specific API or state transition blocks this?

**Scores:** Architectural Fidelity: 2, Practical Operability: 1

**Recommendation:** Add a DCP transport section with concrete message formats. Replace vague blocking language with specific state transitions:

**Current §5.9:** "SHALL not proceed to substantive drafting except via explicit §5.4 scaffold/outline path."

**Proposed:** "When composition contract validation fails, the DCP SHALL return `COMP_CONTRACT_INCOMPLETE` and set `artifact_state` to `scaffold_only`. The runtime SHALL NOT transition to `drafting` state until all required contract fields are satisfied."

### §16.7 Shell and voice-first behavior

**Feedback:** Creates confusion about ownership boundaries. While correctly stating that ADD-002 owns depth/VC definitions, the language implies §16 can influence how these settings are applied. This violates the separation of concerns established in §2.1.

**Scores:** Cross-Document Consistency: 2, Architectural Fidelity: 2

**Recommendation:** Clarify that language settings are orthogonal to depth/VC application:

**Current §16.7:** "The shell SHALL track `output_language` for editing and voice delivery and SHALL apply the current depth and VC settings established under ADD-002 to the active language surface..."

**Proposed:** "Language selection SHALL NOT alter the active output depth class or VC semantics defined in ADD-002. The shell SHALL apply depth and VC controls consistently across all language surfaces without reinterpreting their definitions."

### §19 Originality and source-boundary verification

**Feedback:** §19.9 creates a dangerous legal tension. While disclaimer language is necessary, it should not undermine the binding obligations in §19.2-§19.5. The current wording could be interpreted as excusing implementation failures.

**Scores:** Legal Enforceability: 1, Practical Operability: 2

**Recommendation:** Strengthen §19.9 to clarify that disclaimer applies only to absolute guarantees, not to implementation obligations:

**Current §19.9:** "The non-waiver and no-absolute-guarantee language in §19.9 does not weaken the enforcement obligations in §19.2–§19.5..."

**Proposed:** "§19.2–§19.5 establish binding implementation obligations for originality verification. §19.9 disclaims only absolute legal guarantees of non-infringement and does not excuse failures to implement the verification gates, thresholds, or enforcement states defined in those sections."

### §6 Control-plane axes

**Feedback:** The 12-axis model creates unnecessary complexity. Several axes (navigation, output depth, shell voice controls) are owned by other addenda and should not be listed as primary axes here. This creates implementation confusion.

**Scores:** Architectural Fidelity: 1, Practical Operability: 2

**Recommendation:** Simplify to core composition axes owned by this addendum:

**Replace entire §6 with:**
```
## 6. Composition control-plane axes

| # | Axis | Governed Section |
|---|------|------------------|
| 1 | Composition class | §§7–10 |
| 2 | Document subclass | §9.2 |
| 3 | Composition contract | §5 |
| 4 | Language/localization | §16 |
| 5 | Measurement contract | §17 |
| 6 | Knowledge basis | §18 |
| 7 | Originality verification | §19 |
| 8 | Reference guidance | §20 |

*Navigation, output depth, shell voice controls, and packaging are governed by ADD-001 and ADD-002.*
```

### Missing: DCP Transport Specification

**Feedback:** The entire addendum lacks concrete DCP message formats, which are essential for practical operability. References to AIOS-OPS-020 §13 codes are insufficient without message schemas.

**Scores:** Practical Operability: 1, Developer Synchrony: 1

**Recommendation:** Add new §21 "DCP Transport and State Management" with:
1. CompositionContract message schema
2. ArtifactState enumeration and transitions
3. ValidationError response format
4. Audit logging requirements
5. Retry and recovery semantics

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §5.9 | Incomplete fail-closed semantics | Add DCP message schemas and concrete state transitions | Critical | 4, 7, 9 |
| 2 | §19.9 | Legal tension with enforcement obligations | Strengthen disclaimer to protect implementation obligations | Critical | 3, 7 |
| 3 | §6 | Overly complex 12-axis model | Simplify to 8 core composition axes | High | 4, 7, 8 |
| 4 | §16.7 | Confusion about ownership boundaries | Clarify language-depth-VC orthogonality | High | 1, 4 |
| 5 | Missing | No DCP transport specification | Add §21 with message schemas and state management | Critical | 4, 7, 9 |
| 6 | Throughout | Excessive conceptual density | Trim repetitive phrasing and consolidate examples | Medium | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** While comprehensive in scope, the document suffers from architectural over-complexity, incomplete fail-closed semantics, legal tensions in originality verification, and missing implementation artifacts essential for practical operability.

**Top 3 Actions Required:**
1. **Add concrete DCP transport specifications** including message schemas, state transitions, and validation rules.
2. **Resolve legal tension in §19** by strengthening the disclaimer to protect implementation obligations without weakening enforcement.
3. **Simplify the control-plane model** from 12 axes to 8 core composition axes to reduce implementation friction.
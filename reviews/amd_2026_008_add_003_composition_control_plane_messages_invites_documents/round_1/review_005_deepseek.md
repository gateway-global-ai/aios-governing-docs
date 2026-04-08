---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.12.0
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
| 1 | Cross-Document Consistency | 3 | Most terms align with ADD-002 and glossary, but §16.7 incorrectly redefines depth/VC semantics that belong exclusively to ADD-002. |
| 2 | Business Model Alignment | 4 | Clear premium gates and entitlement mapping to MPOA, though some commercial triggers lack specific thresholds. |
| 3 | Legal Enforceability | 2 | Professional-use disclosure (§9.4) is strong, but originality gate (§19) contains contradictory "SHALL NOT claim" language that undermines enforceability. |
| 4 | Architectural Fidelity | 2 | Control-plane axes are defined but JSON schemas are missing; reference adherence (§20) conflates architectural control with model behavior. |
| 5 | Completeness | 3 | Covers all promised axes but lacks implementation schemas and fails to define how composition classes map to DCP pipeline stages. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other documents, though §16.7 creates tension with ADD-002's exclusive ownership of depth/VC. |
| 7 | Practical Operability | 2 | Many rules are abstract (e.g., "knowledge basis check") without specific thresholds or implementation guidance for developers. |
| 8 | Style & Clarity | 3 | Follows Style Guide but suffers from excessive length and repetitive cross-references that obscure core requirements. |
| 9 | Developer Synchrony | 2 | No JSON schemas or API contracts provided; developers cannot implement from this document alone. |
| 10 | Platform Economics Synchrony | 4 | Clear premium vs base split aligns with MPOA; BOOK workflow gates properly separate commercial entitlements. |
| 11 | Friction Factor | 3 | Adds necessary governance but creates implementation complexity without providing clear integration points. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane definition** (§6): The twelve-axis model properly partitions concerns across ADD-001, ADD-002, and this document.
2. **Professional-use disclosure framework** (§9.4): Clear, enforceable disclosure requirements with specific text and metadata fields.
3. **Premium entitlement gating** (§14): Properly defers to ADD-002 §10.11 and MPOA for commercial tiers.
4. **Knowledge basis gating sequence** (§18.11): Logical A/B sequencing provides clear workflow for non-trivial creation.

### Critical Gaps

1. **Missing implementation schemas**: No JSON schemas for composition contract, knowledge basis, or reference adherence controls despite being architectural documents.
2. **Architectural conflation**: §16.7 attempts to redefine depth/VC semantics that belong exclusively to ADD-002, violating separation of concerns.
3. **Unenforceable originality gate**: §19.9's "SHALL NOT claim" language contradicts the gate's normative requirements, creating legal ambiguity.
4. **Abstract operability**: Many requirements (e.g., "knowledge basis check") lack specific thresholds or implementation guidance.

---

## Article-by-Article Review

### §2.1 Addendum seams

**Feedback:** This section correctly identifies ownership boundaries but fails to enforce them. §16.7 later violates these seams by attempting to bind depth/VC semantics.

**Scores:** Architectural Fidelity: 2, Conflict Freedom: 3

**Recommendation:** Add enforcement language: "Violations of these seams SHALL be treated as governance failures. Any reference to ADD-002-defined concepts SHALL use them as defined in ADD-002 without modification."

### §5 Composition contract requirements

**Feedback:** Clear triad definition but missing JSON schema. The informative examples in Annex A are insufficient for implementation.

**Scores:** Developer Synchrony: 2, Practical Operability: 3

**Recommendation:** Add normative JSON schema in §5.7:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CompositionContract",
  "type": "object",
  "required": ["role", "intent", "outcome", "artifact_class"],
  "properties": {
    "role": {"type": "string", "enum": ["founder", "operator", "policy_author", "analyst", "executive_assistant", "brand_voice"]},
    "intent": {"type": "string", "enum": ["inform", "request", "persuade", "document", "analyze", "propose", "coordinate", "approve", "publish", "teach"]},
    "outcome": {"type": "string"},
    "artifact_class": {"type": "string", "enum": ["EMAIL", "CALENDAR_INVITE", "DOCUMENT", "POST", "BLOG", "ARTICLE", "NEWSLETTER", "REPORT", "BOOK"]},
    "professional_review_required": {"type": "boolean", "default": false}
  }
}
```

### §9.4 Professional-use draft disclosure

**Feedback:** Strong disclosure framework with specific text requirements. However, the relationship to DCP validation is unclear.

**Scores:** Legal Enforceability: 5, Architectural Fidelity: 3

**Recommendation:** Add DCP validation rule: "The DCP SHALL reject any professional-use artifact lacking the required disclosure metadata fields defined in §9.4.5."

### §16.7 Shell and voice-first behavior

**Feedback:** Violates §2.1 seams by attempting to "bind language/authoritative version rules to those controls." Depth and VC semantics are exclusively owned by ADD-002.

**Scores:** Cross-Document Consistency: 1, Architectural Fidelity: 1

**Recommendation:** Replace entire section with: "Language selection SHALL NOT modify output depth or VC class semantics defined in ADD-002. The shell SHALL apply language transformations within the constraints of the active depth and VC classes."

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** §19.2 establishes a normative gate but §19.9 undermines it with "SHALL NOT claim" language, creating unenforceable requirements.

**Scores:** Legal Enforceability: 1, Practical Operability: 2

**Recommendation:** Remove §19.9 and replace with: "This gate provides operational risk reduction consistent with platform policy. Implementation SHALL use the verification states defined in §19.5 to enforce publish/send/export restrictions."

### §20 Reference-guided composition

**Feedback:** Conceptually sound but conflates architectural control with model behavior. The 1-10 scale lacks implementation guidance for mapping to DCP parameters.

**Scores:** Architectural Fidelity: 2, Developer Synchrony: 2

**Recommendation:** Add DCP mapping: "Reference adherence values 1-10 SHALL map to specific DCP policy parameters (structure_fidelity: 0.0-1.0, style_fidelity: 0.0-1.0). The runtime SHALL expose these as separate controls when split mode is enabled."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §16.7 | Violates ADD-002 ownership | Replace with language respecting ADD-002 exclusivity | Critical | 1, 4 |
| 2 | §19.9 | Undermines gate enforceability | Remove contradictory "SHALL NOT claim" language | Critical | 3, 7 |
| 3 | §5.7 | Missing implementation schema | Add normative JSON schema for composition contract | High | 4, 9 |
| 4 | §20 | Lacks DCP mapping | Add mapping from adherence scale to DCP parameters | High | 4, 9 |
| 5 | §2.1 | Weak seam enforcement | Add violation consequences | Medium | 4, 6 |
| 6 | §9.4 | Missing DCP validation | Add DCP rejection rule for missing disclosure | Medium | 4, 7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document contains critical architectural violations (§16.7 contravenes ADD-002 ownership) and legal unenforceability (§19.9 contradicts normative gates), compounded by missing implementation schemas that prevent developer adoption.

**Top 3 Actions Required:**
1. Fix §16.7 to respect ADD-002's exclusive ownership of depth/VC semantics
2. Remove §19.9's contradictory language and strengthen the originality gate's enforceability
3. Add normative JSON schemas for composition contract, knowledge basis, and reference adherence controls
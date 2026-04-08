---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.13.0
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
| 1 | Cross-Document Consistency | 3 | Most terms match but §16.7 creates confusion about ADD-002 ownership boundaries. |
| 2 | Business Model Alignment | 4 | Clear premium gates and MPOA references, but §19.9 disclaimer may dilute commercial risk posture. |
| 3 | Legal Enforceability | 2 | §19 contains contradictory "SHALL NOT" obligations followed by disclaimer that could undermine enforcement. |
| 4 | Architectural Fidelity | 2 | Control-plane axes defined but JSON schemas missing; §5.9 table is insufficient for DCP validation. |
| 5 | Completeness | 3 | Covers all 12 axes but lacks implementation schemas and concrete validation rules for §18/§19 gates. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other documents, respects ADD-001/ADD-002 seams. |
| 7 | Practical Operability | 2 | Many "SHALL" rules lack concrete thresholds, states, or validation mechanisms for developers. |
| 8 | Style & Clarity | 3 | Structure is logical but document is overly dense with repetitive cross-references. |
| 9 | Developer Synchrony | 2 | No JSON schemas or concrete API contracts for composition contract, knowledge states, or adherence controls. |
| 10 | Platform Economics Synchrony | 4 | Clear premium BOOK gates and MPOA alignment for commercial features. |
| 11 | Friction Factor | 3 | Gate stacking in §18.11 is architecturally sound but may create excessive friction without clear policy thresholds. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane architecture** (§6 twelve-axis table) provides clear separation of concerns across ADD-001/ADD-002/ADD-003.
2. **Professional-use disclosure** (§9.4) establishes clear liability boundaries with mandatory text and export preservation rules.
3. **Reference-guided composition** (§20) correctly distinguishes structure/style adherence from model temperature with concrete 1-10 scale.
4. **Gate stacking logic** (§18.11) provides sensible sequencing for knowledge basis, reference disposition, and originality checks.

### Critical Gaps

1. **Missing implementation schemas**: No JSON schemas for composition contract (§5), knowledge states (§18), or adherence controls (§20), making DCP validation impossible.
2. **Contradictory legal posture**: §19.2 imposes "SHALL NOT" obligations but §19.9 disclaimer could be interpreted as waiving those same obligations.
3. **Unclear validation thresholds**: §18.5 knowledge states and §19.4 internal/external thresholds lack concrete numerical or policy-defined boundaries.
4. **Overly dense cross-referencing**: Every section repeats "[ADD-002]" references, creating readability issues without adding clarity.

---

## Article-by-Article Review

### §0 Status and intent

**Feedback:** Clear separation from ADD-001/ADD-002, but informative grounding references should be in a separate "Context" section, not the status table.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:** Move "Informative grounding" to a new §0.1 Context section. Keep status table focused on ratification status only.

### §1 Purpose

**Feedback:** Single 200+ word sentence is unreadable. Violates Style Guide §1 (clarity). Contains repetitive cross-references.

**Scores:** Style & Clarity: 1, Practical Operability: 2

**Recommendation:** Rewrite as 3-4 clear sentences:
"This addendum defines the composition control plane for governed artifact creation: messages, calendar invites, documents, and publications. It establishes composition contracts (§5), professional-use disclosure (§9.4), language controls (§16), measurement contracts (§17), knowledge basis gating (§18), originality verification (§19), and reference-guided composition (§20). These controls SHALL be read with ADD-002 for output depth, voice controls, packaging, and BOOK-specific gates. Informative context documents (listed in §0) provide R&D and architectural background."

### §5 Composition contract requirements

**Feedback:** §5.9 "Normative fields and validation posture" table is insufficient for DCP implementation. Missing JSON schema with required/optional fields, data types, and validation rules.

**Scores:** Architectural Fidelity: 2, Developer Synchrony: 1, Practical Operability: 2

**Recommendation:** Add §5.10 "Implementation schema" with:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CompositionContract",
  "type": "object",
  "required": ["role", "intent", "outcome"],
  "properties": {
    "role": {"type": "string", "minLength": 1},
    "intent": {"type": "string", "enum": ["inform", "request", "persuade", "document", "analyze", "propose", "coordinate", "approve", "publish", "teach"]},
    "outcome": {"type": "string", "minLength": 1},
    "audience": {"type": "string"},
    "action_mode": {"type": "string", "enum": ["DRAFT_ONLY", "SEND_READY", "PUBLISH_READY"]},
    "professional_review_required": {"type": "boolean"},
    "professional_domain": {"type": "string", "enum": ["legal", "tax", "compliance", "medical", "engineering", "other_licensed"]},
    "artifact_status": {"type": "string", "enum": ["draft_for_professional_review", "final"]}
  }
}
```

### §16.7 Shell and voice-first behavior

**Feedback:** Creates confusion about ADD-002 ownership. Language about "not altering underlying depth/VC definitions" is redundant since §2.1 already establishes seams.

**Scores:** Cross-Document Consistency: 2, Architectural Fidelity: 3

**Recommendation:** Simplify to: "§16 language controls SHALL NOT modify ADD-002 §4 output depth or §5 VC class definitions. The shell SHALL apply ADD-002 depth and VC controls to the active language surface."

### §18 Knowledge basis and discovery gating

**Feedback:** §18.5 states define meanings but lack concrete validation rules. What constitutes "sufficient" vs "partial"? No thresholds for "high" grounding tier.

**Scores:** Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Add §18.12 "Validation thresholds" with:
- "sufficient": >80% of required knowledge fields populated with verified sources
- "partial": 40-80% populated or unverified sources
- "insufficient": <40% populated
- Policy MAY override these defaults with tenant-specific rules.

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** Critical architectural flaw: §19.2 imposes "SHALL NOT" obligations but §19.9 disclaimer states "No waiver of §19.2/§19.4/§19.5" while also saying "those are legal determinations outside this addendum." This creates enforcement ambiguity.

**Scores:** Legal Enforceability: 1, Architectural Fidelity: 2

**Recommendation:** Rewrite §19.9 as:
"The runtime SHALL implement the verification gates in §19.2-19.5 as binding product obligations. This addendum does not guarantee absolute copyright compliance or non-infringement in all jurisdictions—those remain legal determinations outside product warranties. Permitted claims: originality verification, source-boundary control, non-reproduction gate, high-overlap review."

Also add concrete thresholds in §19.4:
- "high verbatim reproduction": >30% character overlap with any single source
- "high-overlap paraphrase": >50% structural similarity (section order, argument flow)
- Policy SHALL define stricter thresholds for external publish (e.g., >15% verbatim blocks publication).

### §20 Reference-guided composition

**Feedback:** Excellent distinction from model temperature (§20.11) and clear 1-10 scale (§20.13). Missing: JSON schema for reference_documents array and adherence controls.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 2

**Recommendation:** Add §20.16 "Implementation schema" with:
```json
{
  "reference_documents": {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["id", "role"],
      "properties": {
        "id": {"type": "string"},
        "role": {"type": "string", "enum": ["R1", "R2", "R3"]},
        "reference_mode": {"type": "string", "enum": ["structure_only", "style_only", "tone_only", "format_and_structure"]}
      }
    }
  },
  "reference_adherence": {"type": "integer", "minimum": 1, "maximum": 10},
  "structure_adherence": {"type": "integer", "minimum": 1, "maximum": 10},
  "style_adherence": {"type": "integer", "minimum": 1, "maximum": 10},
  "innovation_mode": {"type": "string", "enum": ["preserve", "improve", "reimagine"]}
}
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §1 | Unreadable 200+ word sentence | Rewrite as 3-4 clear sentences | Critical | 8 |
| 2 | §5 | Missing implementation schema | Add §5.10 with JSON schema for composition contract | Critical | 4,7,9 |
| 3 | §19 | Contradictory legal posture | Rewrite §19.9 to clarify obligations vs disclaimers | Critical | 3,4 |
| 4 | §18 | Unclear validation thresholds | Add §18.12 with concrete percentages for knowledge states | High | 7,9 |
| 5 | §19 | Missing overlap thresholds | Add concrete percentages for verbatim/structural overlap | High | 3,7 |
| 6 | §20 | Missing reference schema | Add §20.16 with JSON schema for reference controls | High | 4,9 |
| 7 | §16.7 | Redundant seam language | Simplify to clarify ADD-002 ownership | Medium | 1,4 |
| 8 | §0 | Informative grounding in status table | Move to separate §0.1 Context section | Low | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** Composite score of 2.8 with critical gaps in implementation schemas (Architectural Fidelity: 2), contradictory legal posture (Legal Enforceability: 2), and unclear validation thresholds (Practical Operability: 2).

**Top 3 Actions Required:**
1. Add JSON schemas for composition contract (§5), knowledge states (§18), and reference controls (§20) to enable DCP validation.
2. Fix contradictory legal language in §19.9 to clarify that "SHALL NOT" obligations are binding despite disclaimer.
3. Add concrete numerical thresholds for knowledge sufficiency (§18) and originality verification (§19) to make rules implementable.
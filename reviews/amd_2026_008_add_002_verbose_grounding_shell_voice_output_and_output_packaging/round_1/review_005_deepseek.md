---
review_id: REV-AMD-2026-008-ADD-002-001
document_reviewed: AMD-2026-008-ADD-002
document_version: 0.13.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-008-ADD-002 — Verbose Grounding, Shell Voice Output Control, and Output Packaging

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The twelve-axis table correctly references ADD-003 but lacks explicit binding to ADD-001 navigation classes for voice control mapping. |
| 2 | Business Model Alignment | 4 | Section 10.11 clearly separates base vs premium BOOK workflows with commercial gating aligned with MPOA. |
| 3 | Legal Enforceability | 2 | VC0-VC5 classes lack concrete implementation requirements and fail-closed semantics for unauthorized promotion. |
| 4 | Architectural Fidelity | 2 | Voice control classes are described as "shell affordances" but lack DCP transport definitions and JSON schemas for state transitions. |
| 5 | Completeness | 3 | Covers depth ladder and packaging but omits concrete promotion validation rules and error codes for unauthorized transitions. |
| 6 | Conflict Freedom | 4 | No direct conflicts with AMD-2026-008 or ADD-001; clear separation of concerns maintained. |
| 7 | Practical Operability | 2 | VC classes lack implementation mapping tables; BOOK workflow phases lack concrete state machine JSON schema. |
| 8 | Style & Clarity | 4 | Well-structured with clear tables; follows Style Guide conventions consistently. |
| 9 | Developer Synchrony | 3 | References ADD-003 but doesn't specify how packaging classes integrate with composition contract fields. |
| 10 | Platform Economics Synchrony | 4 | Premium BOOK gating clearly ties to MPOA commercial entitlements with proper feature class separation. |
| 11 | Friction Factor | 2 | Missing concrete validation rules creates risk of silent promotion bypassing governance gates. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Clear separation of concerns** - The twelve-axis table (Section 3) correctly partitions responsibilities between ADD-001 (navigation), ADD-002 (depth/voice/packaging), and ADD-003 (composition).
2. **Commercial gating architecture** - Section 10.11 provides excellent separation of base vs premium BOOK workflows with explicit entitlement mapping to MPOA.
3. **Structured workflow definition** - BOOK phases B0-B9 (Section 10.7) provide clear progression gates with mandatory human approval checkpoints.
4. **Style consistency** - Follows AIOS Style Guide with proper tables, cross-references, and canonical terminology.

### Critical Gaps

1. **Missing implementation bindings** - VC0-VC5 classes lack concrete JSON schemas, DCP transport definitions, and fail-closed validation rules.
2. **Incomplete promotion enforcement** - Section 9 states "SHALL NOT promote" but lacks concrete validation mechanisms and error codes.
3. **No voice segmentation specification** - Section 10.9 requires "navigable voice segmentation" but provides no technical definition or implementation requirements.
4. **Packaging-class integration gaps** - Missing explicit binding between packaging classes (TXT, MD, PDF, etc.) and ADD-003 composition contract fields.

---

## Article-by-Article Review

### Section 3: Control-plane model (twelve axes)

**Feedback:** The table correctly references ADD-003 for composition classes but fails to specify how Axis 2 (Output depth) and Axis 3 (Shell voice controls) integrate with Axis 1 (Navigation class from ADD-001). There's no mapping table showing which VC classes are valid for which navigation states (e.g., VC5 segment navigation only valid for BOOK depth).

**Scores:** Cross-Document Consistency: 3, Architectural Fidelity: 3

**Recommendation:** Add a mapping table showing valid VC classes per navigation class and depth level. Add explicit reference: "VC classes SHALL be invoked only when the active navigation class permits them per ADD-001 §4."

### Section 4: Output depth ladder

**Feedback:** The V0-V4 ladder is clear but lacks concrete validation rules. Missing: maximum word counts per level, explicit promotion triggers, and error codes for unauthorized promotion attempts. No reference to how depth levels map to ADD-003 composition classes.

**Scores:** Practical Operability: 2, Completeness: 3

**Recommendation:** Add normative validation table:
| Depth | Max Words | Promotion Triggers | Error Code (unauthorized) |
|-------|-----------|-------------------|---------------------------|
| V0 | 50 | User request, policy | `DEPTH_PROMOTION_UNAUTHORIZED` |
| V1 | 200 | VC2, workflow | `DEPTH_EXCEEDS_AUTHORIZATION` |
| V2 | 1000 | Export intent, VC3 | `DEPTH_REQUIRES_CONTRACT` |
| V3 | 5000 | BOOK workflow entry | `DEPTH_REQUIRES_TOC_APPROVAL` |
| V4 | Unlimited | B3 TOC approval | `BOOK_NOT_APPROVED` |

### Section 5: Shell voice control classes

**Feedback:** VC0-VC5 are described as "shell affordances" but lack concrete implementation requirements. Missing: JSON schema for VC state, DCP transport binding, mapping to actual shell UI controls, and fail-closed semantics when VC invocation is invalid.

**Scores:** Architectural Fidelity: 1, Legal Enforceability: 2

**Recommendation:** Add normative implementation requirements:
1. "Each VC class SHALL have a defined JSON schema for state representation."
2. "VC state transitions SHALL be transported via DCP with codes `aios.dcp.vc.{class}.{action}`."
3. "Invalid VC invocations SHALL return error code `VC_INVALID_FOR_STATE` with current navigation class and depth level."
4. Add mapping table: VC class → required shell UI control → valid navigation classes.

### Section 7: Output packaging classes

**Feedback:** Clear definitions but missing integration with ADD-003 composition contract. No specification of which packaging classes are valid for which composition classes (e.g., EMAIL can't export as PDF for send action).

**Scores:** Developer Synchrony: 3, Practical Operability: 3

**Recommendation:** Add cross-reference table to ADD-003:
| Packaging Class | Valid Composition Classes | Notes |
|-----------------|--------------------------|-------|
| TXT | All | Default fallback |
| MD | DOCUMENT.*, POST, BLOG, ARTICLE, BOOK | Preferred for documentation |
| PDF | DOCUMENT.*, BOOK, REPORT | Requires ADD-003 §9.4 disclosure when professional-use |
| DOCX | DOCUMENT.*, BOOK | Editable business documents |
| JSON | System interchange only | Not for human consumption |
| HTML | POST, BLOG, ARTICLE, NEWSLETTER | Web publishing |

### Section 9: Promotion rules

**Feedback:** States "SHALL NOT promote" but lacks concrete validation mechanism. Missing: promotion validation function specification, error codes, and audit logging requirements.

**Scores:** Legal Enforceability: 2, Friction Factor: 2

**Recommendation:** Add normative validation function:
```json
{
  "current_depth": "V0",
  "requested_depth": "V2",
  "authorization_source": "user_request",
  "valid": true,
  "required_gates": ["composition_contract"],
  "error_code": null
}
```
Add: "Unauthorized promotion attempts SHALL log audit event `PROMOTION_DENIED` with source, current state, and requested state."

### Section 10: BOOK approval and review gates

**Feedback:** Excellent workflow definition but lacks concrete state machine JSON schema and DCP transport codes. Section 10.9 mentions "navigable voice segmentation" but provides no technical specification.

**Scores:** Architectural Fidelity: 3, Practical Operability: 3

**Recommendation:** 
1. Add JSON schema for BOOK state machine with fields: `phase`, `toc_approved`, `chapters_approved`, `assembly_status`, `export_ready`.
2. Define DCP codes: `aios.dcp.book.phase_transition`, `aios.dcp.book.toc_approved`, `aios.dcp.book.chapter_approved`.
3. Add technical specification for voice segmentation: "BOOK voice segmentation SHALL use chapter/section boundaries with unique IDs for VC5 navigation. Each segment SHALL have: `segment_id`, `title`, `word_count`, `duration_estimate`."

### Section 10.11: Base and premium BOOK workflows

**Feedback:** Excellent commercial gating architecture. Clear separation of entitlements. Missing: concrete entitlement check function and error codes for unauthorized premium actions.

**Scores:** Business Model Alignment: 5, Platform Economics Synchrony: 5

**Recommendation:** Add entitlement validation specification:
```json
{
  "action": "add_images",
  "required_entitlement": "premium_enhancement",
  "user_entitlements": ["standard_authoring"],
  "authorized": false,
  "error_code": "ENTITLEMENT_REQUIRED",
  "upgrade_path": "premium_tier"
}
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 5 | VC classes lack implementation specs | Add JSON schemas, DCP codes, and validation tables | Critical | 3,4,7,11 |
| 2 | Section 4 | Missing promotion validation | Add concrete validation rules with error codes | Critical | 4,5,7,11 |
| 3 | Section 10.9 | No voice segmentation spec | Define technical requirements for navigable segments | High | 4,5,7 |
| 4 | Section 7 | Packaging-class integration gaps | Add cross-reference table to ADD-003 composition classes | Medium | 1,9 |
| 5 | Section 3 | Missing axis integration | Add mapping table for VC × navigation × depth | Medium | 1,4 |
| 6 | Section 10.11 | Missing entitlement validation | Add concrete check function and error codes | Medium | 3,7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has strong conceptual architecture but lacks concrete implementation specifications, validation rules, and technical bindings required for governed execution. Critical gaps in VC class implementation and promotion enforcement prevent practical operability.

**Top 3 Actions Required:**
1. Add concrete JSON schemas and DCP transport definitions for VC0-VC5 classes with fail-closed validation.
2. Implement promotion validation rules with specific error codes and audit logging requirements.
3. Define technical specifications for BOOK voice segmentation and state machine implementation.
---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.4
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
| 1 | Cross-Document Consistency | 3 | Multiple cross-references to ADD-002 are correct, but §16.7 seam language creates ambiguity about ownership of depth/VC semantics. |
| 2 | Business Model Alignment | 4 | Clear premium gates and entitlement mapping in §10.11 references, but lacks specific SLA numbers for review workflows. |
| 3 | Legal Enforceability | 2 | Professional-use disclosure (§9.4) is strong, but §19 originality gate lacks concrete thresholds and relies on external OPS-020 without binding integration. |
| 4 | Architectural Fidelity | 2 | Control-plane axes (§6) are well-defined, but JSON schemas are deferred to annexes without normative binding, creating implementation ambiguity. |
| 5 | Completeness | 3 | Covers all promised axes from architecture memo, but §18.11 sequence lacks DCP pipeline integration points and fails to define "substantive drafting" threshold. |
| 6 | Conflict Freedom | 4 | No direct contradictions with parent AMD-2026-008 or ADD-002, though §16.7 creates tension about VC semantics ownership. |
| 7 | Practical Operability | 2 | Many SHALL rules lack implementable validation logic; §5.9 fail-closed table is descriptive but missing error codes and DCP transport bindings. |
| 8 | Style & Clarity | 3 | Follows Style Guide generally but suffers from excessive inline emphasis formatting and repetitive seam declarations. |
| 9 | Developer Synchrony | 3 | Control-plane axes map to product concepts, but missing concrete JSON Schema references for composition contract fields. |
| 10 | Platform Economics Synchrony | 4 | Clear premium BOOK workflow gates (§10.11) and MPOA references align with commercial model. |
| 11 | Friction Factor | 2 | Overly complex gate stacking (§18.11) with 6+ sequential checks before drafting creates high cognitive load for implementers. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane architecture** (§6 twelve-axis table) provides clear separation of concerns across the AMD-2026-008 addendum family.
2. **Professional-use disclosure framework** (§9.4) establishes rigorous mandatory labeling for licensed-professional contexts with export preservation rules.
3. **Reference-guided composition controls** (§20.11-20.15) correctly distinguish structure/style adherence from model temperature with clear 1-10 scale.
4. **Clear premium entitlement mapping** (§10.11 references to ADD-002) properly gates enhancement/publishing capabilities separate from base authoring.

### Critical Gaps

1. **Missing normative JSON Schemas**: Composition contract (§5), knowledge basis (§18), and originality evaluation (§19) fields are described conceptually but lack binding schemas, making validation unenforceable.
2. **Incomplete DCP pipeline integration**: §18.11 sequence mentions "DCP outcome codes" but doesn't define transport bindings or error handling for fail-closed scenarios.
3. **Ambiguous "substantive drafting" threshold**: Multiple sections (§5.3, §18.1) gate "substantive drafting" but never define what constitutes scaffold vs. substantive output.
4. **Over-reliance on external OPS-020**: §19 originality gate delegates thresholds and scoring to AIOS-OPS-020 without binding the current version or defining fallback behavior if OPS-020 is unavailable.

---

## Article-by-Article Review

### §0 Status and intent

**Feedback:** Clear separation from ADD-001/ADD-002, but informative grounding references to architecture/surface memos should be marked as non-normative more prominently.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:** Add explicit "(non-normative)" label after each memo reference in the table: "AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001 (non-normative)".

### §2.1 Addendum seams

**Feedback:** Correctly defines ownership boundaries but repeats the same seam declarations excessively throughout document.

**Scores:** Architectural Fidelity: 5, Style & Clarity: 2

**Recommendation:** Consolidate all seam rules into §2.1 and reference it from other sections rather than repeating. Change §16.7 from "§16 governs only language mode..." to "Language controls in §16 SHALL NOT alter ADD-002 §4 depth or §5 VC semantics per §2.1."

### §5 Composition contract requirements

**Feedback:** Role/intent/outcome triad is architecturally sound, but §5.7 defers JSON examples to Annex A without normative binding, making field validation impossible.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Add normative JSON Schema reference in §5.7: "Products SHALL validate composition contracts against JSON Schema `composition-contract-v1.json` (registered at [URI]) with required fields: `role`, `intent`, `outcome`, `artifact_class`."

### §5.9 Normative fields and validation posture

**Feedback:** Fail-closed table is useful but lacks DCP error codes and transport binding for auditability.

**Scores:** Practical Operability: 2, Architectural Fidelity: 3

**Recommendation:** Add DCP namespace and error code column to table:
| Condition | Enforcement outcome | DCP error code |
|-----------|---------------------|----------------|
| Mandatory composition contract fields missing | SHALL not proceed to substantive drafting | `COMP_CONTRACT_MISSING` |

### §9.4 Professional-use draft disclosure

**Feedback:** Strong disclosure framework with clear mandatory text, but §9.4.0 trigger determinism is overly complex with 3-level precedence.

**Scores:** Legal Enforceability: 4, Practical Operability: 3

**Recommendation:** Simplify §9.4.0 to binary trigger: "Professional-use treatment SHALL apply when ANY of: (a) document subclass is CONTRACT_SUMMARY, POLICY, or RESEARCH_REPORT; (b) `professional_review_required` metadata field is true; (c) user explicitly classifies artifact as professional-use."

### §16.7 Shell and voice-first behavior

**Feedback:** Creates ambiguity about VC semantics ownership despite §2.1 declaration.

**Scores:** Cross-Document Consistency: 2, Architectural Fidelity: 2

**Recommendation:** Rewrite to eliminate ambiguity: "Language selection SHALL NOT alter the active output depth (ADD-002 §4) or VC class semantics (ADD-002 §5). The shell SHALL apply current depth and VC settings to the active language surface without redefining ADD-002 semantics."

### §18 Knowledge basis and discovery gating

**Feedback:** Conceptually sound but §18.11 sequence lacks DCP integration points and doesn't define "substantive drafting" threshold.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2, Completeness: 2

**Recommendation:** Add to §18.11: "Substantive drafting SHALL be defined as output beyond scaffold (§5.4) that asserts factual claims, makes recommendations, or represents the artifact as complete for its intended use." Add DCP state transition points: "After step 1 (composition contract), runtime SHALL emit `DCP_STATE_CONTRACT_RESOLVED`; after step 5 (creation mode), runtime SHALL emit `DCP_STATE_KB_SUFFICIENT` or `DCP_STATE_KB_INSUFFICIENT`."

### §19 Originality and source-boundary verification

**Feedback:** Delegates implementation entirely to OPS-020 without binding version or defining fallback, making §19 unenforceable as standalone governance.

**Scores:** Legal Enforceability: 1, Practical Operability: 1, Architectural Fidelity: 2

**Recommendation:** Add binding version reference in §19.10: "Products claiming §19 conformance SHALL implement AIOS-OPS-020 v0.3.1 or later, and SHALL fail closed with error `ORIGINALITY_EVAL_UNAVAILABLE` if the evaluation service is unavailable when §19.2 applies."

### §20 Reference-guided composition

**Feedback:** Excellent separation of structure/style adherence from model temperature, but §20.4 fields lack schema binding.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 3

**Recommendation:** Add normative schema reference: "`reference_adherence` field SHALL be integer 1-10; `structure_adherence` and `style_adherence` SHALL be optional integers 1-10 when split controls are used."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §5.7, §18.9, §20.4 | Missing normative JSON Schemas | Add binding JSON Schema references for composition contract, knowledge basis, and reference adherence fields | Critical | 4, 7, 9 |
| 2 | §19.10 | Over-reliance on external OPS-020 | Add binding version requirement and fail-closed behavior if OPS-020 unavailable | Critical | 3, 4, 7 |
| 3 | §18.1, §5.3 | Undefined "substantive drafting" threshold | Add clear definition distinguishing scaffold (§5.4) from substantive output | High | 4, 5, 7 |
| 4 | §5.9, §18.11 | Missing DCP integration points | Add DCP error codes and state transition events to fail-closed table and gate sequences | High | 4, 7, 9 |
| 5 | §16.7 | Ambiguity about VC semantics ownership | Rewrite to eliminate any suggestion that §16 can alter ADD-002 definitions | Medium | 1, 4 |
| 6 | §9.4.0 | Overly complex trigger determinism | Simplify to binary trigger conditions | Medium | 7, 11 |
| 7 | Throughout | Excessive inline emphasis formatting | Remove bold/italic emphasis from normative text except defined terms | Low | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** While the document establishes a comprehensive architectural framework, critical gaps in normative schemas, DCP integration, and binding external dependencies render it unimplementable in its current form, with Architectural Fidelity (2) and Practical Operability (2) scores below acceptable thresholds.

**Top 3 Actions Required:**
1. Add binding JSON Schema references for composition contract, knowledge basis, and reference adherence fields to make validation enforceable.
2. Define fail-closed behavior and binding version requirements for the §19 originality gate's dependency on external OPS-020.
3. Add DCP error codes and state transition events to §5.9 and §18.11 to enable auditable control-plane implementation.
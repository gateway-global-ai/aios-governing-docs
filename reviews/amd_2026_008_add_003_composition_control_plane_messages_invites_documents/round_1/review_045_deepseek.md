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
| 1 | Cross-Document Consistency | 3 | Multiple cross-references to ADD-002 are correct, but §16.7 seam language creates ambiguity about ownership of depth/VC semantics. |
| 2 | Business Model Alignment | 4 | Clear alignment with MPOA for professional-use disclosure and premium BOOK workflows via ADD-002 references. |
| 3 | Legal Enforceability | 2 | §19.9 disclaimer creates tension with §19.2-§19.5 enforcement obligations, potentially weakening operational mandates. |
| 4 | Architectural Fidelity | 2 | Control-plane axes (§6) correctly separate concerns, but §5.9 fail-closed table references external DCP codes without defining transport envelope requirements. |
| 5 | Completeness | 3 | Covers all promised areas but §18.11 sequence lacks concrete implementation hooks for state transitions between grounding and originality gates. |
| 6 | Conflict Freedom | 2 | §19.9 "no waiver" language conflicts with §19.2 enforcement posture by creating ambiguity about what is actually required. |
| 7 | Practical Operability | 3 | Conceptual fields are defined but lack concrete JSON Schema or implementation mapping for mandatory composition contract validation. |
| 8 | Style & Clarity | 4 | Generally clear with good section organization, though some sections are overly verbose with repetitive seam statements. |
| 9 | Developer Synchrony | 3 | References AIOS-OPS-020 for implementation details, but §5.9 fail-closed table assumes DCP transport without defining minimum envelope. |
| 10 | Platform Economics Synchrony | 4 | Properly defers premium features to ADD-002 §10.11 and commercial terms to MPOA. |
| 11 | Friction Factor | 3 | Multiple mandatory gates (§5, §18, §19, §20) create complex sequencing that may overwhelm simple use cases. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane model** (§6) correctly separates twelve axes with clear ownership boundaries between ADD-001, ADD-002, and this addendum.
2. **Professional-use disclosure framework** (§9.4) provides clear, actionable requirements for licensed-professional contexts with proper MPOA alignment.
3. **Reference-guided composition controls** (§20.11-§20.15) correctly distinguish structure/style adherence from model temperature, addressing a common implementation confusion.
4. **Knowledge basis gating** (§18) establishes important "discover before create" principle with practical sufficiency states.

### Critical Gaps

1. **§19.9 disclaimer undermines enforcement** by creating legal ambiguity that could be interpreted to weaken the operational SHALL/MUST NOT requirements in §19.2-§19.5.
2. **Missing transport envelope definition** in §5.9 fail-closed table references DCP codes from AIOS-OPS-020 §13 but doesn't define minimum envelope fields for validation.
3. **§16.7 seam language is contradictory** stating "language does not alter depth/VC" while also saying shell "SHALL apply the current depth and VC settings" - this creates implementation ambiguity.
4. **§18.11 sequence lacks concrete state transition hooks** between knowledge basis sufficiency and originality verification, making the gate stack difficult to implement.

---

## Article-by-Article Review

### §0 Status and intent

**Feedback:** Clear separation of concerns with proper references to other addenda. The informative grounding pointers to architecture/surface memos are appropriate for Round 1.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 4

**Recommendation:** Add explicit note that AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001 §2 (bounded domains) is the authoritative source for seam boundaries.

### §2.1 Addendum seams

**Feedback:** Generally correct but repetitive. The same seam statements appear in multiple sections (§2.1, §16.7, etc.), creating maintenance burden.

**Scores:** Architectural Fidelity: 4, Style & Clarity: 3

**Recommendation:** Consolidate all seam definitions to §2.1 and reference it from other sections rather than repeating. Add: "For authoritative seam boundaries and dependency mapping, see AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001 §2 (bounded domains table)."

### §5.9 Normative fields and validation posture

**Feedback:** The fail-closed table correctly identifies mandatory gates but references external DCP codes without defining transport requirements. This creates implementation risk.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Add minimum transport envelope definition: "Implementations emitting §5.9 fail-closed codes SHALL include at minimum: `dcp_namespace` (string), `dcp_code` (string from AIOS-OPS-020 §13/§10), `artifact_id` (optional string), `trace_id` (optional string). Empty or missing `dcp_code` SHALL NOT be treated as success."

### §16.7 Shell and voice-first behavior

**Feedback:** Contradictory language: "language does not alter depth/VC" vs "shell SHALL apply the current depth and VC settings." This creates ambiguity about whether language changes can trigger depth/VC changes.

**Scores:** Cross-Document Consistency: 2, Architectural Fidelity: 2

**Recommendation:** Rewrite for clarity: "Language selection SHALL NOT redefine ADD-002 §4 depth class or §5 VC semantics. The shell SHALL track `output_language` for editing and voice delivery while preserving the active depth and VC settings established under ADD-002."

### §18.11 Recommended sequence

**Feedback:** The A/B sequence correctly orders gates but lacks concrete implementation hooks for state transitions. No mechanism defined for joining §18 knowledge basis results with §19 originality evaluation.

**Scores:** Practical Operability: 2, Architectural Fidelity: 3

**Recommendation:** Add implementation requirement: "When §19.2 applies, the `OriginalityEvaluationRecordV1` (AIOS-OPS-020 §9) SHALL reference the same composed artifact identifier and SHALL include knowledge-basis metadata reference when §18 also applied, enabling audit join between grounding and originality results."

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** §19.2-§19.5 establish strong operational requirements, but §19.9 disclaimer creates legal ambiguity that could undermine enforcement. The "no waiver" language attempts to preserve obligations but creates contradictory messaging.

**Scores:** Legal Enforceability: 1, Conflict Freedom: 1, Practical Operability: 3

**Recommendation:** Restructure §19.9 to clearly separate product obligations from legal disclaimers: "§19.2-§19.5 establish binding product obligations for release-time gating. Nothing in this addendum warrants or guarantees absolute copyright compliance, guaranteed uniqueness, or guaranteed non-infringement in all jurisdictions—those are legal determinations outside typical product warranties."

### §20.14 Maximum adherence and the originality gate

**Feedback:** Correctly states that high reference adherence doesn't bypass §19 verification, but doesn't address the tension between structural conformity requirements and originality thresholds.

**Scores:** Architectural Fidelity: 4, Conflict Freedom: 3

**Recommendation:** Add explicit policy requirement: "Policy SHALL define how structural conformity requirements (e.g., court-mandated forms at adherence 10) interact with §19 originality thresholds, including any necessary exceptions or review procedures."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.9 | Disclaimer undermines enforcement obligations | Restructure to clearly separate product obligations from legal disclaimers | Critical | 3, 6 |
| 2 | §5.9 | Missing transport envelope definition | Add minimum envelope fields for DCP fail-closed codes | High | 4, 7, 9 |
| 3 | §16.7 | Contradictory seam language | Rewrite for clarity about language vs depth/VC ownership | High | 1, 4 |
| 4 | §18.11 | Lack of state transition hooks | Add requirement for joining knowledge basis and originality records | Medium | 4, 7 |
| 5 | §2.1 | Repetitive seam statements | Consolidate to single reference to architecture memo | Low | 8 |
| 6 | §20.14 | Tension between conformity and originality | Add policy requirement for handling structural conformity exceptions | Medium | 4, 6 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** §19.9 creates a critical conflict that undermines the enforceability of originality verification requirements, and §5.9 lacks necessary transport definitions for fail-closed implementation.

**Top 3 Actions Required:**
1. Restructure §19.9 to eliminate ambiguity between product obligations and legal disclaimers.
2. Define minimum transport envelope requirements in §5.9 for DCP fail-closed codes.
3. Clarify §16.7 language to resolve contradictory statements about depth/VC ownership.
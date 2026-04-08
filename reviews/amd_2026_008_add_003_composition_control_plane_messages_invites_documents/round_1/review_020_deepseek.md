---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.1
reviewer: DeepSeek
review_date: 2026-04-08
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with ADD-001/ADD-002 seams, but §19.10 references a non-existent operations standard (AIOS-OPS-020) that doesn't match the provided context document. |
| 2 | Business Model Alignment | 3 | Clear premium gates for BOOK workflows, but lacks specific SLA numbers or enforcement mechanisms for originality verification. |
| 3 | Legal Enforceability | 2 | Professional-use disclosure is strong, but originality verification lacks concrete thresholds and relies on deferred implementation standards. |
| 4 | Architectural Fidelity | 3 | Good separation of concerns, but §5.9 fail-closed table mixes conceptual fields with implementation details without clear validation schemas. |
| 5 | Completeness | 4 | Covers all twelve axes comprehensively, though §19 originality verification defers critical numeric thresholds to future versions. |
| 6 | Conflict Freedom | 5 | No contradictions with parent AMD-2026-008 or referenced addenda; respects supremacy clauses. |
| 7 | Practical Operability | 2 | Many "SHALL" statements lack implementable validation rules; originality verification has no scoring algorithms; reference adherence scale (1-10) lacks mapping to actual model parameters. |
| 8 | Style & Clarity | 3 | Structurally sound but overly dense; §5.9 table mixes normative intent with implementation hints; cross-references to informative memos clutter the normative text. |
| 9 | Developer Synchrony | 3 | Clear conceptual fields but missing JSON schemas for composition contracts and validation states. |
| 10 | Platform Economics Synchrony | 4 | Good alignment with MPOA for premium BOOK workflows and professional-use liability. |
| 11 | Friction Factor | 2 | Excessive governance overhead for simple compositions; §18 knowledge basis gating may block legitimate use cases without clear policy exceptions. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane architecture** (§6 twelve-axis table) clearly separates navigation, depth, composition classes, and specialized gates.
2. **Strong professional-use disclosure framework** (§9.4) with mandatory text and export preservation rules.
3. **Clear dependency mapping** with ADD-001/ADD-002, avoiding definition duplication.
4. **Reference-guided composition** (§20) provides innovative structure/style adherence controls distinct from model temperature.

### Critical Gaps

1. **§19 originality verification lacks implementable thresholds** - references AIOS-OPS-020 which in context shows deferred numeric scoring (v0.3.0).
2. **§5.9 fail-closed table mixes abstraction levels** - combines conceptual fields with implementation hints without clear validation schemas.
3. **Reference adherence scale (1-10) has no technical mapping** - no guidance on how to implement structural vs style adherence in model prompts or shell controls.
4. **§18 knowledge basis gating is overly restrictive** - may block legitimate draft creation without clear policy exceptions for different artifact classes.

---

## Article-by-Article Review

### §0 Status and intent

**Feedback:** The table correctly positions this addendum relative to ADD-001/ADD-002, but includes "informative grounding" references to implementation memos that should not appear in normative text. These belong in cross-references YAML, not the status table.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:** Remove the "Informative grounding" row from §0 table. Move AIOS-COMPOSITION-CONTROL-* memo references to the cross_references YAML field only.

### §2.1 Addendum seams

**Feedback:** Correctly delegates output depth and VC classes to ADD-002, but doesn't explicitly forbid this addendum from redefining those terms. The negative prohibition is implied but should be explicit.

**Scores:** Architectural Fidelity: 4, Cross-Document Consistency: 5

**Recommendation:** Add explicit "SHALL NOT" language: "This addendum SHALL NOT redefine output depth ladder steps (RESPONSE...BOOK), shell voice control classes (VC0-VC5), or packaging classes as defined in ADD-002."

### §5 Composition contract requirements

**Feedback:** The triad (role, intent, outcome) is architecturally sound, but §5.9 creates confusion by mixing conceptual fields with implementation validation. The table includes "Minimum conceptual fields" but then adds "Validation posture" which belongs in a separate implementation standard.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2

**Recommendation:** Split §5.9 into two sections: (1) normative field requirements (conceptual only), and (2) implementation validation rules (to be defined in a separate operations standard). Provide a clear JSON Schema reference for the composition contract.

### §5.9 Fail-closed rejection semantics

**Feedback:** The table mixes abstraction levels dangerously. "Mandatory composition contract fields missing or invalid" is a conceptual rule, but "SHALL not proceed to substantive drafting except via explicit §5.4 scaffold/outline path" is an implementation rule. No error codes or DCP bindings are provided.

**Scores:** Practical Operability: 1, Developer Synchrony: 2

**Recommendation:** Replace the entire table with: (1) A clear list of mandatory conceptual fields per artifact class, (2) Reference to a separate operations standard (e.g., "AIOS-OPS-021: Composition Contract Validation") that defines validation schemas, error codes, and DCP bindings.

### §16 Language, localization, and authoritative version control

**Feedback:** L0-L3 modes are well-defined, but §16.7 creates unnecessary complexity by stating what language controls "SHALL NOT" do relative to ADD-002. This is defensive writing that should be unnecessary if seams are properly defined in §2.1.

**Scores:** Style & Clarity: 3, Architectural Fidelity: 4

**Recommendation:** Simplify §16.7 to: "Language selection SHALL NOT alter the active output depth class or VC semantics defined in ADD-002. The shell SHALL apply ADD-002 depth and VC controls to the active language surface."

### §18 Knowledge basis and discovery gating

**Feedback:** The "discover before create" principle is architecturally sound, but the implementation is overly restrictive. §18.11 sequence requires resolving reference disposition (§20) before substantive drafting, which may create circular dependencies when references themselves need knowledge basis checking.

**Scores:** Practical Operability: 2, Friction Factor: 1

**Recommendation:** Add policy exceptions: "For artifact classes MEMO, CHECKLIST, and internal EMAIL, policy MAY allow substantive drafting with partial knowledge basis (state: 'partial') when user explicitly acknowledges assumptions."

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** Critical architectural flaw: §19.10 references ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD (AIOS-OPS-020) as the "default registered home," but the provided context shows this standard is at v0.2.0 with deferred numeric thresholds. This creates a circular dependency where normative rules reference unimplemented standards.

**Scores:** Architectural Fidelity: 2, Practical Operability: 1

**Recommendation:** Either: (1) Define minimum implementable thresholds in this addendum (e.g., "For external channels, verbatim overlap >15% SHALL trigger 'overlap_review_required'"), or (2) Create a placeholder operations standard with concrete scoring algorithms before ratifying this addendum.

### §19.4 Internal vs external thresholds

**Feedback:** Requires policy to define thresholds but provides no guidance on what constitutes "stricter" rules for external channels. The bridge to §19.9 creates confusion about whether the non-waiver language weakens enforcement obligations.

**Scores:** Legal Enforceability: 2, Style & Clarity: 3

**Recommendation:** Add concrete examples: "For example, policy MAY define: internal drafts allow up to 30% verbatim overlap from any single source, while external publish requires <10% verbatim overlap and <25% structural similarity."

### §20 Reference-guided composition

**Feedback:** The 1-10 adherence scale is innovative but lacks technical implementation guidance. No mapping to model parameters, prompt engineering, or shell controls. §20.14 correctly notes that maximum adherence doesn't authorize reproduction, but doesn't specify how to enforce this distinction technically.

**Scores:** Developer Synchrony: 2, Practical Operability: 2

**Recommendation:** Add an implementation note: "Reference adherence SHALL be implemented through prompt engineering that emphasizes structural patterns over verbatim reproduction, potentially using retrieval-augmented generation with strict source attribution."

### §20.11-20.15 Reference adherence controls

**Feedback:** Correctly distinguishes adherence from model temperature, but provides no guidance on how to implement the 1-10 scale. The split structure/style adherence is conceptually sound but doubles the implementation complexity without clear use cases.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2

**Recommendation:** Simplify to a single 1-10 scale initially, with clear mapping to implementation: "Level 1-3: Use reference for general inspiration only; Level 4-7: Preserve section order and heading hierarchy; Level 8-10: Maintain exact structural conformity where policy permits."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.10 | References unimplemented operations standard | Define minimum originality thresholds in this addendum or create implemented standard first | Critical | 4, 7, 9 |
| 2 | §5.9 | Mixes conceptual fields with implementation rules | Split into normative requirements and separate validation standard | High | 4, 7, 8 |
| 3 | §20.13 | 1-10 adherence scale lacks technical mapping | Add implementation guidance for prompt engineering and shell controls | High | 7, 9 |
| 4 | §18 | Overly restrictive knowledge basis gating | Add policy exceptions for lower-stakes artifact classes | Medium | 7, 11 |
| 5 | §0 | Informative memos in normative text | Move implementation memo references to YAML only | Medium | 8 |
| 6 | §19.4 | Lacks concrete threshold examples | Add illustrative numeric examples for verbatim overlap limits | Medium | 3, 7 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has strong architectural foundations but fails on practical operability due to deferred implementation standards (§19) and mixed abstraction levels (§5.9). The originality verification framework references unimplemented operations standards, creating unenforceable "SHALL" statements.

**Top 3 Actions Required:**
1. Resolve the §19.10 circular dependency by either defining minimum originality thresholds in this addendum or ensuring AIOS-OPS-020 has concrete scoring algorithms before ratification.
2. Clean up §5.9 to separate conceptual field requirements from implementation validation rules.
3. Add technical implementation guidance for the reference adherence scale (1-10) with clear mapping to model parameters or prompt engineering patterns.
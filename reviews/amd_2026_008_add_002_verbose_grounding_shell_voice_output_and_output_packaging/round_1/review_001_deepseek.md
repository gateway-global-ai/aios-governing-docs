---
review_id: REV-AMD-2026-008-ADD-002-001
document_reviewed: AMD-2026-008-ADD-002
document_version: 0.13.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: AMD-2026-008-ADD-002 — Verbose Grounding, Shell Voice Output Control, and Output Packaging

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with ADD-001 and ADD-003, but some packaging references need tighter integration with composition classes. |
| 2 | Business Model Alignment | 5 | Excellent separation of base vs premium BOOK workflows with clear entitlement gating and MPOA alignment. |
| 3 | Legal Enforceability | 3 | Some "SHALL" statements lack specific enforcement mechanisms for shell controls and promotion rules. |
| 4 | Architectural Fidelity | 4 | Clear separation of concerns between depth, voice controls, and packaging aligns with DCP principles. |
| 5 | Completeness | 4 | Covers all promised axes but lacks JSON schemas for state machines and packaging metadata. |
| 6 | Conflict Freedom | 5 | No contradictions found with parent amendment or referenced documents. |
| 7 | Practical Operability | 3 | VC classes and promotion rules need more specific implementation guidance for shell developers. |
| 8 | Style & Clarity | 4 | Well-structured with clear tables, but some sections are overly verbose with illustrative examples. |
| 9 | Developer Synchrony | 4 | Control-plane model provides clear interfaces, but missing concrete API specifications. |
| 10 | Platform Economics Synchrony | 5 | Premium BOOK gating perfectly aligns with MPOA commercial tiers and entitlement models. |
| 11 | Friction Factor | 3 | Complex BOOK workflow (B0-B9) may create excessive friction for simple long-form generation. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

1. **Excellent control-plane architecture** (Section 3): The twelve-axis model provides clear separation of concerns between navigation, depth, voice controls, packaging, and composition classes.
2. **Strong commercial alignment** (Section 10.11): Clear distinction between base authoring and premium enhancement/publishing workflows with proper entitlement gating.
3. **Architectural rigor** (Sections 4-5): Output depth ladder (V0-V4) and shell voice controls (VC0-VC5) are well-defined and orthogonal to composition classes.
4. **BOOK workflow governance** (Section 10): Mandatory approval gates (TOC, chapter, final) ensure human-guided co-authorship rather than opaque single-pass generation.

### Critical Gaps

1. **Missing enforcement mechanisms**: The document states "SHALL" for shell controls but doesn't specify how violations are detected or remediated.
2. **Incomplete packaging-class mapping**: Section 7 defines packaging formats but doesn't specify which composition classes (ADD-003) support which packaging options.
3. **Overly complex state transitions**: The BOOK workflow (B0-B9) has 10 phases which may be excessive for practical implementation.
4. **Lack of technical schemas**: No JSON schemas for packaging metadata, BOOK state machine, or VC control mappings.

---

## Article-by-Article Review

### Section 3: Control-plane model (twelve axes)

**Feedback:** Excellent architectural decomposition. The twelve-axis table clearly shows the separation of concerns between ADD-001 (navigation), ADD-002 (depth/voice/packaging), and ADD-003 (composition). However, the "Scope" column is inconsistent - some entries describe the axis while others list examples.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 4, Completeness: 4

**Recommendation:** Standardize the "Scope" column to consistently describe the axis purpose rather than mixing descriptions and examples. Add a note clarifying that axis 12 (reference-guided composition) is governed by ADD-003 §20 but referenced here for completeness.

### Section 4: Output depth ladder

**Feedback:** Well-defined progression from V0 (RESPONSE) to V4 (BOOK). The "Allowed" and "Use when" columns provide clear guidance. However, the transition from V3 (BRIEF) to V4 (BOOK) is abrupt - there's no intermediate level for medium-length structured documents.

**Scores:** Architectural Fidelity: 4, Practical Operability: 3, Completeness: 4

**Recommendation:** Consider adding a V3.5 level for "REPORT" or "WHITEPAPER" that has structured sections but doesn't require the full BOOK approval workflow. Alternatively, clarify that V3 (BRIEF) can scale to multi-page documents without triggering BOOK gates.

### Section 5: Shell voice control classes

**Feedback:** VC0-VC5 provide a good taxonomy, but the mapping from user utterances to VC classes is underspecified. The document states "SHALL map to VC1, not an unconstrained model length change" but doesn't specify the mapping mechanism.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2, Developer Synchrony: 3

**Recommendation:** Add a normative mapping table or JSON schema showing how common user utterances map to VC classes. Specify that this mapping must be configurable by policy but have default bindings.

### Section 7: Output packaging classes

**Feedback:** Clear definitions of TXT, MD, PDF, DOCX, JSON, HTML. However, Section 7.3 creates confusion by distinguishing "simple PDF" from "publish-ready PDF" without defining the technical difference.

**Scores:** Completeness: 3, Practical Operability: 3, Style & Clarity: 3

**Recommendation:** Define technical criteria for "simple PDF" (e.g., single column, no images, basic typography) vs "publish-ready PDF" (multi-column, images, advanced typography, covers). Add a table mapping composition classes (from ADD-003) to supported packaging options.

### Section 9: Promotion rules

**Feedback:** The six conditions for promotion beyond V0 are reasonable, but the enforcement mechanism is unclear. How does the system detect "policy requires explanation" or "workflow requires structured review"?

**Scores:** Practical Operability: 2, Legal Enforceability: 2, Architectural Fidelity: 3

**Recommendation:** Add specific implementation guidance: promotion decisions must be traceable in audit logs with clear references to the triggering condition (e.g., "promoted to V2 due to policy P123 requiring explanation for financial documents").

### Section 10: BOOK approval and review gates

**Feedback:** Excellent governance model for long-form artifacts. The B0-B9 phases provide clear structure, and the mandatory approval gates ensure human oversight. However, 10 phases may be excessive - consider consolidating B4/B5 and B7/B8.

**Scores:** Business Model Alignment: 5, Architectural Fidelity: 4, Friction Factor: 2

**Recommendation:** Consolidate B4 (Chapter planning) and B5 (Chapter draft) into a single "Chapter development" phase. Consider making B8 (Final approval) optional for internal-use documents. Add escape hatches for "rapid draft" mode where users can bypass some gates with explicit acknowledgment.

### Section 10.11: Base and premium BOOK workflows

**Feedback:** Excellent commercial architecture. Clear separation of authoring (standard) from enhancement/publishing (premium). The entitlement gating aligns perfectly with MPOA commercial tiers.

**Scores:** Business Model Alignment: 5, Platform Economics Synchrony: 5, Legal Enforceability: 5

**Recommendation:** Add a technical enforcement mechanism: premium features must check entitlement via a defined API (e.g., `entitlement.check("book.enhancement")`) before execution. Shell controls for premium features should be disabled (not hidden) when not entitled, with clear upgrade prompts.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 5 | VC class mapping underspecified | Add normative mapping table from user utterances to VC classes with default bindings | High | 4,7,9 |
| 2 | Section 7 | Packaging-class mapping incomplete | Add table mapping ADD-003 composition classes to supported packaging options | High | 1,5,7 |
| 3 | Section 9 | Promotion enforcement unclear | Add audit logging requirement with clear triggering condition references | Medium | 3,7,10 |
| 4 | Section 10 | BOOK workflow too complex | Consolidate B4/B5 and consider optional B8 for internal documents | Medium | 7,11 |
| 5 | Section 10.11 | Premium enforcement mechanism missing | Add entitlement check API requirement and disabled (not hidden) UI pattern | High | 3,7,10 |
| 6 | Throughout | Missing technical schemas | Add JSON schemas for packaging metadata, BOOK state, VC mappings | Medium | 5,7,9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document has strong architectural foundations and excellent commercial alignment, but requires more specific implementation guidance for shell controls, packaging mappings, and enforcement mechanisms before ratification.

**Top 3 Actions Required:**
1. Add normative mapping from user utterances to VC classes with concrete implementation guidance
2. Define packaging support matrix linking ADD-003 composition classes to Section 7 packaging options
3. Add technical enforcement mechanisms for premium BOOK features and promotion rules
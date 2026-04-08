---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.10.0
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
| 1 | Cross-Document Consistency | 3 | Terminology aligns with ADD-001/ADD-002 but creates new control-plane axes that duplicate some ADD-002 concepts. |
| 2 | Business Model Alignment | 2 | References MPOA but lacks specific commercial hooks for composition classes; premium gates for professional documents are vague. |
| 3 | Legal Enforceability | 2 | Professional-use disclosure is strong but originality/source-boundary sections contain weasel words that undermine enforceability. |
| 4 | Architectural Fidelity | 4 | Correctly separates composition from packaging/execution and defines clear composition contracts with role/intent/outcome triad. |
| 5 | Completeness | 3 | Covers extensive ground but lacks JSON schemas for composition contract objects and fails to define enforcement mechanisms for many rules. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other documents, though axis definitions create potential overlap with ADD-002. |
| 7 | Practical Operability | 2 | Many rules are aspirational ("SHALL prefer") rather than actionable; lacks specific thresholds for originality verification. |
| 8 | Style & Clarity | 3 | Follows Style Guide but document is overly long with repetitive sections; some definitions are buried in prose. |
| 9 | Developer Synchrony | 2 | No implementation examples or integration points with existing DCP pipeline; reference adherence scale is abstract. |
| 10 | Platform Economics Synchrony | 2 | Mentions premium gates but doesn't specify how composition classes map to MPOA tiers or entitlement checks. |
| 11 | Friction Factor | 3 | Adds necessary governance but creates significant implementation burden without clear incremental value demonstration. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Architectural Separation**: Correctly distinguishes composition class from packaging/execution (Section 3), maintaining ADD-002's orthogonal design.
2. **Composition Contract**: The role/intent/outcome triad (Section 5) provides a solid foundation for governed artifact creation.
3. **Professional Disclosure**: Section 9.4 establishes clear mandatory disclosure text for professional-use documents.
4. **Control-Plane Model**: The twelve-axis summary (Section 6) helps position this addendum within the broader governance framework.

### Critical Gaps

1. **Missing Enforcement Mechanisms**: Many "SHALL" statements lack implementation pathways or DCP integration points.
2. **Abstract Originality Controls**: Section 19's "prefer transformed composition" and "high-overlap" concepts are too vague for technical implementation.
3. **No JSON Schemas**: Critical composition contract objects (Section 5.7) are only informative examples without normative schemas.
4. **Business Model Disconnect**: Fails to specify how composition classes map to MPOA commercial tiers or entitlement checks.
5. **Implementation Burden**: The reference adherence scale (Section 20.13) requires complex new controls without clear product requirements.

---

## Article-by-Article Review

### Section 0: Status and Intent

**Feedback:** Clear separation from ADD-001/ADD-002 is well-stated. The "does not replace" table effectively communicates scope boundaries.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 5

**Recommendation:** No changes needed for this section.

### Section 1: Purpose

**Feedback:** Overly long single sentence (168 words) violates Style Guide clarity principles. Lists many governed areas but doesn't prioritize them.

**Scores:** Style & Clarity: 2, Completeness: 4

**Recommendation:** Break into multiple sentences. Consider: "This addendum defines the composition control plane for governed artifact creation on AI OS surfaces, including: (1) message, invite, document, and publication classes; (2) the composition contract (role/intent/outcome) for non-trivial composition; (3) professional-use draft disclosure; (4) language and localization rules; (5) measurement contracts; (6) knowledge basis gating; (7) originality verification; and (8) reference-guided composition. It SHALL be read with ADD-002 for depth, voice controls, packaging, and BOOK-specific gates."

### Section 5: Composition Contract Requirements

**Feedback:** Strong architectural foundation but lacks technical implementation details. The informative JSON examples (5.7) should be normative schemas.

**Scores:** Architectural Fidelity: 5, Developer Synchrony: 2

**Recommendation:** Add normative JSON Schema in an appendix. Define required vs optional fields for each composition class. Specify DCP validation points for contract compliance.

### Section 9.4: Professional-Use Draft Disclosure

**Feedback:** Excellent legal safeguard with specific disclosure text. However, lacks integration with MPOA liability sections.

**Scores:** Legal Enforceability: 4, Business Model Alignment: 2

**Recommendation:** Add cross-reference to MPOA Article IV (Liability Caps) and specify that professional-use documents may have different liability terms. Add: "Professional-use documents as defined in this section SHALL be subject to MPOA Section 4.3 (Professional Services Disclaimer) and may have reduced liability caps as specified in product agreements."

### Section 17: Measurement Contract and Quantified Claims

**Feedback:** Conceptually sound but operationally vague. "Materially significant" is undefined. No technical mechanism for measurement validation.

**Scores:** Practical Operability: 2, Architectural Fidelity: 3

**Recommendation:** Define specific thresholds (e.g., "measurements affecting legal terms, financial amounts > $1,000, safety-critical dimensions"). Add: "The DCP SHALL validate measurement contracts against known authoritative sources where available and flag unverified measurements for human review."

### Section 19: Originality, Source-Boundary, and Non-Reproduction Verification

**Feedback:** Contains critical weasel words ("SHALL prefer," "too closely," "too high") that undermine enforceability. No technical implementation pathway.

**Scores:** Legal Enforceability: 1, Practical Operability: 1

**Recommendation:** Replace vague language with specific thresholds and technical controls. Change "SHALL prefer transformed composition" to "SHALL ensure output contains ≤ 20% verbatim overlap with any single source document for external publish/send actions." Add: "The DCP SHALL implement similarity detection at artifact export/send boundaries with configurable thresholds by artifact class and distribution channel."

### Section 20: Reference-Guided Composition

**Feedback:** The 1-10 adherence scale is abstract without technical grounding. No connection to model inference parameters or DCP validation.

**Scores:** Developer Synchrony: 1, Architectural Fidelity: 2

**Recommendation:** Either remove the numerical scale or define specific technical mappings. Consider: "Reference adherence SHALL be implemented as a DCP validation rule comparing output structure to reference document section hierarchy, with failure triggering human review when divergence exceeds policy thresholds."

### Section 21: Non-Goals

**Feedback:** Correctly scopes out navigation, depth, and packaging. However, misses opportunity to clarify relationship with AIOS-SPEC-009 (intent primitives).

**Scores:** Cross-Document Consistency: 4, Completeness: 3

**Recommendation:** Add: "This addendum does not define intent primitives or execution model details — see AIOS-SPEC-009 for intent routing and lane governance."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 19 | Vague originality controls | Replace "SHALL prefer" with specific thresholds (≤20% overlap) and DCP validation | Critical | 3, 7, 9 |
| 2 | Section 5 | Missing normative schemas | Add JSON Schema appendix for composition contract objects | High | 5, 9 |
| 3 | Section 9.4 | Missing MPOA integration | Add cross-reference to MPOA liability sections | High | 2, 3, 10 |
| 4 | Section 20 | Abstract adherence scale | Define technical implementation or remove numerical scale | High | 4, 9 |
| 5 | Section 17 | Undefined "materially significant" | Add specific thresholds and DCP validation points | Medium | 5, 7 |
| 6 | Section 1 | Overly long purpose statement | Break into multiple sentences for clarity | Low | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document contains critical architectural gaps in enforcement mechanisms (Section 19 originality controls are unenforceable) and lacks technical implementation pathways for key concepts like reference adherence and measurement validation.

**Top 3 Actions Required:**
1. Replace vague originality controls (Section 19) with specific thresholds and DCP validation mechanisms.
2. Add normative JSON schemas for composition contract objects and define DCP integration points.
3. Integrate professional-use disclosure with MPOA liability terms and specify commercial tier mappings.
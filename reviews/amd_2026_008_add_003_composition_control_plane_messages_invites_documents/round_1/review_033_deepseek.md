---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.2
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
| 1 | Cross-Document Consistency | 3 | Multiple cross-references to ADD-002 are correct, but §16.7 creates confusion by attempting to govern ADD-002 domains. |
| 2 | Business Model Alignment | 4 | Clear alignment with MPOA for professional-use disclosure and premium BOOK workflows. |
| 3 | Legal Enforceability | 2 | §19 contains contradictory language that weakens enforcement obligations while claiming to maintain them. |
| 4 | Architectural Fidelity | 2 | The document sprawls across multiple domains without clear architectural boundaries, violating separation of concerns. |
| 5 | Completeness | 4 | Covers all promised composition control plane aspects with detailed sections for each axis. |
| 6 | Conflict Freedom | 2 | §16.7 conflicts with ADD-002's ownership of depth/VC semantics; §19 contains internal contradictions. |
| 7 | Practical Operability | 3 | Many concepts are abstract without concrete implementation hooks; JSON schemas deferred to annex. |
| 8 | Style & Clarity | 2 | Excessive length (21 sections), repetitive cross-references, and dense prose make review difficult. |
| 9 | Developer Synchrony | 3 | Control-plane axes are defined but mapping to actual product implementation is unclear. |
| 10 | Platform Economics Synchrony | 4 | Clear gates for premium BOOK workflows and professional-use artifacts align with MPOA economics. |
| 11 | Friction Factor | 3 | Multiple mandatory gates could create workflow friction without clear user benefit communication. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive coverage** of composition control plane with 12 distinct axes (§6) provides complete taxonomy.
2. **Clear business model alignment** with MPOA through §9.4 professional-use disclosure and §10.11 premium BOOK gates.
3. **Strong integration with sibling addenda** through explicit cross-references to ADD-001 and ADD-002 domains.
4. **Detailed originality verification framework** (§19) with concrete states and channel-based thresholds.

### Critical Gaps

1. **Architectural boundary violations**: §16.7 attempts to govern ADD-002 domains (depth/VC semantics) creating domain conflicts.
2. **Contradictory enforcement language**: §19.2 establishes SHALL obligations while §19.9 contains language that could be interpreted as weakening them.
3. **Excessive document sprawl**: 21 sections covering everything from language controls to measurement contracts creates review fatigue and implementation complexity.
4. **Abstract implementation guidance**: Many "conceptual fields" lack concrete JSON schema or DCP binding specifications.

---

## Article-by-Article Review

### §0-§2: Status, Purpose, and Governing Principle

**Feedback:** The status table correctly identifies domain boundaries with ADD-001/ADD-002. However, the "Purpose" section (§1) is excessively long (over 300 words) and repeats information from the status table. The governing principle (§2) correctly states artifact generation SHALL follow composition class, but §2.1's "normative for authors" language is confusing—should be normative for implementations.

**Scores:** Architectural Fidelity: 3, Style & Clarity: 2

**Recommendation:** Split §1 into two sections: "1. Purpose" (concise statement) and "1.1 Scope" (detailed bullet points). Move the informative grounding references to a separate "Context" section. Clarify §2.1 to state "Implementations SHALL respect these domain boundaries" rather than "normative for authors."

### §5: Composition Contract Requirements

**Feedback:** The triad (role, intent, outcome) is architecturally sound. However, §5.9's "Normative fields and validation posture" table mixes conceptual fields with implementation concerns. The fail-closed rejection semantics are well-defined but reference §19 which has contradictory language.

**Scores:** Architectural Fidelity: 4, Practical Operability: 3

**Recommendation:** Move the §5.9 table to an implementation annex. Add concrete JSON schema examples showing how role/intent/outcome map to DCP fields. Clarify that missing contract fields SHALL block progression to "send-ready" state, not just "substantive drafting."

### §16: Language, Localization, and Authoritative Version Control

**Feedback:** §16.7 creates a direct architectural conflict: "Language SHALL not by itself change the active output depth ladder step" attempts to govern ADD-002's domain. This violates the separation of concerns established in §0 and §2.1. The language modes (L0-L3) are well-defined but overlap with existing i18n/l10n patterns.

**Scores:** Architectural Fidelity: 1, Conflict Freedom: 1

**Recommendation:** Remove §16.7 entirely. Language controls should not reference ADD-002 domains. Instead, state: "Language selection SHALL govern expression semantics only; output depth and voice control semantics remain governed by ADD-002." Consider moving language controls to a separate addendum if they're this complex.

### §18: Knowledge Basis and Discovery Gating

**Feedback:** The "discover before create" principle is architecturally sound. However, §18.11's "Recommended sequence" mixes pre-drafting and pre-release gates in a way that could create implementation confusion. The reference to §19 thresholds in step 6 is appropriate but relies on §19's problematic language.

**Scores:** Architectural Fidelity: 3, Practical Operability: 3

**Recommendation:** Split §18.11 into two clear sequences: "A. Pre-drafting validation sequence" and "B. Pre-release validation sequence." Add concrete DCP state transition diagrams showing how knowledge_state moves from insufficient → partial → sufficient.

### §19: Originality, Source-Boundary, and Non-Reproduction Verification

**Feedback:** Critical architectural flaw: §19 contains contradictory language. §19.2 establishes strong SHALL obligations for release-time gating, but §19.9 states "No waiver of §19.2/§19.4/§19.5" while simultaneously containing language that could be interpreted as weakening enforcement. The reference to AIOS-OPS-020 is correct but the document should not contain internal contradictions.

**Scores:** Legal Enforceability: 1, Architectural Fidelity: 2

**Recommendation:** Rewrite §19.9 entirely. Remove all "does not claim" language that could weaken enforcement. Instead state: "§19 establishes product obligations for originality verification; legal outcomes for third-party claims remain subject to MPOA liability terms and applicable law." Ensure the enforcement obligations in §19.2-§19.5 are unambiguous.

### §20: Reference-Guided Composition

**Feedback:** The distinction between template/reference/authority (§20.3) is architecturally sound. However, the adherence scale (1-10) in §20.13 is overly granular for practical implementation. The warning in §20.14 that "maximum adherence SHALL not bypass §19 verification" is critical and well-placed.

**Scores:** Architectural Fidelity: 4, Practical Operability: 2

**Recommendation:** Simplify the adherence scale to 3-5 discrete levels (e.g., loose/guided/strict). Add concrete examples showing how structure_adherence vs style_adherence produce different outputs. Include JSON schema showing how reference_documents array maps to DCP context.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §16.7 | Architectural boundary violation with ADD-002 | Remove §16.7 entirely; language controls should not govern depth/VC semantics | Critical | 4, 6 |
| 2 | §19.9 | Contradictory language weakens enforcement | Rewrite to remove "does not claim" language; maintain strong SHALL obligations | Critical | 3, 4 |
| 3 | Entire doc | Excessive length and sprawl | Split into core composition document + annexes for language, measurement, reference guidance | High | 8, 7 |
| 4 | §5.9, §18.11 | Abstract implementation guidance | Add concrete JSON schemas and DCP state transition diagrams | Medium | 7, 9 |
| 5 | §20.13 | Overly granular adherence scale | Simplify to 3-5 discrete levels with clear implementation mapping | Medium | 7, 9 |
| 6 | §1 | Overly verbose purpose statement | Split into concise purpose + detailed scope sections | Low | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document contains critical architectural flaws (§16.7 conflicts with ADD-002 domains) and legal enforceability issues (§19 contradictory language), compounded by excessive length that makes review and implementation difficult.

**Top 3 Actions Required:**
1. Remove §16.7 entirely to resolve architectural boundary violation with ADD-002.
2. Rewrite §19.9 to eliminate contradictory language while maintaining strong SHALL obligations for originality verification.
3. Split the document into a core composition control plane document (covering §§1-15) with separate annexes or addenda for language (§16), measurement (§17), knowledge basis (§18), originality (§19), and reference guidance (§20).
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
| 1 | Cross-Document Consistency | 3 | Most terminology aligns but §19.10 references OPS-020 v0.3.0 which doesn't exist in context documents. |
| 2 | Business Model Alignment | 4 | Clear premium gates and MPOA alignment, but §10.11 references are indirect. |
| 3 | Legal Enforceability | 2 | §19.9 disclaimer weakens enforcement posture; §5.9 fail-closed rules lack specific error codes. |
| 4 | Architectural Fidelity | 2 | §18 vs §19 scope confusion; §20.14 contradicts §19; DCP pipeline references incomplete. |
| 5 | Completeness | 3 | Covers all axes but §19 implementation handoff is incomplete; JSON schemas missing. |
| 6 | Conflict Freedom | 2 | §20.14 conflicts with §19; §18.11 step 6 creates circular dependency. |
| 7 | Practical Operability | 3 | Fields defined but validation logic deferred; no concrete DCP transport bindings. |
| 8 | Style & Clarity | 4 | Well-structured but §19 disclaimer language creates confusion. |
| 9 | Developer Synchrony | 3 | Control-plane axes clear but implementation artifacts not fully specified. |
| 10 | Platform Economics Synchrony | 4 | Premium gates align with ADD-002 §10.11; MPOA references correct. |
| 11 | Friction Factor | 2 | §19.9 creates legal uncertainty; §18/§19 boundary confusion increases implementation risk. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive control-plane model** (§6) with 12 axes provides clear separation of concerns.
2. **Professional-use disclosure** (§9.4) is well-specified with mandatory text and export preservation rules.
3. **Reference-guided composition** (§20) introduces innovative adherence controls distinct from model temperature.
4. **Clear addendum seams** (§2.1) properly defer to ADD-001/ADD-002 for navigation and depth.

### Critical Gaps

1. **§19.9 disclaimer undermines enforcement**: The "no absolute guarantee" language conflicts with §19.2-§19.5 SHALL/MUST NOT obligations.
2. **§18 vs §19 scope confusion**: §18.11 creates circular dependency; §19.10 references OPS-020 v0.3.0 which doesn't exist in context.
3. **§20.14 conflicts with §19**: Maximum adherence "SHALL NOT bypass §19" but structure fidelity at level 10 inherently risks overlap.
4. **Missing DCP transport specifications**: §19.10 defers to OPS-020 but no DCP protobuf/OpenAPI artifacts exist in context.

---

## Article-by-Article Review

### §2.1 Addendum seams

**Feedback:** Clear separation from ADD-001/ADD-002 is architecturally sound. However, §16.7 references ADD-002 §5 for VC classes but ADD-002 §5 defines VC0-VC5, not just "VC classes" - this creates minor inconsistency.

**Scores:** Architectural Fidelity: 4, Cross-Document Consistency: 3

**Recommendation:** Change §16.7 second bullet to: "Language or locale selection SHALL NOT redefine VC0–VC5 meaning; VC classes (VC0–VC5) remain authoritative in ADD-002 §5."

### §5.9 Normative fields and validation posture

**Feedback:** Fail-closed table is good but lacks specific error codes or DCP outcome codes. "Exact error codes... SHALL bind in implementation artifacts" is too vague for governance.

**Scores:** Practical Operability: 2, Architectural Fidelity: 2

**Recommendation:** Add a normative table mapping conditions to DCP outcome codes (e.g., `COMPOSITION_CONTRACT_INCOMPLETE`, `PROFESSIONAL_DISCLOSURE_MISSING`). Reference OPS-020 §10 for originality codes as example pattern.

### §18 Knowledge basis and discovery gating

**Feedback:** §18.11 step 6 creates circular dependency: "§19 SHALL not substitute for §18 grounding where §18 applies" but §19 is about release-time verification, not grounding. The boundary between §18 (pre-draft) and §19 (pre-release) is architecturally confused.

**Scores:** Architectural Fidelity: 1, Conflict Freedom: 2

**Recommendation:** Rewrite §18.11 to clarify temporal sequence: "B — Before external publish, send, or formal export (when §19.2 applies): 6. Originality/source-boundary verification — §19 governs release-time overlap risk; this is distinct from §18 knowledge sufficiency check."

### §19 Originality, source-boundary, and non-reproduction verification

**Feedback:** Critical architectural flaw: §19.9 disclaimer ("No waiver of §19.2/§19.4/§19.5") attempts to preserve enforcement while disclaiming legal outcomes, creating confusion. §19.10 references OPS-020 v0.3.0 which doesn't exist in context documents (only v0.2.0 shown).

**Scores:** Legal Enforceability: 1, Architectural Fidelity: 1, Conflict Freedom: 1

**Recommendation:** 
1. Remove §19.9 entirely or rewrite as: "§19.2-§19.5 establish product behavior obligations; these do not constitute legal advice or guarantee specific legal outcomes."
2. Update §19.10 to reference OPS-020 v0.2.0 (shown in context) or remove version specificity.
3. Add explicit DCP transport requirement: "Products SHALL implement DCP transport per OPS-020 §10 codes for originality evaluation outcomes."

### §20.14 Maximum adherence and the originality gate

**Feedback:** Direct conflict with §19: "structure fidelity does not imply originality_clear" but level 10 adherence ("Exact layout conformity") inherently creates high structural similarity that §19 would flag.

**Scores:** Conflict Freedom: 1, Architectural Fidelity: 1

**Recommendation:** Add warning: "Level 10 adherence SHALL trigger §19 verification with elevated scrutiny; policy MAY require manual review for external channels when adherence ≥ 8."

### §19.10 Implementation handoff

**Feedback:** References OPS-020 v0.3.0 but context shows v0.2.0. "Algorithm IDs and concrete scorers remain deferred to policy" creates implementation ambiguity.

**Scores:** Practical Operability: 2, Completeness: 2

**Recommendation:** 
1. Update reference to OPS-020 v0.2.0 (matching context).
2. Add: "Products SHALL document which scoring algorithm IDs (e.g., n-gram window size, structural similarity metric) are used for each conformance claim."
3. Reference Annex A for example evaluation records.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §19.9 | Disclaimer weakens enforcement | Remove or rewrite to clarify product vs legal obligations | Critical | 3, 4, 11 |
| 2 | §18.11 | Circular dependency with §19 | Clarify temporal sequence: §18 pre-draft, §19 pre-release | Critical | 4, 6 |
| 3 | §20.14 | Conflicts with §19 | Add warning about elevated §19 scrutiny at high adherence | High | 4, 6 |
| 4 | §19.10 | References non-existent OPS-020 v0.3.0 | Update to v0.2.0; add algorithm ID requirement | High | 1, 7 |
| 5 | §5.9 | Missing DCP error codes | Add normative table mapping conditions to DCP codes | Medium | 7, 9 |
| 6 | §16.7 | Inconsistent VC class reference | Specify VC0-VC5 explicitly | Low | 1 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** Critical architectural conflicts between §18/§19 and §19/§20, combined with §19.9's enforcement-weakening disclaimer and references to non-existent OPS-020 version, require substantial revision before ratification.

**Top 3 Actions Required:**
1. Resolve §19.9 disclaimer conflict with §19.2-§19.5 enforcement obligations.
2. Clarify temporal boundary between §18 (knowledge sufficiency) and §19 (release verification).
3. Fix OPS-020 version reference and add concrete DCP transport requirements.
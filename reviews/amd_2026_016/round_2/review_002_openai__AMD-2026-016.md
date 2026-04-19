---
review_id: REV-AMD-2026-016-002
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.2.0
reviewer: OpenAI
review_date: 2026-04-10
review_round: 2
review_type: editorial
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: AMD-2026-016 — Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Round 1 cross-document gaps were substantially improved, but the amendment still introduces principal terminology that is not yet fully reconciled with the `Actor` model and naming patterns in AIOS-SPEC-009 and AMD-2026-007. |
| 2 | Business Model Alignment | 4 | The amendment supports enterprise-grade governed delegation and application participation without undermining the marketplace or Kit-based model, though it remains largely silent on Vendor-facing packaging implications. |
| 3 | Legal Enforceability | 4 | The revision materially strengthened enforceability through lifecycle, attribution, deny-and-audit, and conformance rules, but a few phrases still leave approval authority and acceptance mechanics underspecified. |
| 4 | Architectural Fidelity | 5 | The document now aligns strongly with policy supremacy, routed authority, shell/control-plane separation, and fail-closed execution principles across AMD-2026-012, AMD-2026-007 §11.9, AIOS-SPEC-002, and AIOS-SPEC-009. |
| 5 | Completeness | 4 | The major Round 1 omissions were addressed with lifecycle, attribution, conformance, and examples, though the amendment still stops short of defining a canonical schema or mandatory registry surface. |
| 6 | Conflict Freedom | 4 | The revision now states its boundaries clearly and avoids direct conflict with shell-state and domain-intent law, but some implementation overlap with AIOS-SPEC-002 and AIOS-SPEC-009 remains to be harmonized in follow-on edits. |
| 7 | Practical Operability | 3 | The document is now operational in doctrine, but implementers still need more precise acceptance criteria for conformance records, route-class authority sources, and registry validation surfaces. |
| 8 | Style & Clarity | 4 | The writing is clear and disciplined overall, but several sections use list-heavy prose and lower-case defined-term introductions that reduce editorial sharpness relative to the strongest documents in the set. |
| 9 | Developer Synchrony | 3 | The new examples and conformance probes materially improve usability, but developers still lack a canonical schema, field ownership map, and explicit linkage to existing execution-envelope structures. |
| 10 | Platform Economics Synchrony | 4 | The new economic-subject and metered-activity rules close the main Round 1 gap, though the amendment should align more explicitly with MPOA/Funded Data Account terminology in follow-on text. |
| 11 | Friction Factor | 3 | The added controls are justified by risk, but the amendment introduces governance overhead without yet defining the leanest acceptable documentation surface for smaller deployment patterns. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

This Round 2 revision addresses the core failures identified in Round 1. Most importantly, it now supplies actual governing doctrine where the prior draft had only principles. Sections **4.6**, **4.12**, **4.13**, **4.14**, and **4.15** materially improve the amendment by defining admission checks, fail-closed consequences, lifecycle management, liability/economic attribution, and conformance records. The document also now does a much better job of respecting existing authority boundaries: **§2** and **§5** correctly avoid re-legislating shell-state law already governed by **AMD-2026-007 §11.9**, shell authority already governed by **AMD-2026-012 §§4.2, 7**, and domain intent / policy execution already governed by **AIOS-SPEC-009 §§2.1, 5, 6, 12, 15** and **AIOS-SPEC-002**. Informative examples in **§8** and probes in **§9** are a meaningful improvement for implementers and reviewers.

### Critical Gaps

The remaining issues are mostly editorial-coherence and implementation-surface issues rather than conceptual failures. First, the amendment still does not fully reconcile its principal model with the existing `Actor` and session terminology in **AIOS-SPEC-009 §5** and **AMD-2026-007 §11.2**; it references joinability but does not define whether non-human principal facts extend `Actor`, sit beside it, or remain separate. Second, **§4.4** and **§4.15** leave approval/acceptance authority somewhat vague: “ratified specification, implementation conformance record, or policy annex” and “accepted under governance” need a tighter statement of who accepts what. Third, the document would benefit from stronger terminology normalization and a few targeted editorial refinements so it reads more like the ratified amendments around it and less like a strong draft.

---

## Article-by-Article Review

### §0. Status

**Feedback:** The status section is concise and appropriately scoped. It correctly frames the amendment as a narrow authority instrument and avoids overclaiming. However, unlike several adjacent amendments, it does not yet include a “depends on” or “alignment with” note that would help readers immediately understand its relationship to **AMD-2026-012**, **AMD-2026-007**, **AIOS-SPEC-002**, and **AIOS-SPEC-009**.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 4

**Recommendation:** Add a short dependency/alignment row to mirror the stronger status sections in AMD-2026-012 and AMD-2026-013.

**Proposed text addition:**
> | Depends on | Conceptual alignment with **AMD-2026-012** (Shell authority), **AMD-2026-007 §11.9** (shell-state routing boundary), **AIOS-SPEC-002** (`PolicyRecord` runtime authorization), and **AIOS-SPEC-009** (domain intent execution and audit truth). This amendment adds principal-governance law; it does not replace those documents’ technical definitions. |

---

### §1. Purpose

**Feedback:** The section is much improved from Round 1 and clearly states the governing thesis. The final paragraph is the strongest part because it gives a crisp validity test. Editorially, however, the section uses informal sentence fragments (“The problem is simple:” / “This amendment establishes the missing law:”) that are readable but slightly less formal than the surrounding corpus.

**Scores:** Style & Clarity: 4, Legal Enforceability: 4

**Recommendation:** Tighten the prose into fully normative governance style.

**Proposed replacement language:**
> This amendment addresses a governance gap: AI OS depends on non-human actors that can observe state, route communication, invoke actions, mutate configuration, or package output. If those actors are not explicitly governed, authority drifts into hidden infrastructure, hidden prompts, or hidden background logic.  
>
> This amendment therefore establishes that non-human authority in AI OS is lawful only when the acting principal is explicitly identified, explicitly bound to a governed role, explicitly bound to governed scope, routed through a documented authority path, evaluated under policy, and recorded in auditable action records.

---

### §2. Scope

**Feedback:** This section is strong and directly addresses a major Round 1 problem by clarifying what the amendment does not replace. The explicit non-overlap with **AMD-2026-007 §11.9**, **AIOS-SPEC-009**, and **AIOS-SPEC-002** is especially helpful. One editorial issue remains: the out-of-scope list mixes legal boundaries, implementation boundaries, and document-boundary statements without grouping.

**Scores:** Conflict Freedom: 5, Cross-Document Consistency: 4

**Recommendation:** Group the out-of-scope items into “authority boundaries” and “implementation boundaries” for readability. No substantive change required.

---

### §3. Definitions

**Feedback:** This section is substantially better than the Round 1 draft. The new definitions for **Route class**, **Authority-bearing action**, **Principal registry**, and **Conformance record** directly answer prior reviewer concerns. The remaining issue is cross-document harmonization: the amendment defines “Non-human principal” and related classes well, but it does not explicitly say how these concepts relate to `Actor` in **AIOS-SPEC-009 §5** and **AMD-2026-007 §11.2**. That omission is now manageable, but still real.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 3, Style & Clarity: 4

**Recommendation:** Add a non-duplication / relationship note clarifying that principal facts supplement rather than silently replace `Actor` facts in intent and session records.

**Proposed text addition after the definition list:**
> **Relationship to `Actor` records.** Where **AIOS-SPEC-009** or related specifications require an `Actor`, implementations **SHALL** either (a) represent non-human principal facts as a documented extension to that actor model, or (b) carry principal facts in a joinable adjacent record. This amendment does not by itself redefine the canonical `Actor` schema in **AIOS-SPEC-009**.

---

### §4. Normative decisions

**Feedback:** This is the core of the amendment and the revision is materially stronger than Round 1. The structure is logical: identity/binding/routing, then validation, then class-specific rules, then attribution/lifecycle/conformance. The strongest additions are **§4.6**, **§4.12**, **§4.13**, **§4.14**, and **§4.15**. They convert the amendment from doctrine into enforceable governance.

The remaining weaknesses are mostly precision issues:

- **§4.4** still leaves route-class authority sources somewhat open-ended. “Ratified specification, implementation conformance record, or policy annex” is workable, but “policy annex” and “implementation conformance record” need clearer governance status.
- **§4.11** is much improved, but “the system SHALL define” is still slightly abstract before the default attribution bullets rescue it.
- **§4.15** says conformance records may be satisfied through “another governed documentation surface that is reviewable and auditable,” which is sensible but broad enough to invite inconsistent practice.

**Scores:** Legal Enforceability: 4, Practical Operability: 3, Architectural Fidelity: 5, Developer Synchrony: 3

**Recommendation:** Tighten the acceptance language in **§4.4** and **§4.15** so implementers know what counts as an authoritative surface.

**Proposed replacement for the second paragraph of §4.4:**
> Each route class used for authority-bearing action **SHALL** be identified in either (a) a ratified specification or amendment, or (b) a governed conformance record or policy annex whose owning authority and review status are explicitly documented. A route that is not documented in one of those authority sources **SHALL** be treated as under-governed.

**Proposed replacement for the final sentence of §4.15:**
> Implementations **MAY** satisfy this requirement through DCP-validated records, policy annexes, versioned registry records, or another governed documentation surface **only where** that surface identifies its owning authority, review status, and canonical repository location.

---

### §5. Relationship to existing governance

**Feedback:** This section is one of the strongest in the document. It directly addresses the Round 1 criticism that the amendment lacked integration points. The table is coherent, cites the right sections, and correctly positions this amendment as additive rather than substitutive. The best row is the **AIOS-SPEC-002** row, which clearly states that `PolicyRecord` remains primary while this amendment defines facts policy must be able to see.

One remaining editorial issue: the final row groups **AIOS-AMD-PLAN-001** and **AIOS-AMENDMENT-INTAKE-SCAFFOLD-001** together, but those are process artifacts of different kinds. Splitting them would improve clarity.

**Scores:** Cross-Document Consistency: 5, Conflict Freedom: 4

**Recommendation:** Split the final row into two rows if the authors want maximum precision; otherwise acceptable as-is.

---

### §6. Cross-document impact (informative)

**Feedback:** This section is useful and appropriately modest. It gives concrete follow-up targets without pretending those changes are already complete. Editorially, it would be stronger if the follow-up for **AIOS-SPEC-009** explicitly mentioned `Actor` / principal linkage, since that is the main unresolved coherence issue.

**Scores:** Cross-Document Consistency: 4, Completeness: 4

**Recommendation:** Revise the AIOS-SPEC-009 row to mention `Actor` reconciliation explicitly.

**Proposed replacement row text:**
> | AIOS-SPEC-009 | Add principal identity / class linkage to `Actor` or adjacent joinable records, plus execution-envelope or audit-envelope guidance where non-human actors initiate or execute plans. |

---

### §7. Non-goals

**Feedback:** Clear and disciplined. This section helps prevent overreading and is consistent with the style of AMD-2026-012 and AMD-2026-013. No substantive issue found.

**Scores:** Style & Clarity: 5, Conflict Freedom: 5

**Recommendation:** No change needed.

---

### §8. Minimum conformance examples (informative)

**Feedback:** This section is a major improvement over Round 1 and directly addresses prior operability concerns. The examples are plausible and useful. The main editorial issue is that the examples introduce field names like `principal_class`, `owner_subject`, and `economic_subject` without explicitly stating whether they are illustrative only or intended as preferred naming. Because the amendment elsewhere allows implementation variation, that distinction should be explicit.

**Scores:** Developer Synchrony: 4, Practical Operability: 4, Cross-Document Consistency: 3

**Recommendation:** Add a prefatory sentence clarifying that the shapes are illustrative and semantic, not mandatory field names unless adopted by a ratified schema.

**Proposed text addition before §8.1:**
> The following examples are illustrative semantic shapes. Field names are not mandatory unless adopted by a ratified schema, but conformant implementations **SHALL** preserve the semantic content required by §§4.5, 4.6, and 4.15.

---

### §9. Conformance probes (informative)

**Feedback:** Strong and useful. These probes are concrete enough to guide testing and peer review. They also align well with the style used in AMD-2026-012 Appendix B. No major issue found.

**Scores:** Practical Operability: 4, Completeness: 4

**Recommendation:** No substantive change needed. Optional enhancement: add one probe for principal-class substitution failure under **§4.10**.

**Optional text addition:**
> 6. An action that attempts to substitute one principal class for another in routing or audit records is denied or flagged as non-conformant.

---

### §10. Amendment history

**Feedback:** Clear and sufficient.

**Scores:** Style & Clarity: 5

**Recommendation:** No change needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §3 / §6 | Principal terminology is still not fully reconciled with `Actor` in AIOS-SPEC-009 and AMD-2026-007 | Add explicit language stating whether non-human principal facts extend `Actor` or live in a joinable adjacent record, and update the AIOS-SPEC-009 follow-up row accordingly | Critical | 1, 5, 6, 9 |
| 2 | §4.4 / §4.15 | Authority/acceptance mechanics for route classes and conformance records remain too open-ended | Require each conformance surface to identify owning authority, review status, and canonical location | High | 3, 7, 9 |
| 3 | §8 | Examples may be misread as canonical schemas | Add a prefatory note that field names are illustrative unless adopted by a ratified schema | High | 1, 7, 9 |
| 4 | §0 | Status section lacks an immediate dependency/alignment note | Add a “Depends on” row mirroring adjacent amendments for faster cross-document orientation | Medium | 1, 8 |
| 5 | §1 | Purpose section uses slightly informal framing relative to the ratified corpus | Rewrite the introductory prose into more formal governance style | Medium | 3, 8 |
| 6 | §5 | Final relationship row groups two distinct process artifacts together | Split the combined row for cleaner cross-document mapping | Low | 1, 8 |
| 7 | §9 | Conformance probes omit a direct test for principal-class substitution failure | Add a probe covering §4.10 non-substitution behavior | Low | 5, 7, 9 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The Round 1 issues were substantially and credibly addressed. The document is now conceptually sound, enforceable in its core doctrine, and broadly coherent with the governing set. Remaining issues are important but no longer rise to major-revision level; they are chiefly about schema/interface reconciliation and tightening authoritative documentation surfaces.

**Top 3 Actions Required:**
1. Reconcile the amendment’s principal model explicitly with `Actor` and adjacent execution/session records in AIOS-SPEC-009 and AMD-2026-007.
2. Tighten §4.4 and §4.15 so route-class and conformance-record authority sources have explicit ownership and review status.
3. Clarify in §8 that the JSON examples are semantic illustrations, not silently canonical schemas.
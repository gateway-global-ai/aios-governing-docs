---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.5
reviewer: OpenAI
review_date: 2026-04-08
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The document is substantially aligned to AMD-2026-008, ADD-001, and ADD-002, but several cross-references use inconsistent path/title forms and a few section/version references are brittle or mismatched. |
| 2 | Business Model Alignment | 4 | The addendum generally respects MPOA and ADD-002 premium-gating boundaries, especially in §§9.4, 10, 14, and 19, with only minor ambiguity around export/send monetization boundaries. |
| 3 | Legal Enforceability | 3 | Core obligations are stated in enforceable SHALL language, but several clauses rely on policy-defined triggers without always specifying the minimum deterministic rule needed when policy is absent or conflicting. |
| 4 | Architectural Fidelity | 4 | The document preserves the seam that ADD-002 owns depth/VC and this addendum owns composition classes/contracts, and it correctly keeps release-time originality distinct from grounding. |
| 5 | Completeness | 4 | The document covers the promised composition-plane scope comprehensively, including contract, language, measurement, knowledge, originality, and reference-guided composition. |
| 6 | Conflict Freedom | 3 | No direct contradiction is evident, but there is tension between this addendum’s broad composition governance and the style guide’s stricter cross-reference conventions, plus some ambiguity around informative vs normative implementation homes. |
| 7 | Practical Operability | 3 | The control logic is conceptually strong, but implementation teams would still need a tighter minimum state model and clearer mandatory field/action matrices for several classes to avoid divergent product behavior. |
| 8 | Style & Clarity | 2 | The document is materially over-bolded, visually noisy, and harder to parse than necessary, which undermines editorial clarity despite strong substantive content. |
| 9 | Developer Synchrony | 2 | The product snapshot does not yet show a composition-plane implementation surface comparable to this document’s breadth, and the addendum does not clearly distinguish immediate implementation minimums from future extensibility. |
| 10 | Platform Economics Synchrony | 4 | The text consistently defers liability and commercial terms to MPOA and ADD-002’s premium gates, avoiding most economic overreach. |
| 11 | Friction Factor | 1 | The document is too dense and cognitively expensive for efficient review or implementation, largely due to formatting overload, repeated seam language, and long normative paragraphs. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- **Strong doctrinal partitioning**: §§2.1, 6, 16.7, 18, 19, and 20 do a good job separating navigation, depth/VC, composition class, grounding, originality, and reference adherence.
- **Good cross-document seam discipline**: the document repeatedly reinforces that **ADD-002** owns output depth, VC classes, packaging, and BOOK workflow, while this addendum owns composition classes and contracts.
- **Substantive completeness**: the addendum covers the full composition plane promised by its history and related memos, especially in §§5, 9.4, 16, 17, 18, 19, and 20.
- **Useful fail-closed posture**: §5.9 and §§19.2–19.5 appropriately reject silent pass-through for missing contract, disclosure, knowledge, and originality gates.
- **Good implementation handoff discipline**: §19.10 and the AIOS-OPS-020 linkage avoid embedding unstable scoring logic directly in the addendum.

### Critical Gaps

- **Editorial readability is materially below governance-document standard**: pervasive bolding and over-segmented prose make the document difficult to read and review, especially in §§1–2, 16, 18, 19, and 20.
- **Cross-reference hygiene is inconsistent**: some references use markdown paths, some use bare IDs, some use relative repository paths that do not match the bundled context, and the footer version line still says **0.14.2** instead of **0.14.5**.
- **Minimum implementation surface is still too implicit in places**: §§8–10 and 12–15 define classes and actions, but do not always specify which fields/actions are mandatory versus policy-optional at product v1.
- **Policy-dependence is sometimes under-bounded**: several clauses say policy defines thresholds or precedence, but do not always specify the minimum default behavior if policy is incomplete, except in some sections like §19.2.
- **Developer synchrony is weak**: the product snapshot does not yet evidence a composition control plane of this scope, and the document does not clearly mark what is mandatory now versus doctrinally reserved for later implementation slices.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section correctly frames the addendum as subordinate to AMD-2026-008 and distinct from ADD-001 and ADD-002. The informative-grounding row is useful, but the relative paths appear inconsistent with the bundled document set: the cited files are presented in the review packet as top-level reference documents, not clearly at `../reference/implementation/...`. That creates avoidable path fragility. The section is also visually over-bolded.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 2, Conflict Freedom: 4

**Recommendation:**  
Standardize all cross-references in this section to document IDs and titles first, with repository paths only as informative appendices if needed. Replace the current informative-grounding row with:

> **Informative grounding (not incorporated as law):** **AIOS-COMPOSITION-CONTROL-RD-NOTES-001**, **AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001**, and **AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001** provide non-normative process, architecture, and surface-mapping context for this addendum.

Also reduce bolding to defined terms and critical mandates only.

---

### 1. Purpose

**Feedback:**  
Substantively strong and complete. It clearly states the addendum’s scope and its relationship to ADD-002. However, the prose is overloaded with bold emphasis and parenthetical insertions, which reduces readability. The final sentence about informative documents is useful but stylistically awkward.

**Scores:** Completeness: 5, Style & Clarity: 2, Cross-Document Consistency: 4

**Recommendation:**  
Split the section into two short paragraphs and remove most inline bolding. Proposed replacement for the final sentence:

> This addendum shall be read with **AMD-2026-008-ADD-002** for output depth, shell voice controls, packaging, and BOOK-specific gates. The related R&D, architecture, and surface memos listed in Section 0 are informative only and do not create additional runtime obligations.

---

### 2. Governing principle

**Feedback:**  
The section correctly establishes that composition class is distinct from packaging and execution. Section 2.1 is especially valuable as a seam-control provision. However, “normative for authors” is slightly awkward in a runtime-governance document because it shifts audience from implementers to document maintainers. If retained, it should be clearer that these seam rules govern future drafting of related documents, not runtime behavior.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:**  
Retitle §2.1 to:

> **2.1 Addendum seam rules (document-governance rule)**

And add:

> This subsection governs future drafting and interpretation of related addenda; it does not independently expand runtime obligations beyond the sections cited.

---

### 3. Composition class versus packaging and execution

**Feedback:**  
Clear and useful. The examples are practical and reinforce the orthogonality of class, packaging, and action. This is one of the cleaner sections.

**Scores:** Practical Operability: 4, Architectural Fidelity: 5, Style & Clarity: 4

**Recommendation:**  
No substantive change required. Minor editorial improvement: change “An EMAIL’s primary path is message action” to “The primary path for an **EMAIL** is message action” for style consistency.

---

### 4. Responsive, procedural, and composed outputs

**Feedback:**  
This section is structurally sound and gives a workable three-tier gating model. The distinction between Class 1, 2, and 3 is useful. The main gap is that Class 2 remains somewhat under-specified: it says partial contract “may” be required depending on stakes and policy, but does not define a minimum default when policy is silent.

**Scores:** Completeness: 4, Practical Operability: 3, Legal Enforceability: 3

**Recommendation:**  
Add a default rule to §4.2:

> When policy is silent, **Class 2** outputs shall require at least **intent** and **outcome** if they are persistent, review-bearing, or used to drive a multi-step workflow.

---

### 5. Composition contract requirements

**Feedback:**  
This is a core section and generally strong. §§5.1–5.6 are coherent and operationally meaningful. §5.9 is important, especially the fail-closed table. The main issue is that the section mixes conceptual governance, implementation abstraction, and DCP handoff in a way that is slightly too compressed. Also, the Annex A link text appears inconsistent with the annex title in the bundled context.

**Scores:** Completeness: 5, Legal Enforceability: 4, Practical Operability: 3, Cross-Document Consistency: 3

**Recommendation:**  
1. Standardize the annex citation to the actual bundled title:
> **AMD-2026-008-ADD-003-ANNEX-A — Informative composition and knowledge-basis examples**

2. Tighten §5.9 with a default applicability sentence:
> Unless policy defines a narrower rule that is auditable, the minimum validation posture in this section applies to all **Class 3** artifacts.

3. Consider splitting §5.9 into:
- **Minimum governed fields**
- **Fail-closed outcomes**
- **Implementation handoff**

for readability.

---

### 6. Control-plane axes (twelve axes summary)

**Feedback:**  
This is a strong orienting table and aligns well with ADD-002 and the architecture memo. It is one of the best cross-document coherence devices in the draft.

**Scores:** Cross-Document Consistency: 5, Architectural Fidelity: 5, Style & Clarity: 4

**Recommendation:**  
No substantive change required. Minor editorial suggestion: add “See also §2.1” after the table to reinforce seam discipline.

---

### 7. Composition families

**Feedback:**  
Useful high-level taxonomy. The family labels are coherent with later sections. No major issues.

**Scores:** Completeness: 4, Style & Clarity: 4, Architectural Fidelity: 4

**Recommendation:**  
No substantive change required.

---

### 8. Message and invite classes

**Feedback:**  
EMAIL and CALENDAR_INVITE are well framed as action-bearing artifacts. The action semantics are useful. The gap is operability: the section says these classes “shall support, at minimum” certain conceptual fields, but does not define which are mandatory before draft, before review, and before send. That leaves too much room for divergent implementations.

**Scores:** Practical Operability: 3, Completeness: 4, Developer Synchrony: 2

**Recommendation:**  
Add a mandatory-state matrix, for example:

> For **EMAIL**, **subject**, **recipients**, and **body** shall be present before **send**; **thread context** shall be present for **reply** actions; **tone** may remain policy-optional unless required by template or workflow.  
> For **CALENDAR_INVITE**, **title**, **attendees**, **date/time**, and **timezone** shall be present before **send invite**.

---

### 9. Document composition

**Feedback:**  
§9.2 is a useful subclass registry. §9.3 appropriately delegates templates to policy. §9.4 is substantively strong and one of the better legal/compliance sections in the draft. The trigger-determinism language in §9.4.0 is especially helpful. The main editorial issue is density; the main legal issue is that “reasonable classification” in §9.4.0 is softer than the style guide prefers.

**Scores:** Legal Enforceability: 4, Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:**  
Replace “after reasonable classification” in §9.4.0 with more objective wording:

> When signals conflict or remain unresolved after application of the policy precedence rules above, the runtime shall apply the §9.4 draft posture and disclosure by default...

Also add a short lead sentence to §9.2:
> The identifiers below are canonical subclass labels for governance and audit.

---

### 10. Publication and distribution classes

**Feedback:**  
Clear and appropriately tied to ADD-002 §10.11. No major issue.

**Scores:** Business Model Alignment: 4, Cross-Document Consistency: 4, Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

### 11. Publication-oriented labels (continuity from v0.1.0)

**Feedback:**  
Useful continuity bridge, but it introduces aliasing that could become a second taxonomy if not tightly controlled. The phrase “remain valid aliases” is acceptable, but the section should explicitly state that the §10 classes are canonical.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 3, Practical Operability: 3

**Recommendation:**  
Add:
> The §10 class labels remain canonical for new governance, audit, and implementation work; the A0–A5 labels are legacy compatibility aliases only.

---

### 12. Action semantics (cross-cutting)

**Feedback:**  
Good section. It reinforces the execution distinction well. The action-bearing examples are useful. Minor issue: the action list is broad, but the section does not specify whether all listed actions are required for every applicable class or merely available where supported.

**Scores:** Practical Operability: 3, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:**  
Add:
> Products shall implement the subset of actions applicable to each supported composition class, but shall not collapse distinct supported actions into an unlabeled generic generation flow.

---

### 13. Shell controls (illustrative)

**Feedback:**  
Useful as an illustrative mapping, but because it is illustrative, it should be more clearly separated from mandatory shell obligations elsewhere. As written, it is acceptable but could be mistaken for a minimum required control inventory.

**Scores:** Style & Clarity: 3, Practical Operability: 3, Cross-Document Consistency: 4

**Recommendation:**  
Retitle to:
> **13. Illustrative shell-control mappings (informative)**

---

### 14. Review, approval, and paid gates

**Feedback:**  
This section is short and coherent. It aligns well with ADD-002. No major issue.

**Scores:** Business Model Alignment: 5, Cross-Document Consistency: 5, Conflict Freedom: 5

**Recommendation:**  
No substantive change required.

---

### 15. Packaging defaults (informative)

**Feedback:**  
Appropriately informative and aligned to ADD-002. Clear enough.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 4, Practical Operability: 4

**Recommendation:**  
No substantive change required.

---

### 16. Language, localization, and authoritative version control

**Feedback:**  
Substantively strong and well partitioned from ADD-002, especially §16.7. The L0–L3 model is coherent. The main issue is editorial density and repeated seam language. The final standalone line “§2.1 addendum seams.” is not a complete sentence and reads like an editing artifact.

**Scores:** Cross-Document Consistency: 4, Architectural Fidelity: 5, Style & Clarity: 2

**Recommendation:**  
Delete the stray line:
> **§2.1 addendum seams.**

Also compress §16.7 by removing repeated bold emphasis and converting the bullets into plain prose or a short table.

---

### 17. Measurement contract and quantified claims

**Feedback:**  
This section is strong and practical. It clearly distinguishes procedural obligations from liability guarantees and properly defers reliance/remedies to MPOA in §17.7. Good cross-document discipline.

**Scores:** Legal Enforceability: 4, Platform Economics Synchrony: 5, Practical Operability: 4

**Recommendation:**  
No substantive change required. Minor editorial suggestion: in §17.1, replace “certified survey” with “certified survey or other authoritative measurement record” if broader coverage is desired.

---

### 18. Knowledge basis and discovery gating

**Feedback:**  
Substantively important and mostly well done. The seam with §19 is now much clearer than in earlier drafts implied by the history. §18.11 is useful, but the “Recommended sequence” heading is slightly misleading because parts of it are effectively mandatory. The implementation-joinability sentence is valuable but dense.

**Scores:** Completeness: 5, Architectural Fidelity: 5, Practical Operability: 3, Style & Clarity: 2

**Recommendation:**  
Rename §18.11 to:
> **18.11 Required gate order for non-trivial creation**

Then split into:
- **Before substantive drafting**
- **Before external release**
- **Audit joinability requirement**

Proposed text for the last paragraph:
> When both §18 and §19 apply, the originality evaluation record shall reference the same artifact identifier used for the knowledge-basis state so the two controls are joinable in audit.

---

### 19. Originality, source-boundary, and non-reproduction verification

**Feedback:**  
This is one of the strongest substantive sections. It clearly distinguishes risk control from legal guarantee, defines states, and binds to AIOS-OPS-020. The main issues are readability and some duplication across §§19.1, 19.2, 19.4, and 19.10. Also, the section should use one canonical naming pattern for the implementation home: either document ID plus registry ID, or title plus registry ID, consistently.

**Scores:** Legal Enforceability: 4, Cross-Document Consistency: 4, Practical Operability: 4, Style & Clarity: 2

**Recommendation:**  
1. Standardize all references to the implementation home as:
> **ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD (AIOS-OPS-020)**

2. Consolidate repeated non-waiver language by keeping it in §19.9 and shortening the earlier references.

3. Add one explicit sentence in §19.5:
> These state labels are canonical for governance and audit even if product-facing labels differ.

---

### 20. Reference-guided composition

**Feedback:**  
This section is conceptually rich and generally coherent. It correctly prevents “temperature” conflation and ties adherence to structure rather than copying. The main issue is length and repetition. §§20.1, 20.2, 20.7, 20.10, 20.12, and 20.14 all restate variants of “guidance not copying.” That is doctrinally sound but editorially excessive.

**Scores:** Completeness: 5, Architectural Fidelity: 4, Style & Clarity: 2, Friction Factor: 1

**Recommendation:**  
Condense the section by:
- Keeping the core rule in §20.2
- Keeping taxonomy in §20.3
- Keeping controls in §§20.4–20.5 and §§20.11–20.15
- Moving some repeated explanatory prose from §§20.1, 20.7, and 20.10 into one concise “Boundary rule” subsection

Proposed replacement sentence for §20.1:
> Reference-guided composition shall guide structure, tone, and document anatomy without authorizing verbatim or near-verbatim reproduction of protected expression.

---

### 21. Non-goals

**Feedback:**  
Good section and consistent with the architecture memo. It helps prevent scope bleed.

**Scores:** Conflict Freedom: 5, Cross-Document Consistency: 5, Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Global / all sections | Excessive bolding and visual noise materially reduce readability | Remove most inline bold formatting and reserve bold for defined terms, section labels, and critical mandates only | Critical | 1, 8, 11 |
| 2 | Footer / metadata | Footer says version 0.14.2 while document header says 0.14.5 | Update the closing line to match version 0.14.5 | Critical | 1, 6, 8 |
| 3 | §§0, 1, 5, 16, 19 | Cross-reference forms are inconsistent and path-fragile | Standardize citations to document ID + title, with repository paths only as secondary informative references | High | 1, 6, 8 |
| 4 | §4.2 | Class 2 default contract posture is under-specified | Add a minimum default requiring intent and outcome when policy is silent for persistent or workflow-driving procedural outputs | High | 3, 5, 7 |
| 5 | §5.9 | Minimum validation posture is too policy-dependent in places | Add a default sentence making §5.9 the minimum posture for all Class 3 artifacts unless auditable policy narrows it | High | 3, 5, 7 |
| 6 | §8 | Mandatory fields/actions before send or issue are not explicit enough | Add per-class minimum required-field rules for EMAIL and CALENDAR_INVITE before send/invite issuance | High | 5, 7, 9 |
| 7 | §11 | Legacy A0–A5 labels could create a second taxonomy | State explicitly that §10 labels are canonical and A0–A5 are compatibility aliases only | Medium | 1, 6, 7 |
| 8 | §13 | Informative shell-control examples may be mistaken for mandatory inventory | Retitle section as informative mapping and clarify that mandatory shell obligations live elsewhere | Medium | 1, 7, 8 |
| 9 | §16.7 | Contains a stray fragment and repeated seam language | Delete “§2.1 addendum seams.” and compress the seam language | High | 8, 11 |
| 10 | §18.11 | “Recommended sequence” understates mandatory gate order | Rename as required gate order and split audit joinability into a separate explicit requirement | High | 3, 7, 8 |
| 11 | §19 | Repetition and naming inconsistency around AIOS-OPS-020 | Use one canonical reference form for the implementation home and trim duplicate non-waiver language | Medium | 1, 8, 11 |
| 12 | §20 | Section is too repetitive and cognitively heavy | Consolidate repeated “guidance not copying” language into one boundary rule and shorten surrounding prose | Critical | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is substantively strong and largely coherent with the AMD-2026-008 addendum stack, but its editorial clarity, formatting discipline, and implementation readability are materially below the standard expected for a binding governance document. The composite score is 3.0, and the very low Friction Factor score, combined with weak Style & Clarity and Developer Synchrony, warrants major revision before ratification.

**Top 3 Actions Required:**
1. Remove the pervasive over-formatting and compress repeated seam/boundary language, especially in §§1, 16, 18, 19, and 20.
2. Fix metadata and citation hygiene, including the incorrect footer version and inconsistent cross-reference/path conventions.
3. Tighten minimum implementation rules for Class 2/3 gating and action-bearing artifacts so product teams have a clearer mandatory baseline.
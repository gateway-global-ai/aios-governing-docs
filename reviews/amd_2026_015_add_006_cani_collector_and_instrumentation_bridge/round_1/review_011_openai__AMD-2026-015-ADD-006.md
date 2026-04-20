---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.3
reviewer: OpenAI
review_date: 2026-04-09
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The document is broadly aligned with the CANI family, but Section 3 conflicts with the support contract by using `blocked` instead of the governed provisional status `normalization_blocked`, and several references cite whole documents rather than precise sections. |
| 2 | Business Model Alignment | 3 | The document does not appear to disturb platform economics, but it also does not expressly state its non-economic posture in the way other governance bridges often do. |
| 3 | Legal Enforceability | 3 | The operative prohibitions are mostly clear, but several phrases such as “bounded review” and “other separately governed downstream assessment surfaces” are too open-textured to be enforceable without interpretation. |
| 4 | Architectural Fidelity | 3 | The document preserves the non-authority boundary and validator-before-writer sequencing, but its terminology drift around pre-validator statuses weakens the deterministic handoff model established by ADD-004/005 and the support contract. |
| 5 | Completeness | 3 | The core bridge is present, but the document omits a concise section-level crosswalk of how Section 3, 4, 5, and 6 map to the support contract’s Sections 2-8, leaving edge-case interpretation partially implicit. |
| 6 | Conflict Freedom | 2 | Section 3 creates a direct tension with AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001 Section 2 and Section 7 by classifying `unknown` as `blocked` rather than `normalization_blocked`. |
| 7 | Practical Operability | 3 | A developer or reviewer can generally follow the sequence, but the transition from provisional normalization status to validator outcome is not operationally crisp enough for implementation or validation tooling. |
| 8 | Style & Clarity | 3 | The prose is readable and disciplined, but several sentences are repetitive, some defined concepts are introduced twice, and the document does not consistently use the most exact terminology available from companion documents. |
| 9 | Developer Synchrony | 3 | The document is close to implementable for repo tooling authors, but terminology mismatch with the support contract would likely produce avoidable branching logic or validator confusion. |
| 10 | Platform Economics Synchrony | 3 | No economic contradiction is visible, but the document is silent on whether any collector-related artifacts could impose storage/process overhead constraints, leaving synchrony implicit rather than explicit. |
| 11 | Friction Factor | 3 | The document is not hard to read, but repeated caveats and near-duplicate boundary language increase review friction without adding much new governance precision. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- Sections 1 and 2 clearly position the addendum as a narrow subordinate bridge and preserve the parent authority structure under AMD-2026-015, AMD-2026-015-ADD-004, and AMD-2026-015-ADD-005.
- Section 5 correctly states the core sequencing rule that validator review precedes writer-lane materialization and that `advisory_warning` is not writer-lane admission.
- Section 7 maintains the CANI family’s central governance principle that capture, normalization, and tooling do not collapse into execution authority.
- The document is generally coherent with the storage and validation contracts in treating the writer lane as subordinate to ADD-003 rather than as a new authority surface.

### Critical Gaps

- Section 3 uses `blocked` instead of `normalization_blocked`, which is inconsistent with both the document’s own Section 6 and AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001 Sections 2 and 7.
- Section 2 says the support contract specifies details in “Sections 2 through 8,” but the document does not map its own operative rules to those sections, making cross-document use harder than necessary.
- Section 5 uses vague phrases such as “bounded review” and “other separately governed downstream assessment surfaces” without naming the actual governed lanes or artifact classes.
- The document under review is being scored under an 11-dimension template, but its governing prompt states RUBRIC MODE: LIGHT with 5 dimensions only; this packet-level inconsistency should be corrected outside the document, but it also increases ambiguity in review expectations.

---

## Article-by-Article Review

### 0. Status

**Feedback:**  
The status table is structurally sound and the scope posture is mostly clear. The parenthetical “see Section 5 for writer-lane meaning” is helpful, but it also signals that a key term appears before it is fully defined. That is acceptable, though slightly awkward. More importantly, the scope posture says the document does not create “collector implementations” or “browser instrumentation implementations,” which is consistent with the family, but the phrase “writer handoff” would benefit from a tighter pointer to the exact downstream storage contract section rather than a forward reference only.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 4, Practical Operability: 3

**Recommendation:**  
Revise the scope posture to anchor the writer lane more precisely. Proposed replacement for the Scope posture sentence:

> Narrow doctrine bridge for capture surfaces, intake-envelope normalization, and validator-to-writer handoff into persisted CANI artifact materialization under `AMD-2026-015-ADD-003`. It does not create collector implementations, browser instrumentation implementations, database/event-store services, or execution authority.

---

### 1. Purpose and problem statement

**Feedback:**  
This section is clear and follows the family pattern well. It correctly identifies the gap between intake-envelope doctrine and validator doctrine. The sentence introducing `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` is useful, but “corresponding technical support contract” would be stronger if it named the exact relationship type more explicitly, such as “implementation support contract subordinate to this bridge.” Editorially, the section is slightly repetitive: “This addendum establishes the governing bridge rule” and “This addendum closes that gap” say nearly the same thing.

**Scores:** Cross-Document Consistency: 4, Completeness: 4, Style & Clarity: 3

**Recommendation:**  
Condense the closing lines and tighten the support-contract relationship. Proposed replacement for the last three paragraphs:

> This addendum establishes the governing bridge rule for capture-surface eligibility, pre-validator normalization, and validator-to-writer handoff.  
> `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.1` provides the implementation support contract subordinate to this bridge. It elaborates governed capture-surface classes, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations without creating independent execution authority.  
> This addendum closes the capture-boundary gap without authorizing collector implementation.

---

### 2. Relationship to AMD-2026-015

**Feedback:**  
This section is substantively sound and preserves hierarchy correctly. The strongest part is the explicit subordination to ADD-004 and ADD-005. The weakness is editorial and cross-document: the section cites the support contract’s “Sections 2 through 8” but does not identify which of this addendum’s sections correspond to those support sections. For a governance set that emphasizes precise cross-reference discipline, this is a missed opportunity. Also, “does not expand authority beyond that contract's bounded implementation framing” is slightly backward; the amendment should be primary and the support contract subordinate, not the other way around in phrasing.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 4, Style & Clarity: 3

**Recommendation:**  
Replace the last paragraph with a clearer hierarchy-preserving crosswalk:

> Detailed capture-surface classification is specified in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` Section 2; raw-capture and pre-envelope requirements in Sections 3 through 6; fail-closed pre-validator handling in Section 7; and validator/writer handoff expectations in Section 8. This addendum governs those bridges at the amendment layer and does not enlarge the authority granted by `AMD-2026-015`, `ADD-004`, or `ADD-005`.

---

### 3. Governed capture-surface bridge rule

**Feedback:**  
This is the document’s most important problem section. The first half is coherent and matches the support contract’s allowed surface classes. The defect is the treatment of `unknown`. The support contract states that unresolved `unknown` source surfaces “SHALL be classified as `normalization_blocked` for manual review and SHALL NOT be normalized automatically.” This addendum instead says “classified as `blocked` for manual review.” That is not a harmless abbreviation; it collides with the validator outcome model in ADD-005 and the validator contract, where `blocked` is an authoritative validator outcome. Section 6 of this same document also says pre-validator statuses are `normalization_*` values only. So Section 3 is internally inconsistent and cross-document inconsistent.

**Scores:** Cross-Document Consistency: 1, Conflict Freedom: 1, Architectural Fidelity: 2, Developer Synchrony: 2

**Recommendation:**  
Replace the `unknown` paragraph in full:

> `unknown` is a boundary classification only.  
> It is not an eligible capture surface for automatic normalization.  
> If the source surface cannot be resolved beyond `unknown`, the signal **SHALL** be classified as `normalization_blocked` for manual review and **SHALL NOT** be normalized automatically.

Also add a final sentence to prevent future drift:

> Pre-validator classification in this section uses the provisional normalization statuses defined in Section 6, not the authoritative validator outcomes defined by `AMD-2026-015-ADD-005`.

---

### 4. Raw-capture and normalization rule

**Feedback:**  
This section is generally strong. It aligns well with ADD-004 and the support contract’s distinction between raw capture and normalized intake. The minimum pre-envelope list is useful and mostly mirrors the support contract. The phrase “or an explicit blocked result when sequence cannot be proven” is again terminologically risky because Section 6 later reserves `normalization_blocked` as the provisional status. Even if “blocked result” is descriptive rather than normative here, it invites confusion. The final paragraph correctly avoids converting optional fields into mandatory ones unless needed to avoid fabrication.

**Scores:** Cross-Document Consistency: 3, Practical Operability: 3, Style & Clarity: 3

**Recommendation:**  
Change the last bullet in the minimum pre-envelope list from:

> sequence context sufficient to derive `stream_key` and `sequence_id`, or an explicit blocked result when sequence cannot be proven

to:

> sequence context sufficient to derive `stream_key` and `sequence_id`, or an explicit `normalization_blocked` classification when sequence cannot be proven without invention

This keeps terminology aligned with Section 6 and the support contract.

---

### 5. Validator and writer handoff rule

**Feedback:**  
This section contains the document’s clearest operational rule and is one of its strongest parts. Defining the writer lane as “the non-authoritative downstream materialization surface” is helpful and consistent with ADD-003. The prohibition on treating `advisory_warning` as writer-lane admission is also a good correction relative to the amendment history. The weak point is the phrase “may proceed only to bounded review or other separately governed downstream assessment surfaces.” That language is too vague for a governance document. The document already has named downstream lanes elsewhere in the CANI family: architect planning, UI planning, amendment intake, review preparation, and manual governance review. Those should be named here.

**Scores:** Legal Enforceability: 3, Practical Operability: 4, Style & Clarity: 3

**Recommendation:**  
Replace the paragraph beginning “Under this addendum...” with:

> Under this addendum, validator outcome `advisory_warning` does not authorize writer-lane materialization. It may be attached only to a separately governed review surface, including architect planning, UI planning, amendment intake, review preparation, or manual governance review, when another governing document permits that attachment.

This removes the vague “bounded review” phrase.

---

### 6. Fail-closed outcome rule before validator handoff

**Feedback:**  
This section is conceptually correct and likely reflects the intended repair to earlier drift. It clearly distinguishes provisional normalization statuses from authoritative validator outcomes. That said, because Section 3 still uses `blocked`, this section currently reads as if it corrects a problem the document itself reintroduces. The phrase “must not be emitted as final validator outcomes and must be superseded” is good, but a developer-facing reader would benefit from one explicit sentence stating that no artifact may carry both a provisional normalization status and a final validator outcome as co-equal truth.

**Scores:** Architectural Fidelity: 4, Practical Operability: 3, Developer Synchrony: 3

**Recommendation:**  
Add the following sentence after the paragraph ending with “version `0.1.0`”:

> A single review state surface **SHALL NOT** present a provisional normalization status and an authoritative validator outcome as co-equal final truth for the same handoff decision.

This would make the state transition model crisper.

---

### 7. Non-authority boundary

**Feedback:**  
This section is consistent with the CANI family and well written. It preserves the anti-autonomy posture and avoids overclaiming. Editorially, it is somewhat repetitive with Sections 0, 1, and 9, but that repetition is tolerable in a governance bridge. No substantive conflict is visible here.

**Scores:** Conflict Freedom: 4, Style & Clarity: 4, Architectural Fidelity: 4

**Recommendation:**  
No substantive rewrite required. Optional editorial tightening: remove either “automatic recommendation execution” or “autonomous routing decisions” only if the drafting team wants to reduce repetition, but keeping both is defensible.

---

### 8. Implementation follow-through and affected surfaces

**Feedback:**  
This section is useful but could be more precise. “Registry, tracker, and review-package surfaces that record discoverability and review state for this amendment package” is broad and slightly hand-wavy. Since the document already cross-references AIOS-REVIEW-PACKET-TAXONOMY-001, it would be better to say whether any specific packet artifacts are affected or whether this is merely discoverability metadata. As written, the section is understandable but not maximally crisp.

**Scores:** Completeness: 3, Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:**  
Replace the final bullet with:

> review-packet and registry/discoverability surfaces that record amendment-package identity, status, and review evidence, including structures governed by `AIOS-REVIEW-PACKET-TAXONOMY-001` where this addendum enters peer review

This ties the statement to an existing governed artifact taxonomy.

---

### 9. Out of scope

**Feedback:**  
This section is clear and consistent with the family. The list is appropriately narrow. “Implement browser/runtime collectors” and “define browser instrumentation hooks” are slightly overlapping, but not enough to create confusion. No major issue here.

**Scores:** Conflict Freedom: 4, Style & Clarity: 4, Completeness: 4

**Recommendation:**  
No substantive change required.

---

### 10. Addendum intent summary

**Feedback:**  
The summary accurately captures the bridge. It is concise and consistent with the parent package. The phrase “writer-lane handoff under existing governance boundaries” is good, though it would be even stronger if it echoed the “non-authoritative downstream materialization surface” language from Section 5.

**Scores:** Style & Clarity: 4, Cross-Document Consistency: 4

**Recommendation:**  
Optional refinement:

> The CANI family may now define which capture surfaces are governed, how raw capture becomes normalized intake, and how normalized intake envelopes progress through validator and non-authoritative writer-lane handoff under existing governance boundaries.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Uses `blocked` instead of `normalization_blocked`, creating internal and cross-document conflict with the support contract and validator model. | Replace `blocked` with `normalization_blocked` and add a sentence clarifying that Section 3 uses provisional normalization statuses, not validator outcomes. | Critical | 1, 4, 6, 7, 9 |
| 2 | Section 4 | The phrase “explicit blocked result” repeats the same terminology drift and weakens implementation clarity. | Replace “explicit blocked result” with “explicit `normalization_blocked` classification.” | High | 1, 4, 7, 9 |
| 3 | Section 5 | “Bounded review or other separately governed downstream assessment surfaces” is too vague for enforceable governance prose. | Name the actual governed downstream lanes: architect planning, UI planning, amendment intake, review preparation, and manual governance review. | High | 3, 7, 8 |
| 4 | Section 2 | Cross-reference to the support contract is broad and not section-specific enough for a governance set emphasizing precise coherence. | Add a section-by-section crosswalk to support-contract Sections 2-8. | Medium | 1, 5, 8 |
| 5 | Section 6 | The transition from provisional normalization status to validator outcome is conceptually clear but not explicit enough as a single-state-truth rule. | Add a sentence prohibiting any review state surface from presenting provisional normalization status and validator outcome as co-equal final truth. | Medium | 4, 7, 9 |
| 6 | Section 8 | “Registry, tracker, and review-package surfaces” is too broad and under-specified. | Tie the statement explicitly to review-packet and registry/discoverability structures governed by AIOS-REVIEW-PACKET-TAXONOMY-001. | Medium | 1, 5, 8 |
| 7 | Sections 1-2 | Repetitive support-contract framing slightly obscures hierarchy and adds reading friction. | Condense repeated “closes that gap / establishes the bridge” language and preserve amendment-over-contract hierarchy in phrasing. | Low | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is close to a workable bridge, but Section 3 contains a direct terminology conflict with both its own Section 6 and AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001, which is sufficient to pull Cross-Document Consistency and Conflict Freedom below approval range. Because multiple dimensions score at 2 or below and the composite is below 3.0, major revision is required under the stated disposition rules.

**Top 3 Actions Required:**
1. Correct all pre-validator status terminology so `normalization_blocked` is used consistently instead of `blocked`.
2. Replace vague downstream-routing phrases in Section 5 with named governed lanes already defined elsewhere in the CANI family.
3. Add a precise crosswalk in Section 2 and a single-state-truth clarification in Section 6 to tighten cross-document coherence and implementation clarity.
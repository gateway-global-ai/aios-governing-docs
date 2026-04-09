---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.4
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
| 1 | Cross-Document Consistency | 3 | The document is broadly aligned with the CANI addendum family, but it mixes shorthand references like `ADD-004`/`ADD-005` with full citations and does not follow the rubric’s expected precise section-level citation discipline consistently. |
| 2 | Business Model Alignment | 3 | Nothing in the text appears to conflict with the platform business model, but this dimension is only indirectly addressed because the document is governance-technical and contains no explicit commercial boundary mapping. |
| 3 | Legal Enforceability | 2 | Core prohibitions are clear, but several operative phrases remain interpretive rather than enforceable, especially around “reviewable,” “bounded,” and “suitable for later `payload_ref` and `evidence_refs` handling.” |
| 4 | Architectural Fidelity | 4 | The document preserves the non-authority boundary, validator-before-writer sequencing, and subordination to the persisted-artifact and intake-envelope contracts. |
| 5 | Completeness | 3 | The core bridge is covered, but the amendment omits a tighter definition of the writer lane’s scope, artifact ownership boundaries, and how this addendum relates to the support contract when the two drift. |
| 6 | Conflict Freedom | 3 | No direct contradiction is evident, but there is tension between this amendment’s use of amendment-layer rules and the support contract’s more detailed operational classifications, which could create interpretive drift. |
| 7 | Practical Operability | 2 | The sequence is understandable, but a developer or validator implementer still lacks enough amendment-level precision on when a signal is merely retained as evidence, when it is discarded, and what exact handoff state is authoritative. |
| 8 | Style & Clarity | 3 | The prose is generally clean, but repetitive “does not authorize” phrasing, mixed citation styles, and a few abstract nouns reduce precision and readability. |
| 9 | Developer Synchrony | 2 | The document points to downstream contracts but does not cleanly specify which document is authoritative when amendment text and support-contract detail diverge, which is a likely implementation pain point. |
| 10 | Platform Economics Synchrony | 3 | No economic inconsistency is visible, but the document does not materially engage this dimension. |
| 11 | Friction Factor | 3 | The fail-closed posture is governance-safe, but the document may impose interpretive friction because key operational terms are not normalized at the amendment layer. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- **Sections 2, 5, and 7** preserve the CANI family’s core separation-of-authority doctrine by keeping collectors, normalization, validators, and writers subordinate to existing governance lanes.
- **Section 5** is the strongest operative section; it clearly states that validator outcome `pass` is required before writer-lane progression and that `advisory_warning` is not writer-lane admission.
- **Section 6** usefully distinguishes provisional normalization statuses from authoritative validator outcomes, which is an important anti-drift clarification relative to `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`.
- The document is generally coherent with **AMD-2026-015**, **AMD-2026-015-ADD-004**, **AMD-2026-015-ADD-005**, and **AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001** in preserving non-autonomous, governance-preserving flow.

### Critical Gaps

- **Section 2** relies on support-document section crosswalks but does not state a clear precedence rule if the amendment and the support contract diverge; that is a cross-document coherence gap.
- **Sections 3 and 4** use terms such as “governed,” “reviewable,” “bounded,” and “repo-local reviewable payload reference” without amendment-level definitions or incorporation language, weakening enforceability.
- **Section 5** defines the writer lane only functionally, not normatively enough to prevent future scope creep into validation, routing, or recommendation-state mutation.
- The document does not follow the style guide’s preferred full-document citation discipline consistently; shorthand references like `ADD-004` and `ADD-005` are readable but not ideal for a binding governance instrument.
- The amendment’s authority relationship to the support contract is implied rather than crisply stated, creating implementation ambiguity for future tooling authors.

---

## Article-by-Article Review

### Section 0. Status

**Feedback:**  
This section is concise and mostly effective. The scope posture is aligned with the parent amendment family and correctly denies implementation and execution authority. The phrase “validator-to-writer handoff into persisted CANI artifact materialization” is accurate but dense; it reads more like internal shorthand than governance prose. The section would benefit from one sentence clarifying that this amendment governs only the bridge conditions, while the technical support contract governs the detailed operational model.

**Scores:** Cross-Document Consistency: 4, Legal Enforceability: 3, Style & Clarity: 3

**Recommendation:**  
Add a final sentence to the Scope posture cell:  
**Proposed text:** “This amendment governs the amendment-layer bridge conditions only; detailed operational classification and handoff mechanics remain in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`.”

---

### Section 1. Purpose and problem statement

**Feedback:**  
The section clearly explains why this addendum exists and fits the pattern used across `ADD-002` through `ADD-005`. The strongest sentence is the explicit identification of the gap between capture surfaces, normalization, and writer-lane handoff. However, the paragraph introducing the support contract is slightly awkward because it both delegates detail and asserts non-authority, without clarifying whether the support contract is merely explanatory or incorporated by reference for implementation detail. That distinction matters for cross-document coherence.

**Scores:** Cross-Document Consistency: 3, Completeness: 3, Style & Clarity: 3

**Recommendation:**  
Revise the support-contract paragraph to clarify incorporation scope.  
**Proposed text:** “`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.2` supplies the technical implementation-facing detail for the bridge established here. Where this amendment states a rule and the support contract elaborates that rule, the support contract is subordinate and interpretive, not authority-expanding.”

---

### Section 2. Relationship to AMD-2026-015

**Feedback:**  
This is the section with the most important editorial and coherence issue. It correctly states subordination to the parent amendment and to `AMD-2026-015-ADD-004` and `AMD-2026-015-ADD-005`. It also helpfully maps support-contract sections. But it does not state what happens if the support contract later changes section numbering, wording, or detail in a way that appears broader than the amendment. Because the section explicitly cites “version `0.1.2` Section 2” and “Sections 3 through 6,” it is brittle and may drift quickly. It also mixes full-title citation and shorthand citation style in the same section.

**Scores:** Cross-Document Consistency: 2, Conflict Freedom: 3, Developer Synchrony: 2, Style & Clarity: 3

**Recommendation:**  
Replace the final paragraph with a clearer precedence rule and less brittle crosswalk language.  
**Proposed text:**  
“Detailed capture-surface classification, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations are specified in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.2`. If that support contract and this amendment are read in tension, this amendment controls at the doctrine layer, and the support contract must be interpreted narrowly so as not to expand authority beyond `AMD-2026-015`, `AMD-2026-015-ADD-004`, or `AMD-2026-015-ADD-005`.”

---

### Section 3. Governed capture-surface bridge rule

**Feedback:**  
The core rule is sound and consistent with the support contract. The mandatory handling of `unknown` as `normalization_blocked` is a strong anti-drift provision. The main weakness is definitional precision: “governed and reviewable capture surfaces” is not self-defining at the amendment layer, and the five allowed classes are listed in natural language rather than tied to the controlled values in the support contract. That creates a small but real risk of terminology drift between amendment text and implementation-facing documents.

**Scores:** Architectural Fidelity: 4, Legal Enforceability: 2, Cross-Document Consistency: 3, Practical Operability: 3

**Recommendation:**  
Add a sentence tying the listed classes to the support contract’s controlled source-surface model.  
**Proposed text:** “The surface classes listed in this section are the amendment-layer names for the governed capture classes defined in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`; implementation-facing controlled values must remain consistent with that contract and must not introduce additional eligible classes without amendment.”

---

### Section 4. Raw-capture and normalization rule

**Feedback:**  
This section captures the intended boundary well: raw capture is not yet governed persisted artifact state, and normalization must not invent authority or hidden support. The minimum pre-envelope list is useful. The problem is that several terms remain soft: “bounded reviewable evidence,” “repo-local reviewable payload reference,” and “repo-local evidence basis” are understandable in context but not crisp enough for a binding amendment. The section also says the bridge “SHALL NOT normalize the signal” if any required element is absent, but it does not explicitly say whether the signal may still remain as non-normalized evidence or must be rejected from the governed bridge entirely.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Completeness: 3, Style & Clarity: 3

**Recommendation:**  
Clarify retention-versus-rejection posture.  
**Proposed text:** Add after the last paragraph: “A signal that fails these minimum pre-envelope requirements may remain as non-normalized intake evidence only if it is repo-local and reviewable; it must not be treated as a governed intake envelope, a persisted CANI artifact, or a valid writer-lane input.”

---

### Section 5. Validator and writer handoff rule

**Feedback:**  
This is the strongest section in the document. It clearly subordinates the writer lane to validator outcomes and downstream governance. It also correctly prevents collectors and instrumentation from directly writing persisted artifacts or deciding routing acceptance. The remaining issue is that “writer lane” is defined only as a “non-authoritative downstream materialization surface,” which is conceptually right but still leaves room for future confusion about whether the writer may enrich metadata, assign identifiers, or perform structural transformations. The amendment should say more explicitly that the writer lane materializes only what the governing contracts already permit.

**Scores:** Architectural Fidelity: 5, Practical Operability: 3, Developer Synchrony: 3, Legal Enforceability: 3

**Recommendation:**  
Tighten the writer-lane definition.  
**Proposed text:** Add after the first paragraph: “The writer lane may materialize only the artifact classes, fields, and lifecycle surfaces already authorized by `AMD-2026-015-ADD-003`, `AMD-2026-015-ADD-004`, and their support contracts. It must not create new authority-bearing fields, new persisted location classes, or new routing states.”

---

### Section 6. Fail-closed outcome rule before validator handoff

**Feedback:**  
This section is materially improved over the likely earlier drafts reflected in the amendment history. The distinction between provisional normalization statuses and validator outcomes is now clear. The strongest sentence is the prohibition on silently downgrading hard boundary violations into soft warnings. The only remaining issue is editorial density: the section repeats the distinction between provisional and authoritative outcomes several times. A slightly tighter structure would improve readability without changing meaning.

**Scores:** Cross-Document Consistency: 4, Conflict Freedom: 4, Style & Clarity: 3, Friction Factor: 3

**Recommendation:**  
Condense the opening two paragraphs into one operative statement.  
**Proposed text:** “Before validator handoff, the normalization bridge shall classify capture results only with the provisional statuses in this section. These statuses are pre-validator normalization results only and must not be emitted as final validator outcomes, which remain governed exclusively by `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001` version `0.1.0`.”

---

### Section 7. Non-authority boundary

**Feedback:**  
This section is consistent with the CANI family and appropriately denies collector implementation, browser instrumentation, autonomous routing, and approval-lane collapse. It is clear and familiar in pattern. The only editorial concern is repetition: nearly identical non-authority lists appear across the parent amendment and multiple addenda. That is not a contradiction, but it does create some reading fatigue and increases maintenance burden.

**Scores:** Conflict Freedom: 4, Style & Clarity: 3, Architectural Fidelity: 4

**Recommendation:**  
Keep the section, but tighten one line to align with the rest of the family.  
**Proposed text:** Replace “This addendum governs capture eligibility, normalization discipline, and handoff only.” with “This addendum governs capture-surface eligibility, normalization discipline, and validator-to-writer handoff only.”

---

### Section 8. Implementation follow-through and affected surfaces

**Feedback:**  
The section is coherent and correctly identifies affected surfaces. The phrase “downstream persisted-artifact materialization surfaces subordinate to `AMD-2026-015-ADD-003`” is accurate but cumbersome. More importantly, the section would benefit from a sentence clarifying that discoverability and registry references here do not create new authority surfaces, only package visibility. That would align better with `AMD-2026-015-ADD-001`.

**Scores:** Cross-Document Consistency: 3, Completeness: 3, Style & Clarity: 3

**Recommendation:**  
Add a final sentence before the closing sentence.  
**Proposed text:** “References to registry, tracker, and review-package surfaces in this section concern discoverability and review traceability only; they do not create new authority-bearing execution or persistence surfaces.”

---

### Section 9. Out of scope

**Feedback:**  
This section is clear and consistent with the family pattern. It effectively prevents overreading of the amendment. No substantive issue appears here.

**Scores:** Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
No substantive change required. Optional editorial tightening: replace “define persistence backends” with “define persistence backends or services” for symmetry with earlier sections.

---

### Section 10. Addendum intent summary

**Feedback:**  
The summary accurately states the amendment’s purpose and preserves the non-authority boundary. It is concise and effective. No major issue appears here.

**Scores:** Style & Clarity: 4, Architectural Fidelity: 4

**Recommendation:**  
No substantive change required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 2 | No explicit precedence rule between the amendment and the support contract creates cross-document ambiguity. | Add a doctrine-layer precedence sentence stating that the amendment controls if read in tension with `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`. | Critical | 1, 3, 6, 9 |
| 2 | Section 4 | The amendment does not clearly state whether failed normalization candidates may remain as evidence or must be discarded. | Add explicit language that such signals may remain only as non-normalized repo-local reviewable evidence and may not be treated as governed intake or writer-lane input. | Critical | 3, 5, 7, 11 |
| 3 | Section 5 | The writer lane is underdefined and could drift into broader authority or transformation scope. | Add language limiting the writer lane to materializing only already-authorized artifact classes, fields, and lifecycle surfaces. | High | 3, 4, 5, 7, 9 |
| 4 | Section 3 | Allowed capture classes are listed in prose without a tight tie to the support contract’s controlled values. | Add a sentence binding implementation-facing controlled values to the support contract and prohibiting new eligible classes without amendment. | High | 1, 4, 7, 9 |
| 5 | Section 1 | The support-contract paragraph does not clearly distinguish interpretive detail from authority expansion. | Revise the paragraph to say the support contract is implementation-facing and subordinate, not authority-expanding. | High | 1, 3, 6, 8 |
| 6 | Sections 2, 4, 8 | Mixed shorthand citation style and abstract terms reduce precision in a binding document. | Replace shorthand references where feasible with full document IDs/titles on first use in each section and tighten terms like “bounded” and “reviewable” through incorporation language. | Medium | 1, 3, 8 |
| 7 | Section 6 | The provisional-status explanation is slightly repetitive and denser than necessary. | Condense the opening explanation into one operative statement while preserving the anti-drift rule. | Low | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is substantively aligned with the CANI governance family, but it falls below approval threshold because legal precision, practical operability, and cross-document coherence are not yet strong enough for a binding amendment-layer bridge. The main issues are not conceptual; they are authority-boundary and precedence ambiguities that should be corrected before ratification.

**Top 3 Actions Required:**
1. Add an explicit precedence rule in Section 2 stating how this amendment controls relative to the support contract if the two are read in tension.
2. Clarify in Section 4 what happens to failed normalization candidates, including whether they may remain as evidence and what authority they do not acquire.
3. Tighten Section 5 so the writer lane is expressly limited to materializing already-authorized artifact classes and cannot expand into new authority-bearing behavior.
---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.0
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
| 1 | Cross-Document Consistency | 3 | The document is broadly aligned with the CANI family, but it introduces terminology and outcome handling that are not cleanly harmonized with the bundled technical support contract and does not cite specific sections when invoking controlling documents. |
| 2 | Business Model Alignment | 3 | Nothing in the addendum appears commercially destabilizing, but the document is largely silent on any operational boundary implications beyond governance posture. |
| 3 | Legal Enforceability | 2 | Several rules rely on broad phrases such as “policy/routing conditions are satisfied” and “clean automatic normalization” without defining the controlling source or decision standard. |
| 4 | Architectural Fidelity | 4 | The addendum preserves the non-authority boundary, validator-before-writer sequencing, and repo-governed artifact model consistently with the parent CANI architecture. |
| 5 | Completeness | 3 | The core bridge is present, but important details from the referenced technical contract are omitted or compressed, especially source-surface classification behavior and pre-envelope minimum requirements. |
| 6 | Conflict Freedom | 3 | No direct contradiction is evident, but there is tension with the more detailed capture-surface contract because this addendum narrows and paraphrases rules in ways that could drift over time. |
| 7 | Practical Operability | 2 | A developer or reviewer cannot reliably implement or validate this bridge from the addendum alone because key decision points and required fields are deferred or underspecified. |
| 8 | Style & Clarity | 4 | The prose is concise and mostly clear, with strong scope discipline and consistent sectioning, but some phrases remain ambiguous and under-defined. |
| 9 | Developer Synchrony | 2 | The document does not map its high-level rules tightly enough to the concrete field and state model already defined in the technical support documents, increasing implementation drift risk. |
| 10 | Platform Economics Synchrony | 3 | The document does not create obvious economic conflict, but it also does not materially address cost, operational burden, or lane ownership implications. |
| 11 | Friction Factor | 2 | The bridge adds another layer of doctrine without enough explicit crosswalk language, so readers must reconcile this addendum against ADD-004, ADD-005, and the capture-surface contract manually. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- Sections 2, 5, and 7 preserve the CANI family’s core non-authority doctrine and correctly keep collectors/instrumentation subordinate to validator and writer lanes.
- Section 5 is architecturally coherent with `AMD-2026-015-ADD-003`, `AMD-2026-015-ADD-004`, and `AMD-2026-015-ADD-005` in requiring normalization before validation and validation before persistence.
- Section 7 clearly restates the prohibition on autonomous routing, runtime UI mutation, and silent self-amendment, which is important for family-wide coherence.

### Critical Gaps

- Section 3 is materially thinner than `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` Sections 2 and 7 and omits the explicit `unknown` boundary classification rule, creating avoidable drift.
- Section 4 does not incorporate the minimum pre-envelope capture requirements defined in the technical support contract Section 4, leaving the bridge under-specified.
- Section 5 uses the phrase “if validator outcome permits and policy/routing conditions are satisfied” without identifying the governing source for those conditions, which weakens enforceability and operability.
- The document repeatedly references controlling documents only by document ID/title and not by section, contrary to the injected style guide’s preferred cross-reference practice.
- The output rubric supplied in the prompt is the full 11-dimension template, but the governing review instructions specify LIGHT mode with 5 dimensions only; this mismatch should be corrected in the review pipeline, though it is external to the document text.

---

## Article-by-Article Review

### 0. Status

**Feedback:** This section is structurally sound and consistent with sibling addenda. The scope posture is clear and correctly disclaims implementation and execution authority. Editorially, it reads well. The only issue is that “validator/writer handoff” is introduced here before the document later defines the exact sequencing and without tying “writer” back to the persisted-artifact contract section that governs it.

**Scores:** Cross-Document Consistency: 4, Legal Enforceability: 4, Style & Clarity: 4

**Recommendation:** Add one sentence tying “writer lane” explicitly to the persisted-artifact contract. Proposed text after the scope posture sentence: “For avoidance of doubt, any ‘writer lane’ referenced in this addendum means a downstream materialization step subordinate to the persisted-artifact contract defined by `AMD-2026-015-ADD-003` and its technical support document.”

---

### 1. Purpose and problem statement

**Feedback:** The section correctly positions this addendum after `ADD-004` and `ADD-005`, but it omits the already-bundled technical support document `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`, which is the closest companion document. Because this addendum is effectively the doctrine bridge for that contract, the omission weakens cross-document coherence. The problem statement is otherwise clear.

**Scores:** Cross-Document Consistency: 3, Completeness: 3, Style & Clarity: 4

**Recommendation:** Add an explicit sentence acknowledging the companion technical support contract. Proposed insertion before the final sentence: “The corresponding technical support contract defines the field-level capture-surface classes, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations that implement this bridge.”

---

### 2. Relationship to AMD-2026-015

**Feedback:** This section is consistent with the family pattern and correctly states subordination to `ADD-004` and `ADD-005`. However, because the addendum also depends heavily on the capture-surface technical contract, the relationship statement should acknowledge that this amendment is doctrinal while the technical contract carries the detailed operational framing. Without that, readers must infer the doctrinal/technical split.

**Scores:** Cross-Document Consistency: 4, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:** Add a final sentence: “Detailed capture-surface classification, pre-envelope requirements, and fail-closed handoff expectations are specified in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`; this addendum supplies the governing bridge only.”

---

### 3. Governed capture-surface bridge rule

**Feedback:** This is the section with the largest coherence problem. The listed classes generally match the technical support contract, but the wording drifts: “UI surface observations” differs from the contract’s “UI surface observation”; “bounded operator notes” differs from “Operator note”; and the section omits the explicit rule that `unknown` is a boundary classification and not an eligible capture surface. The final sentence also says signals “must fail or block,” but does not preserve the contract’s more precise distinction between ineligible capture and ambiguous-but-reviewable capture. This creates editorial and implementation drift.

**Scores:** Cross-Document Consistency: 2, Completeness: 2, Developer Synchrony: 2

**Recommendation:** Replace the section with language that mirrors the technical contract more closely. Proposed replacement text:

“Only governed and reviewable capture surfaces **MAY** emit CANI-relevant signals for intake-envelope construction. Allowed surface classes are:

1. shell/operator flow  
2. UI surface observation  
3. planning artifacts  
4. review artifacts  
5. operator note

`unknown` is a boundary classification only. It is not an eligible capture surface for clean automatic normalization. If the source surface cannot be resolved beyond `unknown`, the signal should be `blocked` for manual review rather than silently normalized. Signals outside the allowed classes must fail closed rather than being treated as governed intake.”

---

### 4. Raw-capture and normalization rule

**Feedback:** The section is directionally correct but too compressed relative to the technical support contract. It does not state that raw capture may exist only as bounded reviewable evidence referenced by `payload_ref` and `evidence_refs`, and it omits the minimum pre-envelope capture requirements that make normalization possible without invention. Because this section is the doctrinal bridge for normalization, those omissions matter. The phrase “boundary discipline” is also vague.

**Scores:** Completeness: 2, Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Expand the section to include the minimum doctrinal requirements. Proposed added paragraph after item 4: “Raw capture is not yet a governed persisted CANI artifact. It may exist only as bounded reviewable evidence suitable for later `payload_ref` and `evidence_refs` handling under the intake-envelope contract. Before normalization, the capture candidate must preserve enough information to support source-surface classification, signal-family candidate, signal-type candidate, repo-local reviewable payload reference, repo-local evidence basis, admitted-by attribution, and sequence context sufficient to derive `stream_key` and `sequence_id`, or else the signal must be blocked rather than normalized.”

---

### 5. Validator and writer handoff rule

**Feedback:** Architecturally this section is strong, but the phrase “if validator outcome permits and policy/routing conditions are satisfied” is under-defined. Which policy? Which routing conditions? Are these conditions those in `ADD-003`, `ADD-004`, `ADD-005`, the schema contract, or lane-specific downstream documents such as `AIOS-AMD-PLAN-001` and `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001`? The section should specify that the writer lane is subordinate to the persisted-artifact contract and that routing acceptance remains governed by downstream lane documents, not this bridge.

**Scores:** Legal Enforceability: 2, Architectural Fidelity: 4, Practical Operability: 3

**Recommendation:** Replace “if validator outcome permits and policy/routing conditions are satisfied” with more precise language. Proposed revision: “only if the validator outcome is `pass` or a non-blocking `advisory_warning`, and only where downstream lane rules permit materialization under `AMD-2026-015-ADD-003`, may the envelope hand off into the writer lane for persisted artifacts. Routing acceptance, planning acceptance, and review acceptance remain governed by the downstream lane documents that own those decisions.”

---

### 6. Fail-closed outcome rule before validator handoff

**Feedback:** This section is useful, but it risks duplicating and slightly mutating the outcome model already defined in the technical support contract and validator contract. The phrase “missing required sequence/provenance needed for clean normalization” is understandable but still vague. More importantly, this section should explicitly state that these are pre-validator classification outcomes aligned to the same outcome family used by the validator contract, not validator outcomes themselves. Otherwise readers may confuse capture-normalization classification with formal validator results.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 3, Style & Clarity: 4

**Recommendation:** Add a clarifying lead sentence and tighten the wording. Proposed insertion after the first sentence: “These are pre-validator classification outcomes aligned to the CANI outcome family; they are not a substitute for the formal validator result governed by `AMD-2026-015-ADD-005`.” Also replace “missing required sequence/provenance needed for clean normalization” with “missing sequence or provenance data required by the intake-envelope contract to construct a reviewable envelope without invention.”

---

### 7. Non-authority boundary

**Feedback:** This section is strong and consistent with the family. The only editorial issue is the phrase “collector implementation by itself,” which is slightly awkward and could be read as implying collector implementation might be authorized by some combination of documents. The intended meaning is likely that this addendum does not itself authorize implementation. Similar phrasing appears in sibling documents, so this is not unique, but it remains stylistically imprecise.

**Scores:** Conflict Freedom: 4, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:** Replace “collector implementation by itself” with “collector implementation” or “collector implementation authority.” Proposed text: “Nothing in this addendum authorizes collector implementation, browser instrumentation implementation, database schema or migrations, event-store implementation, persistence backends outside the governed repo tree, automatic recommendation execution, runtime UI modification, autonomous routing decisions, silent self-ratification, silent self-amendment, or approval-lane collapse across architect, UI, review, kernel, or ratification.”

---

### 8. Implementation follow-through and affected surfaces

**Feedback:** This section is coherent but under-specific. It references “the new technical support document for capture-surface and normalization handoff” without naming it, even though the front matter includes the exact document ID and title. For cross-document coherence, the named document should appear in the body. Also, “existing validator and writer lanes” would benefit from explicit linkage to `ADD-005` and `ADD-003`.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 2, Style & Clarity: 4

**Recommendation:** Replace the second bullet with a named reference and tighten the downstream references. Proposed bullets:
- “`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` as the technical support document for capture-surface classification, pre-envelope requirements, and normalization handoff”
- “validator lanes governed by `AMD-2026-015-ADD-005` and persisted-artifact writer lanes subordinate to `AMD-2026-015-ADD-003` as downstream recipients of valid normalized intake envelopes”

---

### 9. Out of scope

**Feedback:** This section is clear and consistent with the family pattern. The phrase “redesign the approved writer slice” is the only notable problem; “approved writer slice” is not a term used elsewhere in the bundled CANI documents and may confuse readers. It appears to refer to the existing persisted-artifact writer lane, but that is not the same phrase.

**Scores:** Cross-Document Consistency: 2, Style & Clarity: 3, Conflict Freedom: 4

**Recommendation:** Replace “redesign the approved writer slice” with a canonical phrase already used elsewhere. Proposed text: “redesign the existing persisted-artifact writer lane” or, better, “redesign the persisted-artifact materialization path governed by `ADD-003`.”

---

### 10. Addendum intent summary

**Feedback:** The summary is concise and accurate. It restates the bridge cleanly and preserves the family’s non-authority posture. No substantive issue here.

**Scores:** Style & Clarity: 5, Architectural Fidelity: 4, Conflict Freedom: 4

**Recommendation:** No substantive change required. Optional editorial refinement: replace “Those bridges remain governance-preserving seams” with “Those bridges remain governance-preserving boundaries” for plainer wording.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Capture-surface classes drift from the technical support contract and omit the `unknown` boundary rule. | Rewrite Section 3 to mirror the allowed surface classes and explicitly state that `unknown` is a boundary classification that must be blocked for manual review. | Critical | 1, 5, 6, 9, 11 |
| 2 | Section 4 | Raw-capture normalization is under-specified and omits minimum pre-envelope requirements. | Add doctrinal language covering repo-local evidence, payload/evidence references, admitted-by attribution, and sequence context requirements before normalization. | Critical | 3, 5, 7, 9 |
| 3 | Section 5 | “Policy/routing conditions are satisfied” is vague and not tied to controlling documents. | Specify which validator outcomes permit handoff and state that downstream lane acceptance remains governed by `ADD-003`, `ADD-005`, and lane-specific documents. | Critical | 3, 7, 9 |
| 4 | Section 6 | Pre-validator outcomes may be confused with formal validator outcomes. | Clarify that Section 6 defines pre-validator classification aligned to, but distinct from, the formal validator outcome model in `ADD-005`. | High | 1, 6, 7, 11 |
| 5 | Sections 1, 2, 8 | The companion technical support document is not named in the body, weakening doctrinal/technical crosswalk clarity. | Name `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` explicitly in the body and describe its role. | High | 1, 5, 9, 11 |
| 6 | Section 9 | “approved writer slice” is non-canonical terminology. | Replace it with “persisted-artifact writer lane” or equivalent canonical phrasing tied to `ADD-003`. | Medium | 1, 8, 9 |
| 7 | Global | Cross-references cite document IDs/titles but not specific sections, contrary to the style guide. | Add section-specific references where this addendum relies on particular rules from `ADD-003`, `ADD-004`, `ADD-005`, and the technical support contract. | Medium | 1, 3, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is architecturally sound and directionally consistent with the CANI family, but it is too thin and slightly drift-prone in the exact areas where it is supposed to bridge doctrine to the capture-surface technical contract. The resulting ambiguity in Sections 3 through 6 materially weakens cross-document coherence and practical operability.

**Top 3 Actions Required:**
1. Rewrite Sections 3 and 4 so they align explicitly with the capture-surface technical support contract, including the `unknown` boundary rule and minimum pre-envelope requirements.
2. Tighten Section 5 to define exactly when writer-lane handoff is permitted and which downstream documents govern routing and acceptance.
3. Add explicit doctrinal-to-technical crosswalk language naming `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` and using canonical terminology consistently throughout.
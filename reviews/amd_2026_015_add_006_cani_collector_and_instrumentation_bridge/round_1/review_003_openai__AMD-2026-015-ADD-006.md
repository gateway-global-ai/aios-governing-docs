---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.1
reviewer: OpenAI
review_date: 2026-04-09
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The document is broadly aligned with the CANI family, but it mixes shorthand references (`ADD-003`, `ADD-004`, `ADD-005`) with full document IDs and does not consistently use the more precise support-contract terminology already established elsewhere. |
| 2 | Business Model Alignment | 3 | The document does not create obvious business-model conflict, but this dimension is only indirectly addressed because the addendum is purely governance-technical and does not expressly situate its constraints against platform-commercial boundaries. |
| 3 | Legal Enforceability | 3 | Most rules are framed with enforceable modal verbs, but several provisions rely on soft phrasing such as “should be `blocked`” and “where downstream lane rules permit,” which weakens determinacy. |
| 4 | Architectural Fidelity | 4 | The addendum preserves the CANI architecture’s non-authority boundary, validator-before-writer sequencing, and repo-governed artifact discipline with good fidelity. |
| 5 | Completeness | 3 | The core bridge is present, but the document leaves key edge conditions under-specified, especially the relationship between pre-validator outcomes and formal validator outcomes and the exact meaning of “writer lane.” |
| 6 | Conflict Freedom | 4 | No direct contradiction with the bundled CANI documents appears, though some wording creates tension with the stricter fail-closed language in the support contract. |
| 7 | Practical Operability | 3 | The sequence is understandable, but an implementer still lacks crisp decision rules for when `advisory_warning` may proceed and what policy surface governs “downstream lane rules.” |
| 8 | Style & Clarity | 3 | The prose is generally clear, but several sentences are repetitive, some defined concepts are introduced imprecisely, and the document does not fully follow the style guide’s preference for exact cross-references and canonical naming. |
| 9 | Developer Synchrony | 3 | A developer can infer the intended pipeline, but the handoff semantics are split across this addendum and the support contract without a clean normative boundary statement. |
| 10 | Platform Economics Synchrony | 3 | No economic inconsistency is evident, but the document is largely silent on this dimension and therefore only acceptable by absence of conflict rather than affirmative alignment. |
| 11 | Friction Factor | 4 | The document is narrow and readable, and it avoids overbuilding the bridge, but some ambiguity in outcome handling would create avoidable implementation friction. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- Sections 1-2 clearly position the addendum as a narrow subordinate bridge within the `AMD-2026-015` family and preserve the parent amendment’s recommendation non-authority boundary.
- Sections 5 and 7 are strong on governance preservation: they clearly prohibit direct persisted writes, validator bypass, autonomous routing, and approval-lane collapse.
- The document is materially consistent with `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`, `AMD-2026-015-ADD-004`, and `AMD-2026-015-ADD-005` in treating raw capture as pre-envelope evidence and normalized intake as the first governed intake boundary.

### Critical Gaps

- Section 5 uses the phrase “writer lane” without fully defining it in-document, then relies on a brief clarification in Section 0; that is too thin for a binding bridge document.
- Sections 3 and 6 use softer language than the support contract on fail-closed handling; “should be `blocked`” is weaker than the surrounding family’s otherwise mandatory posture.
- The document does not clearly distinguish the legal status of pre-validator classification outcomes from formal validator outcomes, creating a risk of process confusion across `ADD-005` and the support contract.
- Cross-document citation style is inconsistent with the style guide: the document cites by document ID only and not by specific section where the dependency is substantive.

---

## Article-by-Article Review

### 0. Status

**Feedback:**  
This section is concise and useful, especially the sentence clarifying that “writer lane” means a downstream materialization step subordinate to `AMD-2026-015-ADD-003`. However, that clarification is too important to be confined to a brief “avoidance of doubt” sentence in the status section. Because “writer lane” is a central operational term in Sections 5, 8, and 10, it should be defined in the body where operative rules are stated. As written, the reader must carry a quasi-definition from Section 0 into the normative core.

**Scores:** Architectural Fidelity: 4, Style & Clarity: 3, Practical Operability: 3

**Recommendation:**  
Move the definition into Section 5 and tighten it. Proposed text:

> For purposes of this addendum, the **writer lane** means the downstream governed materialization step that writes persisted CANI artifacts under the storage contract defined by `AMD-2026-015-ADD-003`. The writer lane is not an independent authority surface and remains subordinate to validator outcomes and downstream governance rules.

---

### 1. Purpose and problem statement

**Feedback:**  
This section effectively states the gap and ties the document to `ADD-004`, `ADD-005`, and the support contract. Editorially, it is one of the stronger sections. The main issue is that it says the support contract “supplies the detailed operational crosswalk,” but does not specify whether that support contract is merely explanatory or incorporated as the technical implementation reference for this addendum. Given the family structure, that relationship should be explicit.

**Scores:** Cross-Document Consistency: 3, Completeness: 3, Style & Clarity: 4

**Recommendation:**  
Add a sentence clarifying the normative/support relationship. Proposed text:

> This addendum establishes the governing bridge rule. `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` defines the corresponding technical support contract and should be read as the implementation-facing elaboration of this addendum, not as an independent source of execution authority.

---

### 2. Relationship to AMD-2026-015

**Feedback:**  
The section is structurally consistent with the other CANI addenda and appropriately limits scope. The main editorial weakness is the use of shorthand references (`ADD-004` / `ADD-005`) without pairing them with full titles or section-level anchors. Across the bundled set, shorthand is common, but the style guide expressly prefers full title plus specific section when the dependency is substantive. This section is where those dependencies are most substantive.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 4, Style & Clarity: 3

**Recommendation:**  
Replace the final sentence with a more precise cross-reference. Proposed text:

> It remains subordinate to `AMD-2026-015-ADD-004 — CANI Telemetry Ingestion Envelope and Normalization Bridge` for intake-envelope behavior and to `AMD-2026-015-ADD-005 — CANI Validator and Tooling Bridge` for validator behavior. Detailed capture-surface classification, minimum pre-envelope requirements, and fail-closed handoff expectations are specified in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` (Sections 2-8).

---

### 3. Governed capture-surface bridge rule

**Feedback:**  
This section is substantively aligned with the support contract’s allowed surface classes and the `unknown` boundary classification. The problem is enforceability drift: “If the source surface cannot be resolved beyond `unknown`, the signal should be `blocked` for manual review rather than silently normalized.” In the support contract, unresolved `unknown` classification is treated more strictly as a blocked condition. In a binding addendum, “should” is too soft and creates unnecessary interpretive slack.

**Scores:** Legal Enforceability: 2, Cross-Document Consistency: 3, Conflict Freedom: 3

**Recommendation:**  
Replace the soft sentence with mandatory language. Proposed text:

> If the source surface cannot be resolved beyond `unknown`, the signal **SHALL** be classified as `blocked` for manual review and **SHALL NOT** be normalized automatically.

Also consider adding:

> Only the allowed surface classes listed in this section are eligible for intake-envelope construction.

---

### 4. Raw-capture and normalization rule

**Feedback:**  
This section is mostly strong and tracks the support contract well. It clearly distinguishes raw capture from normalized intake and preserves the `payload_ref` / `evidence_refs` boundary inherited from `ADD-004`. The main issue is that the minimum pre-envelope requirements are embedded as a prose list without clearly stating whether all are mandatory prerequisites or whether some may be absent if the result is `blocked`. The final sentence partly answers this, but the logic could be cleaner.

**Scores:** Completeness: 3, Practical Operability: 3, Architectural Fidelity: 4

**Recommendation:**  
Split the requirements into “required for normalization” and “required for blocked classification.” Proposed text:

> A capture candidate is eligible for normalization only if it preserves all of the following: source-surface classification, signal-family candidate, signal-type candidate, repo-local reviewable payload reference, repo-local evidence basis, admitted-by attribution, and sequence context sufficient to derive `stream_key` and `sequence_id`.  
> If any required element is absent, the bridge **SHALL NOT** normalize the signal and **SHALL** classify it as `blocked` or `fail` under Section 6, as applicable.

---

### 5. Validator and writer handoff rule

**Feedback:**  
This is the most operationally important section and the one most in need of tightening. The sequence is clear, and the prohibition on direct persisted writes is excellent. The ambiguity lies in the phrase “only if the validator outcome is `pass` or a non-blocking `advisory_warning`, and only where downstream lane rules permit materialization under `ADD-003`.” That leaves at least three open questions: who decides whether an `advisory_warning` is non-blocking, what exact downstream rules are being invoked, and whether the writer lane itself may impose additional checks. This is implementable in spirit but not crisp enough for governance text.

**Scores:** Practical Operability: 2, Legal Enforceability: 3, Developer Synchrony: 2

**Recommendation:**  
Define the decision boundary explicitly. Proposed text:

> The handoff sequence **SHALL** be: (1) eligible capture candidate identified; (2) normalized intake envelope constructed; (3) envelope submitted to validator/tooling; (4) envelope may proceed to the writer lane only if validator/tooling returns `pass`, or returns `advisory_warning` together with an explicit policy result that persistence may proceed.  
> A collector, instrumentation surface, or normalization bridge **SHALL NOT** treat `advisory_warning` as self-authorizing. Any persistence decision associated with `advisory_warning` **SHALL** be governed by the validator/tooling policy surface and the persisted-artifact contract under `AMD-2026-015-ADD-003`.

---

### 6. Fail-closed outcome rule before validator handoff

**Feedback:**  
This section usefully distinguishes pre-validator classification outcomes from formal validator outcomes, but it does not state that these pre-validator outcomes are provisional and local to the normalization bridge. Without that sentence, readers may confuse them with the authoritative validator outcomes in `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`. Also, the phrase “aligned to the CANI outcome family” is not itself a defined term elsewhere in the bundled set, so it reads as a loose family resemblance rather than a precise governance concept.

**Scores:** Cross-Document Consistency: 2, Style & Clarity: 3, Completeness: 3

**Recommendation:**  
Clarify the status of these outcomes and remove the undefined “outcome family” phrasing. Proposed text:

> These classifications are pre-validator normalization outcomes only. They exist to control fail-closed handling before formal validator review and do not replace or override the authoritative validator outcomes defined by `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`.  
> The normalization bridge **SHALL** record one of the following provisional classifications before validator handoff: `pass`, `fail`, `blocked`, or `advisory_warning`.

Also replace “Use:” with “The normalization bridge **SHALL** use:” for stronger rule framing.

---

### 7. Non-authority boundary

**Feedback:**  
This section is strong and consistent with the rest of the CANI family. It clearly preserves governance boundaries and avoids accidental expansion into runtime authority. Editorially, it is repetitive with prior addenda, but that repetition is acceptable in a boundary section because it reduces ambiguity.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5, Style & Clarity: 4

**Recommendation:**  
No substantive change required. Minor editorial improvement: add “direct persisted-artifact writing” to the list for symmetry with Section 5.

---

### 8. Implementation follow-through and affected surfaces

**Feedback:**  
This section is coherent and correctly identifies the support contract and downstream recipients. The phrase “validator lanes governed by `ADD-005` and persisted-artifact writer lanes subordinate to `ADD-003`” is directionally clear but still relies on the undefined “writer lane” concept noted earlier. Also, “registry, tracker, and review-package surfaces” is broad and somewhat vague; if these are not governed surfaces with defined names in the bundled set, the phrase should be narrowed or qualified.

**Scores:** Completeness: 3, Style & Clarity: 3, Developer Synchrony: 3

**Recommendation:**  
Tighten the last bullet. Proposed text:

> validator surfaces governed by `AMD-2026-015-ADD-005` and downstream persisted-artifact materialization surfaces subordinate to `AMD-2026-015-ADD-003` as recipients of valid normalized intake envelopes

If “tracker” is retained, cite the governing tracker document; otherwise remove it.

---

### 9. Out of scope

**Feedback:**  
This section is clear and consistent with the family’s narrow-bridge pattern. It appropriately excludes collectors, hooks, services, persistence backends, and autonomous routing. No major issue here.

**Scores:** Conflict Freedom: 4, Style & Clarity: 4, Architectural Fidelity: 4

**Recommendation:**  
No substantive revision required.

---

### 10. Addendum intent summary

**Feedback:**  
The summary accurately states the document’s purpose and preserves the non-authority boundary. It is concise and readable. The only editorial issue is that “writer lanes” again appears without a body definition, reinforcing the need to define that term in Section 5.

**Scores:** Style & Clarity: 3, Friction Factor: 4

**Recommendation:**  
After defining “writer lane” in Section 5, retain this section with only a conforming terminology update if needed.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Soft wording weakens fail-closed enforcement for `unknown` source classification. | Replace “should be `blocked`” with “SHALL be classified as `blocked` and SHALL NOT be normalized automatically.” | Critical | 1, 3, 6, 7, 8 |
| 2 | Section 5 | `advisory_warning` persistence path is under-specified and operationally ambiguous. | Define who may allow progression after `advisory_warning` and state that collectors/normalizers cannot self-authorize persistence. | Critical | 3, 5, 7, 9, 11 |
| 3 | Section 6 | Pre-validator outcomes are not clearly distinguished from formal validator outcomes. | State expressly that these are provisional normalization classifications and do not replace `ADD-005` validator outcomes. | High | 1, 5, 7, 8, 9 |
| 4 | Sections 0, 5, 8, 10 | “Writer lane” is central but insufficiently defined. | Move and expand the definition into Section 5 as an operative term tied to `AMD-2026-015-ADD-003`. | High | 5, 7, 8, 9 |
| 5 | Sections 1-2 | Cross-reference style is too shorthand-heavy for a binding governance document. | Use full document titles and, where dependency is substantive, cite the relevant sections of the support contract. | Medium | 1, 8 |
| 6 | Section 4 | Minimum pre-envelope requirements are not cleanly separated from blocked/fail handling. | Rewrite to distinguish mandatory prerequisites for normalization from conditions that require `blocked` or `fail`. | Medium | 5, 7, 9 |
| 7 | Section 8 | “registry, tracker, and review-package surfaces” is broader than the cited governed set supports. | Narrow the phrase or cite the specific governing tracker/reference document if one is intended. | Low | 1, 5, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is structurally sound and architecturally aligned, but multiple core provisions remain too soft or too ambiguous for a binding bridge addendum, especially around fail-closed handling, pre-validator versus validator outcomes, and writer-lane progression after `advisory_warning`. The composite score is 3.0, and the operational ambiguities are substantive enough to require revision before approval.

**Top 3 Actions Required:**
1. Make Section 3’s `unknown`-surface handling mandatory rather than advisory.
2. Rewrite Section 5 to define the writer lane and specify exactly when `advisory_warning` may still proceed.
3. Clarify in Section 6 that pre-validator classifications are provisional normalization outcomes and do not replace formal validator results.
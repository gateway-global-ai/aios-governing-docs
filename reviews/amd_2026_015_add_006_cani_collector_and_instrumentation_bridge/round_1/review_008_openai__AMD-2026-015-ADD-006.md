---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.2
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
| 1 | Cross-Document Consistency | 3 | The document is broadly aligned with the CANI family, but it introduces section-specific references and outcome semantics that do not fully match the bundled Light rubric or the surrounding document-set citation discipline. |
| 2 | Business Model Alignment | 3 | The document does not appear to disrupt the platform business model, but this dimension is only indirectly addressed because the addendum is narrowly procedural and contains no explicit commercial or tenant-facing framing. |
| 3 | Legal Enforceability | 2 | Several operative phrases remain too abstract for enforceable interpretation, especially “explicit policy result that persistence may proceed” and “writer lane,” which are not anchored to a named governing authority surface. |
| 4 | Architectural Fidelity | 4 | The document preserves the non-authority boundary, validator supremacy, and storage-contract subordination with strong consistency to ADD-003 through ADD-005. |
| 5 | Completeness | 3 | The core bridge is present, but the document omits a precise crosswalk for who issues the policy result permitting persistence after `advisory_warning` and does not fully define the status of provisional pre-validator outcomes once validator review begins. |
| 6 | Conflict Freedom | 3 | No direct contradiction is present, but there is tension with AMD-2026-015-ADD-005 because this addendum appears to create a second outcome layer using the same labels without a sharper hierarchy rule. |
| 7 | Practical Operability | 2 | An implementer could follow the high-level sequence, but the decision point for `advisory_warning` persistence is under-specified and likely to produce inconsistent downstream handling. |
| 8 | Style & Clarity | 3 | The prose is generally clear, but several terms are used as if already defined elsewhere when they are not normatively defined in this addendum, and the document could be tightened to reduce ambiguity. |
| 9 | Developer Synchrony | 2 | The document is understandable to governance readers, but a developer or tooling author lacks a concrete decision table for pre-validator classification versus validator outcome versus writer-lane admission. |
| 10 | Platform Economics Synchrony | 3 | Nothing in the text appears economically destabilizing, but the document does not materially engage this dimension and therefore only merits a neutral score. |
| 11 | Friction Factor | 3 | The bridge is intentionally narrow and avoids overreach, but the duplicated outcome vocabulary and undefined persistence-approval seam will create review friction during implementation. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- **Sections 1-2** clearly position the addendum as a narrow subordinate bridge and correctly subordinate it to `AMD-2026-015`, `ADD-004`, and `ADD-005`.
- **Section 3** is strong on boundary discipline: it cleanly distinguishes allowed capture surfaces from the `unknown` boundary classification and makes fail-closed handling mandatory.
- **Section 5** correctly preserves validator precedence and prohibits collectors or instrumentation from writing persisted artifacts directly, which aligns well with `AMD-2026-015-ADD-003`, `AMD-2026-015-ADD-005`, and `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`.
- **Sections 7-10** maintain the CANI family’s recurring non-authority pattern and avoid accidental expansion into runtime autonomy.

### Critical Gaps

- **Section 5** uses the phrase “explicit policy result that persistence may proceed” without identifying the governing document, actor, or artifact that issues that result; this is the document’s largest enforceability and operability gap.
- **Section 5** defines “writer lane” only descriptively, not normatively enough to distinguish it from collectors, validators, or downstream routing surfaces.
- **Section 6** reuses `pass` / `fail` / `blocked` / `advisory_warning` for pre-validator normalization outcomes, creating avoidable tension with the authoritative validator outcomes in `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`.
- The required output template conflicts with the governing prompt’s Light rubric, and while this review complies with the required template, the document itself would benefit from more precise citation style and internal anchoring to reduce cross-document ambiguity.

---

## Article-by-Article Review

### 0. Status

**Feedback:**  
This section is concise and consistent with the CANI addendum family. The scope posture is appropriately narrow and tracks the recurring non-authority formula used in `ADD-003`, `ADD-004`, and `ADD-005`. Editorially, “validator/writer handoff” is introduced here before “writer lane” is defined in Section 5, which is acceptable but slightly front-loads an undefined term.

**Scores:** Architectural Fidelity: 4, Style & Clarity: 4, Cross-Document Consistency: 4

**Recommendation:**  
Add a parenthetical forward reference to Section 5 so the undefined term is not left hanging. Proposed text change in **Section 0, Scope posture**:

> Narrow doctrine bridge for capture surfaces, intake-envelope normalization, and validator/writer handoff (see Section 5 for writer-lane meaning). It does not create collector implementations, browser instrumentation implementations, database/event-store services, or execution authority.

---

### 1. Purpose and problem statement

**Feedback:**  
This section is structurally strong and clearly explains the gap being closed. The sentence tying `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` to this addendum is especially useful for hierarchy. However, “implementation-facing elaboration” is helpful prose but not quite as precise as the rest of the family’s “technical support document” phrasing.

**Scores:** Cross-Document Consistency: 4, Completeness: 4, Style & Clarity: 4

**Recommendation:**  
Align the support-document phrasing to the family pattern used in `ADD-003` through `ADD-005`. Proposed replacement for the fifth paragraph:

> `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` defines the corresponding technical support contract for this bridge. It elaborates the governed capture-surface classes, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations. It does not create independent execution authority.

---

### 2. Relationship to AMD-2026-015

**Feedback:**  
This section is mostly coherent and successfully places the addendum beneath `ADD-004` and `ADD-005`. The final sentence is useful, but the citation style is inconsistent with the broader style guide because it cites document IDs and section ranges informally rather than by full title plus specific section names. Since the referenced support contract uses numbered sections, the citation is understandable, but the document set would read more cleanly if the addendum used a more uniform reference pattern.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 4, Style & Clarity: 3

**Recommendation:**  
Tighten the final sentence and reduce mixed citation styles. Proposed replacement for the last paragraph:

> Detailed capture-surface classification, minimum pre-envelope requirements, fail-closed handling, and handoff expectations are specified in *AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001* (Sections 2 through 8). This addendum supplies the governing bridge and does not expand authority beyond that contract’s bounded implementation framing.

---

### 3. Governed capture-surface bridge rule

**Feedback:**  
This is one of the strongest sections in the document. The allowed classes match the support contract, and the treatment of `unknown` as a boundary classification only is clear and enforceable. The final sentence is slightly redundant because the section already says the same thing in multiple ways.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
Remove the redundant closing sentence or convert it into a sharper exclusivity rule. Proposed replacement for the final sentence:

> No capture surface outside the classes listed in this section is eligible for intake-envelope construction under this addendum.

---

### 4. Raw-capture and normalization rule

**Feedback:**  
This section is generally clear and aligns well with `ADD-004` and the support contract. It properly preserves the distinction between raw capture, normalized intake, and persisted artifacts. The strongest part is the explicit prohibition on inventing routing, authority, approval, or hidden external support. The main editorial issue is that the list of required pre-normalization elements is strong but does not explicitly say whether all items are mandatory for every signal or whether some may be absent if the intake-envelope contract marks them optional. As written, it implies all are mandatory, which may be stricter than `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`, where some linkage fields are optional.

**Scores:** Cross-Document Consistency: 3, Completeness: 3, Practical Operability: 3

**Recommendation:**  
Clarify that the mandatory pre-normalization set is the minimum needed to construct a compliant envelope without inventing required fields, not a blanket override of optional intake-envelope fields. Proposed insertion after the bullet list:

> These elements are the minimum pre-envelope inputs required to construct a compliant intake envelope without inventing required fields. This section does not convert optional intake-envelope fields under `ADD-004` into mandatory fields unless they are necessary to avoid fabrication or to preserve reviewable provenance.

---

### 5. Validator and writer handoff rule

**Feedback:**  
This section contains the document’s most important substantive gap. The first three steps are clear. Step 4 is not. The phrase “returns `advisory_warning` together with an explicit policy result that persistence may proceed” is not anchored to a named authority surface, named actor, or named document. `AMD-2026-015-ADD-005` defines validator outcomes and says `advisory_warning` is informative only; this addendum then introduces a second approval seam without specifying whether that seam belongs to validator tooling, a human operator, a policy engine, a coordinator, or the persisted-artifact contract. That is a legal, editorial, and operational ambiguity.

The definition of “writer lane” is directionally helpful but still too loose. “Downstream governed materialization step” describes function, not authority. The section also needs a cleaner statement that the writer lane is a mechanical persistence surface, not a decision-making surface.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Developer Synchrony: 2, Architectural Fidelity: 4

**Recommendation:**  
Revise Section 5 to identify the authority seam explicitly and to define the writer lane as a non-discretionary persistence surface. Proposed replacement for the first three paragraphs:

> The handoff sequence **SHALL** be:
>
> 1. eligible capture candidate identified  
> 2. normalized intake envelope constructed  
> 3. envelope handed to validator/tooling  
> 4. envelope may proceed to the writer lane only when validator/tooling returns `pass`, or when validator/tooling returns `advisory_warning` and a separately governed persistence-admission decision explicitly authorizes materialization under the policy surface that owns that writer flow
>
> For purposes of this addendum, the writer lane is the non-authoritative downstream materialization surface that writes persisted CANI artifacts under the storage contract defined by `AMD-2026-015-ADD-003`.
>
> The writer lane does not decide eligibility, authority, routing acceptance, planning acceptance, or review acceptance. It materializes only what upstream governed policy and validator handling permit.

Also replace the sentence:

> Any persistence decision associated with `advisory_warning` **SHALL** be governed by the validator/tooling policy surface and the persisted-artifact contract under `AMD-2026-015-ADD-003`.

with:

> Any persistence decision associated with `advisory_warning` **SHALL** be recorded by the separately governed policy or operator-review surface that owns persistence admission for that writer flow. Neither collector tooling nor the writer lane may infer that permission from `advisory_warning` alone.

If such a policy surface does not yet exist elsewhere in the document set, then the safer alternative is to remove the `advisory_warning` persistence exception entirely in this addendum.

---

### 6. Fail-closed outcome rule before validator handoff

**Feedback:**  
This section is conceptually sound but creates unnecessary friction by reusing the exact validator outcome vocabulary for provisional pre-validator classifications. The section does say these do not replace authoritative validator outcomes, but the duplication still invites confusion in logs, tooling, and review packets. This is especially problematic because `AMD-2026-015-ADD-005` already makes `pass`, `fail`, and `blocked` authoritative validator outcomes. A developer reading both documents could reasonably ask whether a pre-validator `pass` should be persisted, displayed, or overwritten.

**Scores:** Conflict Freedom: 2, Practical Operability: 2, Developer Synchrony: 2, Style & Clarity: 3

**Recommendation:**  
Rename the pre-validator classifications so they cannot be mistaken for validator outcomes. Proposed replacement for the opening paragraphs of Section 6:

> Before validator handoff, capture normalization must already distinguish provisional normalization classifications.
>
> Allowed provisional classifications are:
>
> - `normalization_pass`
> - `normalization_fail`
> - `normalization_blocked`
> - `normalization_advisory_warning`
>
> These classifications are pre-validator normalization results only. They exist to control fail-closed handling before formal validator review and do not replace, mirror, or override the authoritative validator outcomes defined by `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`.

Then update the bullets in the remainder of the section to use the renamed values. This would materially improve conflict freedom and developer synchrony.

---

### 7. Non-authority boundary

**Feedback:**  
This section is strong and consistent with the rest of the CANI family. It clearly excludes implementation, persistence backends outside the governed repo tree, autonomous routing, and approval-lane collapse. No major editorial issues appear here.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5, Style & Clarity: 4

**Recommendation:**  
No substantive change required. Optional editorial tightening: change “database schema or migrations” to “database schemas or migrations” for parallelism with neighboring bullets.

---

### 8. Implementation follow-through and affected surfaces

**Feedback:**  
This section is coherent and correctly identifies the support contract and downstream recipient surfaces. The phrase “the governed documentation surfaces that record amendment discovery and review state for this package” is somewhat vague compared with the otherwise concrete references in the section.

**Scores:** Completeness: 3, Style & Clarity: 3, Cross-Document Consistency: 3

**Recommendation:**  
Replace the vague final bullet with named surfaces or remove it. Proposed replacement:

> - registry, tracker, and review-package surfaces that record discoverability and review state for this amendment package

This would align better with the phrasing used in `ADD-003`, `ADD-004`, and `ADD-005`.

---

### 9. Out of scope

**Feedback:**  
This section is clear and consistent with the family pattern. It appropriately avoids accidental expansion into runtime collectors, instrumentation hooks, storage backends, or autonomous routing. No substantive issue appears.

**Scores:** Completeness: 4, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:**  
No substantive revision required.

---

### 10. Addendum intent summary

**Feedback:**  
The summary is concise and faithful to the body. “Valid intake envelopes” is slightly imprecise because the document distinguishes pre-validator normalization from validator outcomes; an envelope may be normalized before it is validator-approved. That wording could be sharpened.

**Scores:** Style & Clarity: 3, Cross-Document Consistency: 3

**Recommendation:**  
Revise the second sentence for precision. Proposed replacement:

> The CANI family may now define which capture surfaces are governed, how raw capture becomes normalized intake, and how validator-cleared intake envelopes hand off into validator-governed writer lanes.

If the intent is to describe the whole bridge rather than only post-validation state, an alternative is:

> The CANI family may now define which capture surfaces are governed, how raw capture becomes normalized intake, and how normalized intake envelopes progress through validator and writer-lane handoff under existing governance boundaries.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 5 | `advisory_warning` persistence path is not tied to a named authority surface, actor, or record. | Define the persistence-admission authority explicitly, or remove the `advisory_warning` exception and require `pass` before writer-lane admission. | Critical | 3, 5, 6, 7, 9 |
| 2 | Section 6 | Pre-validator classifications reuse the exact validator outcome vocabulary, creating cross-document tension with `ADD-005`. | Rename provisional outcomes to `normalization_pass`, `normalization_fail`, `normalization_blocked`, and `normalization_advisory_warning`. | Critical | 1, 6, 7, 8, 9, 11 |
| 3 | Section 5 | “Writer lane” is described functionally but not normatively enough. | Define the writer lane as a non-authoritative materialization surface that cannot decide eligibility, routing, or acceptance. | High | 3, 7, 8, 9 |
| 4 | Section 4 | Minimum pre-envelope inputs may be read as overriding optionality in `ADD-004`. | Clarify that the listed inputs are the minimum needed to construct a compliant envelope without inventing required fields, not a blanket override of optional fields. | High | 1, 5, 7, 8 |
| 5 | Section 8 | One affected-surface bullet is vague compared with the rest of the family. | Replace “governed documentation surfaces” with named registry, tracker, and review-package surfaces. | Medium | 1, 8 |
| 6 | Sections 0 and 10 | Forward and summary references use slightly imprecise terminology around writer handoff and valid envelopes. | Add a forward reference in Section 0 and tighten Section 10 to distinguish normalized intake from validator-cleared progression. | Medium | 1, 8 |
| 7 | Section 2 | Citation style is somewhat mixed and less precise than the style guide prefers. | Standardize references to full document titles and section ranges where cited. | Low | 1, 8 |
| 8 | Section 3 | Final sentence is redundant. | Replace it with a sharper exclusivity rule or delete it. | Low | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is architecturally sound and largely coherent with the CANI family, but it contains two material governance gaps: an undefined authority seam for persistence after `advisory_warning`, and a confusing duplication of validator outcome labels for pre-validator normalization. Those issues materially reduce enforceability, operability, and conflict freedom.

**Top 3 Actions Required:**
1. Define who or what may authorize persistence after validator `advisory_warning`, or remove that exception.
2. Rename the pre-validator normalization outcomes so they cannot be confused with authoritative validator outcomes under `AMD-2026-015-ADD-005`.
3. Tighten the definition of the writer lane as a non-authoritative materialization surface and clarify its relationship to upstream policy and downstream governance.
---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.5
reviewer: OpenAI
review_date: 2026-04-09
review_round: 1
review_type: editorial
disposition: approved_with_changes
composite_score: 4.0
---

# Peer Review: AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The addendum is largely aligned with AMD-2026-015 and ADD-003 through ADD-005, but several cross-references rely on support-document section numbers rather than citing amendment-local sections, and terminology around “writer lane” is introduced here more strongly than in prior addenda. |
| 2 | Business Model Alignment | 4 | Nothing in the document appears to disturb platform governance or commercial boundaries, but the document is operational rather than business-facing and does not explicitly restate any economic or liability boundary. |
| 3 | Legal Enforceability | 4 | The operative prohibitions are clear and mostly enforceable, but a few phrases such as “suitable for later `payload_ref`” and “non-authoritative downstream materialization surface” would benefit from tighter drafting. |
| 4 | Architectural Fidelity | 5 | The document strongly preserves the CANI doctrine’s separation between capture, normalization, validation, persistence, and downstream governance, and it consistently rejects autonomous execution authority. |
| 5 | Completeness | 4 | The document covers the intended bridge well, but it leaves one practical edge unclear: what minimum retention or disposition rule applies to failed or blocked raw-capture evidence before normalization. |
| 6 | Conflict Freedom | 4 | No direct contradiction appears, but the addendum’s use of amendment-layer names versus implementation-facing controlled values creates mild interpretive tension with the support contract unless explicitly crosswalked more formally. |
| 7 | Practical Operability | 4 | The handoff sequence and fail-closed rules are actionable, but the document still depends on readers consulting the support contract for exact controlled values and operational handling details. |
| 8 | Style & Clarity | 4 | The prose is disciplined and mostly precise, but several sentences are long, layered, and harder to parse than necessary for a binding bridge document. |
| 9 | Developer Synchrony | 4 | The document gives developers a coherent control-plane boundary, but implementation teams would benefit from a short explicit statement that no code path may persist raw capture except as repo-local reviewable evidence under the ADD-004 boundary. |
| 10 | Platform Economics Synchrony | 4 | The document does not create any obvious economic inconsistency, but it also does not connect its storage and review burdens to any broader platform-operating constraint. |
| 11 | Friction Factor | 3 | The document is usable, but repeated doctrinal restatements and dense cross-reference prose increase reading friction for coordinators and implementers. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

- **Section 2** is strong on hierarchy and precedence. It clearly places this addendum beneath `AMD-2026-015-ADD-004` and `AMD-2026-015-ADD-005` while also stating that the amendment controls over the support contract if tension arises.
- **Section 5** is the document’s strongest operative section. It cleanly separates collector, validator, and writer responsibilities and preserves the non-authority boundary established in `AMD-2026-015` Section 3.5 and `AMD-2026-015-ADD-005`.
- **Section 6** is well aligned with `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` and avoids the validator-outcome collision that earlier drafts in this family risked.
- **Sections 7–10** maintain consistent CANI-family doctrine: governance-preserving seams, no autonomous routing, no runtime mutation, no bypass of human review.

### Critical Gaps

- **Section 4** does not fully specify the governance status of failed or blocked raw-capture evidence beyond saying it may remain as “non-normalized repo-local reviewable evidence.” That is directionally correct but still leaves retention, discoverability, and non-authority handling somewhat implicit.
- **Section 3** introduces amendment-layer capture-class names while deferring implementation-facing controlled values to the support contract, but it does not provide a compact explicit mapping table. That creates avoidable interpretive friction.
- **Section 5** defines “writer lane” in this addendum, but the term is not yet as canonically stabilized across the family as “validator” or “intake envelope,” which creates a small cross-document coherence issue.
- **Section 2** cites support-contract sections precisely, but the document does not similarly use internal section cross-references for its own operative rules, making navigation less consistent than it could be.

---

## Article-by-Article Review

### Section 0. Status

**Feedback:**  
This section is concise and consistent with the CANI addendum family. The scope posture properly states that the document is a narrow doctrine bridge and does not authorize implementation or execution authority. The phrase “validator-to-writer handoff into persisted CANI artifact materialization” is accurate but dense.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 4, Architectural Fidelity: 5

**Recommendation:**  
Consider simplifying the scope-posture sentence for readability without changing substance. Proposed replacement:

> Narrow doctrine bridge for governed capture surfaces, intake-envelope normalization, and validator-cleared handoff into persisted CANI artifact materialization under `AMD-2026-015-ADD-003`. It does not authorize collector implementation, browser instrumentation implementation, database or event-store services, or execution authority.

---

### Section 1. Purpose and problem statement

**Feedback:**  
This section clearly explains the doctrinal gap and fits the family pattern used in ADD-002 through ADD-005. The support-contract reference is useful and appropriately bounded. Editorially, the section repeats “established” several times in short succession, and the final sentence could be tighter.

**Scores:** Completeness: 4, Style & Clarity: 4, Conflict Freedom: 4

**Recommendation:**  
Tighten repetition and clarify the support-contract relationship. Proposed replacement for the final two paragraphs:

> This addendum establishes the amendment-layer bridge rule for governed capture surfaces, pre-validator normalization, and validator-to-writer handoff.  
> `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.2` provides the corresponding technical support contract. It elaborates capture-surface classes, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations, but it does not create independent execution authority.

---

### Section 2. Relationship to AMD-2026-015

**Feedback:**  
This is a strong section. It correctly states subordination to the parent amendment and to ADD-004 and ADD-005. The explicit precedence clause is especially valuable. The main editorial issue is density: the paragraph listing support-contract sections is long and harder to scan than necessary.

**Scores:** Cross-Document Consistency: 5, Legal Enforceability: 4, Style & Clarity: 4

**Recommendation:**  
Convert the support-contract crosswalk into bullets or a table. Proposed replacement for the long paragraph:

> `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.2` provides technical detail for this bridge as follows:  
> - Section 2: capture-surface classification  
> - Sections 3–6: raw capture and pre-envelope requirements  
> - Section 7: fail-closed pre-validator handling  
> - Section 8: validator and writer handoff expectations  
> This addendum governs those bridges at the amendment layer and does not enlarge the authority granted by `AMD-2026-015`, `AMD-2026-015-ADD-004`, or `AMD-2026-015-ADD-005`.

---

### Section 3. Governed capture-surface bridge rule

**Feedback:**  
The rule is substantively sound and consistent with the support contract. The treatment of `unknown` is clear and mandatory, which is an improvement over softer formulations. The main issue is editorial coherence: the amendment-layer names are listed, but there is no explicit one-to-one mapping to the support contract’s controlled `source_surface` values. That omission does not create a contradiction, but it does create interpretive drag.

**Scores:** Cross-Document Consistency: 4, Practical Operability: 4, Friction Factor: 3

**Recommendation:**  
Add a compact mapping table or sentence. Proposed insertion after the numbered list:

> For avoidance of doubt, these amendment-layer classes map to the implementation-facing `source_surface` values in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` as follows: shell/operator flow → `shell`; UI surface observation → `ui_surface`; planning artifacts → `planning_artifact`; review artifacts → `review_artifact`; operator note → `operator_note`.

This would materially improve cross-document coherence.

---

### Section 4. Raw-capture and normalization rule

**Feedback:**  
This section is operationally useful and preserves the ADD-004 boundary well. The minimum pre-envelope inputs are clear. The remaining gap is that the document says failed candidates may remain as “non-normalized repo-local reviewable evidence,” but it does not specify whether such evidence is merely permissible, whether it must remain outside governed persisted classes, or whether any routing/discoverability rule applies. The current text implies the right answer but does not state it crisply enough for a binding bridge.

**Scores:** Completeness: 3, Legal Enforceability: 4, Developer Synchrony: 4

**Recommendation:**  
Add one sentence clarifying non-authority and non-persistence status for failed or blocked evidence. Proposed insertion at the end of the section:

> Such non-normalized evidence remains intake-adjacent review material only, is not a governed persisted CANI artifact, and must not be assigned routing, authority, or lifecycle state reserved for intake envelopes or persisted artifacts under `AMD-2026-015-ADD-003` and `AMD-2026-015-ADD-004`.

If desired, a second sentence could also clarify that any retention or indexing rule must come from a later storage or tooling instrument rather than this addendum.

---

### Section 5. Validator and writer handoff rule

**Feedback:**  
This is the best section in the document. It clearly defines the writer lane as subordinate, limits it to already-authorized artifact classes and fields, and blocks `advisory_warning` from becoming a persistence shortcut. This section is highly consistent with `AMD-2026-015-ADD-003`, `AMD-2026-015-ADD-004`, and `AMD-2026-015-ADD-005`. The only editorial concern is that “writer lane” is defined here but not yet normalized as a family-wide canonical term.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5, Practical Operability: 5

**Recommendation:**  
Retain the substance. For cross-family coherence, consider adding a parenthetical on first use:

> For purposes of this addendum, the **writer lane** (the non-authoritative downstream materialization surface)...

That small formatting change would help mark the term as locally defined rather than globally canonical.

---

### Section 6. Fail-closed outcome rule before validator handoff

**Feedback:**  
This section is strong and resolves a common ambiguity in governance stacks: it distinguishes provisional normalization statuses from validator outcomes. The rule that hard boundary violations must not be silently downgraded is especially good. The section is slightly repetitive, but the repetition is mostly justified because it prevents category confusion.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 4, Style & Clarity: 4

**Recommendation:**  
Minor editorial tightening only. Proposed replacement for the second paragraph:

> These statuses govern pre-validator normalization handling only. They do not replace, mirror, or override the authoritative validator outcomes defined by `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001` version `0.1.0`.

---

### Section 7. Non-authority boundary

**Feedback:**  
This section is consistent with the rest of the CANI family and properly preserves separation of powers. It is clear, enforceable, and stylistically aligned with the family’s non-authority sections.

**Scores:** Conflict Freedom: 5, Architectural Fidelity: 5, Style & Clarity: 5

**Recommendation:**  
No substantive change required.

---

### Section 8. Implementation follow-through and affected surfaces

**Feedback:**  
This section is complete enough for a narrow bridge addendum and correctly identifies affected surfaces. The phrase “registry, tracker, and review-package surfaces that record discoverability and review state” is slightly abstract and could be simplified. Otherwise, the section is coherent.

**Scores:** Completeness: 4, Developer Synchrony: 4, Style & Clarity: 4

**Recommendation:**  
Simplify the final bullet for readability. Proposed replacement:

> - registry, tracker, and review-package surfaces that record discoverability and review state for this amendment package

This is already close; only minor tightening is needed.

---

### Section 9. Out of scope

**Feedback:**  
This section is consistent with the family pattern and appropriately excludes implementation and autonomy concerns. No conflict or ambiguity is apparent.

**Scores:** Conflict Freedom: 5, Style & Clarity: 5, Architectural Fidelity: 5

**Recommendation:**  
No substantive change required.

---

### Section 10. Addendum intent summary

**Feedback:**  
The summary accurately reflects the document’s purpose and preserves the non-authority boundary. It is concise and aligned with the family’s closing pattern.

**Scores:** Style & Clarity: 5, Cross-Document Consistency: 5, Friction Factor: 4

**Recommendation:**  
No substantive change required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Amendment-layer capture-class names are not explicitly crosswalked to implementation-facing controlled values. | Add a one-to-one mapping sentence or table linking the five amendment-layer classes to `source_surface` values in the support contract. | High | 1, 6, 7, 9, 11 |
| 2 | Section 4 | Failed or blocked raw-capture evidence is not fully bounded after non-normalization. | Add text stating that such evidence remains intake-adjacent review material only and must not receive routing, authority, or persisted-artifact lifecycle state. | Critical | 3, 5, 6, 7, 9 |
| 3 | Section 2 | Support-contract crosswalk is accurate but dense and harder to navigate than necessary. | Convert the long support-contract section-reference sentence into a bullet list. | Medium | 1, 8, 11 |
| 4 | Section 5 | “Writer lane” is defined locally but may read as a globally canonical term. | Mark “writer lane” as a locally defined term on first use, e.g., by bolding it and adding a parenthetical definition. | Medium | 1, 8, 11 |
| 5 | Sections 0–1 | Several sentences are longer and denser than needed for a binding bridge document. | Tighten repeated phrasing and simplify scope and purpose sentences without changing doctrine. | Low | 8, 11 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is substantively strong, architecturally faithful, and largely coherent with the CANI family. The remaining issues are not structural failures, but they should be corrected to reduce interpretive friction and tighten the governance boundary around failed raw-capture evidence.

**Top 3 Actions Required:**
1. Clarify in Section 4 that failed or blocked raw-capture evidence remains non-authoritative review material only and cannot acquire intake-envelope or persisted-artifact status.
2. Add an explicit Section 3 crosswalk between amendment-layer capture classes and the support contract’s implementation-facing `source_surface` values.
3. Simplify Section 2’s support-contract cross-reference paragraph to improve readability and reduce navigation friction.
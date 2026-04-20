---
review_id: REV-AMD-2026-015-ADD-006-001
document_reviewed: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
document_version: 0.1.6
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
| 1 | Cross-Document Consistency | 4 | The addendum is strongly aligned with the AMD-2026-015 CANI family, but it uses a few local formulations such as “writer lane” and amendment-layer/support-contract crosswalk language that would benefit from tighter harmonization. |
| 2 | Business Model Alignment | 4 | Nothing in the document appears to disturb platform economics or commercial boundaries, but this dimension is only indirectly addressed because the document is narrowly governance-technical rather than economic. |
| 3 | Legal Enforceability | 4 | The operative rules are mostly clear and enforceable, though several phrases such as “bounded reviewable evidence” and “intake-adjacent review material only” would be stronger if defined more concretely. |
| 4 | Architectural Fidelity | 5 | The document preserves the core AIOS governance architecture by maintaining non-authority boundaries, validator precedence, and separation between capture, normalization, validation, and persisted materialization. |
| 5 | Completeness | 4 | The document covers the promised bridge scope well, but it omits one concise section clarifying document-path examples or canonical repo locations for support artifacts and amendment package discoverability. |
| 6 | Conflict Freedom | 4 | No direct contradiction appears, but there is mild tension between this addendum’s local terminology and the support contract’s terminology that should be normalized to avoid future interpretive drift. |
| 7 | Practical Operability | 4 | The handoff sequence and fail-closed logic are operationally usable, but implementation teams would benefit from one more explicit statement about what artifact, if any, records provisional normalization status before validator handoff. |
| 8 | Style & Clarity | 4 | The prose is disciplined and mostly precise, but several sections repeat the same boundary concepts and could be tightened for readability without changing meaning. |
| 9 | Developer Synchrony | 4 | The document gives developers a coherent doctrinal map to the support contracts, but it stops short of specifying where provisional normalization evidence should live or how it should be referenced in repo practice. |
| 10 | Platform Economics Synchrony | 4 | The document does not create economic inconsistency, but it also does not materially engage this dimension beyond preserving existing governance boundaries. |
| 11 | Friction Factor | 3 | The document is understandable, but repeated caveats and layered cross-references create moderate reading friction for operators trying to distinguish amendment rules from support-contract detail. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

- **Sections 2, 5, and 7** are especially strong in preserving authority boundaries across the CANI family. The document clearly states that capture, normalization, validation, and writing are distinct governance seams rather than collapsed execution authority.
- **Section 3** aligns well with `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` by mapping amendment-layer capture classes to implementation-facing `source_surface` values.
- **Section 5** is the strongest operative section. It clearly prohibits direct persisted-artifact writes by collectors or instrumentation and correctly subordinates the locally defined writer lane to `AMD-2026-015-ADD-003`, `AMD-2026-015-ADD-004`, and `AMD-2026-015-ADD-005`.
- **Section 6** successfully resolves a common ambiguity in governance documents by distinguishing provisional normalization statuses from authoritative validator outcomes.

### Critical Gaps

- **Section 5** introduces the local term `writer lane`, but the document does not fully anchor where this term should or should not appear elsewhere in the CANI family; that creates a small but real terminology-drift risk.
- **Sections 4 and 6** describe pre-validator classification and fail-closed handling, but they do not specify the governed artifact or evidence surface in which those provisional statuses are recorded, leaving an operability gap.
- **Section 2** contains a useful precedence rule, but the crosswalk bullets to the support contract are more detailed than necessary for an amendment and add reading friction without adding much normative force.
- **Sections 4, 6, and 8** use several near-synonymous phrases—“bounded reviewable evidence,” “repo-local reviewable evidence,” “intake-adjacent review material only”—that should be normalized or defined to reduce ambiguity.

---

## Article-by-Article Review

### 0. Status

**Feedback:**  
This section is concise and coherent. It correctly frames the addendum as a narrow doctrine bridge and preserves consistency with the rest of the CANI package by disclaiming collector implementation, browser instrumentation, database work, and execution authority. The phrase “validator-cleared handoff into persisted CANI artifact materialization” is accurate, though slightly dense.

**Scores:** Cross-Document Consistency: 4, Architectural Fidelity: 5, Style & Clarity: 4

**Recommendation:**  
Retain the section substantially as written. For readability, consider replacing “validator-cleared handoff into persisted CANI artifact materialization” with “validator-cleared handoff into persisted CANI artifact writing under `AMD-2026-015-ADD-003`.”

---

### 1. Purpose and problem statement

**Feedback:**  
This section clearly states the gap being closed and properly situates the addendum after `ADD-004` and `ADD-005`. The final two paragraphs are useful, but the support-contract description is slightly repetitive with Section 2. The phrase “amendment-layer bridge rule” is understandable, though not used elsewhere in the family and therefore mildly idiosyncratic.

**Scores:** Cross-Document Consistency: 4, Completeness: 4, Style & Clarity: 4

**Recommendation:**  
Tighten the last two paragraphs by reducing duplication with Section 2. Proposed replacement:

> This addendum establishes the doctrine-layer bridge for governed capture-surface eligibility, normalization into intake envelopes, and validator-gated handoff into persisted-artifact materialization.  
> `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.3` provides the corresponding technical support contract and does not create independent execution authority.

---

### 2. Relationship to AMD-2026-015

**Feedback:**  
This is a strong relationship section. It correctly preserves parent-amendment supremacy and subordination to `ADD-004` and `ADD-005`. The explicit tension rule is valuable and improves cross-document coherence. The only editorial issue is that the support-contract crosswalk bullets are somewhat implementation-memo-like for an amendment and create extra reading load.

**Scores:** Cross-Document Consistency: 5, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
Condense the support-contract crosswalk while preserving the precedence rule. Proposed replacement for the bullet list:

> `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.3` provides technical detail for capture-surface classification, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations.

This keeps the amendment focused on doctrine while still pointing readers to the support contract.

---

### 3. Governed capture-surface bridge rule

**Feedback:**  
This section is one of the document’s strongest. The allowed classes are clear, the mapping to implementation-facing `source_surface` values is useful, and the treatment of `unknown` is mandatory rather than permissive. That said, the sentence beginning “For avoidance of doubt...” is long and could be reformatted as a table for easier scanning. Also, “implementation-facing controlled values” is accurate but slightly abstract.

**Scores:** Cross-Document Consistency: 4, Practical Operability: 4, Style & Clarity: 4

**Recommendation:**  
Convert the mapping sentence into a table. Proposed text:

| Amendment-layer class | `source_surface` value |
|---|---|
| shell/operator flow | `shell` |
| UI surface observation | `ui_surface` |
| planning artifacts | `planning_artifact` |
| review artifacts | `review_artifact` |
| operator note | `operator_note` |

Then replace the current mapping sentence with:

> The amendment-layer classes in this section map to the implementation-facing `source_surface` values shown below. No additional eligible classes may be introduced without amendment.

---

### 4. Raw-capture and normalization rule

**Feedback:**  
This section is substantively sound and aligned with `AMD-2026-015-ADD-004` and the capture-surface support contract. It correctly distinguishes raw capture from governed intake and prevents hidden authority from entering through pre-envelope material. The main weakness is editorial: the section uses several similar phrases for non-normalized evidence without fully standardizing them. It also leaves open a practical question: where is the provisional classification recorded before validator handoff?

**Scores:** Legal Enforceability: 4, Practical Operability: 3, Style & Clarity: 4

**Recommendation:**  
Add one sentence clarifying the evidence surface for failed or blocked pre-validator material. Proposed insertion after the paragraph ending “without inventing required fields”:

> Any provisional normalization classification produced under this section should be recorded only in a reviewable intake-adjacent evidence surface or helper artifact designated by the support contract or implementation memo; it must not be recorded as persisted CANI workflow truth under `AMD-2026-015-ADD-003`.

Also standardize terminology by using one phrase consistently, preferably “repo-local reviewable intake-adjacent evidence.”

---

### 5. Validator and writer handoff rule

**Feedback:**  
This is the document’s clearest and most operational section. It defines `writer lane` carefully, subordinates it to the storage and intake contracts, and prohibits direct persisted writes by collectors or instrumentation. The treatment of `advisory_warning` is especially helpful because it closes a common loophole. The only remaining issue is terminology governance: because `writer lane` is a local term, the document should say more explicitly that it is not a new canonical family-wide role unless later adopted elsewhere.

**Scores:** Architectural Fidelity: 5, Practical Operability: 5, Cross-Document Consistency: 4

**Recommendation:**  
Add one sentence after the first paragraph:

> `Writer lane` is a local convenience term in this addendum only and does not, by itself, amend the canonical role vocabulary of other CANI documents unless those documents are separately revised.

This will reduce future glossary drift.

---

### 6. Fail-closed outcome rule before validator handoff

**Feedback:**  
This section is strong and materially improves coherence with `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`. The distinction between provisional normalization statuses and validator outcomes is clear. The only editorial concern is that the section repeats concepts already introduced in Sections 3 and 4, which increases friction.

**Scores:** Conflict Freedom: 5, Practical Operability: 4, Friction Factor: 3

**Recommendation:**  
Keep the substance, but tighten repetition. For example, replace:

> These statuses are pre-validator normalization results only. They exist to control fail-closed handling before formal validator review and do not replace, mirror, or override the authoritative validator outcomes...

with:

> These statuses govern pre-validator fail-closed handling only and must not be used as final validator outcomes, which remain governed exclusively by `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001` version `0.1.0`.

---

### 7. Non-authority boundary

**Feedback:**  
This section is fully consistent with the parent amendment and the rest of the CANI family. It is crisp, enforceable, and appropriately narrow. No substantive issue appears here.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5, Style & Clarity: 5

**Recommendation:**  
No substantive change required.

---

### 8. Implementation follow-through and affected surfaces

**Feedback:**  
This section is generally good and correctly identifies the affected surfaces. The phrase “registry, tracker, and review-package surfaces that record discoverability and review state for this amendment package” is understandable but somewhat broad. Since `ADD-001` is the discoverability bridge, this section could more explicitly say that discoverability obligations remain governed there rather than implied here.

**Scores:** Cross-Document Consistency: 4, Completeness: 4, Developer Synchrony: 4

**Recommendation:**  
Add a narrowing sentence:

> Any registry or discoverability alignment required for these materials remains governed by `AMD-2026-015-ADD-001`; this section identifies affected surfaces only and does not create a separate discoverability rule.

This will reduce overlap risk with `ADD-001`.

---

### 9. Out of scope

**Feedback:**  
This section is clear and consistent with the package. It properly excludes collectors, hooks, services, persistence backends, autonomous routing, and redesign of the CANI family. No conflict appears.

**Scores:** Conflict Freedom: 5, Style & Clarity: 5, Completeness: 4

**Recommendation:**  
No substantive change required.

---

### 10. Addendum intent summary

**Feedback:**  
The summary accurately restates the document’s purpose and preserves the non-authority boundary. The phrase “writer-lane handoff” is now understandable because Section 5 defines it, but the summary still reads slightly jargon-heavy for a closing section.

**Scores:** Style & Clarity: 4, Cross-Document Consistency: 4, Friction Factor: 3

**Recommendation:**  
Consider a simpler closing sentence:

> These bridges remain governance-preserving process seams, not execution authority or autonomy.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §4 Raw-capture and normalization rule | The document does not specify where provisional normalization classifications are recorded before validator handoff. | Add a sentence stating that provisional normalization classifications may be recorded only in a reviewable intake-adjacent evidence surface or helper artifact and not as persisted CANI workflow truth. | High | 3, 5, 7, 9 |
| 2 | §5 Validator and writer handoff rule | The local term `writer lane` could drift into an unintended canonical role term. | Add a sentence stating that `writer lane` is a local convenience term in this addendum only unless separately adopted elsewhere. | High | 1, 6, 8 |
| 3 | §2 Relationship to AMD-2026-015 | The support-contract crosswalk is more detailed than necessary for amendment-layer doctrine and adds reading friction. | Condense the crosswalk bullets into one sentence summarizing the support contract’s technical detail areas. | Medium | 1, 8, 11 |
| 4 | §3 Governed capture-surface bridge rule | The source-surface mapping is embedded in a long sentence and is harder to scan than necessary. | Convert the mapping into a two-column table and state that no additional eligible classes may be introduced without amendment. | Medium | 7, 8, 9, 11 |
| 5 | §§4, 8 | Terminology for non-normalized evidence is slightly inconsistent across sections. | Standardize on one phrase, preferably “repo-local reviewable intake-adjacent evidence,” and use it consistently. | Medium | 1, 3, 8 |
| 6 | §8 Implementation follow-through and affected surfaces | The section could be read as implying a discoverability rule that properly belongs to `ADD-001`. | Add a sentence clarifying that registry/discoverability obligations remain governed by `AMD-2026-015-ADD-001`. | Medium | 1, 6, 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is structurally strong, architecturally faithful, and materially consistent with the rest of the CANI package. The remaining issues are editorial-operational rather than foundational, but they should be resolved before ratification to reduce terminology drift and improve implementation clarity.

**Top 3 Actions Required:**
1. Clarify where provisional normalization classifications are recorded before validator handoff.
2. Explicitly limit `writer lane` to a local term unless separately adopted in other CANI documents.
3. Simplify the amendment/support-contract crosswalk and normalize evidence terminology across Sections 4 and 8.
---
review_id: REV-AMD-2026-016-001
document_reviewed: amendments/AMD-2026-016.md
document_version: 0.1.0
reviewer: OpenAI
review_date: 2026-04-10
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: AMD-2026-016 — Governed Non-Human Principals and Deterministic Routed Authority

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The amendment is conceptually aligned with AMD-2026-007, AMD-2026-012, AIOS-SPEC-002, and AIOS-SPEC-009, but it uses several new terms without anchoring them to existing section-level authorities or glossary conventions. |
| 2 | Business Model Alignment | 3 | The document does not conflict with the marketplace model, but it does not explain how non-human principals relate to Tenant, Vendor, Kit, or application ecosystem governance. |
| 3 | Legal Enforceability | 2 | Core rules are directionally strong, but several binding provisions rely on undefined terms such as “permission family,” “approved routed surfaces,” and “privileged shell state,” which weakens enforceability. |
| 4 | Architectural Fidelity | 4 | The amendment correctly reinforces policy-evaluated, routed, auditable authority and is broadly consistent with shell/control-plane separation. |
| 5 | Completeness | 2 | The amendment defines doctrine but omits the minimum conformance structures needed to apply it, including required schema shape, scope-class taxonomy, failure outcomes, and cross-document implementation deltas. |
| 6 | Conflict Freedom | 3 | No direct contradiction is present, but the amendment risks overlap with AIOS-SPEC-009 §2.1 and AMD-2026-007 §11.9 because it does not sharply distinguish shell-state routing from domain execution authority. |
| 7 | Practical Operability | 2 | A developer or reviewer cannot reliably test conformance because the document lacks deterministic field definitions, approval paths, and validation rules. |
| 8 | Style & Clarity | 4 | The prose is readable and disciplined, but several sections use broad declarative bullets where tighter normative drafting and section-internal structure are needed. |
| 9 | Developer Synchrony | 2 | The document gives doctrine but not enough implementation guidance to map principal classes into PolicyRecord, SessionContext, audit records, or control-plane interfaces. |
| 10 | Platform Economics Synchrony | 4 | The amendment does not disturb existing economic mechanics and does not introduce obvious pricing or liability distortions. |
| 11 | Friction Factor | 4 | The doctrine is narrow and proportionate, but the lack of concrete boundaries could create interpretive friction during implementation. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- **§1–§4** establish a useful missing governance concept: non-human actors are not exempt infrastructure and must operate through explicit identity, scope, routing, and audit.
- **§4.2, §4.4, and §4.11** are well aligned with the broader AIOS posture of default-deny, fail-closed, policy-mediated execution.
- **§4.6–§4.10** correctly resist silent substitution among service accounts, agent principals, application principals, and human actors.
- **§5** generally positions the amendment as additive rather than superseding, which helps preserve constitutional and spec hierarchy.

### Critical Gaps

- **§3 and §4** introduce new normative terms without binding mappings to existing artifacts in *AIOS PolicyRecord Specification* §3, *Intent Primitive and Execution Model* §§5, 12, and 15, or *AMD-2026-007* §11.9.
- **§4.4 and §4.5** require routed communication and action-carriage fields, but no canonical schema, minimum record shape, or conformance test rule is provided.
- **§4.6–§4.8** distinguish principal classes, but the document does not define how those classes are represented in policy, session truth, or audit truth.
- **§6** references “current shell-first phase packets,” but this is too informal for a governing amendment and should be converted into explicit cross-document deltas or removed.

---

## Article-by-Article Review

### 0. Status

**Feedback:**  
This section is clear but minimal. “Narrow authority amendment” is understandable editorially, but it is not a defined governance category elsewhere in the provided corpus. The section would be stronger if it explicitly stated precedence boundaries, e.g., that this amendment constrains principal authority but does not alter shell authority under *AMD-2026-012* §4 or domain intent execution under *AIOS-SPEC-009* §2.1.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 4, Conflict Freedom: 3

**Recommendation:**  
Add a final sentence:  
> “This amendment constrains non-human principal authority within the existing shell, policy, and domain-intent architecture; it does not alter shell authority under AMD-2026-012 §4 or domain intent execution boundaries under AIOS-SPEC-009 §2.1.”

---

### 1. Purpose

**Feedback:**  
The section states the problem clearly, but the bullet list is more manifesto-like than amendment-like. It would benefit from one paragraph that states the legal thesis in enforceable terms. The phrase “hidden prompts” is understandable but not a defined governance object in the provided set; it reads as shorthand rather than binding doctrine.

**Scores:** Style & Clarity: 4, Legal Enforceability: 2, Architectural Fidelity: 4

**Recommendation:**  
Replace the final three bullets with a normative summary paragraph such as:  
> “This amendment establishes that non-human authority in AI OS is lawful only when the acting principal is explicitly identified, bound to a governed role, bound to a governed scope, routed through an approved authority path, and recorded in auditable action records. Authority that lacks any of those elements is invalid and SHALL NOT be exercised.”

---

### 2. Scope

**Feedback:**  
The scope is appropriately narrow, but “product-repo implementation detail beyond what is necessary to define binding doctrine” is vague. The section should also expressly exclude redefinition of shell-state semantics already governed by *AMD-2026-007* §11.9 and *AIOS-SPEC-009* §2.1. Without that exclusion, overlap risk remains.

**Scores:** Conflict Freedom: 3, Completeness: 3, Style & Clarity: 4

**Recommendation:**  
Add to **Out of scope**:  
> “- redefining shell-state routing semantics already governed by AMD-2026-007 §11.9  
> - redefining domain intent lifecycle, execution-plan law, or PolicyRecord schema already governed by AIOS-SPEC-009 and AIOS-SPEC-002”

---

### 3. Definitions

**Feedback:**  
This section is the document’s main weakness. The definitions are intelligible, but several are not yet enforceable because they depend on undefined subordinate concepts. Examples: “permission families,” “approved shell intents,” “governed mediated routes,” and “another explicitly ratified scope class.” The definition of **Scope binding** is especially under-specified because it mixes examples with an open-ended catch-all. The definition of **Deterministic non-human action** is useful, but it should be tied to policy and route validation, not just pre-bound permissions and scope.

**Scores:** Legal Enforceability: 2, Cross-Document Consistency: 2, Developer Synchrony: 2

**Recommendation:**  
Revise definitions to align with existing artifacts. Suggested replacement text:

> “**Scope binding** means the governed boundary within which a principal’s authority is valid. A conformant implementation SHALL represent scope binding through one or more documented scope dimensions, including at minimum tenant scope, session scope where applicable, and resource or route scope where applicable. Additional scope classes MAY be used only if documented in a ratified specification or conformance record.”

> “**Routed communication** means non-human communication or action requests carried through a documented authority path that is subject to policy evaluation, audit correlation, and route-class identification.”

> “**Deterministic non-human action** means an action executed by a non-human principal under pre-bound permissions, pre-bound scope, and a documented route class, without runtime human interpretation of whether that principal is authorized to act.”

Also add a definition for **route class** and **authority-bearing action** because both are used normatively later.

---

### 4. Normative decisions

**Feedback:**  
This is the substantive core and generally the strongest part of the amendment. However, it remains too abstract for ratification in its current form.

- **§4.2–§4.3** are sound but should explicitly state whether policy evaluation is required before action or whether role/scope may be embedded in policy truth.
- **§4.4** is directionally correct, but “approved routed surfaces MAY include” is too open-ended for a binding rule. The amendment should either define a closed minimum set or require a documented conformance record.
- **§4.5** is important but incomplete. It should specify whether these fields must exist in the action envelope, audit record, or both.
- **§4.6–§4.8** distinguish principal classes but do not define the legal consequences of misclassification.
- **§4.10** is strong conceptually, but “user-visible artifact” and “ownership” need cross-reference to a source of truth or a required disclosure record.
- **§4.11** correctly imports fail-closed posture, but it should cite *AIOS-SPEC-002* §1 and §6 more precisely and should define failure outcomes.

**Scores:** Architectural Fidelity: 4, Legal Enforceability: 2, Completeness: 2, Practical Operability: 2

**Recommendation:**  
Split §4 into tighter subsections with explicit conformance hooks. At minimum:

1. Add a subsection after **§4.5** titled **“Minimum conformance record”** with text such as:  
   > “A conformant implementation SHALL document, for each non-human principal class in use: (a) principal identifier format, (b) role-binding source, (c) scope-binding dimensions, (d) permitted route classes, (e) audit record location, and (f) failure outcome when validation fails.”

2. Tighten **§4.4** to:  
   > “Non-human principals SHALL communicate through documented route classes only. Each route class used for authority-bearing action SHALL be identified in a ratified specification, implementation conformance record, or policy annex.”

3. Tighten **§4.5** to:  
   > “The minimum facts in this subsection SHALL be present either in the execution envelope, the audit record, or both, provided the records are deterministically joinable by audit correlation identifier.”

4. Add a misclassification rule:  
   > “If an implementation cannot distinguish principal class at evaluation time, it SHALL treat the action as under-governed and SHALL deny execution.”

5. Add a failure rule:  
   > “On failure of principal identification, role-binding validation, scope-binding validation, or route validation, the system SHALL deny the authority-bearing action and record the denial in an auditable record.”

---

### 5. Relationship to existing governance

**Feedback:**  
This section is helpful, but it is too high-level. For an editorially coherent governing set, this table should cite specific sections, not just document titles. The current wording also misses the most important overlap boundary: *AIOS-SPEC-009* §2.1 and *AMD-2026-007* §11.9 on shell-state vs domain execution. The row for *AIOS-SPEC-002* should also clarify whether principal class, role binding, and scope binding are expected to be evaluated through `PolicyRecord.conditions`, `required_context_keys`, or a successor schema.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 3, Developer Synchrony: 2

**Recommendation:**  
Revise the table to cite sections. Example:

- “AMD-2026-012 §4.2 remains authoritative for shell session authority.”
- “AMD-2026-007 §11.9 and AIOS-SPEC-009 §2.1 remain authoritative for shell-state routing vs domain intent execution.”
- “AIOS-SPEC-002 §3 and §5 remain authoritative for policy evaluation artifacts; this amendment adds required principal-governance inputs to that evaluation posture.”

---

### 6. Immediate shell-program implications

**Feedback:**  
This section is currently too informal for a binding amendment. “Current shell-first phase packets” is not a stable legal referent. The section reads like an implementation memo note rather than ratifiable law. It should either be converted into a formal cross-document impact section or moved to a non-normative appendix.

**Scores:** Style & Clarity: 3, Cross-Document Consistency: 2, Completeness: 2

**Recommendation:**  
Replace §6 with a formal **Cross-document impact (informative)** table, for example:

| Document / artifact class | Required follow-up |
|---|---|
| AIOS-SPEC-002 | Add principal-governance guidance for policy context keys and audit linkage |
| AIOS-SPEC-009 | Add principal identity / class disclosure and execution-envelope linkage where non-human actors initiate or execute plans |
| Shell planning packets | Cite this amendment as doctrine source; do not restate principal law in planning prose |

If retained, mark the section explicitly as **informative**.

---

### 7. Non-goals

**Feedback:**  
This section is useful and generally clear. It reinforces the amendment’s bounded thesis. However, some bullets are framed rhetorically rather than as governance exclusions. “Kubernetes-specific borrowing exercise” is too colloquial for this document set and should be generalized.

**Scores:** Style & Clarity: 4, Legal Enforceability: 3, Friction Factor: 4

**Recommendation:**  
Replace the first bullet with:  
> “- limiting service-account governance to a single infrastructure vendor model rather than defining platform-wide authority law”

This preserves the point while matching the style guide.

---

### 8. Amendment history

**Feedback:**  
Adequate for a draft. No issue.

**Scores:** Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §3 Definitions | Key terms are not enforceable because route class, authority-bearing action, scope dimensions, and policy linkage are undefined. | Rewrite definitions to align with existing artifacts and add definitions for `route class` and `authority-bearing action`. | Critical | 1, 3, 5, 7, 9 |
| 2 | §4.4–§4.5 | Routed communication and required fields are mandated without a canonical conformance structure. | Add a minimum conformance record subsection and specify where required facts must live and how they are joined. | Critical | 3, 5, 7, 9 |
| 3 | §4 overall | The amendment does not define deterministic failure outcomes for missing principal identity, role binding, scope binding, or route validation. | Add explicit deny-and-audit failure rules for each validation failure class. | Critical | 3, 5, 7 |
| 4 | §2 and §5 | Overlap boundaries with AMD-2026-007 §11.9 and AIOS-SPEC-009 §2.1 are not sharp enough. | Add explicit out-of-scope and relationship language preserving shell-state vs domain-intent boundaries. | High | 1, 4, 6 |
| 5 | §5 Relationship table | Cross-references are too general and do not cite section-level authorities. | Replace document-only references with section-specific citations. | High | 1, 6, 9 |
| 6 | §6 Immediate shell-program implications | The section is too informal and references unstable planning artifacts in normative prose. | Convert §6 into an informative cross-document impact table or move it to an appendix. | High | 1, 5, 8 |
| 7 | §1 Purpose | The purpose section uses rhetorical bullets where a concise normative thesis would be stronger. | Replace the closing bullets with one enforceable summary paragraph. | Medium | 3, 8 |
| 8 | §7 Non-goals | One bullet uses colloquial wording inconsistent with the style guide. | Replace “Kubernetes-specific borrowing exercise” with platform-neutral governance language. | Low | 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The amendment identifies a real governance gap and is architecturally aligned, but it is not yet ratification-ready because legal enforceability, completeness, practical operability, and developer synchrony are below threshold. Two dimensions score 2, which triggers major revision under the rubric.

**Top 3 Actions Required:**
1. Add enforceable definitions and a minimum conformance structure for principal identity, scope binding, route class, and audit linkage.
2. Tighten §4 with explicit deny-and-audit failure outcomes and deterministic validation rules.
3. Sharpen cross-document boundaries and section-level citations, especially against AMD-2026-007 §11.9, AMD-2026-012 §4.2, AIOS-SPEC-002 §3, and AIOS-SPEC-009 §2.1 / §12 / §15.
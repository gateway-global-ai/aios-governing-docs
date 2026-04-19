---
review_id: REV-AMD-2026-008-ADD-004-002
document_reviewed: amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md
document_version: 0.2.0
reviewer: OpenAI
review_date: 2026-04-08
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: AMD-2026-008-ADD-004 — Pre-Human Browser Review and Visual Proof Gate

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The addendum is broadly aligned to the AMD-2026-008 addendum family, but several cross-references are incomplete or imprecise and the document cites AMD-2026-005 without bundling or section-specific support. |
| 2 | Business Model Alignment | 3 | The document stays mostly neutral on economics, but it does not clearly state who bears the operational cost of browser-proof capture or how entitlement-sensitive review tooling interacts with MPOA-governed product tiers. |
| 3 | Legal Enforceability | 3 | Core obligations are stated in mandatory language, but several approval, exception, and policy-delegation clauses remain too open-ended to be reliably enforced in dispute without tighter authority and record requirements. |
| 4 | Architectural Fidelity | 3 | The doctrine is directionally consistent with shell-governed behavior and evidence-based control, but it does not clearly anchor the browser-review gate within the broader AIOS separation between governance, shell surfaces, and implementation planes. |
| 5 | Completeness | 3 | The document covers the main gate concept, but it omits key edge-case handling for non-browser governed surfaces, multi-variant products, evidence retention, and authority for policy overrides. |
| 6 | Conflict Freedom | 3 | No direct contradiction is apparent, but the addendum creates tension with the ratified status of ADD-003 and draft status of ADD-001/ADD-002 by treating all as coequal dependencies without clarifying precedence. |
| 7 | Practical Operability | 3 | The review-target and evidence concepts are implementable, but the document leaves too much to future policy on schemas, ownership, timing, and acceptance criteria for teams to execute consistently today. |
| 8 | Style & Clarity | 4 | The prose is generally clear and disciplined, but some sections use slogan-like phrasing, uneven capitalization, and undefined approval actors that reduce precision. |
| 9 | Developer Synchrony | 2 | The document repeatedly references machine-readable artifacts and review packets but does not define a canonical implementation home, lifecycle, or minimum field discipline tightly enough for engineering teams to build against. |
| 10 | Platform Economics Synchrony | 3 | The addendum avoids rewriting MPOA economics, but it does not explain whether browser review is mandatory across all tiers or how proportionality interacts with cost-sensitive execution paths. |
| 11 | Friction Factor | 4 | The gate is conceptually narrow and proportionate in intent, but the current drafting still risks process drag because ambiguous cases default to review-required without a crisp triage mechanism. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- **Sections 1, 2, and 15** articulate the governing thesis clearly: rendered UI evidence is distinct from plans, diffs, and claims, and human approval remains separate from promotion or release.
- **Section 4.1** usefully introduces proportionality, which prevents the gate from reading as an absolute full-browser-review mandate for every UI-adjacent change.
- **Sections 6, 7, 8, and 11** create a coherent evidence stack: review target, minimum proof set, required checks, and audit posture.
- **Section 9.4** is a meaningful improvement because it defines remediation paths rather than leaving blocked states as dead ends.
- **Section 16** appropriately keeps the external repository reference quarantined and avoids silently importing third-party patterns into normative law.

### Critical Gaps

- **Section 0.1 and Section 6** define core terms and fields, but the document never identifies a governing implementation home or authority hierarchy for schema, storage, and policy override, leaving engineering and audit teams without a stable conformance target.
- **Sections 4, 9, and 10** rely heavily on “policy” without specifying who may set, narrow, or waive requirements, which weakens enforceability and cross-document coherence.
- **Cross-references are under-specified throughout**: the document names parent and sibling addenda but rarely cites the exact sections it depends on, despite the style guide requiring specific Article/Section references.
- **Section 3 and Section 7** are browser-centric in a way that may conflict with the broader “governed surface” framing in Section 0.1, because the document does not clearly distinguish browser-only proof from policy-equivalent non-browser proof.
- **Metadata coherence is weak**: the addendum history says “Phase E” and “Round 1 feedback,” but this is a Round 1 review packet, and the document references AMD-2026-005 in Section 0.1 even though that text is not bundled here.

---

## Article-by-Article Review

### 0. Status and intent / 0.1 Definitions

**Feedback:**  
This opening is concise and mostly effective, but it has two coherence problems. First, the “Does not replace” row references ADD-001, ADD-002, and ADD-003 only by shorthand, whereas sibling addenda usually restate titles or use more exact cross-reference framing. Second, Section 0.1 says terms “SHALL be read consistently with AMD-2026-005 peer-review thresholds where applicable,” but AMD-2026-005 is not included in the bundled context and no section citation is given. That makes the reference editorially weak and legally thin. The definitions themselves are useful, especially **Stale** and **Current**, but “browser-visible evidence” includes “policy-equivalent governed surface,” which later sections do not consistently honor because the rest of the document is drafted almost entirely around browser capture.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 3, Style & Clarity: 4

**Recommendation:**  
Revise the opening cross-reference language and tighten the AMD-2026-005 dependency. Proposed text:

- Replace in **0. Status and intent / Does not replace**:  
  “**ADD-001** (navigation), **ADD-002** (depth / voice / packaging / BOOK), **ADD-003** (composition control plane).”  
  with  
  “*Base Shell Navigation Primitives and Start-Here Control* (**AMD-2026-008-ADD-001**), *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (**AMD-2026-008-ADD-002**), and *Composition Control Plane for Messages, Invites, and Documents* (**AMD-2026-008-ADD-003**).”

- Replace in **§0.1 lead-in**:  
  “The following terms **SHALL** be read consistently with **[AMD-2026-005](AMD-2026-005.md)** peer-review thresholds where applicable:”  
  with  
  “The following terms apply in this addendum. Where a review workflow also invokes peer-review thresholds under a separately governed amendment, that amendment **SHALL** control its own scoring and disposition rules; this addendum governs only browser-review evidence and approval prerequisites.”

---

### 1. Purpose

**Feedback:**  
Section 1 is clear and well-scoped. It correctly distinguishes rendered proof from doctrine, plans, mock descriptions, and code assertions. The numbered list is useful. Editorially, however, the section would be stronger if it explicitly said whether the gate applies only to browser-rendered surfaces or also to other governed visual surfaces referenced in Section 0.1. Right now, Section 1 reads browser-exclusive, while the definition section leaves room for policy-equivalent surfaces.

**Scores:** Completeness: 3, Style & Clarity: 4, Conflict Freedom: 3

**Recommendation:**  
Add one clarifying sentence at the end of the first paragraph:

> “Where policy recognizes a governed non-browser visual surface as equivalent for a specific review target, that equivalence **SHALL** be recorded in the review target and audit record; otherwise, browser-rendered proof **SHALL** be required.”

---

### 2. Governing principle

**Feedback:**  
The core doctrine is strong, especially the non-substitution rule. However, the sentence “A rendered interface is part of system truth” reads more like manifesto language than enforceable governance text. It is memorable, but less precise than the surrounding clauses. Also, “when policy or review target requires visual proof” is correct but leaves open who defines that policy and under what authority.

**Scores:** Legal Enforceability: 3, Architectural Fidelity: 3, Style & Clarity: 3

**Recommendation:**  
Replace the slogan sentence with enforceable language:

- Replace  
  “A rendered interface is part of system truth.”  
  with  
  “For UI-affecting work within scope, rendered interface state **SHALL** be treated as approval-relevant evidence, not merely an implementation detail.”

Also add after the first sentence:

> “The governing policy authority for requiring, narrowing, or excepting visual proof **SHALL** be identified in the review target or exception record.”

---

### 3. Scope

**Feedback:**  
The scope section is sensible and generally proportional. The in-scope list is good, especially the inclusion of blocked/gated actions and composition surfaces governed by ADD-003. The main issue is boundary precision: “browser-rendered workflow steps” and “UI behavior whose absence or misrender would materially change user understanding or trust” are broad and subjective. The out-of-scope list is helpful, but it does not address hybrid cases such as backend changes that alter disclosures or state rendering indirectly. Section 3.3 is too short to carry the policy-expansion burden.

**Scores:** Completeness: 3, Practical Operability: 3, Friction Factor: 4

**Recommendation:**  
Add a hybrid-case clarifier in **§3.2**:

> “A change that is backend-originated but alters rendered disclosures, visible state, blocked actions, or user-facing workflow behavior **SHALL** be treated as UI-affecting for purposes of this addendum.”

And expand **§3.3**:

> “Policy **MAY** extend browser-review requirements to additional work classes, but any such extension **SHALL** identify the approving authority, affected surfaces, and minimum proof class with audit visibility.”

---

### 4. Trigger conditions / 4.1 Policy proportionality

**Feedback:**  
This is one of the stronger sections. The trigger list is concrete and aligned with the document’s purpose. The ambiguity default is also sound. The weakness is governance authority: “policy” appears repeatedly, but the document never says whether policy means tenant policy, platform policy, product policy, or review-program policy. Section 4.1 is a good addition, but “Any reduction of default §7 minimums” implies that Section 7 is a default baseline while Section 7 itself does not clearly label which items are reducible and which are mandatory.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 3, Practical Operability: 3

**Recommendation:**  
Add a policy-authority sentence at the start of **§4**:

> “For this addendum, ‘policy’ means a governed platform or tenant policy artifact authorized to control review requirements for the relevant surface; ad hoc team practice **SHALL NOT** substitute for such policy.”

Add to **§4.1**:

> “Unless a review target or policy expressly narrows a proof class, **surface proof**, **state proof**, and **review packet pointer** remain mandatory minimums.”

---

### 5. Phase placement

**Feedback:**  
The sequencing is clear and fits well with AIOS-AMD-PLAN-001. The problem is that the cross-document relationship remains descriptive rather than exact. Since this section is effectively integrating with the planning lifecycle, it should cite the relevant phases more precisely. Section 5.3 is also useful, but “bounded local or isolated execution path” would benefit from a traceability requirement back to the review target and artifact version.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 2, Style & Clarity: 4

**Recommendation:**  
Revise **§5.1** to anchor to the planning lifecycle more explicitly:

> “Where the planning lifecycle in *Amendment pre-ratification planning lifecycle (architect → UI → committee → peer review)* (**AIOS-AMD-PLAN-001**) is used, browser-visible review evidence **SHALL** occur after implementation preparation or bounded execution and before human approval of the UI-affecting work item.”

Add to **§5.3**:

> “Any bounded local or isolated execution path used for capture **SHALL** identify the artifact version, environment, and review target it serves.”

---

### 6. Review target contract

**Feedback:**  
This is the operational center of the document, and it is not yet strong enough. The field table is useful, and the doctrine/implementation distinction is sensible, but the section stops short of defining a canonical conformance home. Saying the schema, storage location, and registry “SHALL be defined by policy or product implementation” is too loose for a binding governance document. This is the document’s biggest developer-synchrony gap. It needs either a named default artifact or a requirement that one be registered before conformance claims are made.

**Scores:** Developer Synchrony: 2, Practical Operability: 3, Legal Enforceability: 3

**Recommendation:**  
Strengthen **§6.1** with a default-home rule. Proposed replacement for the second paragraph:

> “Normative field names in **§6.1** are doctrine. Before any product or workflow claims conformance to this addendum, policy **SHALL** register a canonical machine-readable implementation home for the review target contract, including schema location, storage location, and `review_slug` uniqueness discipline. Until such registration exists, the recommended default artifact is `REVIEW_TARGET.yaml` as described in **§14**. Products **SHALL NOT** claim conformance to this addendum on an implementation-defined review-target shape with no traceable governed home.”

Also add to **§6.2**:

> “A ‘not applicable’ disposition **SHALL** identify the specific proof, the reason, and the approving authority if policy requires approval for that disposition.”

---

### 7. Minimum browser evidence

**Feedback:**  
The minimum evidence set is coherent and practical. Section 7.2’s treatment of test-captured proof is one of the better-drafted parts of the document. The main issue is that “rendered browser exports” is vague, and “equivalent visual evidence allowed by policy” again delegates too much. Section 7.3 is good, but it should explicitly say that these items may still be supporting evidence even though they are insufficient alone.

**Scores:** Practical Operability: 3, Completeness: 3, Style & Clarity: 4

**Recommendation:**  
Add a clarifier to **§7.2**:

> “For purposes of this section, ‘rendered browser exports’ means governed artifacts generated from an actual rendered session state, not static design exports or manually reconstructed images.”

Add to **§7.3**:

> “The items below **MAY** be included as supporting evidence, but **SHALL NOT** satisfy the browser-review gate on their own.”

---

### 8. Required checks

**Feedback:**  
This section is well organized and readable. It maps cleanly to the evidence categories and sibling addenda. The main gap is acceptance criteria. For example, “labels and action semantics are clear” and “failure and fallback states are understandable” are too subjective without a standard of review. This is acceptable for doctrine, but the document should say that policy or the review target must define any stricter acceptance criteria for regulated or high-risk surfaces.

**Scores:** Completeness: 3, Legal Enforceability: 3, Friction Factor: 4

**Recommendation:**  
Add a closing sentence to **§8**:

> “Where a surface is regulated, high-risk, or otherwise subject to stricter review, policy or the review target **SHALL** define additional acceptance criteria beyond the baseline checks in **§8.1**–**§8.5**.”

---

### 9. Approval rule

**Feedback:**  
This section is structurally sound and improved by §9.4. The blocked-state list is useful. The remaining issue is authority and finality: partial approval and policy exceptions are allowed, but the document does not specify whether human approval status must distinguish “approved,” “approved in part,” and “exception-approved,” nor whether those states are mutually exclusive. That matters for auditability.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Developer Synchrony: 2

**Recommendation:**  
Add to **§9.1**:

> “`human_approval_status` **SHALL** distinguish at minimum full approval, partial approval, blocked, and exception-based approval where those states are used.”

Add to **§9.3**:

> “A partial approval record **SHALL** identify the approved surfaces, excluded surfaces, and any actions that remain blocked.”

---

### 10. Exceptions

**Feedback:**  
The section is directionally correct but too thin for a binding exception regime. It says an exception must be explicit and auditable, but it does not specify whether exceptions are one-time, time-bounded, surface-bounded, or reusable. It also does not say whether an exception can waive only proof capture, only timing, or the entire gate. This is a legal and editorial weakness.

**Scores:** Legal Enforceability: 2, Conflict Freedom: 3, Style & Clarity: 4

**Recommendation:**  
Expand **§10.2** with boundedness requirements:

> “The exception record **SHALL** also state whether the exception is one-time or reusable, the surfaces and release path it covers, the time window for which it is valid, and whether it waives proof capture, timing, or another specific requirement. An exception **SHALL NOT** be read broadly beyond its recorded scope.”

Add a new **§10.4**:

> “Exception authority **SHALL** be defined by policy. In the absence of such policy, no exception may be granted.”

---

### 11. Audit posture

**Feedback:**  
The field list is good, but retention, immutability, and linkage are missing. Since this section is the audit backbone, it should at least require that the record be preserved in a traceable location and linked to the approval packet. “Where possible” in `artifact_version` is also weak for a normative field list.

**Scores:** Developer Synchrony: 2, Legal Enforceability: 3, Completeness: 3

**Recommendation:**  
Revise the last row and add a preservation sentence:

- Replace  
  “`artifact_version` | Version or commit identity where possible”  
  with  
  “`artifact_version` | Version, build, commit, or equivalent release identity for the reviewed artifact”

- Add after the table:  
  “The audit record **SHALL** be preserved in a traceable location linked to the review target and approval packet. If a precise artifact identity is unavailable, the record **SHALL** state the reason.”

---

### 12. Relationship to other addenda

**Feedback:**  
This section is useful but under-cited. It should reference exact sibling sections where the browser gate most directly applies, especially ADD-002 Section 10.11 and ADD-003 Sections 5, 9.4, 18, 19, and 20. As written, it is coherent but not precise enough for a cross-document governance set.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 3, Style & Clarity: 4

**Recommendation:**  
Revise each subsection to include section-specific references. Example for **§12.3**:

> “*Composition Control Plane for Messages, Invites, and Documents* (**AMD-2026-008-ADD-003**) governs composition class, composition contract (**§5**), professional-use disclosure (**§9.4**), knowledge-basis gating (**§18**), originality and source-boundary verification (**§19**), and reference-guided composition (**§20**). This addendum governs the browser-visible review phase used to verify that those controls render clearly on governed surfaces when visual proof is required.”

Apply similar specificity to **§12.1** and **§12.2**.

---

### 13. Non-goals

**Feedback:**  
This section is concise and appropriate. No major issue beyond a minor editorial point: “ratify code by itself” is understandable but slightly colloquial for this document set.

**Scores:** Style & Clarity: 4, Conflict Freedom: 4

**Recommendation:**  
Replace “ratify code by itself” with:

> “treat code implementation alone as sufficient approval evidence”

---

### 14. Recommended artifacts

**Feedback:**  
This section is practical, but it creates a coherence issue with Section 6. If these artifacts are recommended and one of them is the likely default implementation home, the document should say so more directly. Otherwise, engineering teams are left with a recommendation list rather than a conformance path.

**Scores:** Developer Synchrony: 2, Practical Operability: 3, Style & Clarity: 4

**Recommendation:**  
Add:

> “Unless policy registers an alternative governed implementation home under **§6.1**, `REVIEW_TARGET.yaml` **SHALL** serve as the default machine-readable review-target artifact for conformance claims under this addendum.”

---

### 15. Decision rule

**Feedback:**  
This is a strong summary section and one of the clearest parts of the document. It preserves the separation between proof, approval, and release. No substantive issue beyond the need to align terminology with the approval states in Section 9.

**Scores:** Style & Clarity: 5, Conflict Freedom: 4, Friction Factor: 4

**Recommendation:**  
Add one sentence:

> “The approval outcomes in this section **SHALL** map to the recorded approval states defined under **§9** and policy.”

---

### 16. Informative external reference (quarantine)

**Feedback:**  
This section is appropriately bounded and consistent with AMD-2026-011 and AIOS-SPEC-013. The quarantine posture is clear. The only editorial issue is that the section cites a relative path into `specifications/` for AIOS-SPEC-013 while the rest of the document mostly uses document IDs and titles; consistency would improve if the inline citation style matched the rest of the addendum family.

**Scores:** Cross-Document Consistency: 4, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
Use full title plus document ID in the lead sentence, e.g.:

> “For pattern study only, the following repository is registered under quarantine per *External Repository Acquisition, Quarantine, Promotion, and Minimal Governance Execution Dependencies* (**AMD-2026-011**) and *External Repository Acquisition, Analysis, and Promotion* (**AIOS-SPEC-013**).”

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §6.1, §14 | No canonical implementation home for review-target schema and artifacts | Require policy to register a canonical machine-readable implementation home before conformance claims; make `REVIEW_TARGET.yaml` the default if no alternative is registered | Critical | 3, 7, 9 |
| 2 | §4, §10 | “Policy” and exception authority are undefined | Define what policy means for this addendum and require policy-defined exception authority, scope, and validity limits | Critical | 1, 3, 6, 7 |
| 3 | §12.1–§12.3 | Cross-document references are too general | Add exact sibling-section citations to ADD-001, ADD-002, and ADD-003 to improve coherence and interpretation | High | 1, 6, 8 |
| 4 | §0.1, §1, §3 | Browser-only drafting conflicts with “policy-equivalent governed surface” language | Clarify when non-browser governed surfaces may satisfy the gate and require that equivalence be recorded in the review target | High | 1, 4, 5 |
| 5 | §11 | Audit posture lacks retention and artifact identity discipline | Require traceable storage, linkage to approval packet, and explicit reason when precise artifact identity is unavailable | High | 3, 5, 9 |
| 6 | §9.1, §9.3 | Approval-state taxonomy is incomplete | Require `human_approval_status` to distinguish full, partial, blocked, and exception-based approval and define partial-approval contents | High | 3, 7, 9 |
| 7 | §8 | Acceptance criteria are too subjective for high-risk surfaces | Require policy or review target to define stricter acceptance criteria for regulated or high-risk surfaces | Medium | 3, 5, 7 |
| 8 | §7.2, §7.3 | Evidence categories need sharper boundaries | Define “rendered browser exports” and state that insufficient items may be supporting evidence but not sufficient evidence alone | Medium | 5, 7, 8 |
| 9 | §5.1, §5.3 | Planning-lifecycle integration is descriptive rather than exact | Tie browser review more explicitly to AIOS-AMD-PLAN-001 phase placement and require artifact-version/environment traceability for execution paths | Medium | 1, 4, 9 |
| 10 | §2, §13 | A few phrases are more rhetorical than enforceable | Replace slogan-like or colloquial phrases with precise governance language | Low | 3, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has a solid governing concept and a workable structure, but it is not yet sufficiently precise on implementation home, policy authority, exception authority, and cross-document citation discipline to function as a reliable binding addendum. The low Developer Synchrony score and multiple “3” scores keep it below approval quality for Round 1.

**Top 3 Actions Required:**
1. Define a canonical conformance path for the review-target contract and audit artifacts, with a default implementation home if policy has not yet registered one.
2. Tighten authority language for policy, exceptions, and approval states so the gate is enforceable and auditable rather than implementation-defined.
3. Add exact cross-document section citations and resolve the browser-only versus policy-equivalent-surface ambiguity.
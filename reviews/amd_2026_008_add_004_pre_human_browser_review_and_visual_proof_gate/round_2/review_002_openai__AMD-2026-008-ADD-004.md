---
review_id: REV-AMD-2026-008-ADD-004-004
document_reviewed: amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md
document_version: 0.3.0
reviewer: OpenAI
review_date: 2026-04-09
review_round: 2
review_type: editorial
disposition: approved_with_changes
composite_score: 3.7
---

# Peer Review: AMD-2026-008-ADD-004 — Pre-Human Browser Review and Visual Proof Gate

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Round 1 cross-document gaps were materially improved through §2.1, §3.4, §11.1, and §12.4, but several citations still rely on shorthand or path-only references instead of exact document-title-and-section discipline. |
| 2 | Business Model Alignment | 3 | The new MPOA pointer in §2.1 acknowledges cost and tier context, but the document still does not clearly state whether browser-proof obligations are universal or tier-sensitive when policy applies proportionality. |
| 3 | Legal Enforceability | 4 | The gate, blocked states, and exception posture are substantially tighter than in v0.2.0, though exception scope, approval-state taxonomy, and artifact identity language still need sharper binding text. |
| 4 | Architectural Fidelity | 4 | The addendum now better respects the separation between review evidence, execution, and sibling addenda, but it still lacks a precise statement tying browser proof to governed surfaces under AIOS-SPEC-006 and execution truth under AIOS-SPEC-009. |
| 5 | Completeness | 4 | The revised draft now covers most Round 1 omissions, including non-browser equivalence and implementation seam, but it still leaves retention, approval-state granularity, and hybrid backend-to-UI cases underdefined. |
| 6 | Conflict Freedom | 4 | The new precedence clause in §12.4 resolves the main ratified-vs-draft tension from Round 1, with no direct contradiction found, though some ambiguity remains around AMD-2026-005 dependence in §0.1 and §0 artifact-vs-gate language. |
| 7 | Practical Operability | 4 | The document is now operational enough to guide teams, especially through §§6–11, but a few key controls still depend on future policy registration rather than a default conformance path. |
| 8 | Style & Clarity | 3 | The structure is sound, but the draft still contains over-bolded prose, slogan-like language in §2, and several sentences whose visual emphasis reduces readability rather than improving precision. |
| 9 | Developer Synchrony | 3 | §11.1 is a meaningful improvement, but the document still stops short of naming a default canonical schema and audit home, leaving engineering teams with doctrine plus deferral rather than a buildable baseline. |
| 10 | Platform Economics Synchrony | 3 | The document now recognizes MPOA context, but it still does not explain how review depth, evidence capture burden, or entitlement-sensitive tooling should interact with platform economics in practice. |
| 11 | Friction Factor | 5 | The gate remains narrow, targeted, and proportionate, and the revised blocked-state and exception structure reduces the risk of bureaucratic overreach while preserving fail-closed behavior. |
| | **Composite Score** | **3.7** | |

---

## Overall Assessment

### Strengths

- **Round 1 issues were substantially addressed.** The revision log accurately reflects real improvements in the text: §2.1 adds missing AIOS-SPEC-006 / AIOS-SPEC-009 / MPOA context; §3.4 addresses the browser-only versus policy-equivalent-surface ambiguity; §11.1 adds the missing implementation seam; and §12.4 resolves the ratified-versus-draft addendum tension identified in Round 1.
- **The core gate is now much more enforceable.** §§4, 7, 9, and 10 create a coherent rule set: trigger conditions, minimum evidence, blocked approval states, remediation paths, and explicit exception handling.
- **The document now reads as a real governance addendum rather than only a concept note.** §§6 and 11 together establish a recognizable review-target and audit model, even if they still need one more tightening pass.
- **The separation-of-powers posture is preserved.** §5 and §15 correctly keep browser review distinct from human approval, and human approval distinct from promotion / merge / release / ratification.
- **The new precedence clause is especially valuable.** §12.4 is the right editorial fix for the Round 1 concern that ratified ADD-003 and draft ADD-001 / ADD-002 were being treated as coequal without interpretive guidance.

### Critical Gaps

- **The canonical implementation home is still not fully closed.** §6.1 and §11.1 improve the seam, but the document still does not require a default schema artifact or default audit record home before conformance claims are made.
- **Cross-reference discipline is improved but not yet style-guide clean.** Several sections still use shorthand references like “ADD-001,” “ADD-002,” and “ADD-003” without exact section citations, despite this document now depending materially on those sibling addenda.
- **Approval-state and exception records remain under-specified.** §§9–10 need explicit minimum state taxonomy and bounded exception scope so audit teams can distinguish full approval, partial approval, blocked approval, and exception-based approval consistently.
- **Style has regressed in places due to heavy emphasis formatting.** The dense bolding in §§0.2, 2.1, 3.4, 4.1, 9.4, 11.1, and 12.4 makes the document harder to read and less editorially clean than v0.2 in some passages.

---

## Article-by-Article Review

### 0. Status and intent / 0.1 Definitions / 0.2 Revision posture

**Feedback:**  
This opening is stronger than Round 1, especially because §0.2 candidly states that v0.3.0 is a Round 2 preparation draft rather than a ratification-ready text. That is good packet hygiene and improves coherence with the revision log. However, §0 still has two editorial problems. First, the “Does not replace” row uses shorthand labels rather than full sibling titles, which is weaker than the cross-reference discipline used elsewhere in the AIOS set. Second, §0.1 still says terms “SHALL be read consistently with AMD-2026-005 peer-review thresholds where applicable,” but AMD-2026-005 is not bundled here and no section citation is given. That remains a weak dependency. The definitions themselves are mostly sound, and the revised “Stale” / “Current” language is materially better than Round 1.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 3, Conflict Freedom: 4

**Recommendation:**  
Tighten the opening references and remove the loose AMD-2026-005 dependency.

Proposed edits:

- In **§0 / Does not replace**, replace:  
  “**ADD-001** (navigation), **ADD-002** (depth / voice / packaging / BOOK), **ADD-003** (composition control plane).”  
  with:  
  “*Base Shell Navigation Primitives and Start-Here Control* (**AMD-2026-008-ADD-001**), *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (**AMD-2026-008-ADD-002**), and *Composition Control Plane for Messages, Invites, and Documents* (**AMD-2026-008-ADD-003**).”

- In **§0.1**, replace:  
  “The following terms **SHALL** be read consistently with **[AMD-2026-005](AMD-2026-005.md)** peer-review thresholds where applicable:”  
  with:  
  “The following terms apply in this addendum. Any separate peer-review scoring or ratification thresholds remain governed by their own controlling documents.”

- In **§0.2**, reduce emphasis formatting and convert the table intro to plain prose for readability.

---

### 1. Purpose

**Feedback:**  
Section 1 remains clear and well-scoped. It states the problem crisply and avoids overclaiming. The numbered list is useful and operational. No major substantive issue remains here. The only editorial improvement would be to align the “what this addendum establishes” list more explicitly with later sections, but that is optional.

**Scores:** Completeness: 4, Style & Clarity: 4

**Recommendation:**  
Optional refinement only: add section pointers to the numbered list, e.g. “when browser review is required (§4), what evidence counts (§7), what minimum proof must be captured (§7.1), what can and cannot be approved (§9–§10), and how this phase interacts with planning and approval (§5, §15).”

---

### 2. Governing principle / 2.1 Cross-context pointers

**Feedback:**  
This section improved materially from Round 1 because §2.1 now anchors the addendum to AIOS-SPEC-009, AIOS-SPEC-006, and MPOA. That directly addresses a prior review concern. However, the core sentence “A rendered interface is part of system truth” is still more slogan than rule. It is memorable, but less precise than the surrounding governance language. Also, §2.1 still cites documents by path rather than by exact title plus section, and it does not specify which parts of AIOS-SPEC-006 or AIOS-SPEC-009 are most relevant. For an editorial review, that is the main remaining coherence gap.

**Scores:** Cross-Document Consistency: 4, Architectural Fidelity: 4, Style & Clarity: 3

**Recommendation:**  
Replace the slogan sentence and sharpen the cross-reference language.

Proposed edits:

- In **§2**, replace:  
  “A rendered interface is part of system truth.”  
  with:  
  “For UI-affecting work within scope, rendered interface state **SHALL** be treated as approval-relevant evidence, not merely an implementation detail.”

- In **§2.1**, replace the table entries with section-aware descriptions, for example:  
  “*Intent Primitive and Execution Model* (**AIOS-SPEC-009**) — intent, execution, and primary-surface truth relevant to what must be visibly proven before approval.”  
  “*UI Component Registry Standard* (**AIOS-SPEC-006**) — governed surfaces, transparency expectations, and view/shell discipline relevant to UI evidence.”  
  “*Master Platform Operating Agreement* (**MPOA**) — commercial tier, liability, and economics context where policy ties review depth to cost or entitlement.”

---

### 3. Scope

**Feedback:**  
The addition of §3.4 is a real improvement and adequately addresses the Round 1 ambiguity around policy-equivalent surfaces. That recommendation was accepted and substantively incorporated. The remaining gap is hybrid-case clarity: §3.2 excludes “backend-only changes with no UI effect,” but the document still does not explicitly say that backend-originated changes that alter rendered disclosures, blocked states, or visible behavior are in scope. That omission matters because many UI regressions originate outside front-end code.

**Scores:** Completeness: 4, Practical Operability: 4, Architectural Fidelity: 4

**Recommendation:**  
Add a hybrid-case clarifier to **§3.2** or a new **§3.2.1**:

> “A change that originates in backend, policy, or adapter logic but alters rendered disclosures, visible state, blocked actions, or user-facing workflow behavior **SHALL** be treated as UI-affecting for purposes of this addendum.”

Also expand **§3.3** slightly:

> “Any policy extension under this section **SHALL** identify the approving authority, affected surfaces, and minimum proof class with audit visibility.”

---

### 4. Trigger conditions / 4.1 Policy proportionality

**Feedback:**  
This section is stronger than v0.2.0 and addresses the Round 1 loophole concern better than before. The new language in §4.1 narrows the risk that proportionality could silently waive the gate. I agree with the revision direction. That said, the clause still says policy may shape the minimum visual proof “without waiving §2 where visual proof is required,” which is better but still slightly circular. It would be cleaner to state a non-waivable floor. Also, the document still does not define “policy” for this addendum, which was a Round 1 recommendation not fully accepted.

**Scores:** Legal Enforceability: 4, Practical Operability: 4, Business Model Alignment: 3

**Recommendation:**  
Add a policy-authority sentence at the start of **§4** and a non-waivable minimum in **§4.1**.

Proposed text:

- Add to **§4**, before the numbered list:  
  “For this addendum, ‘policy’ means a governed platform or tenant policy artifact authorized to control review requirements for the relevant surface; ad hoc team practice **SHALL NOT** substitute for such policy.”

- Add to **§4.1**:  
  “Unless a review target or explicit exception narrows scope under recorded authority, **surface proof**, **state proof**, and **review packet pointer** remain mandatory minimums for in-scope UI-affecting work.”

---

### 5. Phase placement

**Feedback:**  
This section remains sound and consistent with AIOS-AMD-PLAN-001. The sequence is clear. The main remaining issue is that §5.1 still describes the planning lifecycle generically rather than citing the planning document more exactly, and §5.3 still does not require artifact-version and environment traceability for the bounded execution path used to capture evidence.

**Scores:** Cross-Document Consistency: 4, Developer Synchrony: 3, Practical Operability: 4

**Recommendation:**  
Strengthen the planning and traceability language.

Proposed edits:

- In **§5.1**, add:  
  “Where the planning lifecycle in *Amendment pre-ratification planning lifecycle (architect → UI → committee → peer review)* (**AIOS-AMD-PLAN-001**) is used, browser-visible review evidence **SHALL** occur after implementation preparation or bounded execution and before human approval of the UI-affecting work item.”

- In **§5.3**, add:  
  “Any bounded local or isolated execution path used for capture **SHALL** identify the artifact version, environment, and review target it serves.”

---

### 6. Review target contract

**Feedback:**  
This is improved from Round 1, but only partially. The document now clearly says a traceable home is required, which is good. However, the recommendation to close the conformance path with a default implementation home was not fully accepted. `REVIEW_TARGET.yaml` remains only “recommended,” and the text still allows policy or product implementation to define the canonical schema later. That is better than v0.2.0, but still not enough for strong developer synchrony. This remains the document’s biggest unresolved editorial-operational gap.

**Scores:** Developer Synchrony: 3, Legal Enforceability: 4, Practical Operability: 4

**Recommendation:**  
Convert the recommendation into a default rule.

Proposed replacement for the second paragraph of **§6.1**:

> “Normative field names in **§6.1** are doctrine. Before any product or workflow claims conformance to this addendum, policy **SHALL** register a canonical machine-readable implementation home for the review target contract, including schema location, storage location, and `review_slug` uniqueness discipline. Unless policy registers an alternative governed artifact, `REVIEW_TARGET.yaml` **SHALL** serve as the default machine-readable review-target artifact for conformance claims under this addendum.”

Also add to **§6.2**:

> “A ‘not applicable’ disposition **SHALL** identify the specific proof, the reason, and the approving authority where policy requires approval for that disposition.”

---

### 7. Minimum browser evidence

**Feedback:**  
This section is operationally solid. The revised §7.2 test-captured proof language is much better than the earlier version and adequately addresses the Round 1 concern that automated proof needed to be mapped, policy-approved, and human-auditable. I agree with that revision. The remaining editorial gap is that “rendered browser exports” is still undefined, and §7.3 should explicitly say that insufficient items may still be supporting evidence.

**Scores:** Practical Operability: 4, Completeness: 4, Style & Clarity: 4

**Recommendation:**  
Add two clarifiers:

- In **§7.2**, after “rendered browser exports,” add:  
  “For this section, ‘rendered browser exports’ means governed artifacts generated from an actual rendered session state, not static design exports or manually reconstructed images.”

- In **§7.3**, add:  
  “The items below **MAY** be included as supporting evidence, but **SHALL NOT** satisfy the browser-review gate on their own.”

---

### 8. Required checks

**Feedback:**  
This section is clear and useful. It remains somewhat subjective in phrases like “labels and action semantics are clear” and “failure and fallback states are understandable,” but that is acceptable at doctrine level if stricter criteria can be layered by policy. The document still should say that explicitly for high-risk or regulated surfaces.

**Scores:** Completeness: 4, Legal Enforceability: 4, Friction Factor: 5

**Recommendation:**  
Add a closing sentence to **§8**:

> “Where a surface is regulated, high-risk, or otherwise subject to stricter review, policy or the review target **SHALL** define additional acceptance criteria beyond the baseline checks in **§8.1**–**§8.5**.”

---

### 9. Approval rule

**Feedback:**  
This section is stronger than Round 1 because §9.4 now provides a real remediation path. That recommendation was accepted and properly incorporated. However, the approval-state taxonomy remains incomplete. The document still does not require `human_approval_status` to distinguish full approval, partial approval, blocked approval, and exception-based approval. That omission weakens audit coherence with §11.

**Scores:** Legal Enforceability: 4, Practical Operability: 4, Developer Synchrony: 3

**Recommendation:**  
Add explicit approval-state taxonomy.

Proposed edits:

- Add to **§9.1**:  
  “`human_approval_status` **SHALL** distinguish at minimum full approval, partial approval, blocked, and exception-based approval where those states are used.”

- Add to **§9.3**:  
  “A partial approval record **SHALL** identify the approved surfaces, excluded surfaces, and any actions that remain blocked.”

---

### 10. Exceptions

**Feedback:**  
This section remains one of the clearest parts of the document, especially §10.3. The “absence of evidence is not an exception” language is strong and should stay. The unresolved issue is boundedness: the exception record still does not say whether an exception is one-time or reusable, what exact requirement it waives, or how long it remains valid. That was a Round 1 recommendation that was not yet accepted.

**Scores:** Legal Enforceability: 3, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
Expand **§10.2** and add an authority clause.

Proposed text:

- Add to **§10.2**:  
  “The exception record **SHALL** also state whether the exception is one-time or reusable, the surfaces and release path it covers, the time window for which it is valid, and whether it waives proof capture, timing, or another specific requirement.”

- Add new **§10.4**:  
  “Exception authority **SHALL** be defined by policy. In the absence of such policy, no exception may be granted.”

---

### 11. Audit posture / 11.1 Implementation seam

**Feedback:**  
This is one of the most improved sections in the revision. §11.1 directly addresses the Round 1 concern that audit fields could otherwise become orphaned doctrine. I agree that this is a meaningful fix. Still, the field table itself remains slightly weak because `artifact_version` still says “where possible,” which is too soft for a normative audit field. The section also still lacks an explicit retention and linkage requirement.

**Scores:** Developer Synchrony: 4, Legal Enforceability: 4, Completeness: 4

**Recommendation:**  
Tighten the field definition and add preservation language.

Proposed edits:

- In **§11** table, replace:  
  “`artifact_version` | Version or commit identity where possible”  
  with:  
  “`artifact_version` | Version, build, commit, or equivalent release identity for the reviewed artifact”

- Add after the table:  
  “The audit record **SHALL** be preserved in a traceable location linked to the review target and approval packet. If a precise artifact identity is unavailable, the record **SHALL** state the reason.”

---

### 12. Relationship to other addenda / 12.4 Addendum precedence

**Feedback:**  
§12.4 is a strong Round 2 fix and directly resolves a real coherence problem from Round 1. I agree with the revision and consider it successful. The remaining issue is citation precision: §§12.1–12.3 still refer to sibling addenda only at document level, even though the relevant sections are known. This is an editorial issue more than a substantive one, but it matters because this document is explicitly about cross-document seams.

**Scores:** Cross-Document Consistency: 4, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
Add section-specific citations.

Example replacement for **§12.3**:

> “*Composition Control Plane for Messages, Invites, and Documents* (**AMD-2026-008-ADD-003**) governs composition contract (**§5**), professional-use disclosure (**§9.4**), knowledge-basis gating (**§18**), originality and source-boundary verification (**§19**), and reference-guided composition (**§20**). This addendum governs the browser-visible review phase used to verify that those controls render clearly on governed surfaces when visual proof is required.”

Apply similar specificity to **§12.1** and **§12.2**.

---

### 13. Non-goals / 14. Recommended artifacts / 15. Decision rule / 16. Informative external reference

**Feedback:**  
These closing sections are generally strong. §15 remains especially clear and preserves the right separation between proof, approval, and release. §16 remains properly quarantined and consistent with AMD-2026-011 and AIOS-SPEC-013. The only notable issue is that §14 still leaves the default artifact posture too soft, which ties back to the unresolved §6 issue. Also, “ratify code by itself” in §13 is slightly colloquial compared with the rest of the set.

**Scores:** Style & Clarity: 4, Practical Operability: 4, Cross-Document Consistency: 4

**Recommendation:**  
Make two small edits:

- In **§13**, replace:  
  “ratify code by itself”  
  with:  
  “treat code implementation alone as sufficient approval evidence”

- In **§14**, add:  
  “Unless policy registers an alternative governed implementation home under **§6.1**, `REVIEW_TARGET.yaml` **SHALL** serve as the default machine-readable review-target artifact for conformance claims under this addendum.”

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §6.1, §14 | Canonical implementation home is still deferred rather than closed | Require policy to register a canonical schema and make `REVIEW_TARGET.yaml` the default conformance artifact unless an alternative governed home is registered | Critical | 3, 7, 9 |
| 2 | §9, §10, §11 | Approval-state and exception records remain under-specified | Define minimum approval-state taxonomy and require exception scope, validity window, waiver type, and authority | High | 3, 5, 7, 9 |
| 3 | §12.1–§12.3, §2.1, §0 | Cross-reference discipline is improved but still too general | Replace shorthand and path-only references with full titles and section-specific citations to sibling addenda and related specs | High | 1, 6, 8 |
| 4 | §3.2–§3.3 | Hybrid backend-to-UI cases remain implicit | Add explicit rule that backend, policy, or adapter changes that alter rendered behavior are UI-affecting for this addendum | High | 4, 5, 7 |
| 5 | §11 | Audit field language and retention remain slightly soft | Replace “where possible” artifact identity language and require traceable preservation linked to review target and approval packet | Medium | 3, 5, 9 |
| 6 | §4 | “Policy” authority remains undefined for this addendum | Define policy as a governed platform or tenant artifact and prohibit ad hoc team practice from substituting for policy | Medium | 1, 3, 7 |
| 7 | §2, §0.2 and emphasized prose throughout | Heavy bolding and slogan-like phrasing reduce editorial clarity | Remove over-emphasis, replace rhetorical lines with enforceable prose, and normalize readability across the draft | Medium | 8 |
| 8 | §7.2–§7.3 | Evidence-category boundaries could still be sharper | Define “rendered browser exports” and state that insufficient items may still be supporting evidence but not sufficient evidence alone | Low | 5, 7, 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The Round 1 revision materially improved the document and resolved the most serious coherence issues, especially around non-browser equivalence, implementation seam, and addendum precedence. The draft now clears the threshold for approval with changes, but it still needs one more tightening pass on canonical implementation home, approval/exception taxonomy, and citation discipline before it reads as fully mature binding text.

**Top 3 Actions Required:**
1. Close the conformance path by making `REVIEW_TARGET.yaml` the default review-target artifact unless policy registers an alternative governed schema home.
2. Define explicit approval-state and exception-record taxonomy so audit and review teams can distinguish full, partial, blocked, and exception-based approval consistently.
3. Replace shorthand and path-only cross-references with full document titles and section-specific citations, and remove over-bolded prose that reduces clarity.
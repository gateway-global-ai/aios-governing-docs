---
review_id: REV-AMD-2026-008-ADD-004-002
document_reviewed: amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md
document_version: 0.4.0
reviewer: OpenAI
review_date: 2026-04-09
review_round: 3
review_type: editorial
disposition: approved_with_changes
composite_score: 4.2
---

# Peer Review: AMD-2026-008-ADD-004 — Pre-Human Browser Review and Visual Proof Gate

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Round 2 findings were materially addressed through §0.1, §4.1, §6.1, §9–§11, and §14, but several cross-references still rely on shorthand or path-only citation rather than full title-and-section discipline. |
| 2 | Business Model Alignment | 4 | §2.1 now properly acknowledges MPOA context and §4.1 allows proportionality, but the document still leaves tier-sensitive review depth mostly to policy rather than stating a clearer default posture. |
| 3 | Legal Enforceability | 4 | The non-waivable proof floor, exception authority, and approval taxonomy substantially improve enforceability, though a few clauses still defer too much to policy without section-level authority mapping. |
| 4 | Architectural Fidelity | 4 | The addendum preserves the separation between planning, execution, browser proof, and approval, but it still stops short of explicitly tying proof categories to governed surfaces and execution truth defined in AIOS-SPEC-006 and AIOS-SPEC-009. |
| 5 | Completeness | 4 | The document now covers the major Round 2 gaps, including policy authority, default conformance home, and approval/exception taxonomy, but hybrid backend-to-UI cases and retention specifics remain slightly underdefined. |
| 6 | Conflict Freedom | 5 | No direct contradiction appears with the bundled governing set, and §12.4 continues to provide a strong precedence rule for ratified-versus-draft addenda. |
| 7 | Practical Operability | 4 | The review-target, evidence, approval, exception, and audit model is now operationally usable, though some implementation details still depend on future policy or operations registration. |
| 8 | Style & Clarity | 4 | The draft is clearer and tighter than v0.3.0, but over-bolded prose, shorthand sibling references, and a few slogan-like lines still reduce editorial polish. |
| 9 | Developer Synchrony | 4 | §6.1 and §11.1 now create a workable conformance seam with a default artifact, but the document still does not name a default audit operations artifact or retention schema. |
| 10 | Platform Economics Synchrony | 4 | The MPOA pointer and proportionality language improve economic coherence, though the document still does not say much about evidence-capture burden or entitlement-sensitive tooling beyond policy deferral. |
| 11 | Friction Factor | 5 | The gate remains narrowly scoped, fail-closed where needed, and proportionate enough to avoid unnecessary bureaucracy while preserving approval integrity. |
| | **Composite Score** | **4.2** | |

---

## Overall Assessment

### Strengths

- **Round 2’s most important findings were actually addressed.** The revision log is credible: §0.1 now defines policy authority; §4.1 adds a non-waivable minimum proof floor; §6.1 and §14 establish a default conformance artifact; and §§9–11 now provide a real approval, exception, and audit taxonomy.
- **The document is now materially more enforceable.** Compared with v0.3.0, the combination of §4.1, §9.1–§9.4, §10.1–§10.4, and §11 closes the biggest loopholes around silent waiver, ambiguous approval state, and orphaned exception handling.
- **The implementation seam is much better.** §6.1 plus §11.1 now gives engineering teams a plausible baseline for conformance claims instead of doctrine with no default artifact.
- **The addendum still respects architectural boundaries.** §5, §12, and §15 correctly preserve the distinction between browser review, human approval, and later promotion / merge / release / ratification.
- **Conflict handling remains strong.** §12.4 is still one of the best sections in the document and continues to resolve a real cross-addendum ambiguity cleanly.

### Critical Gaps

- **Cross-reference discipline is still not fully style-guide clean.** §0, §2.1, and §12 still use shorthand or file-path citation where the broader document set expects exact title-and-section citation discipline.
- **A few editorial formulations remain more rhetorical than normative.** In particular, §2’s “A rendered interface is part of system truth” still reads as a slogan rather than a binding rule.
- **Hybrid backend-to-UI scope remains implicit.** §3.2 still excludes “backend-only changes with no UI effect,” but the document would be stronger if it expressly stated that backend, policy, or adapter changes that alter rendered behavior are in scope.
- **Audit retention remains underbound.** §11.1 requires a system home, but it still does not establish a default retention or preservation rule if policy has not yet named one.

---

## Article-by-Article Review

### 0. Status and intent / 0.1 Definitions / 0.2 Revision posture

**Feedback:**  
This opening is improved from v0.3.0, especially because §0.1 now defines **Policy** in a way that directly answers a major Round 2 concern from Gemini and OpenAI. That fix is real and successful. The revision posture in §0.2 also accurately reflects the document’s status and does not overclaim readiness. However, the section still has two editorial weaknesses. First, the “Does not replace” row still uses shorthand sibling labels rather than the full addendum titles used elsewhere in the governance set. Second, §0.1 still opens with “The following terms SHALL be read consistently with AMD-2026-005 peer-review thresholds where applicable,” which is the same weak dependency previously flagged in Round 2. That sentence still does not add clarity and still cites a document not bundled here by section.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 4, Conflict Freedom: 5

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
  “The following terms apply in this addendum. Separate peer-review scoring and ratification thresholds remain governed by their own controlling documents.”

---

### 1. Purpose

**Feedback:**  
Section 1 remains clear, bounded, and well-structured. It states the problem and the purpose of the gate without overreaching into implementation detail. The numbered list aligns well with later sections. No substantive issue remains here.

**Scores:** Completeness: 4, Style & Clarity: 5

**Recommendation:**  
Optional refinement only: add section pointers to the numbered list for tighter internal navigation, for example “when browser review is required (§4), what evidence counts (§7), and how this phase interacts with planning and approval (§5, §9–§10).”

---

### 2. Governing principle / 2.1 Cross-context pointers

**Feedback:**  
This section is stronger than in v0.3.0 because the cross-context table now clearly anchors the addendum to AIOS-SPEC-009, AIOS-SPEC-006, and MPOA. That addresses a real Round 2 concern. However, the core sentence “A rendered interface is part of system truth” still remains from the prior draft and still reads more like a doctrine slogan than a governance rule. Also, §2.1 still cites by file path rather than by exact document title plus relevant section. Since this document’s purpose is cross-document coherence, that remains an editorial gap.

**Scores:** Cross-Document Consistency: 4, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:**  
Replace the slogan sentence with enforceable prose and tighten the citations.

Proposed edits:

- In **§2**, replace:  
  “A rendered interface is part of system truth.”  
  with:  
  “For UI-affecting work within scope, rendered interface state **SHALL** be treated as approval-relevant evidence, not merely as an implementation detail.”

- In **§2.1**, replace path-style references with title-led references, for example:  
  “*Intent Primitive and Execution Model* (**AIOS-SPEC-009**) — intent, execution, and primary-surface truth relevant to what must be visibly proven before approval.”  
  “*UI Component Registry Standard* (**AIOS-SPEC-006**) — governed surfaces, transparency expectations, and registry discipline relevant to UI evidence.”  
  “*Gateway Global AIOS Master Platform Operating Agreement* (**MPOA**) — tier, liability, and economics context for proportional review depth where policy binds cost to review scope.”

---

### 3. Scope

**Feedback:**  
The scope section is generally sound and the addition of §3.4 in the prior revision remains a strong fix. However, one Round 2 concern remains only partially addressed: the document still does not explicitly say that backend, policy, or adapter changes that alter rendered disclosures, blocked states, or visible workflow behavior are in scope. That rule is still only inferable, not stated.

**Scores:** Completeness: 4, Practical Operability: 4, Architectural Fidelity: 4

**Recommendation:**  
Add an explicit hybrid-case clarifier.

Proposed text for a new **§3.2.1**:

> “A change that originates in backend, policy, adapter, or control-plane logic but alters rendered disclosures, visible state, blocked actions, or user-facing workflow behavior **SHALL** be treated as UI-affecting for purposes of this addendum.”

Also consider expanding **§3.3**:

> “Any policy extension under this section **SHALL** identify the approving authority, affected surfaces, and minimum proof class with audit visibility.”

---

### 4. Trigger conditions / 4.1 Policy proportionality

**Feedback:**  
This is one of the most improved sections in the document. The non-waivable minimum floor directly addresses the strongest Round 2 criticism from Gemini and OpenAI, and the fix is substantive, not cosmetic. I agree that this recommendation was properly accepted and implemented. The remaining issue is minor: the document now defines **Policy** in §0.1, but §4 could still benefit from a short reminder that only governed policy may shape proportionality.

**Scores:** Legal Enforceability: 5, Practical Operability: 4, Business Model Alignment: 4

**Recommendation:**  
Add a short authority reminder at the start of **§4.1**:

> “Only a valid **Policy** as defined in **§0.1** may shape proportionality under this section.”

That would prevent readers from treating local team practice as sufficient to narrow proof requirements.

---

### 5. Phase placement

**Feedback:**  
This section remains structurally sound and coherent with AIOS-AMD-PLAN-001. The sequence is clear and preserves the intended separation between planning, execution, browser proof, and approval. The only remaining gap is traceability: §5.3 still does not explicitly require artifact-version and environment traceability for the bounded execution path used to generate evidence.

**Scores:** Cross-Document Consistency: 4, Developer Synchrony: 4, Practical Operability: 4

**Recommendation:**  
Strengthen **§5.3** with a traceability sentence:

> “Any bounded local or isolated execution path used for capture **SHALL** identify the artifact version, environment, and review target it serves.”

---

### 6. Review target contract

**Feedback:**  
This section is materially better than in v0.3.0. The default `REVIEW_TARGET.yaml` rule directly addresses the prior concern that conformance claims lacked a default machine-readable home. That recommendation was properly accepted. The remaining editorial issue is that §6.2 still allows “marked not applicable with reason” without explicitly requiring authority where policy requires approval for that disposition.

**Scores:** Developer Synchrony: 4, Legal Enforceability: 4, Practical Operability: 5

**Recommendation:**  
Add a bounded disposition rule to **§6.2**:

> “A ‘not applicable’ disposition **SHALL** identify the specific proof, the reason, and the approving authority where policy requires approval for that disposition.”

---

### 7. Minimum browser evidence

**Feedback:**  
This section remains operationally strong. The test-captured proof rule is much better than earlier versions and now reads as implementable. However, one editorial point remains: “rendered browser exports” is still undefined, and §7.3 would be clearer if it explicitly said insufficient items may still be supporting evidence.

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
This section is clear and useful. It still uses some qualitative language such as “labels and action semantics are clear” and “failure and fallback states are understandable,” but that is acceptable at addendum level. The document would be slightly stronger if it explicitly allowed stricter criteria for regulated or high-risk surfaces.

**Scores:** Completeness: 4, Legal Enforceability: 4, Friction Factor: 5

**Recommendation:**  
Add a closing sentence to **§8**:

> “Where a surface is regulated, high-risk, or otherwise subject to stricter review, policy or the review target **SHALL** define additional acceptance criteria beyond the baseline checks in **§8.1**–**§8.5**.”

---

### 9. Approval rule

**Feedback:**  
This section is substantially improved. The explicit `human_approval_status` taxonomy directly addresses a major Round 2 gap and is one of the most important successful revisions in v0.4.0. §9.2 and §9.3 now make blocked and partial approval auditable in a way they were not before. The only remaining issue is that “policy-approved equivalent” is acceptable, but the document could more clearly require semantic equivalence rather than mere naming flexibility.

**Scores:** Legal Enforceability: 4, Practical Operability: 5, Developer Synchrony: 4

**Recommendation:**  
Tighten the equivalence language in **§9.1**:

> “The approval record **SHALL** preserve `human_approval_status` as `approved`, `partially_approved`, `blocked`, or `approved_by_exception`, or a policy-approved equivalent that preserves the same semantic distinctions and audit meaning.”

---

### 10. Exceptions

**Feedback:**  
This section is now much stronger than in v0.3.0. The addition of bounded exception scope, validity window, waived requirement, and authority in §10.2 and §10.4 directly addresses prior review concerns. I agree that these changes were properly accepted and implemented. No major substantive gap remains here.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 5, Style & Clarity: 4

**Recommendation:**  
Minor editorial cleanup only: in **§10.2**, convert the mixed bullet punctuation into a uniform list style for readability.

---

### 11. Audit posture / 11.1 Implementation seam

**Feedback:**  
This section is improved and now operationally credible. The audit field set is clearer, and the traceable-location requirement is a real improvement. However, one residual gap remains: §11.1 requires policy or an operations document to define storage, query, and retention, but the addendum still does not establish a fallback preservation rule if policy has not yet named one. That is not fatal, but it keeps the section just short of exemplary.

**Scores:** Developer Synchrony: 4, Legal Enforceability: 4, Completeness: 4

**Recommendation:**  
Add a default preservation fallback to **§11.1**:

> “Until policy or a referenced operations document defines a stricter retention rule, browser review records **SHALL** be preserved at least through the approval decision and any immediately related promotion, merge, release, or ratification action they support.”

That would give the section a minimum operational floor without overcommitting to a long-term retention schedule.

---

### 12. Relationship to other addenda / 12.4 Addendum precedence

**Feedback:**  
§12.4 remains strong and conflict-resolving. The main remaining issue is editorial: §§12.1–12.3 still refer to sibling addenda only at document level, even though the relevant sections are known and materially relied upon. This is a cross-document coherence issue more than a substantive one.

**Scores:** Cross-Document Consistency: 4, Conflict Freedom: 5, Style & Clarity: 4

**Recommendation:**  
Add section-specific citations.

For example, replace **§12.3** with:

> “*Composition Control Plane for Messages, Invites, and Documents* (**AMD-2026-008-ADD-003**) governs composition contract (**§5**), professional-use disclosure (**§9.4**), knowledge-basis gating (**§18**), originality and source-boundary verification (**§19**), and reference-guided composition (**§20**). This addendum governs the browser-visible review phase used to verify that those controls render clearly on governed surfaces when visual proof is required.”

Apply similar specificity to **§12.1** and **§12.2**.

---

### 13. Non-goals / 14. Recommended artifacts / 15. Decision rule / 16. Informative external reference

**Feedback:**  
These closing sections are generally strong. §14 now properly aligns with §6.1 and successfully incorporates the default conformance artifact rule. §15 remains clear and preserves the right separation between proof, approval, and later lifecycle stages. §16 remains appropriately quarantined and consistent with AMD-2026-011 and AIOS-SPEC-013. The only remaining editorial issue is that “ratify code by itself” in §13 is slightly colloquial for this document set.

**Scores:** Style & Clarity: 4, Practical Operability: 4, Cross-Document Consistency: 4

**Recommendation:**  
In **§13**, replace:

> “ratify code by itself,”

with:

> “treat code implementation alone as sufficient approval evidence,”

for better style-guide alignment.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §0, §0.1, §12 | Cross-reference discipline still uses shorthand and a weak AMD-2026-005 dependency | Replace shorthand sibling references with full titles and remove the AMD-2026-005 threshold sentence from §0.1 | High | 1, 8 |
| 2 | §2 | One core sentence remains rhetorical rather than normative | Replace “A rendered interface is part of system truth” with enforceable approval-evidence language | High | 3, 8 |
| 3 | §3 | Hybrid backend-to-UI cases remain implicit | Add an explicit rule that backend, policy, adapter, or control-plane changes that alter rendered behavior are UI-affecting | High | 4, 5, 7 |
| 4 | §11.1 | Audit retention still lacks a fallback floor | Add a minimum preservation rule until policy or operations artifacts define stricter retention | Medium | 3, 5, 7, 9 |
| 5 | §6.2 | “Not applicable” proof disposition is still slightly underbound | Require the specific proof, reason, and approving authority where policy requires approval | Medium | 3, 7, 9 |
| 6 | §7.2–§7.3 | Evidence-category boundaries could still be sharper | Define “rendered browser exports” and state that insufficient items may still be supporting evidence but not sufficient evidence alone | Medium | 5, 7, 8 |
| 7 | §12.1–§12.3 | Sibling addenda references remain too general | Add section-specific citations to ADD-001, ADD-002, and ADD-003 | Medium | 1, 6, 8 |
| 8 | §13 | One phrase is slightly colloquial for governance prose | Replace “ratify code by itself” with more precise approval-evidence language | Low | 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document has materially improved since Round 2 and now clears the approval-with-changes threshold comfortably. The most important prior findings were addressed successfully, and the remaining issues are primarily editorial-tightening and minor operability clarifications rather than structural defects.

**Top 3 Actions Required:**
1. Replace shorthand and weak cross-reference language in §0, §2.1, and §12 with full title-and-section citation discipline.
2. Add an explicit hybrid-case rule in §3 stating that backend, policy, or adapter changes that alter rendered behavior are UI-affecting.
3. Add a fallback preservation rule in §11.1 so audit retention has a minimum floor before policy or operations artifacts define stricter handling.
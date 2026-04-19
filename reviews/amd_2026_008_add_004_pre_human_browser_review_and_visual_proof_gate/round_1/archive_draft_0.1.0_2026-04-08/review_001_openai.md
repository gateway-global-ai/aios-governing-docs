---
review_id: REV-AMD-2026-008-ADD-004-001
document_reviewed: amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md
document_version: 0.1.0
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
| 1 | Cross-Document Consistency | 3 | The addendum is directionally aligned with AMD-2026-008 and the ADD-001/002/003 seam model, but many cross-references omit section-level citations required by the style guide and several terms are introduced without anchoring to existing governance vocabulary. |
| 2 | Business Model Alignment | 3 | The document does not conflict with commercial posture, but it leaves unclear whether browser-review obligations apply uniformly across founder, internal, tenant, and premium-gated contexts. |
| 3 | Legal Enforceability | 3 | Core obligations are stated in mandatory language, but several operative terms such as “browser-visible evidence,” “current,” “unrelated environment,” and “actual review target” remain too open-textured for strong enforcement. |
| 4 | Architectural Fidelity | 4 | The document generally respects the AIOS separation between shell governance, approval gates, and downstream promotion, and it does not improperly collapse browser proof into release authority. |
| 5 | Completeness | 3 | The doctrine covers trigger, evidence, approval, exceptions, and audit posture, but it omits a more precise state model, failure handling, and implementation handoff comparable to ADD-003’s stronger control-plane discipline. |
| 6 | Conflict Freedom | 4 | No direct contradiction appears with AMD-2026-008, AMD-2026-011, AIOS-SPEC-013, or the other addenda, though some overlap tension exists with AIOS-AMD-PLAN-001 phase language. |
| 7 | Practical Operability | 3 | A reviewer can understand the intended process, but the document lacks enough specificity on artifact schemas, evidence freshness, approval states, and policy precedence to support consistent implementation. |
| 8 | Style & Clarity | 4 | The prose is readable and mostly disciplined, but it is more memo-like than the tighter normative style used in ADD-003 and needs sharper definitions and section-level precision. |
| 9 | Developer Synchrony | 2 | The document does not provide a concrete implementation seam, schema home, or DCP/state-transition handoff, making it hard for product and governance teams to build the same thing. |
| 10 | Platform Economics Synchrony | 3 | The addendum preserves separation between approval and promotion, but it does not clearly state whether the browser-review gate is pre-production only, tenant-triggered, or universally required regardless of cost and environment. |
| 11 | Friction Factor | 2 | The default-fail-closed posture is sensible, but without bounded exceptions, proof minimization rules, or proportionality by risk class, the gate could create heavy operational drag. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- Sections 1, 2, and 15 clearly articulate the central doctrine: browser-visible proof is a precondition to human approval for UI-affecting work when visual proof is required.
- Sections 5 and 9 correctly preserve the governance distinction between browser review, human approval, and later promotion / merge / release / ratification, which is consistent with AMD-2026-008 Section 4 and ADD-003 Section 12.
- Section 16 appropriately treats the external repository as quarantine-only and avoids accidental incorporation of third-party tooling, aligning with AMD-2026-011 Section 2.2 and AIOS-SPEC-013 Sections 2 and 8.
- Sections 7 and 8 provide a useful minimum evidence taxonomy that is understandable to both reviewers and implementers.

### Critical Gaps

- The document lacks section-specific cross-references to the governing documents it relies on, especially AMD-2026-008, AIOS-AMD-PLAN-001, AMD-2026-011, and AIOS-SPEC-013; this weakens cross-document coherence and enforceability.
- Section 6 defines a review target contract, but the document never states where the normative schema, state machine, or transport binding lives; compared with ADD-003 Section 19.10, this is a major developer-synchrony gap.
- Sections 4, 7, 8, and 9 use important but undefined terms such as “current,” “stale,” “equivalent visual evidence,” “actual review target,” and “where applicable,” which leaves too much discretion for a binding gate.
- The document does not clearly distinguish mandatory browser review for all UI-affecting work from browser review only when a review target or policy requires visual proof; that ambiguity appears in Sections 2, 4, 7, and 15.
- The gate is not sufficiently risk-tiered; as drafted, it may impose the same burden on minor label changes and high-stakes approval surfaces.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section is serviceable but under-cited. The “Does not replace” row correctly positions the addendum against ADD-001, ADD-002, and ADD-003, but it should cite the specific sections or axes it leaves untouched. The “Planning alignment” row references the planning lifecycle conceptually, yet does not identify the exact phase mapping in AIOS-AMD-PLAN-001. Because this addendum is fundamentally about inserting a governed phase into an existing lifecycle, the lack of section-level anchoring is a coherence weakness.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 4, Conflict Freedom: 4

**Recommendation:**  
Revise the table to include section-level anchors. Proposed text change in Section 0, “Does not replace” row:

> **Does not replace** | **ADD-001** Section 3–5 (navigation classes and shell obligations), **ADD-002** Sections 4, 5, 7, and 10 (depth, voice controls, packaging, BOOK workflow), and **ADD-003** Sections 5, 9.4, 12, and 18–20 (composition controls, disclosure, action semantics, grounding, originality, references). This addendum governs **review evidence**, **browser-visible proof**, and **approval prerequisites** for UI-affecting changes.

And in “Planning alignment”:

> **Planning alignment** | This addendum codifies a pre-human browser review phase adjacent to **AIOS-AMD-PLAN-001** Phase F and any bounded execution lane adopted by policy; it defines minimum evidence required before human approval of UI-affecting work is complete.

---

### 1. Purpose

**Feedback:**  
The purpose is clear and well framed. However, the phrase “the system SHALL produce browser-visible evidence” is too broad without identifying whether the obligation falls on the shell, the review workflow, CI tooling, or a human operator. The list of prohibited substitutes is useful, but the section would benefit from a tighter statement of actor responsibility and applicability threshold.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Style & Clarity: 4

**Recommendation:**  
Add an actor-neutral but enforceable responsibility clause. Proposed insertion at end of Section 1:

> The governed review workflow **SHALL** ensure that browser-visible evidence is captured, linked to the review target, and available to the human approver before approval is recorded as complete.

---

### 2. Governing principle

**Feedback:**  
This is the doctrinal core and is mostly strong. The problem is the phrase “when policy or review target requires visual proof,” which narrows the rule, while later sections sometimes read as if all UI-affecting work requires browser review by default. That ambiguity should be resolved here, because the rest of the document depends on it. Also, “A rendered interface is part of system truth” is rhetorically effective but slightly less precise than the surrounding governance style.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 3, Style & Clarity: 4

**Recommendation:**  
Tighten the rule and remove ambiguity. Proposed replacement for the first sentence of Section 2:

> For UI-affecting work within Section 3, **browser review SHALL be required before human approval** when Section 4 trigger conditions are met; absent a recorded policy exception under Section 10, textual plans, code assertions, or agent claims **SHALL NOT** substitute for browser-visible proof.

Optional replacement for “A rendered interface is part of system truth”:

> For governed UI work, rendered browser state is part of the evidentiary record.

---

### 3. Scope

**Feedback:**  
The scope is sensible and readable. The main issue is that “UI behavior whose absence or misrender would materially change user understanding or trust” is broad and subjective. That may be acceptable as a catch-all, but it should be tied to policy classification or review-target declaration. Section 3.2 is appropriately bounded. Section 3.3 is fine but minimal.

**Scores:** Completeness: 3, Legal Enforceability: 3, Friction Factor: 2

**Recommendation:**  
Narrow the catch-all in Section 3.1. Proposed replacement for the final bullet:

> user-visible behavior that policy classifies as material to user understanding, approval posture, disclosure, or trust

Also add to Section 3.3:

> Policy **SHALL** define any additional in-scope classes with audit-visible criteria rather than ad hoc reviewer discretion.

---

### 4. Trigger conditions

**Feedback:**  
This section is important and mostly well structured. The ambiguity lies in the interaction between item 1 (“review target declares `required_visual_proofs`”) and items 2–6, which independently trigger browser review. If item 2 alone is enough, then the phrase in Section 2 limiting the rule to cases where policy or review target requires visual proof is misleading. The default posture is appropriately fail-closed, but “explicit policy exception recorded with audit visibility” should point to Section 10.

**Scores:** Cross-Document Consistency: 3, Practical Operability: 3, Friction Factor: 2

**Recommendation:**  
Clarify precedence and trigger logic. Proposed replacement for the lead sentence of Section 4:

> Browser review **SHALL** be required before human approval when any trigger below is met, whether by review-target declaration, policy classification, or the nature of the UI-affecting change itself.

Add final sentence:

> Any exception to a triggered browser-review requirement **SHALL** comply with Section 10.

---

### 5. Phase placement

**Feedback:**  
The sequencing is helpful and aligns conceptually with AIOS-AMD-PLAN-001, but the relationship is not fully coherent. AIOS-AMD-PLAN-001 Phase F is “Peer review (binding),” whereas this addendum inserts browser review before human approval for UI-affecting work. The document should say whether this gate belongs inside execution evidence gathering, inside committee review, or as a prerequisite to a human review packet. As written, “bounded execution or implementation preparation” is too vague.

**Scores:** Cross-Document Consistency: 3, Developer Synchrony: 2, Practical Operability: 3

**Recommendation:**  
Replace step 5 with more precise language and tie it to review artifacts. Proposed revised sequence in Section 5.1:

1. doctrine / requirements  
2. architect planning  
3. UI planning  
4. committee packet or approved planning baseline  
5. bounded implementation or execution sufficient to render the governed surface  
6. browser-visible review evidence and capture packet  
7. human approval  
8. promotion / merge / release / ratification as applicable

Add sentence:

> This addendum governs the evidentiary gate between implementation-ready work and human approval; it does not replace binding peer review under **AIOS-AMD-PLAN-001**.

---

### 6. Review target contract

**Feedback:**  
This is one of the strongest sections conceptually, but it is underdeveloped operationally. The table defines useful fields, yet there is no statement about whether these are conceptual fields only, whether policy may rename them, or where the normative schema lives. In this document set, ADD-003 repeatedly solves this problem by distinguishing doctrine from implementation home. ADD-004 should do the same.

**Scores:** Developer Synchrony: 2, Practical Operability: 3, Completeness: 3

**Recommendation:**  
Add a schema-handoff clause. Proposed insertion after Section 6.1:

> Products **MAY** map these conceptual fields to implementation identifiers, but policy **SHALL** register the governing schema, file shape, or equivalent machine-readable contract used for review targets and approval packets. This addendum defines minimum governed fields; implementation-specific serialization **SHALL NOT** be left undocumented.

And revise Section 6.2 to read:

> A review target **SHALL NOT** be considered satisfied unless each required proof is captured, marked not applicable with recorded reason, or placed in an explicit blocked state with failure reason.

---

### 7. Minimum browser evidence

**Feedback:**  
The evidence taxonomy is good, but “review packet pointer” and “stable link or file reference” need more precision. Section 7.2 is too permissive because “equivalent visual evidence allowed by policy” could swallow the rule. Section 7.3 is strong and should remain.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Style & Clarity: 4

**Recommendation:**  
Constrain the open-ended evidence language. Proposed replacement for the last bullet in Section 7.2:

> other policy-approved visual evidence that preserves review-target identity, capture date, and human-reviewability

Add to Section 7.1 item 6:

> **review packet pointer** — a stable file path, artifact identifier, or governed link tying the evidence to the review target and review run

---

### 8. Required checks

**Feedback:**  
This section is useful but reads as a checklist memo rather than a binding control taxonomy. The repeated phrase “where applicable” is implied but not operationalized. It would help to state that policy or the review target must specify which categories are mandatory for a given review. Also, Section 8.4 references “recovery / restart / continue / choose states,” which is a good seam to ADD-001, but it should cite that addendum explicitly.

**Scores:** Cross-Document Consistency: 3, Practical Operability: 3, Style & Clarity: 4

**Recommendation:**  
Add a governing sentence before Section 8.1:

> The review target or governing policy **SHALL** specify which of the following check categories are mandatory for the work item; omission **SHALL** be explicit rather than assumed.

Revise Section 8.4 second bullet to:

> recovery / restart / continue / choose states governed by **AMD-2026-008-ADD-001** render and behave correctly where in scope

---

### 9. Approval rule

**Feedback:**  
This section is central and mostly sound. The blocked states are helpful, but the document never says whether these are conceptual states or required literal identifiers. Also, “contradictory” proof should be defined more concretely, perhaps as evidence inconsistent with the review target, current build, or claimed approval scope.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Developer Synchrony: 2

**Recommendation:**  
Add a conceptual-state clarification and tighten “contradictory.” Proposed insertion after Section 9.2:

> The blocked states above are minimum conceptual meanings; products **MAY** map them to implementation-specific identifiers if audit surfaces preserve equivalent meaning.

Proposed replacement in Section 9.2 lead sentence:

> If required visual proof is missing, stale relative to the review run, or materially inconsistent with the review target or approval scope, the approval state **SHALL** be one of:

---

### 10. Exceptions

**Feedback:**  
This section is necessary and generally good. However, it should define who may authorize an exception by policy role, not just “who authorized the exception.” Without that, exception handling is too discretionary. It also should state that exceptions do not convert missing proof into proof; they only narrow approval scope or accept risk.

**Scores:** Legal Enforceability: 3, Conflict Freedom: 4, Friction Factor: 3

**Recommendation:**  
Add a role-bound authorization clause. Proposed insertion after Section 10.1:

> Policy **SHALL** define which actor or governance role may authorize an exception; exception authority **SHALL NOT** be implied by ordinary reviewer access alone.

Add to Section 10.2:

> An exception record **SHALL NOT** be treated as substitute proof; it records accepted deviation, residual risk, and bounded approval scope only.

---

### 11. Audit posture

**Feedback:**  
This section is useful but incomplete relative to the rest of the document set. “review_date” is too weak if evidence freshness matters; a timestamp or review-run identifier would be better. “artifact_version” says “where possible,” which is a weasel phrase in a normative table. If version identity is genuinely optional, the condition should be explicit.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Style & Clarity: 3

**Recommendation:**  
Tighten the table. Proposed replacements:

- `review_date` → `review_timestamp` | Date/time of review or review run
- `artifact_version` → `artifact_version_or_commit` | Version, commit, build id, or equivalent identity for the reviewed artifact

Add sentence after table:

> If no version, commit, or build identity is available, the audit record **SHALL** state the reason explicitly; absence **SHALL NOT** be silent.

---

### 12. Relationship to other addenda

**Feedback:**  
This section is directionally correct but too high-level for a document whose main risk is seam ambiguity. It should cite specific sections in ADD-001/002/003. The current prose is accurate but not sufficiently precise for cross-document coherence.

**Scores:** Cross-Document Consistency: 3, Conflict Freedom: 4, Style & Clarity: 4

**Recommendation:**  
Revise each subsection to include section-level references. Example replacement for Section 12.2:

> **ADD-002** Sections 4, 5, 7, and 10 govern output depth, shell voice controls, packaging, and BOOK workflow. This addendum governs browser-visible review of those UI-affecting surfaces, disclosures, and gates when Section 4 trigger conditions require visual proof.

Apply similar treatment to Sections 12.1 and 12.3.

---

### 13. Non-goals

**Feedback:**  
This section is concise and appropriate. No major issue beyond style consistency; the list is clear and bounded.

**Scores:** Style & Clarity: 4, Conflict Freedom: 4

**Recommendation:**  
No substantive change required. Optionally add:

> define production-release criteria or supersede promotion controls in parent governance documents

to reinforce the approval/promotion separation.

---

### 14. Recommended artifacts

**Feedback:**  
This section is helpful, but it creates a quasi-standard artifact set without saying whether these are illustrative or expected defaults. Because Section 6 introduces a review target contract and Section 11 introduces audit fields, this section should say whether these artifacts are informative examples or policy defaults.

**Scores:** Practical Operability: 3, Developer Synchrony: 2, Style & Clarity: 4

**Recommendation:**  
Retitle to make status explicit. Proposed heading change:

> ## 14. Recommended artifacts (informative unless policy elevates)

Add sentence:

> These artifact names are illustrative defaults; policy **MAY** require them verbatim or map them to equivalent governed artifacts if the Section 6 and Section 11 content requirements are preserved.

---

### 15. Decision rule

**Feedback:**  
This is a strong summary, but it slightly overstates the trigger by saying “If the work is UI-affecting and the review target requires visual proof,” which again leaves unresolved whether UI-affecting work can independently trigger browser review under Section 4 items 2–6. This section should mirror Section 4 exactly.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 4, Friction Factor: 3

**Recommendation:**  
Replace the lead sentence with:

> If Section 4 triggers browser review for a UI-affecting work item:

This keeps the summary aligned with the operative trigger section.

---

### 16. Informative external reference (quarantine)

**Feedback:**  
This section is prudent and mostly well drafted. The cross-reference style is stronger here than elsewhere because it cites AMD-2026-011 and AIOS-SPEC-013 directly. However, it should cite the relevant sections: AMD-2026-011 Section 2.2 and AIOS-SPEC-013 Sections 2, 8, and 10. Also, the path-based citation to the governed record is acceptable internally, but the document should preserve the registry-style discipline used elsewhere.

**Scores:** Cross-Document Consistency: 4, Conflict Freedom: 4, Architectural Fidelity: 4

**Recommendation:**  
Revise the lead sentence:

> This addendum **does not** incorporate third-party code or establish a runtime dependency. For pattern study only, the following repository is registered under **quarantine** consistent with **AMD-2026-011** Section 2.2 and **AIOS-SPEC-013** Sections 2, 8, and 10.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §§2, 4, 15 | Trigger logic is ambiguous between “policy/review-target required” and broader UI-affecting triggers. | Harmonize the operative rule so Section 2 and Section 15 explicitly defer to Section 4 triggers, and clarify that any listed trigger independently requires browser review absent Section 10 exception. | Critical | 1, 3, 5, 6, 7 |
| 2 | §6 | Review target contract lacks a normative schema/serialization handoff. | Add language stating that conceptual fields may be mapped by product, but policy must register the governing schema or machine-readable contract. | Critical | 5, 7, 9 |
| 3 | §§7, 9, 11 | Key evidentiary terms are too vague for enforcement. | Define or tighten “stale,” “current,” “contradictory,” “stable link,” and version/build identity requirements in the evidence and audit sections. | High | 3, 5, 7, 8 |
| 4 | §§0, 5, 12, 16 | Cross-document references are too general and do not cite section-level authorities. | Add specific section citations to AMD-2026-008, ADD-001, ADD-002, ADD-003, AIOS-AMD-PLAN-001, AMD-2026-011, and AIOS-SPEC-013. | High | 1, 6, 8 |
| 5 | §§4, 8, 10 | Fail-closed posture may create excessive friction without role and scope controls. | Add policy-defined proportionality, mandatory-category selection, and authorized-exception-role language. | High | 7, 10, 11 |
| 6 | §5 | Phase placement is not fully synchronized with AIOS-AMD-PLAN-001. | Clarify that browser review is the evidentiary gate between bounded implementation/execution and human approval, not a replacement for binding peer review. | High | 1, 7, 9 |
| 7 | §14 | Recommended artifacts are presented without clear normative status. | Mark the section as informative unless policy elevates specific artifact names, while preserving required content from Sections 6 and 11. | Medium | 5, 7, 8, 9 |
| 8 | §3 | Scope catch-all is too subjective. | Replace the “materially change user understanding or trust” clause with policy-classified materiality language. | Medium | 3, 7, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has a sound doctrinal core and no obvious direct conflicts, but it is not yet precise enough for binding governance because trigger logic, implementation handoff, and evidentiary definitions remain under-specified. The developer-synchrony and friction risks are substantial enough to require another revision before approval.

**Top 3 Actions Required:**
1. Resolve the trigger ambiguity by making Sections 2, 4, and 15 say the same thing about when browser review is mandatory.
2. Add a normative implementation handoff for the review target contract, approval states, and audit/evidence schema.
3. Tighten definitions and section-level cross-references so the gate is enforceable, auditable, and coherent with the rest of the AMD-2026-008 addendum family.
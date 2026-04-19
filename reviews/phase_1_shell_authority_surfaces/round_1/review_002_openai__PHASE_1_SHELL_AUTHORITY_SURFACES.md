---
review_id: REV-AIOS-SHELL-PHASE1-001
document_reviewed: reviews/aios_shell_governing_document_and_artifact_plan_001/phase_packets_2026-04-10/PHASE_1_SHELL_AUTHORITY_SURFACES.md
document_version: unversioned draft
reviewer: OpenAI
review_date: 2026-04-10
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.1
---

# Peer Review: Phase 1 shell authority surfaces

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The draft is conceptually aligned with the shell governance program, but it does not use the governing set’s required document structure, canonical citation style, or glossary terms consistently enough to be coherent as a governed artifact. |
| 2 | Business Model Alignment | 4 | The document stays within platform-governance scope and does not undermine the Kit marketplace or enterprise positioning. |
| 3 | Legal Enforceability | 2 | Several binding statements rely on informal phrases such as “should,” “must preserve,” and “review should fail” without defining the actor, approval authority, or enforceable mechanism. |
| 4 | Architectural Fidelity | 4 | The draft correctly preserves shell authority as distinct from Workspace execution authority and is consistent with the Technical Manifesto’s separation-of-powers model at a high level. |
| 5 | Completeness | 3 | The draft covers the main shell-authority concerns, but it omits a formal relationship-to-governing-documents section, defined terms, explicit audit fields, and a concrete future identity-bound authority model. |
| 6 | Conflict Freedom | 3 | No direct contradiction appears, but the draft creates tension with the Governance Constitution and MPOA by introducing approval and review gates without specifying which governing body or legal instrument controls them. |
| 7 | Practical Operability | 3 | The tables are useful, but the document does not yet define a stepwise approval flow, evidence standard, or machine-checkable criteria for privileged entry and audit logging. |
| 8 | Style & Clarity | 2 | The prose is readable, but it is not in the mandated governing-document format, uses informal drafting language, and lacks the article/section hierarchy required by the style guide. |
| 9 | Developer Synchrony | 4 | The implementation references are concrete and helpful, and a developer can understand the current runtime seams and intended control points. |
| 10 | Platform Economics Synchrony | 4 | The document does not materially touch pricing or billing and does not conflict with MPOA economics. |
| 11 | Friction Factor | 3 | The proposed review gates are directionally reasonable, but they may add process friction because the approving actor, artifact status, and downstream dependency rule are not crisply bounded. |
| | **Composite Score** | **3.1** | |

---

## Overall Assessment

### Strengths

- The draft clearly identifies the real implementation seam between shell authority and domain execution authority, especially in **Runtime evidence snapshot**, **Workspace subordinate boundary**, and **Shell-state versus shell-mode distinction**.
- The current-state tables are strong editorial devices; **Current authority sources**, **Authority matrix**, and **Transition and denial rules** make the runtime legible and reviewable.
- The document is well aligned with the implementation snapshot’s governed Workspace routing model, particularly the separation between `app.shell.*` and `workspace.*` noted in **Runtime evidence snapshot** and **Workspace subordinate boundary**.
- The acceptance criteria are useful and concrete enough to serve as a draft checklist for a later ratified specification.

### Critical Gaps

- The document is not yet written as a governed specification or amendment. It lacks the required **Relationship to Governing Documents** section, article hierarchy, governance footer, and precise cross-references required by the Style Guide.
- The draft does not consistently use canonical terms from the *AIOS Technical Manifesto & Platform Economics* Appendix; for example, it centers “shell authority” and “shell modes” without anchoring them to **Stateful Shell**, **PolicyRecord**, **IntentKey**, or other glossary terms.
- Several review and approval requirements are under-specified. **Review gate**, **Dependency rule**, and **Doctrine escalation triggers** do not identify the authoritative approver under the *Gateway Global AIOS Governance Constitution*.
- The document introduces governance consequences (“review should fail,” “may be drafted in parallel,” “may rely on this phase”) without defining status states, ratification mechanics, or audit artifacts in a way that is enforceable.

---

## Article-by-Article Review

### Purpose

**Feedback:**  
The purpose statement is clear, but it is framed as a planning memo rather than a governed specification. It does not identify whether this artifact is a specification, amendment support packet, or reference document. It also does not state its governing relationship to the *Gateway Global AIOS Governance Constitution* (Article VI, Section 4), the *AIOS Technical Manifesto & Platform Economics* (Article I, Article II), or the *Gateway Global AIOS Master Platform Operating Agreement* (Article X). Because the document governs authority surfaces, it should explicitly state whether it constrains implementation, review sequencing, or both.

**Scores:** Cross-Document Consistency: 2, Style & Clarity: 3, Completeness: 3

**Recommendation:**  
Convert this opening into a formal architectural-purpose section and add a relationship table immediately after it. Proposed text:

> ## 1. Architectural Purpose  
> This document defines the Phase 1 authority model for the **Stateful Shell** surfaces that control entry into `primary`, `developer`, and `operator` shell surfaces. This document governs review and implementation sequencing for shell-surface authority only. It does not govern domain execution authority, Vendor Kit authority, or Tenant economic terms.  
>
> ## 2. Relationship to Governing Documents  
> | Governing Document | Relevant Section | Relationship | Effect on This Document |  
> |---|---|---|---|  
> | *The Gateway Global AIOS Governance Constitution* | Article VI, Section 4 | constrained_by | Constitutional governance and approval rules control review status and downstream reliance. |  
> | *AIOS Technical Manifesto & Platform Economics* | Article I, Article II, Article IV | implements | Shell authority must preserve deterministic execution, UI sovereignty, and Kit/domain subordination. |  
> | *Gateway Global AIOS Master Platform Operating Agreement* | Article X | constrained_by | This document does not alter liability, economics, or legal supremacy rules. |

---

### Declared inputs

**Feedback:**  
The source list is useful, but it is not normalized as governed references. Some entries are implementation artifacts, some are amendments, and some are review packets. The draft should distinguish normative sources from informative evidence. As written, a reader cannot tell which inputs are binding and which are merely evidentiary. This weakens cross-document coherence and creates ambiguity if one of the listed packets conflicts with a ratified document.

**Scores:** Cross-Document Consistency: 2, Practical Operability: 3, Developer Synchrony: 4

**Recommendation:**  
Split this section into **Normative Sources** and **Implementation Evidence**. Proposed text:

> ## 3. Source Classification  
> ### 3.1 Normative Sources  
> - *AMD-2026-012*  
> - *AMD-2026-007*  
> - *Intent Primitive and Execution Model*  
>
> ### 3.2 Informative Implementation Evidence  
> - `reference/implementation/AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001.md`  
> - `reference/implementation/AIOS-SHELL-BASELINE-RECOVERY-PACKET-001.md`  
> - `reviews/.../SHELL_CONTROLS_MATRIX.md`  
> - `reviews/.../SHELL_SCHEMA_ROUTE_STORAGE_MAP.md`  
> - `reviews/.../SHELL_BASELINE_GAP_MAP.md`  
> - implementation evidence in `ai-os-voice-interface` for `ShellSurfaceMode`, `shellAuthority`, `shellNavigationApply`, and `shellIntentRouter`  
>
> Add one sentence: “If informative evidence conflicts with a ratified governing document, the ratified governing document prevails.”

---

### Current baseline / Runtime evidence snapshot / Current authority sources

**Feedback:**  
These sections are among the strongest in the draft because they clearly separate current implementation reality from target governance. However, the terminology is still partly ad hoc. The governing glossary uses **Stateful Shell**, while the draft repeatedly uses “shell” generically. The phrase “authority plane” is understandable but undefined. The section also needs a sharper distinction between eligibility signals, persistence state, and authority decisions. Right now, the table mixes them together.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 4, Style & Clarity: 3

**Recommendation:**  
Define three terms before the table: **Shell Surface**, **Authority Signal**, and **Authority Decision**. Also replace generic “shell” references with **Stateful Shell** where the runtime component is meant. Proposed text:

> **Authority Signal** means a runtime input that indicates possible eligibility for an elevated Shell Surface but does not itself grant authority.  
> **Authority Decision** means the deterministic allow-or-deny result applied by the Stateful Shell before a surface transition.  
> **Shell Surface** means one of the governed Stateful Shell authority surfaces: `primary`, `developer`, or `operator`.

Then revise the table headings to:

| Current source | Classification | Current function | Governance posture |

This will reduce ambiguity and improve consistency with the Technical Manifesto Appendix.

---

### Authority matrix

**Feedback:**  
The matrix is useful, but it is incomplete as a governed control artifact. It identifies actor postures and allowed surfaces, yet it does not define who assigns those postures, whether they are session-scoped or tenant-scoped, or whether they are evaluated by a PolicyRecord-equivalent control. The “future identity-bound admin role” row is especially underdefined; it is a placeholder rather than a rule.

**Scores:** Completeness: 3, Legal Enforceability: 2, Practical Operability: 3

**Recommendation:**  
Add columns for **Authority Source**, **Decision Scope**, and **Audit Requirement**. Replace “to be defined” with a bounded placeholder rule. Proposed text for the final row:

> | future identity-bound administrative role | `primary`, `developer`, `operator` as authorized | yes | not in Phase 1 | This role is reserved for a later identity-bound authority mechanism that must bind elevation to authenticated identity, tenant or platform administrative policy, and auditable approval state. Phase 1 does not authorize implementation of that mechanism. |

This preserves the seam without pretending the mechanism already exists.

---

### Transition and denial rules

**Feedback:**  
This is a strong section structurally, but it needs more precise rule language. “Allowed because target remains elevated but eligible under current authority model” is explanatory prose, not a deterministic rule. The section also omits the actor that evaluates the transition and the required audit/disclosure outputs for each denial or success path.

**Scores:** Practical Operability: 3, Legal Enforceability: 2, Architectural Fidelity: 4

**Recommendation:**  
Rewrite each row as a deterministic rule with actor and output. For example:

> | Requested transition | Evaluator | Rule | Required output |  
> |---|---|---|---|  
> | `primary` -> `operator` | Stateful Shell authority gate | Allow only if `operatorEligible=true`; otherwise deny | On allow, disclose entry into `operator`; on deny, disclose denial reason and interim-authority status |  

Also add a sentence below the table:

> “The Stateful Shell records each attempted transition to an elevated Shell Surface with the requested target, decision result, decision basis, and session correlation identifier.”

That sentence would materially improve operability and auditability.

---

### Shell-state versus shell-mode distinction

**Feedback:**  
This section is substantively important and one of the clearest in the document. It correctly protects the distinction between privileged authority surfaces and ordinary UI state. However, “Review should fail” is not proper governing language because it does not identify the reviewer or the controlling standard. The section should instead define a non-conformance condition.

**Scores:** Architectural Fidelity: 5, Style & Clarity: 3, Conflict Freedom: 4

**Recommendation:**  
Replace the last sentence with:

> “A derivative artifact is non-conforming if it treats ordinary shell settings overlays, chat or voice mode changes, or subordinate Workspace routing as equivalent to privileged Shell Surface authority.”

This is clearer, enforceable, and consistent with specification style.

---

### Disclosure obligations

**Feedback:**  
This section is directionally correct and aligns with the implementation’s disclosure posture, but it needs tighter linkage to the *Intent Primitive and Execution Model* disclosure framework. It should explicitly connect shell-surface disclosure to the broader primary disclosure obligations rather than standing alone as a local checklist. It also needs to specify when disclosure is required: on entry, on attempted elevation, on denial, and on current-state display.

**Scores:** Cross-Document Consistency: 3, Completeness: 3, Style & Clarity: 3

**Recommendation:**  
Add a cross-reference to the *Intent Primitive and Execution Model* disclosure section and convert the bullets into event-triggered rules. Proposed text:

> The Stateful Shell shall disclose the following events and states in a user-visible manner, consistent with the *Intent Primitive and Execution Model* (Section 12.2):  
> 1. the current Shell Surface on entry and while active;  
> 2. each denied elevation attempt, including the denial reason;  
> 3. the interim, device-local nature of current elevated eligibility when such eligibility is used;  
> 4. each transition into `developer` or `operator`; and  
> 5. each Workspace opening event as a subordinate controlled surface rather than an authority bypass.

---

### Workspace subordinate boundary

**Feedback:**  
This section is strong and coherent with the implementation snapshot. It correctly preserves the routing distinction between shell-state control and Workspace execution. Editorially, however, it should cite the governing source more precisely. The current text references the concept but not the exact controlling document sections.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 3, Developer Synchrony: 4

**Recommendation:**  
Add explicit citations to the *AIOS Technical Manifesto & Platform Economics* (Article IV) and the *Intent Primitive and Execution Model* / Workspace governance materials. Proposed text:

> This subordinate boundary implements the architectural separation described in the *AIOS Technical Manifesto & Platform Economics* (Article IV) and the governed routing model reflected in the Workspace integration control-plane materials. The Stateful Shell may open a Workspace surface, but Workspace execution remains separately policy-gated and may not serve as an alternate authority path.

If the intended normative source is AMD-2026-012 or AIOS-SPEC-007, cite the exact section once available.

---

### Immediate remediation direction

**Feedback:**  
This section identifies the right future seam, but it is too abstract to govern downstream work. “Identity-bound administrator posture” and “reviewable administrative elevation rule” are good concepts, yet the document does not define the minimum attributes of that future mechanism. Without those attributes, later drafts may claim compliance while implementing materially different authority models.

**Scores:** Completeness: 3, Legal Enforceability: 2, Practical Operability: 3

**Recommendation:**  
Add a minimum future-state requirements list. Proposed text:

> Any successor to interim device-local authority shall, at minimum:  
> 1. bind elevated eligibility to an authenticated identity;  
> 2. bind elevated eligibility to a defined administrative policy scope;  
> 3. record the approver, approval basis, and approval time where human approval is required;  
> 4. record each privileged entry and privileged mutation event in an auditable log; and  
> 5. preserve deterministic downgrade to `primary`.

This gives later phases a concrete seam.

---

### Required phase outputs / Surface requirements / Dependency rule / Acceptance criteria / Review gate / Doctrine escalation triggers

**Feedback:**  
These sections contain the document’s governance logic, but they are currently the least mature from a formal-governance perspective. They read like internal project management instructions rather than ratifiable rules. The biggest issue is missing authority attribution: who issues the “recorded human approval”? Is it the Governance Council, a designated reviewer, a product owner, or a repository maintainer? Under the *Gateway Global AIOS Governance Constitution* (Article II; Article VI, Section 4), that distinction matters. The phrase “governed output” is also undefined in this draft.

**Scores:** Legal Enforceability: 2, Conflict Freedom: 2, Friction Factor: 3

**Recommendation:**  
Consolidate these sections into a formal **Governance Status and Review Controls** article. Define status states and approvers. Proposed text:

> ## Article V: Governance Status and Review Controls  
> ### Section 1. Status States  
> This artifact shall use the following status states: `draft`, `under_review`, `accepted_with_remediation`, `accepted`, and `superseded`.  
>
> ### Section 2. Minimum Review Artifacts  
> Before a downstream shell-authority artifact may rely on this document, the review record shall include:  
> 1. a peer-review output set;  
> 2. a packet status update; and  
> 3. a recorded human decision of `accepted`, `accepted_with_remediation`, or `rejected`.  
>
> ### Section 3. Approval Authority  
> This document shall identify, in front matter or an approval block, the human authority responsible for the recorded decision. If the document is intended to operate as a governed specification, approval authority shall be assigned consistently with the *Gateway Global AIOS Governance Constitution* (Article II and Article VI, Section 4).  
>
> ### Section 4. Non-Reliance Rule  
> No later shell artifact that introduces privileged authority behavior may claim governed reliance on this document while its status is `draft` or `under_review`.  
>
> ### Section 5. Escalation Trigger  
> If review identifies a gap in constitutional governance, shell authority separation, or disclosure doctrine, the reviewer shall open an amendment or doctrine-support path and cite the affected governing document and section.

This would resolve most of the current ambiguity.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Purpose / opening structure | The draft is not in governed-document format and lacks a relationship-to-governing-documents section. | Recast the document into numbered articles/sections and add a formal relationship table citing the Constitution, Technical Manifesto, and MPOA. | Critical | 1, 5, 8 |
| 2 | Declared inputs | Normative and informative sources are mixed together without precedence rules. | Split inputs into Normative Sources and Implementation Evidence, and state that ratified governing documents prevail over evidence packets. | High | 1, 6, 7 |
| 3 | Current baseline through Current authority sources | Key terms are ad hoc and not anchored to the canonical glossary. | Define Shell Surface, Authority Signal, and Authority Decision, and align references to the Stateful Shell glossary term. | High | 1, 4, 8 |
| 4 | Authority matrix | The matrix lacks authority source, scope, and audit requirements, and the future admin row is too vague. | Expand the matrix with decision-scope and audit columns and replace “to be defined” with a bounded placeholder rule. | High | 3, 5, 7 |
| 5 | Transition and denial rules | Rules are explanatory rather than deterministic and omit required outputs. | Rewrite each transition as evaluator + rule + required output, and require audit recording for attempted elevated transitions. | Critical | 3, 7, 9 |
| 6 | Shell-state versus shell-mode distinction | “Review should fail” is not enforceable governing language. | Replace it with a defined non-conformance rule for derivative artifacts. | Medium | 3, 8 |
| 7 | Disclosure obligations | Disclosure duties are not explicitly tied to the broader disclosure framework. | Cross-reference the Intent Primitive disclosure section and convert the bullets into event-triggered SHALL rules. | High | 1, 5, 8 |
| 8 | Workspace subordinate boundary | The section is substantively sound but under-cited. | Add precise cross-references to the Technical Manifesto and the applicable shell/workspace governance source. | Medium | 1, 4, 6 |
| 9 | Immediate remediation direction | The future identity-bound replacement seam is too abstract. | Add minimum successor requirements: authenticated identity, policy scope, approver record, audit log, and deterministic downgrade. | High | 3, 5, 7 |
| 10 | Review gate / Dependency rule / Doctrine escalation triggers | Approval authority, status states, and non-reliance rules are undefined. | Consolidate these into a Governance Status and Review Controls article with explicit status states and approval authority. | Critical | 3, 6, 7, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The draft is substantively promising and architecturally aligned, but it does not yet meet the governing set’s requirements for structure, citation precision, enforceable review mechanics, and cross-document coherence. It has multiple dimension scores at 2, which requires major revision under the rubric.

**Top 3 Actions Required:**
1. Recast the draft into formal governed-document structure with explicit relationship, article hierarchy, and canonical cross-references.
2. Convert review, transition, and disclosure language into deterministic rules with named actors, outputs, and status controls.
3. Define the minimum identity-bound successor seam and audit requirements so later phases cannot rely on the interim device-local model ambiguously.
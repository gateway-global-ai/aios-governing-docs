---
review_id: REV-AMD-2026-012-ADD-001-001
document_reviewed: AMD-2026-012-ADD-001
document_version: 0.1.0
reviewer: OpenAI
review_date: 2026-04-17
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.0
---

# Peer Review: AMD-2026-012-ADD-001 — Loop Exit and Discovery-First Voice Sequencing

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The addendum is directionally aligned with the cited standards but fails to anchor key rules to the parent amendment’s specific sections and introduces terminology variations such as “shell” instead of the canonical capitalized “Shell.” |
| 2 | Business Model Alignment | 4 | The document does not conflict with marketplace or ecosystem strategy, but it is largely silent on how loop-exit and discovery-first rules interact with Kits, integrations, or vendor-facing surfaces. |
| 3 | Legal Enforceability | 2 | Several core obligations rely on vague terms such as “user-comprehensible,” “real step,” “evidence,” and “preferred sequence,” which weakens enforceability for a binding addendum. |
| 4 | Architectural Fidelity | 4 | The document generally reinforces Shell authority, discovery-first sequencing, and anti-dashboard-first architecture, but it does not clearly bind these rules to control-plane state or deterministic conformance hooks. |
| 5 | Completeness | 2 | The addendum states two major rules but omits conformance criteria, failure states, relationship-to-parent language, and explicit cross-document boundary handling needed for ratifiable completeness. |
| 6 | Conflict Freedom | 3 | The document does not directly contradict the bundled authorities, but its sequencing list partially diverges from the five-pass discovery suite and from the user sovereignty standard without clarifying whether it is extending or restating them. |
| 7 | Practical Operability | 2 | The rules are understandable at a policy level but too abstract for day-one implementation because they lack measurable thresholds, required artifacts, and reviewer test conditions. |
| 8 | Style & Clarity | 3 | The prose is concise and readable, but it departs from the style guide through inconsistent capitalization, limited structural scaffolding, and insufficiently precise normative drafting. |
| 9 | Developer Synchrony | 2 | A developer or agent would not know what exact artifacts, state fields, or UI surfaces must exist to satisfy loop-exit compliance. |
| 10 | Platform Economics Synchrony | 4 | The addendum does not misstate economic mechanics, though it also does not clarify whether “export,” “human review,” or “freeze” have economic or commercial boundary implications. |
| 11 | Friction Factor | 5 | The proposed controls are lightweight and proportional, adding governance value without imposing excessive process overhead. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

- Sections 3 and 7 reinforce the parent amendment’s core anti-dashboard-first posture and preserve Shell primacy rather than allowing tool-first drift.
- Section 5 usefully consolidates the discovery-first planning sequence into a short, readable rule that aligns in spirit with *AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001* §5.
- The document is brief and focused, which helps preserve amendment discipline and avoids unnecessary duplication of unrelated policy domains.

### Critical Gaps

- Section 0 and Section 1 do not explain the legal relationship to *AMD-2026-012* v1.0.0 with sufficient precision; the addendum should state which parent sections it supplements and whether it is binding interpretive law or a substantive amendment.
- Sections 3 through 6 restate concepts from *AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001* §§4–6 and *AIOS-DISCOVER-AGENT-PROCESS-001* without clarifying precedence, incorporation scope, or exact conformance obligations.
- Sections 3, 4, and 5 use vague language that is not yet enforceable in a governance setting, especially for “path,” “evidence,” “closure,” “preferred sequence,” and optional discovery passes.
- The addendum lacks a conformance section analogous to *AMD-2026-012* §15, making it difficult to test or enforce.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section is too thin for an amendment addendum. It identifies purpose, but it does not specify whether the addendum amends, interprets, or incorporates by reference the parent amendment. It also does not identify which sections of *AMD-2026-012 — Shell Authority and Voice-First Entry* are being extended. Under the style guide and cross-document coherence requirements, a binding addendum should explicitly map itself to the parent document’s operative sections, especially §6 (Shell journey model), §8 (Voice-first interaction standard), §11 (Discovery-first rule), and §15 (Conformance). Without that mapping, the reader must infer the legal effect.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2, Style & Clarity: 3

**Recommendation:**  
Revise Section 0 to state the addendum’s legal relationship explicitly. Proposed replacement text:

> **Purpose** | This addendum supplements **AMD-2026-012 — Shell Authority and Voice-First Entry** v1.0.0. It extends **§6 (Shell journey model)**, **§8 (Voice-first interaction standard)**, **§11 (Discovery-first rule)**, and **§15 (Conformance)** by adding binding loop-exit obligations and discovery-first sequencing requirements for voice-first systems. In the event of conflict, **AMD-2026-012** remains controlling except where this addendum expressly supersedes or tightens a requirement.

Also capitalize “Shell” consistently in the table and body.

---

### 1. Purpose

**Feedback:**  
The section is clear at a high level, but it overstates binding effect without defining the operative objects. “Exit the progress loop” is not a defined term in the parent amendment, and “schemas, routes, and storage” appears to summarize discovery outputs without tying them to the bundled discovery authorities. Because this is an addendum, it should either define “progress loop” and “loop exit” or adopt the terminology already used in the user sovereignty standard.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2, Conflict Freedom: 3

**Recommendation:**  
Replace the current text with terminology harmonized to the bundled standard. Proposed text:

> This addendum establishes two binding rules:  
> 1. voice-first systems **SHALL** provide an explicit **loop-exit** path from declared intent to evidential outcome, blocked state, reset, or stop; and  
> 2. voice-first planning **SHALL** follow a discovery-first sequence consistent with **AIOS-DISCOVER-AGENT-PROCESS-001** and **AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001** before dashboard, menu, or broad UI composition begins.

If “progress loop” is retained, add a definition section.

---

### 2. Governing principle

**Feedback:**  
This section is rhetorically strong but not yet precise enough for governance text. “Outcome direction” and “exit clarity” are not defined, and “interface chrome” is informal relative to the style guide. The sentence reads more like a design maxim than enforceable law.

**Scores:** Legal Enforceability: 2, Style & Clarity: 3

**Recommendation:**  
Convert this into a normative interpretive rule using defined terms. Proposed text:

> Voice-first systems **SHALL** be evaluated for conformance based on whether the Shell presents:  
> - a declared or actively clarified intent;  
> - the next governed state transition;  
> - the evidential basis for completion, blockage, or failure where applicable; and  
> - an explicit user path to stop, reset, export, or hand off the session.  
> UI composition depth, menu density, or conversational continuity **SHALL NOT** substitute for those requirements.

---

### 3. Loop-exit rule

**Feedback:**  
This is the document’s core provision and the strongest substantive addition, but it is under-specified. The phrase “user-comprehensible path” needs objective criteria. “Evidence” should be tied to rendered proof, session state, artifact output, or explicit blocked status. “Closure, reset, or explicit stop” is good structure, but the section should also state that summaries alone are insufficient, consistent with the bundled user sovereignty standard §4.2 and §6.1.

**Scores:** Legal Enforceability: 2, Architectural Fidelity: 4, Practical Operability: 2

**Recommendation:**  
Expand Section 3 into a testable rule. Proposed replacement text:

> The **Shell** **SHALL** provide a user-visible loop-exit path from:  
> 1. declared intent or active clarification state;  
> 2. to the next governed step or blocker;  
> 3. to rendered, inspectable, or otherwise reviewable evidence of execution, failure, or blocked status;  
> 4. to one of the following terminal user options: closure, reset, export, handoff, or explicit stop.  
>  
> Conversation quality, reassurance, or summary text **SHALL NOT** by themselves constitute completion. A session is treated as closed only when the Shell presents a visible state transition showing the matter as completed, blocked, reset, handed off, or stopped.

---

### 4. Minimum loop-exit options

**Feedback:**  
This section is useful but too weakly drafted. Because Section 3 uses “SHALL provide a path,” Section 4 should define which options are mandatory versus optional. As written, all listed options are merely examples under “SHOULD,” which leaves conformance uncertain. The phrase “current packet” also assumes discovery-packet terminology that may not exist in every runtime session.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Developer Synchrony: 2

**Recommendation:**  
Separate mandatory minima from optional extensions. Proposed text:

> At minimum, the Shell **SHALL** provide:  
> - an option to stop the active loop and preserve or clear state according to policy;  
> - an option to reset the active intent; and  
> - an option to expose or export the current user-visible evidence bundle, session summary, or equivalent review artifact when policy permits.  
>  
> The Shell **SHOULD**, where supported by the lane, also provide:  
> - handoff to human review; and  
> - freeze of the current work state for external inspection.

Also replace “current packet” with “current evidence bundle, session summary, or equivalent governed artifact.”

---

### 5. Discovery-first sequencing

**Feedback:**  
This section is central but currently creates coherence problems. The sequence partly overlaps with the five-pass suite but adds “schema review,” “route review,” and “storage / state review,” which are not named as part of the governed five-pass discovery suite in *AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001*. That may be acceptable, but the document must clarify whether these are sub-analyses within architect planning, extensions to discovery, or illustrative decomposition. The phrase “preferred sequence” also conflicts with the opening sentence’s “SHALL NOT begin,” because the first sentence is binding while the second sounds advisory.

**Scores:** Cross-Document Consistency: 2, Conflict Freedom: 3, Practical Operability: 2

**Recommendation:**  
Clarify the relationship to the five-pass suite and make the sequence normative where intended. Proposed replacement text:

> For AI-first and especially voice-first systems, planning **SHALL NOT** begin with dashboards, dropdown menus, or omnibus UI composition as the primary architecture move.  
>  
> Where current-system structure matters, the planning lane **SHALL** begin with governed discovery consistent with **AIOS-DISCOVER-AGENT-PROCESS-001** and, when applicable, the **pre_architecture_five_pass** profile defined in **AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001**.  
>  
> After discovery, the lane **SHALL** address, in logical order:  
> 1. architecture cartography;  
> 2. implicit capability extraction;  
> 3. governance breach audit;  
> 4. registry or control-plane migration implications where applicable;  
> 5. schema, route, and storage/state mapping;  
> 6. intent and loop-exit design;  
> 7. only then Shell and UI composition.

This preserves alignment while allowing the added mapping steps.

---

### 6. Multi-agent discovery

**Feedback:**  
This section is the weakest editorially. It says discovery “SHOULD use specialized passes aligned with” two documents, then lists passes that do not fully match either cited authority. In particular, “schemas,” “routes,” and “storage” are not named passes in the five-pass suite, and “rendered-surface inspection” plus “artifact integrity checks” come from the user sovereignty standard’s browser-review logic rather than the pre-architecture discovery reference. The section therefore blends three authorities without boundary language.

**Scores:** Cross-Document Consistency: 2, Conflict Freedom: 3, Developer Synchrony: 2

**Recommendation:**  
Split discovery passes from rendered-proof review obligations. Proposed replacement text:

> When current-system structure materially affects planning, the lane **SHOULD** use the governed discovery process in **AIOS-DISCOVER-AGENT-PROCESS-001** and, where declared in `DISCOVERY_SCOPE.yaml`, the five-pass pre-architecture suite in **AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001**.  
>  
> The governed pre-architecture suite consists of:  
> - architecture cartography;  
> - implicit capability extraction;  
> - governance breach audit;  
> - registry migration planning;  
> - control-plane coverage audit.  
>  
> Rendered-surface inspection and artifact integrity checks **SHOULD** be treated as additional review controls under **AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001**, not as substitutes for the governed discovery suite.

---

### 7. Anti-dashboard-first rule

**Feedback:**  
This section is substantively aligned with the parent amendment and is one of the clearer parts of the draft. However, “planning as a substitute for intent architecture” is somewhat abstract, and “rendered proof of the active path” appears for the first time here without definition. The section should also capitalize “Shell.”

**Scores:** Architectural Fidelity: 4, Style & Clarity: 3, Cross-Document Consistency: 2

**Recommendation:**  
Tighten the language and define rendered proof by reference. Proposed text:

> The **Shell** **SHALL NOT** rely on dashboard-first or tool-catalog-first planning as a substitute for governed intent design, loop-exit design, or control-plane-backed session direction.  
>  
> Menus and dropdowns **MAY** remain subordinate fallback affordances, but they **SHALL NOT** replace:  
> - intent discovery;  
> - loop-exit clarity;  
> - Shell authority; or  
> - rendered, inspectable proof of the active session path where such proof is required by governing review standards.

---

### Final principle

**Feedback:**  
This closing sentence is effective rhetorically but should not be the only concluding governance language. It reads as a slogan rather than a legal footer or conformance bridge. The document also lacks the standard governance footer required by the style guide.

**Scores:** Style & Clarity: 3, Completeness: 2

**Recommendation:**  
Retain the sentence only as an informative note and add a conformance section plus governance footer. Proposed additions:

> ## 8. Conformance  
> An implementation is non-conformant with this addendum if any of the following hold:  
> 1. The Shell does not present a visible loop-exit path from intent to closure, blocked state, reset, handoff, export, or stop as applicable.  
> 2. Summary quality or conversational continuity is treated as completion without evidential or state-based closure.  
> 3. Planning begins with dashboard, menu, or broad UI composition before required discovery and intent design steps are completed.  
> 4. Discovery obligations required by scope are skipped or replaced by summary-only planning.  
>  
> **This addendum is governed by the AIOS Governance Constitution (v1.0) and the ratification path applicable to AMD-2026-012.**

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 0. Status and intent | The addendum does not clearly state how it supplements specific sections of AMD-2026-012 or what its precedence is. | Add explicit parent-section mapping and conflict/precedence language referencing AMD-2026-012 §§6, 8, 11, and 15. | Critical | 1, 3, 5, 6, 8 |
| 2 | 1. Purpose / 3. Loop-exit rule | Core loop-exit obligations use undefined and vague terms that are not enforceable. | Define or replace “progress loop,” “user-comprehensible,” “real step,” and “evidence” with testable state- and artifact-based language. | Critical | 3, 5, 7, 8, 9 |
| 3 | 4. Minimum loop-exit options | Mandatory versus optional exit controls are unclear because the section uses only SHOULD language. | Establish a SHALL minimum set and a separate SHOULD extension set. | High | 3, 7, 9 |
| 4 | 5. Discovery-first sequencing | The sequencing list partially diverges from the governed five-pass discovery suite and uses “preferred” language that weakens the rule. | Reframe the sequence to explicitly incorporate the governed discovery process and clarify where schema/route/storage mapping sits relative to the five-pass suite. | Critical | 1, 4, 6, 7, 9 |
| 5 | 6. Multi-agent discovery | The section blends discovery passes with rendered-surface review controls from different documents without boundary language. | Separate pre-architecture discovery obligations from browser/rendered-proof review obligations and cite each authority to its proper domain. | High | 1, 5, 6, 9 |
| 6 | 7. Anti-dashboard-first rule | Terminology and capitalization are inconsistent with the parent amendment and style guide. | Capitalize “Shell,” tighten “intent architecture,” and define “rendered proof” by reference to governing review standards. | Medium | 1, 8 |
| 7 | New Section 8 | The document lacks conformance tests and non-conformance triggers. | Add a conformance section modeled on AMD-2026-012 §15 with explicit failure conditions. | Critical | 3, 5, 7, 9 |
| 8 | Document footer | The document omits the standard governance footer. | Add the required governance footer referencing the AIOS Governance Constitution (v1.0). | Medium | 5, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is conceptually aligned with the governing set, but it has multiple dimension scores of 2, including cross-document consistency, legal enforceability, completeness, practical operability, and developer synchrony. As drafted, it is not yet precise or integrated enough for ratification as a binding addendum.

**Top 3 Actions Required:**
1. Add explicit legal linkage to AMD-2026-012 and a conformance section with testable non-conformance triggers.
2. Rewrite the loop-exit and discovery-first provisions using defined, enforceable terms tied to artifacts, state, and cited governing authorities.
3. Reconcile Sections 5 and 6 with the exact structure of the governed discovery documents and separate discovery obligations from rendered-proof review controls.
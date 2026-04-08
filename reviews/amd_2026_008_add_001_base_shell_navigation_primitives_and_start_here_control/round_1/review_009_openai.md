---
review_id: REV-AMD-2026-008-ADD-001-001
document_reviewed: amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md
document_version: 0.1.0
reviewer: OpenAI
review_date: 2026-04-08
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-008-ADD-001 — Base Shell Navigation Primitives and Start-Here Control

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The addendum is directionally aligned with AMD-2026-008 and ADD-002, but it uses under-specified cross-references and introduces shell control-plane concepts without anchoring them to the governing sections that appear to supply their authority. |
| 2 | Business Model Alignment | 3 | The document does not create obvious business-model conflict, but it is largely silent on whether any navigation controls have product-tier, tenant-policy, or deployment-bound implications. |
| 3 | Legal Enforceability | 2 | Several obligations use subjective triggers such as “when ambiguity would cause mis-routing” without objective criteria, making enforcement difficult. |
| 4 | Architectural Fidelity | 3 | The shell-governed framing is consistent with the broader architecture, but the document does not clearly distinguish shell state, intent state, and session state as required for deterministic execution. |
| 5 | Completeness | 2 | The document defines labels and a small primitive map, but omits state transitions, failure modes, audit fields, and the operational meaning of START_HERE recovery and Alert behavior. |
| 6 | Conflict Freedom | 3 | No direct contradiction is evident, but the undefined relationship between Alert, START_HERE, and AIOS-SPEC-009 session/intent boundaries creates tension with the parent framework’s precision requirements. |
| 7 | Practical Operability | 2 | A developer could infer the general UX intent, but the document is not yet specific enough to implement consistently across voice, touch, and audit surfaces. |
| 8 | Style & Clarity | 4 | The prose is concise and mostly clear, with good sectioning and limited ambiguity at the sentence level. |
| 9 | Developer Synchrony | 2 | The implementation snapshot shows extensive shell, intent, and control-plane machinery, but this addendum does not define enough interface contract detail for developers to map product behavior to the new navigation classes. |
| 10 | Platform Economics Synchrony | 3 | The addendum appears economically neutral, but it should state that it does not alter MPOA economics or entitlement structure, as ADD-002 does for premium capabilities. |
| 11 | Friction Factor | 5 | The document is short, readable, and low-friction for reviewers and implementers to parse. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- Section 1 states the core purpose clearly: navigation is shell-governed rather than left to model habit.
- Section 2 usefully separates navigation from output depth, shell voice controls, and packaging, which improves coherence with AMD-2026-008-ADD-002.
- Section 3 provides a compact taxonomy that is easy to understand and likely useful as a control-plane axis.
- Section 6 appropriately limits scope and avoids overclaiming.

### Critical Gaps

- Section 3 defines navigation classes but does not define transition rules, entry conditions, or whether the classes are mutually exclusive, session-scoped, step-scoped, or intent-scoped.
- Section 4 introduces **Alert** as a primitive even though it is not one of the Section 3 navigation classes, creating taxonomy drift.
- Section 5.1 uses the subjective standard “when ambiguity would cause mis-routing” without objective disclosure criteria.
- Section 5.3 references AIOS-SPEC-009 session and intent boundaries only generically and does not cite the controlling sections.
- The document does not explain how START_HERE interacts with recovery, re-entry, interrupted flows, or sovereign voice readiness disclosures required by AMD-2026-008 Section 4.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:** This section is clear and appropriately scoped, but it would benefit from one additional sentence clarifying whether this addendum is purely shell-governance doctrine or also creates implementation obligations for session state, audit traces, and control-plane routing. The current text says it defines the “navigation axis of the shell control plane,” but does not say whether that axis is normative for all shell surfaces or only for sovereign voice contexts under AMD-2026-008.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 4, Completeness: 3

**Recommendation:** Add a final sentence such as: “This addendum applies to shell navigation behavior for any session operating within the AMD-2026-008 sovereign voice framework and is normative for shell state, user-facing navigation affordances, and related audit interpretation where applicable.”

---

### 1. Purpose

**Feedback:** The purpose statement is strong editorially, but it is still high-level. “Session flow, choice, and input capture” are named, yet the document later defines only classes and a primitive map. The section should preview whether the addendum governs classification only, transition logic, or both.

**Scores:** Style & Clarity: 4, Completeness: 2, Practical Operability: 2

**Recommendation:** Revise to specify the operative scope. Proposed text: “This addendum defines the normative navigation classes, primitive mappings, and minimum shell obligations for session entry, continuation, choice selection, and governed input capture. It does not define output depth, voice delivery controls, or export packaging.”

---

### 2. Governing principle

**Feedback:** This is the strongest section in the draft. It cleanly separates navigation from the ADD-002 axes. However, “where the user is in the flow” is still colloquial and should be tightened into a governance concept such as session step, branch state, or capture mode. Without that, developers may implement incompatible internal models.

**Scores:** Cross-Document Consistency: 3, Architectural Fidelity: 3, Style & Clarity: 4

**Recommendation:** Replace “where the user is in the flow” with more deterministic language. Proposed text: “Navigation governs the active shell step, branch posture, and capture mode for the current interaction state.”

---

### 3. Navigation classes

**Feedback:** The taxonomy is promising but incomplete. The document does not state whether exactly one navigation class must be active at a time, whether classes can nest, or whether START_HERE is a transient entry state or a reusable recovery state. The title emphasizes “Start-Here Control,” but START_HERE receives only one sentence and no operational doctrine. In addition, CONTINUE is defined negatively (“without forcing a new branch or capture shape”), which leaves too much room for interpretation.

**Scores:** Completeness: 2, Practical Operability: 2, Architectural Fidelity: 3, Cross-Document Consistency: 2

**Recommendation:** Add a subsection after Section 3 with state semantics. Proposed text:
- “At any governed shell step, the shell SHALL assign one primary navigation class.”
- “START_HERE SHALL be used for initial entry, explicit reset to a known entry point, or recovery from unresolved routing ambiguity.”
- “CONTINUE SHALL preserve the current branch and capture mode unless the actor explicitly invokes CHOOSE, SINGLE_INPUT, or MULTI_INPUT.”
- “CHOOSE, SINGLE_INPUT, and MULTI_INPUT are mutually exclusive capture postures for a given active step unless the shell explicitly transitions between them.”

---

### 4. Core primitives (mapping)

**Feedback:** This section currently creates the largest editorial and structural problem in the document. Section 3 defines five navigation classes, but Section 4 lists five primitives, one of which—Alert—does not map to a Section 3 class. That makes the taxonomy internally uneven. Either Alert is a navigation class, or it is a separate shell signal primitive outside the navigation-class model. As written, the reader cannot tell. The phrase “interruptive or high-priority notice” is also too vague for governance text.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2, Completeness: 2, Style & Clarity: 3

**Recommendation:** Separate Alert from the class map or define it formally as a non-navigation shell signal. Proposed replacement heading and text:

“## 4. Core primitives and non-class signals

The following primitives SHALL be realizable as shell affordances (voice, touch, or equivalent), not only as model behaviors:

| Primitive | Role | Relationship to navigation class |
|-----------|------|----------------------------------|
| **Alert** | Governed interrupt or priority notice requiring immediate user attention or acknowledgement under product policy. | Not a navigation class; MAY preempt the current class but SHALL NOT silently rewrite branch or capture state. |
| **Continue** | Advance or resume the current interaction. | Maps to **CONTINUE** |
| **Choose** | Select among explicit options. | Maps to **CHOOSE** |
| **Single input** | Capture one primary free-form response. | Maps to **SINGLE_INPUT** |
| **Multi input** | Capture multiple fields or sequential responses under one governed structure. | Maps to **MULTI_INPUT** |”

---

### 5. Shell obligations (navigation)

**Feedback:** This section contains the document’s binding rules, but they are not yet enforceable enough. Section 5.1 hinges on “ambiguity,” which is subjective. Section 5.2 is useful but should say “SHALL NOT treat navigation state as sufficient authority to alter output depth, packaging, or lane policy.” Section 5.3 is too generic; “preserve auditability” does not specify what must be recorded. Given the implementation snapshot’s emphasis on routing envelopes, scope classes, and audit IDs, this section should require at least minimal trace fields.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Developer Synchrony: 2, Completeness: 2

**Recommendation:** Expand Section 5 into objective obligations. Proposed text:
1. “The shell SHALL expose the active navigation class whenever the active step requires the actor to choose among enumerated options or to provide structured rather than free-form input.”
2. “The shell SHALL NOT use navigation-class changes alone to alter output depth, packaging class, runtime lane, or policy posture; those controls remain governed by AMD-2026-008 and AMD-2026-008-ADD-002.”
3. “For any transition involving CHOOSE, SINGLE_INPUT, MULTI_INPUT, or START_HERE recovery, the shell SHALL preserve an auditable record of the prior class, resulting class, triggering actor action, and resulting branch or capture posture.”
4. “If routing ambiguity is unresolved, the shell SHALL return the interaction to START_HERE or CHOOSE rather than infer a branch silently.”

---

### 6. Non-goals

**Feedback:** This section is clean and useful. It correctly avoids overlap with ADD-002 and AIOS-SPEC-007. However, because the document repeatedly references “shell control plane,” it should also disclaim that it does not define intent schema, session schema, or audit schema unless those are added elsewhere.

**Scores:** Style & Clarity: 4, Conflict Freedom: 4, Completeness: 3

**Recommendation:** Add one bullet: “intent schema, session schema, or audit record schema beyond the minimum navigation obligations in Section 5.”

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Navigation classes lack state semantics, exclusivity rules, and START_HERE operational meaning. | Add explicit rules for primary active class, START_HERE recovery use, CONTINUE preservation, and CHOOSE/SINGLE_INPUT/MULTI_INPUT mutual exclusivity at a given step. | Critical | 1, 4, 5, 7, 9 |
| 2 | Section 4 | Alert is introduced as a primitive without a clear relationship to the Section 3 taxonomy. | Recast Alert as a non-class shell signal or formally add it to the taxonomy with defined preemption rules. | Critical | 1, 3, 5, 6, 8 |
| 3 | Section 5 | Binding obligations are too subjective and not auditable enough. | Replace “when ambiguity would cause mis-routing” with objective triggers and require minimum audit fields for navigation transitions. | Critical | 3, 5, 7, 9 |
| 4 | Sections 0, 1, 2 | Scope is clear conceptually but not precise about whether the addendum governs classification only or also transitions and shell state. | Add explicit language that the addendum is normative for shell state, navigation affordances, and navigation-transition interpretation within AMD-2026-008 contexts. | High | 1, 4, 5, 8 |
| 5 | Section 5.3 | AIOS-SPEC-009 is referenced only generically. | Cite the exact AIOS-SPEC-009 sections governing session and intent boundaries, or remove the reference until exact citations are available. | High | 1, 6, 8 |
| 6 | Section 6 | Non-goals omit schema boundaries. | Add a bullet disclaiming intent, session, and audit schema definition unless expressly added. | Medium | 5, 6, 8 |
| 7 | Front matter / economics boundary | The addendum does not expressly state that it does not alter MPOA economics or entitlement structure. | Add a short cross-reference sentence stating that this addendum governs navigation only and does not modify economics, liability, or entitlement rules under the MPOA or parent amendment. | Medium | 2, 10, 6 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The draft has a sound conceptual core and good editorial economy, but its operative provisions are too under-specified to function as binding governance text. The missing state semantics, unclear Alert taxonomy, and non-objective shell obligations materially weaken enforceability and implementation consistency.

**Top 3 Actions Required:**
1. Define the operational semantics of each navigation class, especially START_HERE, CONTINUE, and class exclusivity at a given step.
2. Resolve the taxonomy problem in Section 4 by clearly distinguishing navigation classes from non-class shell signals such as Alert.
3. Rewrite Section 5 with objective triggers and minimum audit requirements for navigation transitions.
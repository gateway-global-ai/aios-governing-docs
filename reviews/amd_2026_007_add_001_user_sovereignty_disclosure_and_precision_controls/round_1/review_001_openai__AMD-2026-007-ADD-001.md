---
review_id: REV-AMD-2026-007-ADD-001-001
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.1.0
reviewer: OpenAI
review_date: 2026-04-17
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 2.9
---

# Peer Review: AMD-2026-007-ADD-001 — User Sovereignty Disclosure and Precision Controls

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The addendum is directionally aligned with AMD-2026-007 and AIOS-SPEC-009 but uses non-canonical terms, incomplete citation patterns, and a separate normative vocabulary that is not yet integrated into the existing policy register. |
| 2 | Business Model Alignment | 4 | The document generally supports enterprise trust and platform legitimacy, and it does not materially conflict with the marketplace model. |
| 3 | Legal Enforceability | 2 | Core obligations rely too heavily on `SHOULD` and undefined qualifiers such as “materially exist” and “user-comprehensible,” making several provisions difficult to enforce. |
| 4 | Architectural Fidelity | 3 | The document is broadly compatible with shell disclosure principles, but it does not clearly anchor its requirements to the existing intent, policy, and operator-surface architecture. |
| 5 | Completeness | 2 | The addendum introduces a new governance area but omits policy IDs, enforcement hooks, operator-vs-primary boundaries, failure behavior, and cross-document implementation deltas. |
| 6 | Conflict Freedom | 3 | The document does not directly contradict the bundled authorities, but its broad disclosure language creates tension with AMD-2026-007 §11.5 and AIOS-SPEC-009 §12.4 regarding operator-only evidence. |
| 7 | Practical Operability | 2 | A developer or reviewer would not know what exact controls are mandatory, when disclosure is triggered, or what minimum shell surfaces satisfy compliance. |
| 8 | Style & Clarity | 4 | The prose is concise and readable, but several sections are too high-level for binding amendment text and do not consistently follow the citation and precision expectations of the Style Guide. |
| 9 | Developer Synchrony | 2 | The document lacks schemas, policy mappings, UI surface definitions, and implementation loci, so it does not yet tell builders exactly what to implement. |
| 10 | Platform Economics Synchrony | 4 | The text does not misstate platform economics and only indirectly touches cost-related behavior. |
| 11 | Friction Factor | 4 | The proposed controls are proportionate in concept and do not appear to impose excessive governance burden, though implementation ambiguity could create avoidable friction. |
| | **Composite Score** | **2.9** | |

---

## Overall Assessment

### Strengths

- **§1 and §8** articulate a clear governance purpose: hidden state that materially affects user experience should not remain opaque.
- **§3–§6** identify a coherent set of disclosure and control classes that fit naturally with the shell disclosure model established in *AMD-2026-007* §4.3 and §11.6.
- The addendum usefully extends the existing governance set toward user sovereignty without introducing marketing language or product-pitch framing.
- The document is short, readable, and conceptually focused, which makes it a good candidate for conversion into a stronger binding addendum.

### Critical Gaps

- **§2, §4, §5, §6, and §7** rely on `SHOULD` for obligations that appear intended to be binding shell law; this materially weakens enforceability.
- The addendum does not create or reserve **policy identifiers**, unlike *AMD-2026-007* §5, so there is no governance hook for implementation, testing, or audit.
- The document does not specify how its disclosure duties interact with **primary surface vs operator surface** rules in *AMD-2026-007* §11.4–§11.6 and *AIOS-SPEC-009* §12.4.
- Several key terms are undefined or underdefined, including **user-relevant state**, **materially affects behavior**, **user-comprehensible surface**, **behavioral adaptation**, and **signal families**.
- The addendum lacks a **required specification deltas** section telling AIOS-SPEC-006, AIOS-SPEC-007, and AIOS-SPEC-009 what must change after ratification.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section is clear at a high level, but it does not follow the stronger cross-reference style used in the governing set. The status line links only to the parent amendment file name and not to a specific section of *AMD-2026-007* that this addendum extends. Because the addendum claims to establish “binding shell law,” it should explicitly identify the parent sections it amends or supplements, especially *AMD-2026-007* §4.3, §5, and §11.6. The front matter also uses `cross_references` entries with titles but no `relationship` fields, which is inconsistent with the style used in the bundled ratified documents.

**Scores:** Cross-Document Consistency: 2, Style & Clarity: 4, Legal Enforceability: 3

**Recommendation:**  
Revise the front matter and §0 to identify the governing relationship explicitly. Proposed text:

- Add front matter `relationship` values:
  - `amends` for `AMD-2026-007`
  - `extends` for `AIOS-SPEC-009`
  - `references` for `AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001`

- Replace the Purpose row with:  
  “Supplement *AMD-2026-007* §4.3, §5, and §11.6 by establishing minimum shell disclosure and precision-control duties for logging, memory, behavioral adaptation, signal use, and guardrail posture.”

---

### 1. Purpose

**Feedback:**  
The purpose is understandable and aligned with the broader governance direction, but it is still framed more like a principle statement than amendment text. It should state what legal or architectural gap in *AMD-2026-007* this addendum closes. As written, it does not clearly distinguish between shell disclosure, runtime disclosure, and policy-engine disclosure.

**Scores:** Completeness: 2, Architectural Fidelity: 3, Style & Clarity: 4

**Recommendation:**  
Add a second paragraph that narrows scope and ties it to the shell architecture. Proposed text:

> This addendum governs user-visible shell disclosure and user-facing controls only. It does not alter operator-only evidence requirements, Policy Engine authority, or intent execution rules defined in *AMD-2026-007* §11 and *AIOS-SPEC-009* §9–§15.

---

### 2. Governing principle

**Feedback:**  
This is the document’s central rule, but it is not drafted as enforceable law. The use of `SHOULD` undermines the stated purpose of making user sovereignty a requirement. The phrase “user-relevant state that materially affects behavior” is also too open-ended to support conformance review. A reviewer could not reliably determine what qualifies.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Conflict Freedom: 3

**Recommendation:**  
Convert the principle into a binding rule and define the trigger. Proposed replacement text:

> If the shell or a surrounding runtime captures, infers, stores, or applies state that materially changes user-visible behavior, execution gating, retention, adaptation, or review routing, the shell **SHALL** disclose that state class and, where policy permits, provide user-facing inspection, clearing, or control.

Also add a definitions section or subsection defining:
- **Material state**
- **User-facing control**
- **Inspection**
- **Clearing**
- **Policy permits**

---

### 3. Required disclosure classes

**Feedback:**  
This section is the strongest substantive part of the addendum, but it still leaves too much ambiguity. The phrase “when they materially exist” is unclear. For example, does a dormant telemetry subsystem count as active? Does a configured but disabled memory feature count? The section also does not specify whether disclosure belongs on the primary shell, a settings panel, a disclosure bar, or an operator surface. That omission creates coherence problems with *AMD-2026-007* §11.6 and *AIOS-SPEC-009* §12.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2, Practical Operability: 2

**Recommendation:**  
Split this section into trigger, location, and minimum content. Proposed replacement structure:

> ### 3. Required disclosure classes  
> The shell **SHALL** expose a user-visible disclosure surface for any active or policy-enabled class that can affect the current session or retained user state.  
>
> At minimum, the disclosure surface **SHALL** indicate whether the following classes are: `active`, `inactive`, `policy-required`, or `not available`:  
> 1. session memory or carry-forward  
> 2. transcript logging or retention  
> 3. telemetry / analytics collection  
> 4. behavioral adaptation  
> 5. guardrail or policy mode overrides material to the user path  
> 6. voice analysis or transcript processing  
> 7. review, approval, or escalation gates material to execution or closure  
>
> This disclosure surface **SHALL** be user-facing and **SHALL NOT** require operator privileges to access.

---

### 4. Precision controls

**Feedback:**  
The section correctly identifies the need for granular controls, but it is not operationally complete. “Disable logging where policy permits” is sensible, yet the document does not define what happens when policy does not permit disabling. It also does not distinguish between inspectable status, mutable settings, and immutable compliance controls. That distinction is necessary for legal clarity and user expectation management.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Developer Synchrony: 2

**Recommendation:**  
Add mandatory status semantics and policy-bound behavior. Proposed text:

> For each disclosure class in §3, the shell **SHALL** indicate whether the class is:
> - user-configurable,
> - policy-locked,
> - temporarily unavailable, or
> - operator-controlled only.
>
> Where disabling is not permitted by policy, the shell **SHALL** disclose that the control is policy-locked and identify the reason category (for example: safety, legal retention, enterprise compliance, or execution audit).

Also change “At minimum, precision controls SHOULD distinguish” to “At minimum, precision controls **SHALL** distinguish” if these are intended as minimum mandatory categories.

---

### 5. Behavioral and guardrail settings

**Feedback:**  
This section introduces important concepts but uses mixed normative force. The first paragraph is optional (`SHOULD`), while the second paragraph prohibits invisible behavioral management in some cases. The phrase “when policy allows explicit settings” is too vague, and “visible guardrail posture” is not defined. There is also a coherence issue with *AIOS-SPEC-009* §12.2, which already defines minimum system-state disclosure for execution readiness; this section should say whether it supplements that disclosure or creates a separate class.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 2, Architectural Fidelity: 3

**Recommendation:**  
Clarify the relationship to existing transparency rules and define minimum settings. Proposed text:

> This section supplements, and does not replace, system-state disclosure under *AIOS-SPEC-009* §12.2.  
> Where the product exposes configurable communication or adaptation behavior to end users, the shell **SHALL** present those settings in a user-facing controls surface.  
> Where such behavior is active but not user-configurable due to policy, the shell **SHALL** disclose that the behavior is active and policy-constrained.

---

### 6. Inspectable signal use

**Feedback:**  
This section is conceptually valuable but currently too abstract for a binding addendum. “Signal families” is not a defined term in the governing set. The section also does not distinguish between direct inference used for execution safety and softer personalization signals. Without that distinction, implementation teams will not know what must be surfaced, and legal reviewers will not know what is excluded.

**Scores:** Completeness: 2, Legal Enforceability: 2, Developer Synchrony: 2

**Recommendation:**  
Define the term and scope. Proposed text:

> **Signal family** means a named class of inferred user state used to alter tone, pacing, escalation, review gating, memory behavior, or safety posture.  
> If a signal family is used in production to alter user-visible behavior or execution routing, the shell **SHALL** disclose:
> 1. the signal family name or user-comprehensible label,
> 2. whether it is active for the current session,
> 3. the behavior classes it may influence, and
> 4. whether the user may disable, limit, or clear it.

If some signal families must remain undisclosed for safety or abuse prevention, that exception should be stated narrowly.

---

### 7. Conflict-of-interest disclosure

**Feedback:**  
This is the weakest section from an enforceability perspective. “Meaningful conflicts” and “platform continuity, engagement, or data accumulation” are analytically interesting but not governance-ready. The section reads more like research-derived commentary than amendment text. It also risks creating a broad and subjective disclosure duty that is hard to audit and may conflict with the style guide’s prohibition on vague quantifiers.

**Scores:** Legal Enforceability: 1, Style & Clarity: 3, Conflict Freedom: 3

**Recommendation:**  
Either remove this section from the binding body and move it to a rationale appendix, or rewrite it as a narrow disclosure rule. Proposed replacement:

> The shell **SHALL** disclose when a user-facing setting or retention mode remains enabled by default and materially affects retention, adaptation, or continued session carry-forward beyond the current interaction.  
> The shell **MUST NOT** imply that such behavior is disabled when it remains active by default or by policy.

If the broader conflict-of-interest concept is retained, it should be placed in a non-normative rationale section.

---

### 8. Non-goals

**Feedback:**  
This section is useful and helps prevent overreading, but it should also clarify that the addendum does not require disclosure of operator-only evidence, internal security controls, or protected anti-abuse logic except where those controls materially alter the user path. That would reduce tension with *AMD-2026-007* §11.5 and *AIOS-SPEC-009* §12.4.

**Scores:** Conflict Freedom: 4, Style & Clarity: 4, Completeness: 3

**Recommendation:**  
Add one bullet:

- “require operator-only audit payloads, raw transport traces, or protected anti-abuse logic to appear on the primary user surface, except where a user-visible effect must be disclosed under this addendum”

---

### Final principle

**Feedback:**  
The closing sentence is effective rhetorically, but in a governing document it would be stronger if it either restated a binding rule or was labeled non-normative. As written, it risks duplicating §2 without adding precision.

**Scores:** Style & Clarity: 4, Cross-Document Consistency: 3

**Recommendation:**  
Either label this as “Non-normative principle” or replace it with a short enforceable summary:

> Session disclosure **SHALL** include any active retained, inferred, or policy-constrained state that materially shapes the user’s path through the system.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §2–§7 | Core obligations use `SHOULD` and vague qualifiers, making the addendum weakly enforceable. | Convert intended minimum duties to `SHALL`, define key triggers such as “material,” and narrow subjective phrases like “user-comprehensible” and “meaningful conflicts.” | Critical | 3, 5, 7, 8 |
| 2 | Whole document | No policy register or policy IDs exist for the new disclosure/control duties. | Add a policy section parallel to *AMD-2026-007* §5 with identifiers such as `POL-SHELL-007` through `POL-SHELL-010` for disclosure classes, precision controls, inspectable signal use, and policy-locked settings. | Critical | 1, 3, 5, 9 |
| 3 | Whole document | Cross-document integration is incomplete and does not specify what child specs must change. | Add a “Required specification deltas” section directing updates to *AIOS-SPEC-006* (shell components), *AIOS-SPEC-007* (Workspace disclosure surfaces), and *AIOS-SPEC-009* §12 (transparency model). | High | 1, 5, 6, 9 |
| 4 | §3–§5 | The document does not define where disclosures and controls live or how they relate to primary vs operator surfaces. | Specify a mandatory user-facing disclosure surface and state that operator-only evidence remains governed by *AMD-2026-007* §11.5 and *AIOS-SPEC-009* §12.4. | High | 1, 4, 6, 7 |
| 5 | §4 | Precision controls do not distinguish configurable, policy-locked, and immutable categories. | Require each control class to expose status semantics such as `user-configurable`, `policy-locked`, `operator-controlled`, or `unavailable`. | High | 3, 7, 9 |
| 6 | §6 | “Signal families” is undefined and too abstract for implementation. | Define `signal family`, enumerate minimum affected behavior classes, and state what must be disclosed when such signals alter user-visible behavior. | High | 3, 5, 7, 9 |
| 7 | §7 | Conflict-of-interest disclosure is too subjective for binding amendment text. | Move the current language to a non-normative rationale appendix or replace it with a narrower rule about default-enabled retention/adaptation modes. | High | 3, 8 |
| 8 | Front matter and §0 | Cross-reference metadata and citation style are inconsistent with the bundled governing documents. | Add `relationship` fields in front matter and cite the exact parent sections supplemented by this addendum. | Medium | 1, 8 |
| 9 | §8 | Non-goals do not sufficiently protect operator-only evidence boundaries. | Add an explicit non-goal preserving operator-only audit payloads and protected anti-abuse logic except where user-visible effects must be disclosed. | Medium | 6, 8 |
| 10 | Whole document | The addendum lacks implementation alignment or conformance hooks. | Add an implementation alignment section and a ratification checklist requiring policy index registration, shell component updates, and conformance tests. | Medium | 5, 7, 9 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is conceptually strong and directionally valuable, but it is not yet drafted as enforceable amendment text. Multiple dimensions score at 2, and the composite score is below 3.0, so the rubric requires major revision before ratification.

**Top 3 Actions Required:**
1. Replace vague `SHOULD`-based obligations with defined, testable `SHALL` requirements for minimum disclosure and control duties.
2. Add policy IDs, cross-document implementation deltas, and explicit integration with *AMD-2026-007* §11.5–§11.6 and *AIOS-SPEC-009* §12.
3. Define key terms and mandatory user-facing surfaces so developers and reviewers can determine conformance without interpretation.
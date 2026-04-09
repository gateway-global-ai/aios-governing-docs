---
document_id: AMD-2026-008-ADD-004
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 1.0.0
status: ratified
category: amendment_addendum
title: Pre-Human Browser Review and Visual Proof Gate
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-09
ratification_date: 2026-04-09
cross_references:
  - doc_id: AMD-2026-008-ADD-004-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-008-ADD-004
    relationship: ratification_motion
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
  - doc_id: AMD-2026-008-ADD-001
    title: Base Shell Navigation Primitives and Start-Here Control
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
  - doc_id: AMD-2026-008-ADD-003
    title: Composition Control Plane for Messages, Invites, and Documents
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle (architect → UI → committee → peer review)
  - doc_id: AMD-2026-011
    title: External Repository Acquisition, Quarantine, Promotion, and Minimal Governance Execution Dependencies
  - doc_id: AIOS-SPEC-013
    title: External Repository Acquisition, Analysis, and Promotion
  - doc_id: AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001
    title: Browser review gate — R&D and knowledge capture (AMD-2026-008-ADD-004)
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AIOS-SPEC-006
    title: UI Component Registry Standard
  - doc_id: MPOA
    title: Master Platform Operating Agreement
addendum_history:
  - version: 1.0.0
    date: 2026-04-09
    summary: Ratified from reviewed draft 0.4.0 after approved ratification motion and completed Round 3 PASS evidence.
  - version: 0.4.0
    date: 2026-04-09
    summary: Round 2 author revision — §0.1 policy authority; §4.1 non-waivable proof floor; §6.1 default review-target conformance home; §9-§11 approval/exception/audit taxonomy; §14 conformance artifact alignment.
  - version: 0.3.0
    date: 2026-04-08
    summary: Round 2 prep — §0.2 posture; §2.1 SPEC/MPOA pointers; §3.4 policy-equivalent surfaces; §11.1 implementation seam; §12.4 addendum precedence; deliberate response to Round 1 synthesis (implementation seam, cross-docs, precedence).
  - version: 0.2.0
    date: 2026-04-08
    summary: Phase E — §0.1 definitions; §4.1 proportionality; §6 schema/implementability; §7.2 test-captured proof constraints; §7.3 insufficient; §9.4 remediation/exit from blocked states (Round 1 feedback).
  - version: 0.1.0
    date: 2026-04-08
    summary: Initial doctrine for browser-visible review evidence before human approval on UI-affecting work; informative quarantine record for continuedev/continue pattern study (§16).
---

# AMD-2026-008-ADD-004 — Pre-Human Browser Review and Visual Proof Gate

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`ratified` `1.0.0`** — ratified from reviewed **`draft` `0.4.0`** as an addendum to **AMD-2026-008** |
| **Purpose** | Establish a governed **browser review phase** for UI-affecting work **before** human approval, promotion, or release where visual proof is required. |
| **Does not replace** | **ADD-001** (navigation), **ADD-002** (depth / voice / packaging / BOOK), **ADD-003** (composition control plane). This addendum governs **review evidence**, **browser-visible proof**, and **approval prerequisites** for UI-affecting changes. |
| **Planning alignment** | This addendum codifies the **pre-human approval browser review phase** in the planning lifecycle and provides the minimum evidence needed before a human reviewer approves UI-affecting work. |
| **Artifact vs gate** | **Supporting** **artifacts** **(planning, knowledge, packet)** **may** **be** **healthy** **while** **[AMD-2026-005](AMD-2026-005.md)** **peer-review** **gate** **FAIL** — **revise** **draft** **text** **toward** **Round 2**; **do** **not** **conflate** **packet** **integrity** **with** **ratification** **eligibility**. |

---

## 0.1 Definitions

The following terms **SHALL** be read consistently with **[AMD-2026-005](AMD-2026-005.md)** peer-review thresholds where applicable:

| Term | Meaning |
|------|--------|
| **Browser-visible evidence** | Evidence of **rendered** UI in a **browser** (or **policy-equivalent** governed surface) that a **human reviewer** can **inspect** as a truthful render — **not** code, plans, or pipeline logs **alone**. |
| **Policy** | For this addendum, a **governed** **platform** or **tenant** policy artifact **authorized** for the relevant **surface**, **approval** path, or **exception** path. **Ad-hoc** team practice, oral guidance, or local convention **does not** count as **policy**. |
| **Review target** | A **bounded** record (**§6**) that ties **`review_slug`**, **`required_visual_proofs`**, **`allowed_surfaces`**, and **`approval_scope`** to **one** work item or change set. |
| **UI-affecting** | A change that **materially** affects **rendered** surfaces, **interaction** flows, **user-visible** state, disclosures, gates, or controls described in **§3.1** or **classified** as such by **policy**. |
| **Stale** (capture) | Evidence that **does not** correspond to the **`artifact_version`** / build / environment **declared** in the **review packet** for the **current** review run (wrong branch, commit, deployment, or product **variant**). |
| **Current** (capture) | Evidence **produced** under the **same** review run and **artifact_version** (or **packet id**) the **approval packet** claims. |

---

## 0.2 Revision posture (`draft` `0.4.0` — post-Round 2 revision)

This **`draft` `0.4.0`** is a **deliberate author revision** responding to the completed **Round 2** **FAIL** outcome on **`draft` `0.3.0`**, including the **[Round 2 synthesis](../reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_2/REVIEW_SYNTHESIS.md)** and **[ratification gate report](../reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_2/RATIFICATION_GATE_REPORT.md)**.

| Theme | § |
|-------|---|
| **Policy authority** — **valid** **policy** must be **governed** and **authorized** | **§0.1** |
| **Non-waivable floor** — **§4.1** **cannot** **reduce** **proof** below the addendum minimum | **§4.1** |
| **Default conformance home** — **review target** has a **default** **machine-readable** **artifact** unless policy registers another | **§6.1**, **§14** |
| **Approval taxonomy** — **full**, **partial**, **blocked**, and **exception-based** outcomes must stay auditable | **§9**–**§11** |

**Next state:** **peer review** on a **later** **draft** only after this revision is assessed ready; **not** **Council** **ratification** until **AMD-2026-005** thresholds **PASS** on a subsequent reviewed version.

---

## 1. Purpose

This addendum defines the **browser review gate** for UI-affecting work in AI OS. It requires that when a change affects **rendered surfaces**, **interaction flows**, **state transitions**, **review gates**, **disclosures**, or other user-visible behavior, the system **SHALL** produce browser-visible evidence before human approval is treated as complete.

The purpose of this gate is to prevent approval based only on:
- doctrine text,
- architecture plans,
- UI plans,
- mock descriptions,
- or code assertions,

without confirming that the governed UI actually renders and behaves as intended.

This addendum establishes:
1. when browser review is required,
2. what evidence counts,
3. what minimum proof must be captured,
4. what can and cannot be approved without browser-visible review,
5. and how this phase interacts with planning, execution, and human approval.

---

## 2. Governing principle

For UI-affecting work, **human approval SHALL follow browser-visible review when policy or review target requires visual proof**.

The system **SHALL NOT** treat:
- design plans,
- architecture memos,
- code diffs,
- screenshots from unrelated environments,
- or agent claims of completion

as substitutes for governed browser review where this addendum applies.

A rendered interface is part of system truth.  
For UI-affecting work, approval **SHALL** be based on:
- rendered state,
- visible controls,
- actual behavior,
- and captured evidence,

not only on textual intent.

---

## 2.1 Cross-context pointers (parent and incorporated documents)

Where **UI-affecting** work **intersects** **execution** **scope**, **transparency**, **or** **platform** **economics**, **implementations** **SHALL** **read** **this** **addendum** **together** **with**:

| Document | Role |
|----------|------|
| **[AIOS-SPEC-009](../specifications/IntentPrimitiveAndExecutionModel.md)** | Intent / execution model — **governed** **lanes** **and** **surfaces** **relevant** **to** **what** **must** **be** **proven** **visible**. |
| **[AIOS-SPEC-006](../specifications/UIComponentRegistryStandard.md)** | **Transparency** **and** **registry** **discipline** **where** **UI** **evidence** **ties** **to** **declared** **components** **or** **trust** **claims**. |
| **[MPOA](../core/master_platform_operating_agreement.md)** | **Tier**, **liability**, **and** **economics** **context** **for** **§4.1** **proportionality** **where** **policy** **binds** **cost** **to** **review** **depth**. |

This **section** **does** **not** **introduce** **new** **UI** **control** **requirements** **beyond** **§3**; it **anchors** **browser** **review** **evidence** **to** **parent** **and** **incorporated** **law**.

---

## 3. Scope

### 3.1 In scope

This addendum applies when a work item affects any of the following:

- shell surfaces
- overlays
- canvas views
- navigation states
- input capture states
- review / approve / send / publish controls
- disclosures, warnings, or banners
- blocked / gated user actions
- user-visible state transitions
- browser-rendered workflow steps
- composition surfaces governed by ADD-003
- UI behavior whose absence or misrender would materially change user understanding or trust

### 3.2 Out of scope

This addendum does **not** require browser review for every change. It is not automatically required for:

- pure doctrine edits with no UI implication
- backend-only changes with no UI effect
- internal refactors that do not alter rendered behavior
- policy or ops edits whose effect is not yet exposed to any browser surface
- non-UI automation unless product policy explicitly requires visual proof

### 3.3 Policy extension

Policy **MAY** require browser review for additional classes of work beyond the minimum scope above.

### 3.4 Policy-equivalent surfaces

Where **policy** declares a **non-browser** governed surface **equivalent** to **§0.1** **browser-visible** evidence (for example an **embedded** **webview** **or** **shell-hosted** **surface** **under** **the** **same** **audit** **rules**), that **equivalence** **SHALL** be **recorded** in the **review target** or **policy** and **SHALL** be **subject** to the **same** **capture** **and** **§11** **audit** **discipline** **as** **a** **native** **browser** **capture**.

---

## 4. Trigger conditions

Browser review **SHALL** be required before human approval when any of the following are true:

1. the work item changes a **review target** that declares `required_visual_proofs`;
2. the work affects a user-visible shell state, browser route, or governed surface;
3. the work changes or introduces a disclosure, warning, banner, or approval gate;
4. the work changes a send / publish / export / review / approve control visible in browser UI;
5. the work affects a blocked path, fallback path, or failure-state rendering;
6. the work item is classified by policy as **UI-affecting** or **visual-proof required**.

If applicability is ambiguous, the default posture **SHALL** be:
- browser review required, or
- explicit policy exception recorded with audit visibility.

The system **SHALL NOT** silently assume that browser review is unnecessary.

### 4.1 Policy proportionality

Policy **MAY** define **risk classes** (e.g. **severity** of UI change, **regulated** surface, **tenant** visibility, **blast radius**) that **shape** the **minimum** **visual** proof **or** **approval** **path** for in-scope work.

For any in-scope **UI-affecting** change, **policy SHALL NOT reduce** the non-waivable minimum evidence floor below:

1. **surface proof**;
2. **state proof**;
3. **control proof**;
4. **review packet pointer**.

**Behavior proof** and the **capture checklist** **MAY** be shaped by **policy** or the **review target** above that floor. Any **reduction** of **default** **§7** **minimums** **above** the floor **SHALL** be **explicit** in the **review target**, **policy**, or **§10** **exception** record **with** **audit** visibility. **Policy SHALL NOT use proportionality to convert an otherwise required browser-review gate into implied optionality.**

---

## 5. Phase placement

### 5.1 Pre-human approval phase

Browser review is a **pre-human approval phase**.

The default sequence for UI-affecting work is:

1. doctrine / requirements
2. architect planning
3. UI planning
4. committee packet or planning baseline
5. bounded execution or implementation preparation
6. browser-visible review evidence
7. human approval
8. promotion / merge / release / ratification as applicable

### 5.2 Non-substitution rule

Human approval **SHALL NOT** be recorded as complete for UI-affecting work where this addendum applies unless the browser review phase is satisfied or a policy exception is explicitly recorded.

### 5.3 Relationship to execution lanes

This addendum does not require importing or adopting an external execution repo.  
A bounded local or isolated execution path **MAY** be used. The key requirement is that the system can produce:
- governed browser-visible proof,
- tied to the actual review target,
- before approval.

---

## 6. Review target contract

### 6.1 Required review target

When browser review is required, the system **SHALL** define a bounded **review target** that identifies at minimum:

| Field | Meaning |
|------|--------|
| `review_slug` | Review item identity |
| `allowed_surfaces` | The browser-visible surfaces in scope |
| `required_visual_proofs` | The proofs that must exist before approval |
| `approval_scope` | What human approval is being asked to approve |
| `bounded_objective` | What the implementation is supposed to prove |
| `policy_exceptions` | Any explicit exception to the default browser gate |

Normative **field names** in **§6.1** are **doctrine**. Before any workflow or product **claims conformance** to this addendum, **policy SHALL register** a **canonical machine-readable implementation home** for the **review target** contract, including **schema** location, **storage** location, and **`review_slug`** uniqueness discipline, consistent with **§11.1**. Unless **policy** registers an alternative **governed** artifact, **`REVIEW_TARGET.yaml` SHALL serve as the default machine-readable review-target artifact for conformance claims under this addendum**. This addendum **does not** by itself **name** the **sole** file path in the product repo; it **requires** a **traceable** **home** where **§11** audit fields can be **stored** and **queried**.

### 6.2 Visual proof requirement

A review target **SHALL NOT** be considered satisfied unless each required proof is either:
- captured,
- marked not applicable with reason,
- or blocked with an explicit failure reason.

---

## 7. Minimum browser evidence

### 7.1 Minimum evidence set

For UI-affecting work, the minimum browser evidence **SHALL** include:

1. **surface proof** — the intended surface rendered in browser;
2. **state proof** — the visible state relevant to the work item;
3. **control proof** — the relevant buttons, inputs, or gated actions visible;
4. **behavior proof** — evidence of expected transition, block, or fallback where applicable;
5. **capture checklist** — a checklist or equivalent record of what was verified;
6. **review packet pointer** — a stable link or file reference tying the evidence to the review target.

### 7.2 Acceptable forms

Evidence **MAY** include:
- screenshots
- screen recordings
- structured capture checklists
- rendered browser exports
- **test-captured UI proof** — **only** if **all** of the following hold: **(a)** the capture **maps** to **at least one** entry in **`required_visual_proofs`** for the **review target**; **(b)** the **test** or **harness** is **policy-approved** or **registered** for the **surface** (not ad-hoc scripts **unless** **policy** explicitly allows); **(c)** the output is **human-auditable** (a reviewer can **see** the **same** **rendered** state the test asserts — e.g. screenshot, video, or **governed** **visual** **artifact** tied to the run). **Automated** proof **SHALL NOT** **replace** **human** **approval** where **policy** **requires** **human** **sign-off**; it **counts** toward **§7.1** **only** **together** with **§8.5** evidence integrity.
- equivalent visual evidence allowed by policy

### 7.3 Insufficient evidence

The following do **not** count as sufficient by themselves:
- code diff only
- plan only
- verbal claim that the UI works
- agent-generated description without browser render
- stale screenshot from unrelated version
- design file or mockup without rendered browser confirmation
- **test** **green** **without** **mapped** **visual** **capture** to **`required_visual_proofs`**

---

## 8. Required checks

Where applicable, browser review **SHALL** verify the following categories.

### 8.1 Surface integrity
- expected surface loads
- correct title / context / section identity
- no placeholder garbage
- no broken or empty shell state

### 8.2 Control integrity
- required controls are present
- irrelevant controls are absent
- labels and action semantics are clear
- blocked actions are actually blocked where policy requires

### 8.3 Governance integrity
- required disclosures are visible
- review / approve / send / publish separation is visible where applicable
- draft / final distinctions are visible where applicable
- warnings and fallbacks render correctly

### 8.4 Flow integrity
- navigation behaves correctly
- recovery / restart / continue / choose states behave correctly
- state transitions occur as intended
- failure and fallback states are understandable

### 8.5 Evidence integrity
- captures map to the review target
- captures are current to the review run
- missing proofs are explained
- the approval packet can be independently reviewed by a human

---

## 9. Approval rule

### 9.1 Human approval precondition

Where this addendum applies, human approval **SHALL NOT** be treated as complete unless:

- required browser-visible proofs exist,
- the capture checklist is complete,
- missing proofs are either resolved or explicitly accepted by policy exception,
- and the approval scope matches the review target.

The approval record **SHALL** preserve **`human_approval_status`** as **`approved`**, **`partially_approved`**, **`blocked`**, or **`approved_by_exception`**, or a **policy-approved** equivalent that preserves the same distinctions.

### 9.2 Blocked approval

If required visual proof is missing, stale, or contradictory, **`human_approval_status` SHALL be `blocked`**. The recorded blocked state **SHALL** be one of:

- `blocked_pending_browser_review`
- `blocked_pending_visual_proof`
- `review_required`
- or equivalent policy-approved blocked state

The system **SHALL NOT** silently advance to approved.

### 9.3 Partial approval

Policy **MAY** allow partial approval for bounded surfaces if:
- approval scope is explicit,
- missing surfaces are outside scope,
- and the packet clearly states what was and was not approved.

A **partial approval** record **SHALL** identify the **approved** surfaces, **excluded** surfaces, and any **actions** that remain **blocked**.

### 9.4 Remediation and exit from blocked states

When approval is **blocked** (**§9.2**), the system **SHALL** support a **recorded** path to **exit** the block **without** **silent** **approval**:

1. **Resubmit** — supply **missing** or **replacement** **non-stale** captures; update **`captured_proofs`** and **`missing_proofs`** (**§11**).
2. **Narrow scope** — **§9.3** **partial** **approval** with **explicit** **packet** text **reducing** **`approval_scope`**.
3. **Policy exception** — **§10** **explicit** **exception** with **audit** record.
4. **Escalation** — **policy** **SHALL** define **who** may **authorize** **timeline** **extension** or **coordinate** **remediation** **without** treating **delay** **alone** as **§10** **substantive** **exception**.

Policy **MAY** define **SLAs** or **targets** for **remediation**; **absence** of **SLA** **does** **not** **imply** **approval** (**§10.3**).

---

## 10. Exceptions

### 10.1 Policy exception required

Any decision to approve UI-affecting work without browser-visible review where this addendum would otherwise apply **SHALL** require an explicit policy exception with audit visibility.

### 10.2 Minimum exception record

The exception record **SHALL** state:
- why browser review was not performed,
- who authorized the exception,
- what risk was accepted,
- and what approval scope remains valid.
- whether the exception is **one-time** or **reusable**,
- which **surface**, **release path**, or **approval scope** it covers,
- what **time window** it remains valid for,
- and which **requirement** it waives (**proof capture**, **timing**, or another specific obligation).

### 10.3 No implied exception

The absence of evidence is **not** an exception.  
The absence of time is **not** an exception.  
The assumption that a code change is small is **not** an exception by itself.

### 10.4 Exception authority and bounded use

An exception under this section **SHALL** be granted only by authority recognized in a valid **policy** under **§0.1**. In the absence of such **policy**, **no exception may be granted**. An exception **SHALL NOT** be read to waive requirements beyond the specific **scope**, **time window**, and **obligation** recorded in the exception record.

---

## 11. Audit posture

For each governed browser review, the system **SHALL** preserve an auditable record of at least:

| Field | Meaning |
|------|--------|
| `review_slug` | Review identity |
| `approval_scope` | What was being approved |
| `allowed_surfaces` | Surfaces in scope |
| `required_visual_proofs` | Required proofs |
| `captured_proofs` | Captured evidence set |
| `missing_proofs` | Missing items with reason |
| `exception_state` | Exception posture, including whether none, requested, denied, or approved, and pointer to the exception record where used |
| `human_approval_status` | `approved`, `partially_approved`, `blocked`, or `approved_by_exception`, or a policy-approved equivalent preserving the same distinctions |
| `review_date` | Date of review |
| `artifact_version` | Version, build, commit, or equivalent release identity for the reviewed artifact |

Policy **MAY** extend this with screenshots, hashes, trace ids, or other evidence.

The audit record **SHALL** be preserved in a **traceable** location linked to the **review target** and **approval packet**. Where an **exception** is used, the audit trail **SHALL** preserve the **exception authority**, **waived requirement**, **affected scope**, and **validity window**.

### 11.1 Implementation seam (audit storage)

The **§11** **field** **set** **SHALL** be **realizable** in a **governed** **store**, **registry**, **or** **operations** **artifact** **named** **by** **policy** **or** **referenced** **operations** **document**. **Policy** **SHALL** **either** **name** **the** **canonical** **registry** **identifier** **for** **`review_slug`** **and** **`artifact_version`** **or** **cite** **an** **operations** **document** **that** **defines** **storage**, **query**, **and** **retention** **for** **browser** **review** **records**. **This** **addendum** **SHALL** **not** **be** **read** **as** **permitting** **orphan** **audit** **fields** **with** **no** **system** **home**.

---

## 12. Relationship to other addenda

### 12.1 ADD-001
ADD-001 governs navigation primitives.  
This addendum governs the requirement to prove their browser-visible behavior before approval where visual proof is required.

### 12.2 ADD-002
ADD-002 governs output depth, shell voice controls, packaging, and BOOK workflow.  
This addendum governs browser-visible review of those UI-affecting surfaces and gates where review targets require visual proof.

### 12.3 ADD-003
ADD-003 governs composition class, composition contract, disclosure, knowledge-basis, originality, and reference-guided composition.  
This addendum governs the browser-visible review phase used to verify that those controls are actually rendered and understandable to the user before approval.

### 12.4 Addendum precedence (ratified vs draft)

Where **§12** **references** **ADD-001**, **ADD-002**, and **ADD-003** **together**, **normative** **obligations** **from** **ratified** **addenda** **take** **precedence** **over** **draft** **addenda** **where** **both** **would** **apply** **to** **the** **same** **user-visible** **surface**, **until** **draft** **addenda** **are** **ratified** **or** **reconciled** **by** **Council** **or** **policy**. **ADD-004** **does** **not** **adjudicate** **substantive** **conflicts** **between** **addenda**; it **requires** **browser-visible** **proof** **of** **behavior** **under** **the** **governed** **text** **in** **force** **for** **the** **release** **lane** **being** **approved**.

---

## 13. Non-goals

This addendum does **not**:
- define the full UI design system,
- define every test automation format,
- require a separate external execution repo,
- replace human judgment,
- ratify code by itself,
- or convert browser review into automatic production approval.

It establishes the **minimum browser-visible proof gate before human approval** for UI-affecting work.

---

## 14. Recommended artifacts

The following artifacts are recommended when this addendum applies. Unless **policy** registers an alternative **governed** implementation home under **§6.1**, **`REVIEW_TARGET.yaml` SHALL serve as the default machine-readable review-target artifact for conformance claims under this addendum**:

- `REVIEW_TARGET.yaml`
- `HUMAN_REVIEW_PACKET.md`
- `CAPTURE_CHECKLIST.md`
- `EXECUTION_TRANSACTION.json`
- browser screenshots or recordings
- approval notes tied to the review target

Equivalent artifacts **MAY** be used if policy permits and auditability is preserved.

---

## 15. Decision rule

If the work is UI-affecting and the review target requires visual proof:

- **no browser proof** → **no human approval**
- **partial proof** → **partial or blocked approval only**
- **complete proof** → **eligible for human approval**
- **human approval** → still separate from promotion / merge / release / ratification

That separation **SHALL** be preserved.

---

## 16. Informative external reference (quarantine)

This addendum **does not** incorporate third-party code or establish a runtime dependency. For **pattern study** only (source-controlled checks, CI-oriented agent workflows), the following repository is **registered under quarantine** per **[AMD-2026-011](AMD-2026-011.md)** and **[AIOS-SPEC-013](../specifications/ExternalRepositoryAcquisitionAnalysisAndPromotion.md)**:

| Field | Value |
|-------|--------|
| **URL** | `https://github.com/continuedev/continue` |
| **Role** | Informative reference — not adopted law, not default tooling |
| **Governed record** | [`sources/AMD-2026-008-ADD-004/external_reference_quarantine.md`](../sources/AMD-2026-008-ADD-004/external_reference_quarantine.md) |

Promotion beyond **quarantine** (if any) **SHALL** follow **AIOS-SPEC-013** and organizational policy; this addendum only **names** the reference for **review** and **traceability**.

---

*End of AMD-2026-008-ADD-004, version 1.0.0 (ratified).*

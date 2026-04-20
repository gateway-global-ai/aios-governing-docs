---
document_id: AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001
version: 0.1.3
status: draft
category: reference
title: Shell-first governing document and artifact plan
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-SHELL-BASELINE-RECOVERY-PACKET-001
    title: Shell baseline recovery packet and review path
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AMD-2026-012
    title: Shell Authority and Voice-First Entry
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy
  - doc_id: AIOS-KNOWLEDGE-BASE-REVIEW-INTERFACE-MODEL-001
    title: Knowledge-base review interface model
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
  - doc_id: AMD-2026-014
    title: Governed Authoring Knowledge Inputs and Bounded Author-Like Drafting
  - doc_id: AMD-2026-016
    title: Governed Non-Human Principals and Deterministic Routed Authority
note: Non-ratified shell-first plan that defines the reviewed document stack, pre-artifact gates, and phased artifact program to follow shell-baseline approval.
---

# AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001

## Purpose

Define the first trustworthy, review-first path from shell-baseline recovery into governed document and artifact creation.

This plan exists because the shell baseline can no longer be treated as an implied foundation. It must be explicitly extracted, reviewed, approved, and then translated into a phased artifact program that preserves authority boundaries.

## Positioning

This plan is a **reference implementation document plus supporting packet**, not immediate doctrine.

Its role is to:

1. define the shell-first artifact program
2. define the prompt-chain and review-chain that produce that program
3. block downstream artifact creation until the plan itself passes peer review and human approval

If peer review proves that the current doctrine is insufficient, the result is not silent scope drift. The result is a later narrow addendum or amendment opened explicitly from reviewed evidence.

## Scope boundary

This plan is limited to the **shell foundation slice**:

- shell environment and controls
- shell authority and disclosure surfaces
- account-entry, account-profile, and account-administration baseline requirements
- document and folder baseline requirements
- voice-lane and shell-state control requirements
- the review surface needed to inspect and approve these artifacts

This plan does **not** yet authorize broader tenant workflows, marketplace expansion, or unrelated workspace redesign.

## Preconditions

No downstream shell artifact lane may rely on this plan until all of the following are true:

1. planning runs are lane-local, template-bound, and traceable to declared manifest and bundle inputs
2. architect and UI runs are validated at the same strength
3. authoring runs emit reviewable run records under the bounded-authoring rules
4. the shell-first plan packet has completed peer review
5. a human approval decision has been recorded in the governing review artifacts before execution expands:
   - `reviews/aios_shell_governing_document_and_artifact_plan_001/round_<N>/PACKET_STATUS.yaml` records gate state
   - `reviews/aios_shell_governing_document_and_artifact_plan_001/round_<N>/HANDOFF_NOTE.md` records rationale and reviewer-facing disposition
   - `reference/knowledge_base/review_surface/REVIEW_STATUS.yaml` records the review-surface approval posture

## Governing inputs

The minimum governing input set for this plan is:

- shell doctrine anchors already identified by `AIOS-SHELL-BASELINE-RECOVERY-PACKET-001`
- shell implementation evidence from `ai-os-voice-interface`
- planning lifecycle and intake-scaffold governance
- review-packet taxonomy and review-surface model
- bounded authoring rules when editorial drafting support is used

This plan therefore depends on declared packets, not ambient context.

## Governing input map

| Input artifact | Why it is required | What this plan uses it for |
|----------------|--------------------|----------------------------|
| `reference/implementation/AIOS-SHELL-BASELINE-RECOVERY-PACKET-001.md` | freezes the shell-baseline extraction problem | shell-first boundary and baseline gap source |
| `reference/knowledge_base/snapshots/product_context_bundle.md` | preserves current implementation truth | shell evidence and screen/control reality |
| `reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md` | governs pre-ratification phase order | architect, UI, committee, and review sequencing |
| `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md` | governs lane-local packets and status artifacts | reviewable status mutation and fail-closed planning behavior |
| `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md` | governs round packet structure | `PACKET_IDENTITY.yaml`, `PACKET_STATUS.yaml`, `PACKET_EVENTS.yaml`, `HANDOFF_NOTE.md` |
| `reference/implementation/AIOS-KNOWLEDGE-BASE-REVIEW-INTERFACE-MODEL-001.md` | governs human-facing approval surfacing | review-surface publication and approval visibility |
| `reference/implementation/AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md` | governs bounded author-like drafting support | manifest discipline and run-record expectations |
| `amendments/AMD-2026-014-governed-authoring-knowledge-inputs-and-bounded-author-like-drafting.md` | binding authoring-input rule set | non-authority rule and reviewable run records |
| `amendments/AMD-2026-012.md` and `AIOS-SPEC-009` | shell authority and execution-law anchors | shell authority, separation of powers, and promotion boundary |
| `amendments/AMD-2026-016.md` | governs non-human principals and deterministic routed authority | service-account binding, agent/application separation, routed non-human communication, and audit duty |

## Output stack

The shell-first stack begins with reviewed planning artifacts, not execution artifacts.

### Stage A — review target

- this reference document
- the shell-first supporting packet under `reviews/aios_shell_governing_document_and_artifact_plan_001/packet_2026-04-10/`
- peer-review outputs under `reviews/aios_shell_governing_document_and_artifact_plan_001/round_1/`

Stage A packet contents are:

- `PLAN_SCOPE.md`
- `PLAN_TOC.md`
- `PHASE_SEQUENCE.md`
- `META_PROMPT_CHAIN.md`
- `README.md`

### Stage B — post-approval execution lanes

Only after Stage A clears review may the system open phase-bounded artifact work. Those later lanes may include:

- architect and UI planning packets
- shell doctrine-support drafts
- developer and implementation documentation
- review-surface artifacts
- future amendment or addendum planning only if explicitly required

## Shell-first TOC

The governing document and artifact program should follow this table of contents.

| Section | Purpose | Output class |
|---------|---------|--------------|
| 1. Authority and source declaration | Freeze the declared source set, authority order, and shell-first boundary | packet + reference |
| 2. Shell baseline target | Define the exact shell capabilities and surfaces that must exist before expansion | packet + plan |
| 3. Artifact taxonomy | Define which artifacts are planning-only, review-only, implementation-support, or later doctrine candidates | reference |
| 4. Prompt-chain and run-trace model | Define the declared-input planning chain and required run records | reference + prompt set |
| 5. Pre-artifact review gate | Route the plan itself through peer review and human approval | review packet |
| 6. Phase 1 shell authority surfaces | Design shell authority, shell/user distinction, non-human principal binding, disclosure, and state control | later phase packet |
| 7. Phase 2 account and identity surfaces | Design greeting, new-vs-returning path, account creation, OTP or magic-link verification, profile display/edit, admin account-view surfaces, service-account identity, and governed access-level administration | later phase packet |
| 8. Phase 3 document and folder baseline | Design document create/edit/save/rename/delete flows, recycle-bin lifecycle, and their human/non-human storage boundaries | later phase packet |
| 9. Phase 4 voice-lane and agent controls | Design dual voice lanes, provider switching, agent, application, and service-account control paths, and prompt controls | later phase packet |
| 10. Phase 5 output packaging and review surface | Design output-depth progression, artifact packaging, and human-facing review navigation | later phase packet |
| 11. Phase 6 doctrine escalation test | Decide whether reviewed gaps require a narrow addendum or amendment | later gate |

## Phase sequence

The shell-first program uses a gated sequence rather than a single artifact burst.

1. Extract current shell truth and shell gaps.
2. Produce a reviewed shell-first governing plan from declared inputs.
3. Review the plan before any downstream artifact lane opens.
4. After approval, open one bounded phase packet at a time.
5. Review each phase packet before using it to create doctrine or implementation-support artifacts.
6. Open doctrine work only when review proves the current law is insufficient.

## Failure and rework handling

If any of the following occur, the plan returns to the most recent approved state and may not advance:

| Failure condition | Required action | Blocking effect |
|------------------|-----------------|-----------------|
| Review packet fails validation | repair taxonomy or metadata first | no peer-review decision may be treated as valid |
| Round review returns `major_revision_required` or gate `fail` | revise the plan document and rerun review | no downstream shell artifact lane may open |
| Shell evidence becomes stale relative to product changes | refresh the shell-baseline packet and any declared snapshots, then revise the plan if needed | current plan review basis is frozen as historical evidence only |
| A later phase packet fails review | return to the most recent approved phase boundary and record remediation requirements before retry | no later phase may proceed |
| Human approval is withheld | keep the plan in reviewed-but-not-approved state and stop before artifact creation | downstream work remains exploratory only |

## Phase 2 minimum account-administration requirement

Phase 2 is not limited to end-user onboarding and profile maintenance.

The shell-first baseline must also define governed administrative account capabilities, at minimum:

- an admin-visible account roster or equivalent account-view surface
- the ability for an authorized administrator to inspect account identity and current access posture
- the ability for an authorized administrator to change access level or role assignment through a governed control path
- explicit disclosure of who may perform those actions and what review or audit trail is required

Without those admin account-administration surfaces, the shell baseline remains incomplete even if ordinary account creation and profile editing exist.

## Meta-prompted planning chain

The plan-generation chain is explicit:

1. Collect declared governing inputs and shell evidence.
2. Generate a shell-first TOC only.
3. Generate one bounded phase brief per TOC section.
4. Consolidate those briefs into the reviewed governing-plan document.
5. Send that consolidated plan through peer review.
6. Block artifact creation unless the plan clears review and human approval.
7. After approval, repeat the same declared-input pattern phase by phase.

The chain is a planning contract, not an automation shortcut. It exists to make prompt logic reviewable.

## Operator command surface

The shell-first plan is expected to be operated with concrete command surfaces, not only prose.

```bash
py -3 scripts/build_agent_kb.py --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --output-dir reviews/<slug>/planning/agent_kb
py -3 scripts/ollama_planning_agent.py --role architect --amd-slug <slug> --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md
py -3 scripts/ollama_planning_agent.py --role ui --amd-slug <slug> --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md
py -3 scripts/ollama_authoring_agent.py --mode editorial --manifest reference/knowledge_base/agents/style/JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml --prompt "Draft the shell-first governing plan." --output <path>
py -3 scripts/peer_review.py reference/implementation/AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001.md --round <N> --smart-context --expanded --product-context
py -3 scripts/validate_review_packet.py --round-dir reviews/aios_shell_governing_document_and_artifact_plan_001/round_<N>
```

These commands are not execution authority. They are the auditable plan-generation and review surfaces for this shell-first program.

## Run-record minimum fields

The planning and authoring runs used by this plan must expose at least:

- selected role or mode
- selected manifest path
- selected bundle path when applicable
- output path
- tool invocation identity
- reviewable timestamp

This plan relies on those fields so reviewers can test whether a draft was produced from the declared knowledge packet rather than hidden context.

## Review record and approval mechanism

The approval path for this plan is explicit:

1. `peer_review.py` creates the `round_<N>/` review packet.
2. `validate_review_packet.py` must pass for that round.
3. `PACKET_STATUS.yaml` records whether the review gate failed or passed.
4. `HANDOFF_NOTE.md` records the rationale and any required remediation.
5. `REVIEW_STATUS.yaml` on the review surface records whether the plan is still pending human review or has been accepted for the shell-first interface.

If those artifacts do not exist or disagree, the plan is not approved.

## Artifact-creation rule

No actual shell artifact lane may begin merely because a model produced a plausible plan.

The plan must first have:

- declared inputs
- traceable planning and authoring runs
- peer-review output
- recorded human approval

Without those conditions, any downstream shell artifact is exploratory only and must not be treated as approved foundation work.

## Escalation rule

Escalate from supporting packet to doctrine only if peer review or later phase review identifies one or more of the following:

- missing binding authority for shell control surfaces
- unresolved authority separation between shell, operator, and user
- missing law for account, account-administration, storage, or voice-lane baseline behavior
- taxonomy gaps that prevent stable review and ratification routing

If no doctrine gap is proven, remain in the reviewed reference-and-packet lane.

## Acceptance condition

This plan is fit to act as the shell-first foundation gate only when:

1. the plan is grounded in declared shell evidence and doctrine
2. the prompt-chain and run-trace rules are explicit
3. the pre-artifact review gate is explicit
4. the downstream phase structure is explicit
5. peer review confirms that the plan is specific enough to govern later artifact work without silent scope drift
6. the approval record is explicit enough that an operator can prove whether the plan is pending, rejected, or approved without relying on chat memory

---

*Reference plan — AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001 — v0.1.2.*

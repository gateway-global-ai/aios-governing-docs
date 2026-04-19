---
document_id: AMD-2026-008-ADD-005
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 0.7.0
status: draft
category: amendment_addendum
title: Voice-First Rendered Session Proof and Artifact Checks
author: Gateway Global AIOS
created: 2026-04-17
last_updated: 2026-04-17
cross_references:
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
  - doc_id: AMD-2026-008-ADD-004
    title: Pre-Human Browser Review and Visual Proof Gate
  - doc_id: AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001
    title: Browser review gate - R&D and knowledge capture
  - doc_id: AIOS-VOICE-TTS-ARCHITECTURE-STANDARD-001
    title: AI OS Voice TTS Architecture Standard
note: Draft addendum to AMD-2026-008 extending the browser-proof family so voice-first systems that generate UI components on the fly must produce rendered session proof and artifact checks rather than relying on coding-agent summaries.
---

# AMD-2026-008-ADD-005 — Voice-First Rendered Session Proof and Artifact Checks

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`draft` `0.7.0`** — addendum to **[AMD-2026-008](AMD-2026-008.md)** |
| **Purpose** | Extend the browser-proof family for voice-first systems that generate or revise UI on the fly, so rendered session truth and artifact checks are required after meaningful sessions. |

## 0.1 Definitions

| Term | Meaning |
|------|---------|
| **Meaningful session** | A voice-first run that results in one or more of the following objective events: creation or modification of a file in a governed repository, registration or update of a component or artifact in the AIOS UI Component Registry or governed kit family, change to shell or navigation state that persists beyond the current browser session, or generation of a user-visible disclosure, warning, gate, or control surface. |
| **Voice-first generated UI** | User-facing UI whose rendered state, structure, route, or controls are created or revised during a voice-led workflow rather than remaining static across the session. |
| **Rendered session proof** | Governed browser-visible or policy-equivalent evidence showing the rendered state, active controls, and required disclosure surfaces for a meaningful session. |
| **Session artifact pointer** | A stable, machine-readable reference to the governed storage location for the session review artifacts, review packet, or equivalent review target evidence, keyed by `session_id`, `review_slug`, or an equivalent governed identifier. |

## 1. Purpose

This addendum exists to prevent summary substitution in voice-first AI lanes.

If a system uses Voice AI while generating or modifying UI components during the working session, the system SHALL NOT rely only on coding-agent summaries, planner summaries, or generic completion reports as proof that the user-visible system is healthy.

## 2. Governing principle

For voice-first generated UI, rendered session truth SHALL outrank summary claims.

## 3. Browser viewer requirement

When a voice-first lane generates or revises user-facing UI, the workflow SHALL include a governed browser viewer such as Playwright or an equivalent browser inspection surface after each meaningful session.

The browser viewer requirement SHALL be recorded in a `Review Target` governed by `AMD-2026-008-ADD-004`.

Where voice-first generated UI is in scope, the review target SHALL record that session proof is required and SHALL identify the governed storage home for the resulting proof artifacts, consistent with `AMD-2026-008-ADD-004 §6.1` and `§11.1`.

Equivalent inspection surfaces SHALL be policy-authorized and SHALL be subject to the same audit discipline as native browser captures.

Where a workflow uses a DCP or equivalent governed promotion layer, that layer SHALL validate the required session-proof artifact against the Section 4.2 contract before the workflow is treated as approval-ready.

The goal is to inspect:

- rendered output
- visible shell state
- disclosure surfaces
- navigation state
- component presence and absence
- session-critical controls

## 4. Required artifact checks

Voice-first generated-UI lanes SHALL produce artifact checks covering at minimum:

1. rendered surface proof
2. current route or shell region
3. active disclosure state where applicable
4. active logging / memory / guardrail states where user-visible
5. component integrity
6. review packet or session artifact pointer

The session artifact pointer SHALL be a stable, machine-readable reference to a governed storage location linked to the active `review_slug`, packet, or equivalent review target record.

## 4.1 Session-proof contract

Unless policy registers an alternative governed artifact, `SESSION_PROOF.yaml` SHALL serve as the default machine-readable conformance artifact for this addendum.

`SESSION_PROOF.yaml` SHALL be a subordinate conformance artifact of the governing `REVIEW_TARGET.yaml` record under `AMD-2026-008-ADD-004`, and SHALL NOT replace or compete with the review-target contract itself.

For voice-first generated UI, `SESSION_PROOF.yaml` SHALL extend `REVIEW_TARGET.yaml` with session-level proof evidence and SHALL be treated as an additional constraint on the review target rather than a replacement for it.

When a meaningful session generates UI requiring proof under this addendum and no `REVIEW_TARGET.yaml` yet exists, the system SHALL create a minimal governed `REVIEW_TARGET.yaml` with:

- `review_slug` derived from `session_id`
- `required_visual_proofs` set to the session-proof requirements
- `approval_scope` set to the affected session-bound UI change

The session-proof artifact SHALL identify at minimum:

- `session_id`
- `review_slug`
- `required_checks`
- `captured_proofs`
- `missing_proofs`
- `compliance_status`
- `session_artifact_pointer`
- `artifact_version`

This contract SHALL remain traceable to the governing review target and approval packet for the same change.

By default, `REVIEW_TARGET.yaml` remains the governing review-target artifact and `SESSION_PROOF.yaml` supplies additional session-bound evidence under that same review identity.

### 4.2 Session-proof schema

The `SESSION_PROOF.yaml` contract SHALL follow at minimum this normative field shape:

| Field | Type | Rule |
|-------|------|------|
| `session_id` | string | Stable identifier for the reviewed session. |
| `review_slug` | string | SHALL match the governing review target identity. |
| `required_checks` | array of strings | SHALL enumerate the checks required for that session. |
| `captured_proofs` | array | SHALL list the proof artifacts actually captured. |
| `missing_proofs` | array | SHALL list any required proof still absent. |
| `compliance_status` | enum | SHALL be one of `ready`, `blocked`, `approved_by_exception`. |
| `session_artifact_pointer` | string | SHALL point to the governed storage home for the evidence set. |
| `artifact_version` | string | SHALL identify the rendered artifact, build, or packet version under review. |
| `dcp_integration` | object | SHALL record promotion-state integration where a DCP or equivalent governed promotion layer is present. |

Each entry in `captured_proofs` SHALL declare at minimum:

- `check_type`
- `proof_pointer`
- `captured_at`

When `dcp_integration` is present, it SHALL declare at minimum:

- `promotion_state`
- `dcp_job_id`
- `validation_timestamp`

For sessions requiring proof:

- `required_checks` SHALL NOT be empty
- `missing_proofs` SHALL be empty before `compliance_status` may be `ready`
- when `missing_proofs` is non-empty, `compliance_status` SHALL be `blocked` unless an exception is recorded under Section 10
- when `compliance_status` is `blocked`, `dcp_integration.promotion_state` SHALL be `blocked` where a DCP or equivalent governed promotion layer is present

## 5. Summary non-substitution rule

The following SHALL NOT be treated as sufficient by themselves for voice-first generated UI:

- coding-agent summary
- planner summary
- implementation note
- completion status message
- test pass with no browser-visible mapped proof

## 6. Session review cadence

For voice-first generated UI, rendered review SHALL occur after each meaningful session.

End-of-burst review alone SHALL NOT satisfy this cadence.

Policy MAY classify a session as not meaningful only through the governing review target or an explicit policy record created before approval is requested. Convenience alone SHALL NOT narrow the cadence.

Policy MAY define batching rules where multiple voice-first sessions within a governed time window and under the same `review_slug` MAY be treated as one proof unit, provided:

- all batched sessions are recorded in the audit trail
- the final proof covers all UI changes from the batched sessions
- `SESSION_PROOF.yaml` declares which sessions were batched

## 7. Decision rule

If a meaningful session lacks the required rendered session proof or artifact checks:

- the session output SHALL be marked non-compliant for promotion or approval
- summary-only evidence SHALL NOT be accepted as a substitute
- human approval SHALL NOT proceed until the missing rendered proof is supplied
- the audit trail SHALL record the blocked compliance status for that session
- promotion workflows SHALL treat that blocked compliance status as ineligible for approval-ready state
- where a DCP is present, the DCP SHALL reject promotion attempts for session-bound artifacts while `compliance_status` remains `blocked`

## 8. Relationship to ADD-004

This addendum does not replace `AMD-2026-008-ADD-004`.

Instead:

- `ADD-004` remains the parent browser-visible approval gate
- this addendum imposes a higher-frequency session-proof requirement for voice-first generated UI sessions
- summary-only approval remains prohibited where rendered proof is required

## 9. Audit posture

For each meaningful session requiring proof, the system SHALL preserve an auditable record containing at minimum:

- `session_id`
- `review_slug` or equivalent review-target identifier
- `required_checks`
- `captured_proofs`
- `missing_proofs`
- `compliance_status`
- `artifact_version` or equivalent rendered version identifier
- `captured_at`

These records SHALL remain joinable to the governing review target, packet, or approval record for the same change.

Policy SHALL name the canonical storage, query, and retention home for these records, or SHALL cite an operations document that defines that home, so the audit fields do not remain orphaned.

Where policy is silent, the default storage home SHALL be the governed review packet location for the active review target, with `SESSION_PROOF.yaml` stored under `{review_slug}/session_proof/{session_id}/SESSION_PROOF.yaml` and linked from the approval packet.

The DCP or equivalent governed promotion layer SHALL discover `SESSION_PROOF.yaml` through a policy-approved method such as governed repository scanning, runtime notification, or governed registry lookup, and that discovery method SHALL be named in the operations document or policy cited by this section.

## 10. Exceptions

Session-proof requirements MAY be waived only through an explicit governed policy exception.

Exceptions SHALL only be granted when:

- the required browser or inspection surface is technically unavailable
- the session produced only trivial UI changes as defined by policy
- an emergency security or integrity patch requires immediate deployment

Any such exception SHALL record:

- the requirement being waived
- the governing authority granting the exception
- the reason and risk accepted
- the validity window
- the compensating evidence or alternative review path, if any

Any exception SHALL include a remediation plan to capture equivalent proof within the policy-defined recovery window.

Ad-hoc team practice, convenience, or missing automation SHALL NOT count as a valid exception by themselves.

## Final principle

If the system can change the visible UI during a voice-first session, then the rendered session itself becomes part of the evidence surface and must be reviewed as such.

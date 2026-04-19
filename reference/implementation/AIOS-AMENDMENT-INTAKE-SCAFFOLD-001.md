---
document_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
version: 0.1.2
status: draft
category: reference
title: Amendment intake scaffold standard
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-09
cross_references:
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AMD-2026-005
  - doc_id: AMD-2026-010
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
amendment_history:
  - version: 0.1.2
    date: 2026-04-09
    summary: Stage 3B architect-lane quality/evidence hardening freeze: template-based output conformance validation, bundle/build-manifest correspondence checks, deterministic snapshot freshness blocking, and direct-command governance distinction.
  - version: 0.1.1
    date: 2026-04-08
    summary: Stage 3A architect-lane hardening freeze: bundle/build-manifest preconditions, required snapshot presence when manifest-selected, output verification, slug/path reconciliation, and override audit visibility.
  - version: 0.1.0
    date: 2026-04-08
    summary: Stage 2 freeze for the amendment intake scaffold: artifact taxonomy, authority seams, state machine, and read-only orchestration defaults.
---

# Amendment intake scaffold standard

**Purpose:** Freeze the Stage 2 scaffold for a local-first amendment intake orchestrator that follows the existing governed process already present in this repository.

**Scope:** This document freezes the **scaffold**, **state model**, **artifact taxonomy**, and **authority boundaries** for intake orchestration. It does **not** create new process law. It does **not** replace **[AMD-2026-005](../../amendments/AMD-2026-005.md)**, **[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)**, or **[AMD-2026-010](../../amendments/AMD-2026-010.md)**.

**Read this with:** **[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** for the existing planning flow, **[AMD-2026-005](../../amendments/AMD-2026-005.md)** for binding peer-review / ratification law, **[reviews/README.md](../../reviews/README.md)** for review-tree operations, and **[AIOS-REVIEW-PACKET-TAXONOMY-001](AIOS-REVIEW-PACKET-TAXONOMY-001.md)** for the identity / status / events / handoff discipline reused here.

---

## 1. Binding posture

1. This scaffold **SHALL NOT** redesign the governed amendment lifecycle already documented in the repository.
2. The intake scaffold **SHALL** orchestrate the existing process:
   - evidence / knowledge building
   - architect planning
   - UI planning
   - committee packet preparation and manual committee recording
   - author revision flagging / completion recording
   - binding peer review through **`scripts/peer_review.py`**
   - advisory kernel shadow lane
   - ratification handoff preparation
3. The intake scaffold **SHALL NOT** replace:
   - **`scripts/peer_review.py`**
   - committee judgment
   - kernel reviewer judgment
   - ratification approval / execution
4. Default execution mode **SHALL** be orchestration-first and **read-only with respect to doctrine**:
   - amendment files
   - specification files
   - ratification motions
   - other governed normative text
5. The scaffold **MAY** write non-doctrine process artifacts under the review tree:
   - `reviews/<slug>/intake/`
   - `reviews/<slug>/planning/`
   - `reviews/<slug>/kernel/`
   - `reviews/<slug>/ratification/`

---

## 2. Intake artifact taxonomy

The intake scaffold **SHALL** persist state under:

```text
reviews/<slug>/intake/
```

Required artifacts:

```text
reviews/<slug>/intake/
├── INTAKE_IDENTITY.yaml
├── INTAKE_STATUS.yaml
├── INTAKE_EVENTS.yaml
└── HANDOFF_NOTE.md
```

Ownership rules:

| Artifact | Authority | Allowed content |
|----------|-----------|-----------------|
| `INTAKE_IDENTITY.yaml` | Stable intake identity | Document ID, paths, schema version, creation metadata, current head version |
| `INTAKE_STATUS.yaml` | Current workflow truth | Lifecycle state, committee status, verification status, peer-review status, kernel status, ratification handoff status, next action |
| `INTAKE_EVENTS.yaml` | Append-only process memory | Ordered event history with evidence paths |
| `HANDOFF_NOTE.md` | Non-authoritative operator prose | Warnings, reminders, operator instructions only |

**Hard rule:** `HANDOFF_NOTE.md` **SHALL NOT** be the only place where workflow state exists. If prose conflicts with YAML, YAML wins.

---

## 3. Frozen schemas

### 3.1 `INTAKE_IDENTITY.yaml`

Allowed keys only:

- `document_id`
- `document_path`
- `amendment_slug`
- `intake_schema_version`
- `intake_path`
- `planning_path`
- `kernel_path`
- `ratification_path`
- `current_head_version`
- `created_at`
- `created_by`

Forbidden:

- workflow status
- committee status
- verification state
- next action
- events
- prose notes

### 3.2 `INTAKE_STATUS.yaml`

Required keys:

- `document_id`
- `amendment_slug`
- `lifecycle_state`
- `artifact_health`
- `committee_status`
- `architect_verification_status`
- `ui_verification_status`
- `kernel_status`
- `peer_review_status`
- `ratification_handoff_status`
- `next_action`
- `current_head_version`
- `last_reviewed_version`
- `status_updated_at`
- `status_updated_by`

Conditional keys:

- `architect_verified_by`
- `architect_verified_at`
- `ui_verified_by`
- `ui_verified_at`
- `committee_recorded_by`
- `committee_recorded_at`
- `committee_note`
- `kernel_skip_reason`

Controlled values:

#### `lifecycle_state`

- `intake_open`
- `blocked_missing_inputs`
- `phase_a_evidence_pending`
- `phase_a_evidence_ready`
- `phase_b_architect_pending`
- `phase_b_architect_drafted`
- `blocked_architect_human_verification`
- `phase_c_ui_pending`
- `phase_c_ui_drafted`
- `blocked_ui_human_verification`
- `phase_d_committee_pending`
- `blocked_committee_manual`
- `phase_d_committee_approved`
- `phase_e_author_revision_pending`
- `blocked_author_revision_manual`
- `phase_f_peer_review_pending`
- `blocked_peer_review_credentials`
- `phase_f_peer_review_running`
- `phase_f_peer_review_complete`
- `blocked_packet_invalid`
- `kernel_review_pending`
- `kernel_review_advisory_complete`
- `ratification_handoff_pending`
- `blocked_ratification_manual`
- `ratification_handoff_ready`
- `closed_executed`
- `failed`

#### `artifact_health`

- `healthy`
- `stale_supporting_artifacts`
- `identity_mismatch`
- `incomplete_packet`

#### `committee_status`

- `open`
- `answered`
- `closed_superseded_by_review`
- `approved`
- `approved_with_changes`
- `reopened_by_council`

#### `architect_verification_status`

- `pending`
- `verified`
- `rejected`

#### `ui_verification_status`

- `pending`
- `verified`
- `rejected`

#### `kernel_status`

- `not_applicable`
- `pending`
- `advisory_complete`
- `skipped_with_reason`

#### `peer_review_status`

- `not_run`
- `running`
- `pass`
- `fail`
- `incomplete`

#### `ratification_handoff_status`

- `not_ready`
- `pending_manual`
- `ready`
- `executed`

#### `next_action`

- `build_evidence`
- `run_architect`
- `verify_architect`
- `run_ui`
- `verify_ui`
- `prepare_committee`
- `record_committee`
- `author_revision`
- `run_peer_review_round_1`
- `run_peer_review_round_2`
- `validate_packet`
- `prepare_kernel_review`
- `record_kernel_review`
- `prepare_ratification_handoff`
- `manual_resolution`
- `archive`

Dependent-field rules:

1. If `architect_verification_status: verified`, both `architect_verified_by` and `architect_verified_at` are required.
2. If `ui_verification_status: verified`, both `ui_verified_by` and `ui_verified_at` are required.
3. If `committee_status` is anything except `open`, all of the following are required:
   - `committee_recorded_by`
   - `committee_recorded_at`
   - `committee_note`
4. If `kernel_status: skipped_with_reason`, `kernel_skip_reason` is required.

### 3.3 `INTAKE_EVENTS.yaml`

Top-level keys only:

- `intake_schema_version`
- `document_id`
- `amendment_slug`
- `events`

Each event must contain only:

- `event_id`
- `timestamp`
- `actor`
- `event_type`
- `from_state`
- `to_state`
- `summary`
- `evidence_paths`

Allowed `event_type` values:

- `intake_initialized`
- `evidence_refreshed`
- `architect_started`
- `architect_drafted`
- `architect_output_verified`
- `architect_output_conformance_validated`
- `architect_run_identity_recorded`
- `architect_human_verification_blocked`
- `architect_precondition_blocked`
- `architect_input_override_recorded`
- `architect_failed`
- `architect_verified`
- `ui_started`
- `ui_drafted`
- `ui_output_verified`
- `ui_output_conformance_validated`
- `ui_run_identity_recorded`
- `ui_human_verification_blocked`
- `ui_precondition_blocked`
- `ui_bundle_manifest_mismatch_blocked`
- `ui_evidence_freshness_blocked`
- `ui_failed`
- `ui_verified`
- `committee_packet_prepared`
- `committee_state_recorded`
- `author_revision_flagged`
- `peer_review_started`
- `peer_review_completed`
- `peer_review_packet_validated`
- `peer_review_packet_invalid`
- `kernel_brief_prepared`
- `kernel_findings_recorded`
- `kernel_skipped`
- `ratification_handoff_prepared`
- `intake_status_corrected`
- `intake_validation_passed`
- `intake_validation_failed`

Rules:

1. Append-only.
2. Prior events **SHALL NOT** be rewritten.
3. Extra event keys are forbidden.

### 3.4 `HANDOFF_NOTE.md`

Required:

1. File must exist.
2. File must state that structured YAML is authoritative.
3. File must not contain exclusive workflow state absent from YAML.

Required authority sentence:

```text
If this note contradicts `INTAKE_STATUS.yaml` or `INTAKE_EVENTS.yaml`, the YAML artifacts win.
```

---

## 4. Committee authority model

### 4.1 Who may record committee state

Committee state is a **human-recorded authority action**. The intake scaffold **SHALL NOT** infer committee approval from planning artifacts or peer reviews.

Allowed recorders:

- council member
- designated committee reviewer
- coordinator explicitly recording a human committee outcome

The recorder identity **SHALL** be written to:

- `committee_recorded_by`
- `committee_recorded_at`
- `committee_note`

### 4.2 Where committee state lives

Committee state lives in:

- `reviews/<slug>/intake/INTAKE_STATUS.yaml`

Committee narrative and packet content live in:

- `reviews/<slug>/planning/COMMITTEE_PACKET.md`

### 4.3 Legal committee transitions

The scaffold freezes the following legal transitions:

- `open -> answered`
- `open -> approved`
- `open -> approved_with_changes`
- `open -> closed_superseded_by_review`
- `answered -> approved`
- `answered -> approved_with_changes`
- `answered -> closed_superseded_by_review`
- `approved -> reopened_by_council`
- `approved_with_changes -> reopened_by_council`
- `closed_superseded_by_review -> reopened_by_council`
- `reopened_by_council -> answered`
- `reopened_by_council -> approved`
- `reopened_by_council -> approved_with_changes`
- `reopened_by_council -> closed_superseded_by_review`

Any other transition **SHALL FAIL** orchestration. Validation **SHALL** fail illegal committee transitions only where they are detectable from the frozen intake artifacts.

### 4.4 Required evidence

If committee state changes, the event stream **SHALL** record:

- `event_type: committee_state_recorded`
- evidence path to `planning/COMMITTEE_PACKET.md`

---

## 5. Human verification model

Architect verification and UI verification are distinct human checkpoints.

### 5.1 Recording fields

Architect verification fields:

- `architect_verification_status`
- `architect_verified_by`
- `architect_verified_at`

UI verification fields:

- `ui_verification_status`
- `ui_verified_by`
- `ui_verified_at`

These fields live in:

- `reviews/<slug>/intake/INTAKE_STATUS.yaml`

The event stream records:

- `architect_verified`
- `ui_verified`

### 5.2 Blocking rules

Blocked transitions:

1. The system **SHALL NOT** move from architect-drafted states into UI execution unless architect verification has been recorded, unless a future stage explicitly introduces a governed override.
2. The system **SHALL NOT** move from UI-drafted states into committee preparation unless UI verification has been recorded.
3. Verification rejection **SHALL** block forward motion and require manual resolution.

---

## 6. Kernel lane artifact contract

Exact path:

```text
reviews/<slug>/kernel/
```

Required filenames:

- `KERNEL_SHADOW_BRIEF.md`
- `KERNEL_SHADOW_FINDINGS.md`

Front matter:

- required for both files when scaffolded from templates

Skip recording:

- If kernel review is skipped, the skip **SHALL** be recorded in:
  - `INTAKE_STATUS.yaml` via `kernel_status: skipped_with_reason`
  - `kernel_skip_reason`
  - `INTAKE_EVENTS.yaml` via `event_type: kernel_skipped`

Advisory completion:

- `kernel_status: advisory_complete` means the advisory lane is complete
- it does **not** mean binding approval
- it does **not** alter `peer_review_status`

---

## 7. Ratification handoff location

This scaffold freezes exactly one ratification handoff path model:

```text
reviews/<slug>/ratification/
```

The scaffold **SHALL NOT** write directly to amendment motion files in Stage 2.

Stage 2 ratification handoff artifacts are non-doctrine preparation materials only and **MAY** include:

- `README.md`
- `RATIFICATION_HANDOFF.md`

Motion drafting or motion mutation is deferred to a later, explicitly authorized stage.

---

## 8. Doctrine mutation rule

1. The intake scaffold defaults to orchestration mode only.
2. Stage 2 implementation **SHALL NOT** mutate:
   - amendment markdown
   - specification markdown
   - council motion markdown
   - registry by default
3. Stage 2 **MAY** record:
   - that author revision is required
   - that author revision has been completed by a human
4. Stage 3 **MAY** add explicit author-revision helpers, but only behind separate command surfaces and only if doctrine mutation is opt-in and reviewable.

---

## 9. Read-only command posture

The Stage 2 CLI is orchestration-first.

Allowed Stage 2 actions:

- inspect status
- initialize intake artifacts
- build evidence
- build scaffolds
- run planning subprocesses
- record human verification
- record committee outcomes
- run binding peer-review subprocesses
- validate peer-review packet
- prepare advisory kernel scaffolds
- prepare ratification handoff scaffolds

Forbidden Stage 2 actions:

- auto-approve committee
- auto-complete kernel advisory review without explicit recording
- auto-ratify
- write ratified status into doctrine
- substitute local Ollama planning output for binding peer review

---

## 9A. Stage 3A architect-lane hardening

Stage 3A hardens the existing architect lane only. It does **not** redesign the wider lifecycle.

### 9A.1 Required preconditions

The architect lane **SHALL NOT** run unless all of the following are present:

- `reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md`
- `reviews/<slug>/planning/agent_kb/build_manifest.json`
- the selected manifest path used for architect-lane input validation

If the selected manifest declares:

- `reference/knowledge_base/snapshots/product_context_bundle.md`

then that snapshot file **SHALL** exist before the architect lane is invoked.

Stage 3A enforces **presence only** for this snapshot rule. It does **not** introduce a freshness-age heuristic.

### 9A.2 Slug/path reconciliation owner

The intake path layer is the explicit owner of architect-lane slug/path reconciliation.

The wrapper **SHALL**:

- derive the slug from the amendment path
- resolve `reviews/<slug>/planning/`
- confirm that architect output is expected at `reviews/<slug>/planning/ARCHITECT_PLAN.md`
- fail closed on mismatch

The wrapper **SHALL NOT** infer a substitute slug or silently redirect architect output.

### 9A.3 Success recording rule

After the architect subprocess returns, the wrapper **SHALL** verify that:

- `reviews/<slug>/planning/ARCHITECT_PLAN.md`

actually exists on disk before recording architect success.

If the file is missing:

- `phase_b_architect_drafted` **SHALL NOT** be recorded
- `blocked_architect_human_verification` **SHALL NOT** be recorded
- the intake lane **SHALL** fail closed

### 9A.4 Required architect-lane events

The hardened architect lane records distinct events for:

- architect input override use
- architect run start
- architect draft creation
- architect output existence verification
- architect block pending human verification
- architect precondition block
- architect failure before verified output

These events are append-only and **SHALL NOT** overwrite prior intake history.

### 9A.5 Override audit rule

If the architect lane is invoked with a non-default manifest path and/or bundle path, the intake event stream **SHALL** record:

- the override path used
- the actor
- the timestamp
- that a non-default architect input source was used

Override use is auditable input selection, not substitute governance authority.

### 9A.6 Read-only guarantee remains unchanged

Stage 3A architect-lane hardening does **not** authorize mutation of:

- amendment markdown
- specification markdown
- council motion markdown
- registry files as part of architect execution

Stage 3A writes only:

- intake artifacts
- architect planning output written by the existing architect lane
- narrow documentation / review-surface updates for the hardening pass

## 9B. Stage 3B architect-lane quality/evidence hardening

Stage 3B hardens the existing architect lane further. It does **not** redesign the wider lifecycle, the architect role, or any downstream lane.

### 9B.1 Architect output conformance validation

After the architect subprocess returns and `ARCHITECT_PLAN.md` exists, the intake wrapper **SHALL** run a structural conformance validation before architect success is recorded.

This validation is **not** content approval. It is implementation-level proof that the output is the correct artifact class rather than a garbage response or wrong markdown body.

At minimum Stage 3B validates:

- architect output file exists
- architect output file is non-empty
- architect output begins with the expected architect-plan heading
- required top-level `##` headings from `ARCHITECT_PLAN_TEMPLATE.md` are present in order
- unresolved template placeholders are not still present

If conformance fails:

- `phase_b_architect_drafted` **SHALL NOT** be recorded
- `blocked_architect_human_verification` **SHALL NOT** be recorded
- the intake lane **SHALL** fail closed

### 9B.2 Bundle / manifest correspondence rule

Stage 3B requires stronger proof than path existence alone for the selected architect knowledge inputs.

The wrapper **SHALL** validate, where the current artifacts can prove it, that:

- the selected `build_manifest.json` label matches the selected YAML manifest label
- the selected `build_manifest.json` file list exactly matches the selected manifest path list
- the selected bundle header matches that same manifest label
- the selected bundle contains source sections for the file paths recorded in the selected `build_manifest.json`

Stage 3B does **not** claim cryptographic provenance or original manifest-path recording because the current build artifacts do not freeze that stronger proof.

It proves correspondence only to the extent that:

- labels match
- file lists match
- bundle sections match the recorded build-manifest paths

If those proofs fail, the architect lane **SHALL** fail closed.

### 9B.5 UI-lane parity rule

The UI lane **SHALL** apply the same input-identity checks to its selected manifest, selected lane-local bundle, and selected `build_manifest.json` before `UI_PLAN.md` success is recorded.

At minimum Stage 3B parity for UI requires:

- manifest exists
- lane-local bundle exists
- lane-local `build_manifest.json` exists
- manifest / bundle / build-manifest correspondence passes the same label, file-list, and bundle-section checks used for architect
- required `product_context_bundle.md` freshness can be proven when the selected manifest declares that snapshot
- `UI_PLAN.md` exists and passes structural conformance validation against `UI_PLAN_TEMPLATE.md`
- `UI_PLAN.md.run_record.json` exists so the UI drafting run remains reviewable by manifest and bundle identity

If any of those checks fail, the UI lane **SHALL** fail closed before `blocked_ui_human_verification` is recorded.

### 9B.3 Minimal deterministic freshness rule

If the selected manifest declares:

- `reference/knowledge_base/snapshots/product_context_bundle.md`

then Stage 3B applies a deterministic freshness rule for architect-lane use:

- if the snapshot is missing, fail closed
- if the snapshot exists but its generated-date metadata is older than the selected `build_manifest.json` build record, fail closed and require refresh
- if comparable generated-date metadata is unavailable, the wrapper MAY fall back to filesystem modification times
- if neither comparable generated-date metadata nor usable filesystem metadata is available, fail closed rather than silently proceeding

This is an implementation-level freshness rule only. It is not a broader age policy for the whole process.

### 9B.4 Direct architect command governance distinction

The direct architect command:

- `py -3 scripts/ollama_planning_agent.py --role architect --amd-slug <slug>`

remains available for operator/manual use.

Stage 3B requires that this direct path be explicitly distinguished from the governed intake wrapper path.

The governed path remains:

- `py -3 scripts/amendment_intake_agent.py <amendment-path> --phase architect`

The direct path **SHALL NOT** be described as equivalent governance evidence to wrapper-governed execution.

### 9B.5 Required architect-lane events

In addition to Stage 3A events, Stage 3B adds architect-lane events for:

- architect output conformance validated
- architect output validation failed
- architect evidence freshness blocked
- architect bundle / manifest mismatch blocked

These events remain append-only and **SHALL NOT** overwrite prior intake history.

### 9B.6 Read-only guarantee remains unchanged

Stage 3B still does **not** authorize mutation of:

- amendment markdown
- specification markdown
- council motion markdown
- registry files as part of architect execution

Stage 3B writes only:

- intake artifacts
- architect planning output written by the existing architect lane
- narrow documentation / review-surface updates for the hardening pass

---

## 10. State machine freeze

The scaffold freezes the lifecycle states listed in **`INTAKE_STATUS.yaml`** as the authoritative intake lifecycle state machine.

High-level progression:

```text
intake_open
  -> phase_a_evidence_pending
  -> phase_a_evidence_ready
  -> phase_b_architect_pending
  -> phase_b_architect_drafted
  -> blocked_architect_human_verification
  -> phase_c_ui_pending
  -> phase_c_ui_drafted
  -> blocked_ui_human_verification
  -> phase_d_committee_pending
  -> blocked_committee_manual
  -> phase_d_committee_approved
  -> phase_e_author_revision_pending
  -> blocked_author_revision_manual
  -> phase_f_peer_review_pending
  -> phase_f_peer_review_running
  -> phase_f_peer_review_complete
  -> kernel_review_pending
  -> kernel_review_advisory_complete
  -> ratification_handoff_pending
  -> blocked_ratification_manual
  -> ratification_handoff_ready
  -> closed_executed
```

Failure / block states are authoritative and **SHALL NOT** be skipped silently.

---

## 11. What Stage 3 may implement later

Stage 3 may add:

- richer phase automation around existing repo scripts
- explicit author-revision helper commands with opt-in doctrine mutation
- stronger packet-to-intake reconciliation
- motion-draft assistance within the frozen `reviews/<slug>/ratification/` path
- improved local kernel prompt support

Stage 3 may **not**:

- replace `scripts/peer_review.py`
- collapse committee, peer review, kernel review, and ratification into one model decision
- auto-ratify doctrine

---

*End of AIOS-AMENDMENT-INTAKE-SCAFFOLD-001 v0.1.1.*

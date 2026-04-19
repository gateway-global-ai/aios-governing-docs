---
document_id: AMD-2026-007-ADD-001
parent_amendment: AMD-2026-007
parent_version: 0.2.1
version: 0.4.0
status: draft
category: amendment_addendum
title: User Sovereignty Disclosure and Precision Controls
author: Gateway Global AIOS
created: 2026-04-17
last_updated: 2026-04-17
cross_references:
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001
    title: User sovereignty disclosure and loop-exit standard
note: Draft addendum to AMD-2026-007 establishing user-visible disclosure, precision logging controls, inspectable signal use, and behavioral-setting visibility as binding shell law.
---

# AMD-2026-007-ADD-001 — User Sovereignty Disclosure and Precision Controls

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`draft` `0.4.0`** — addendum to **[AMD-2026-007](AMD-2026-007.md)** |
| **Purpose** | Extend shell disclosure law so users can inspect, clear, and govern logging, memory, behavioral adaptation, and guardrail posture rather than being managed through hidden platform state. |

## 0.1 Integration posture

This addendum extends, and SHALL NOT replace, the transparency model in `AIOS-SPEC-009 §12`.

Implementation SHALL use:

- active `PolicyRecord` thresholds or equivalent tenant policy for materiality and execution-readiness boundaries
- disclosure surfaces registered under `AIOS-SPEC-006`
- the typed capability registry and shell/session-disclosure posture defined by `AMD-2026-007`
- the product audit model required by `AIOS-SPEC-009 §12.4` and `§15`

## 1. Purpose

This addendum makes user sovereignty a shell-level disclosure and control requirement.

It exists to prevent a failure mode where:

- the platform captures or infers user-relevant state
- the platform benefits from that hidden state
- the user cannot inspect, clear, or disable it with precision

This addendum SHALL be implemented in coordination with `AIOS-SPEC-009` execution-readiness thresholds, active `PolicyRecord` evaluation, capability-registry metadata, and intent compilation surfaces that shape the visible shell path.

## 2. Governing principle

If a shell or surrounding runtime captures, infers, stores, or applies user-relevant state that materially affects behavior, the user SHALL be able to inspect and govern that state.

For this addendum, materiality SHALL be operationalized through numeric, enumerated, or `PolicyRecord`-backed thresholds for each disclosure class in Section 3.

Where such thresholds are not yet configured, a state SHALL be treated as material when its presence or absence changes visible shell behavior, registered UI state, execution-readiness thresholds, resolved `ExecutionPlan` composition, retention, routing, pacing, escalation, safety posture, or exit ability for the current session or a later session.

## 3. Required disclosure classes

The shell SHALL disclose these classes through the transparency model defined in `AIOS-SPEC-009 §12`, extended with the sovereignty-specific classes below when they materially exist.

The disclosure surface SHALL be implemented through registered shell components with stable identifiers and machine-readable bindings to the underlying state, policy source, or capability-registry metadata.

The disclosed classes are:

1. memory or session carry-forward
2. logging or transcript retention
3. telemetry / analytics
4. behavioral adaptation
5. guardrail or policy mode changes
6. voice-analysis or transcript processing
7. review or escalation gates that materially affect the user path

## 4. Precision controls

Users SHALL be able to:

- view what categories of data are being logged
- clear user-facing session data
- disable logging where policy permits
- adjust logging and memory categories with precision rather than only through a single global toggle

At minimum, precision controls SHALL distinguish:

- transcript logging
- voice transcript retention
- telemetry
- preference memory
- behavioral adaptation state
- review or artifact-trace capture when user-facing

User-configurable logging or retention controls SHALL be implemented as user-preference policy inputs or equivalent governed settings.

User-configurable logging or retention controls SHALL NOT override audit logging required by `AIOS-SPEC-009 §12.4`, `AIOS-SPEC-009 §15`, or the active product audit model for deterministic execution, policy enforcement, security, billing integrity, or lawful compliance.

Where such non-discretionary logging remains active, the shell SHALL disclose that boundary, SHALL distinguish it from user-configurable logging, and SHALL preserve separate audit and user-preference logging streams or equivalent metadata separation.

## 5. Behavioral and guardrail settings

Where a system exposes configurable behavior, the shell SHALL surface user-governable settings for:

- communication style
- verbosity
- compression or detail preference
- behavioral adaptation posture
- memory preference
- visible guardrail posture where configurable

The shell SHALL NOT force users to accept an invisible behavioral-management layer as the only operating mode when policy allows explicit settings.

User-governable behavior settings SHALL be stored as structured preferences under Workspace Domain Pack v1 or an equivalent governed schema.

User-governable behavior settings SHALL influence proposal shaping, retention posture, disclosure behavior, or other shell-visible behavior only through active `PolicyRecord` evaluation or equivalent governed policy inputs, and SHALL NOT override mandatory policy constraints.

## 6. Inspectable signal use

If the system infers user signals that affect pacing, tone, escalation, or safety posture, the shell SHALL disclose:

- which signal families exist
- whether they are active
- what they are allowed to influence
- how the user can limit or clear them where policy permits

Signal families that affect visible system behavior SHALL be registered in the typed capability registry posture recognized by `AMD-2026-007 §7`, or an equivalent governed metadata surface, with their influence domains, default thresholds, and user-override posture so the shell can populate disclosure surfaces from a stable source of truth.

## 7. Conflict-of-interest disclosure

The shell SHALL disclose conflicts where hidden capture, retention, or behavioral adaptation benefits platform continuity, engagement, or data accumulation while reducing user clarity, autonomy, or exit ability.

## 8. Non-goals

This addendum does not:

- require exposing raw model weights or internal reasoning traces
- waive lawful safety or compliance obligations
- define exact UI layout tokens or component styling
- define the full `PolicyRecord` schema or execution-plan compiler

It defines the shell’s minimum disclosure and control duties.

## 9. Failure posture

If a materially active disclosure class, logging boundary, behavior setting, or signal family required by this addendum is missing from the registered disclosure surface, the shell SHALL treat the affected state as non-conformant.

Non-conformant disclosure SHALL NOT be represented as complete session truth, and remediation SHALL be required before the affected flow is treated as fully policy-aligned.

## Final principle

Session disclosure is incomplete unless the user can see and govern the states that materially shape their path through the system.

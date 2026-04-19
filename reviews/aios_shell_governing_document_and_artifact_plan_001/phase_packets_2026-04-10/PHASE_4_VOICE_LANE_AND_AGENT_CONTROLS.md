# Phase 4 voice-lane and agent controls

## Purpose

Define the governed shell controls for voice-lane switching, transcript visibility, agent-behavior controls, and prompt-bearing shell configuration before richer autonomous behavior or deeper interface expansion is treated as governed work.

## Declared inputs

- `reference/implementation/AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_CONTROLS_MATRIX.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_SCHEMA_ROUTE_STORAGE_MAP.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_BASELINE_GAP_MAP.md`
- `amendments/AMD-2026-016.md`
- `amendments/AMD-2026-012.md`
- `amendments/AMD-2026-007.md`
- `specifications/IntentPrimitiveAndExecutionModel.md`
- implementation evidence in `ai-os-voice-interface` for shell voice/chat modes, shell intents, DISC controls, agent-intent fields, desired outcome fields, and voice selection

## Current baseline

The shell is already voice-first and exposes meaningful controls:

- PTT voice entry
- chat fallback
- voice selection
- DISC profile controls
- system configuration fields for agent identity, role, intent, and desired outcome
- deterministic shell switching through `app.shell.*` and `app.open.*`

The major remaining gaps are:

- explicit dual voice-lane switching as a governed shell surface
- a governed control contract for ARCH and system-prompt-bearing controls
- an approved disclosure and audit model for agent-behavior changes

## Runtime evidence snapshot

Current implementation evidence shows this phase already has substantial shell-control material to review:

- `src/App.tsx` defines voice-first entry, chat fallback, voice selection, DISC controls, agent role, agent intent, user intent, and desired outcome fields
- `src/App.tsx` explicitly instructs the shell agent to emit only one final `INTENT_JSON` line for shell actions and separates `app.shell.*`, `app.open.*`, and `workspace.*`
- `src/shell/shellIntentRouter.ts` routes `app.shell.*` and `app.open.*` into the shell plane and keeps `workspace.*` outside that shell-state path
- `src/shell/shellNavigationApply.ts` applies shell-state and chat/voice mode changes through one apply path
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_CONTROLS_MATRIX.md` already records the existing voice, DISC, system configuration, and shell-state surfaces

This means Phase 4 is not starting from zero. It is starting from an implementation that already exposes behavior-shaping controls but does not yet govern them strongly enough.

## Current control inventory

| Surface | Exists now | Governance gap |
|---|---|---|
| PTT voice entry | yes | needs formal review and baseline approval |
| chat fallback | yes | needs explicit disclosure and logging posture |
| voice selection | yes | needs reviewed provider/lane semantics |
| DISC profile control | yes | needs permission and disclosure rules |
| agent role / intent / desired outcome fields | yes | needs reviewed control contract |
| shell voice/chat switching | yes | needs reviewed user-facing control rule |
| dual-lane provider switching | partial | explicit governed lane model still missing |
| ARCH and system-prompt-bearing control | partial to missing | current contract not explicit enough |

## Control grouping rule

This phase should group controls into four classes:

1. interaction mode controls
2. voice-lane and provider controls
3. agent behavior controls
4. privileged prompt-bearing or architecture-bearing controls

Review should fail if those groups are collapsed into one generic settings bucket, because they have different disclosure and authority implications.

## Transcript and visibility rule

The packet must define, at minimum:

- whether every voice exchange is mirrored into visible chat history
- what counts as a complete transcript versus a partial spoken interaction
- what is shown when a lane switch occurs
- what is shown when a provider is unavailable or a local model requirement is unresolved

## Permission floor

This phase must distinguish clearly between:

- controls a primary user may access directly
- controls that require stronger operator or administrator authority
- controls that exist only as implementation internals and must not be silently treated as user-facing shell features

DISC and ordinary voice preference may end up in a more permissive bucket than ARCH or system-prompt-bearing controls, but the packet must say so explicitly.

## Agent-permission rule

This phase must explicitly govern agents as governed actors and governed control surfaces.

At minimum, the packet must distinguish:

- which agent identities exist in the shell
- which shell agents may observe state versus mutate state
- which agents may propose an action versus execute an action
- which agents may read transcripts, profile data, document metadata, or tenant application context
- which agents may influence prompt-bearing, architecture-bearing, or role-bearing settings

The shell must not treat “the agent” as one undifferentiated power source. Agent permissions must be bounded by role, scope, and action family.

## State-to-agent control rule

If an agent may affect shell behavior, the packet must define whether it may:

- request a shell-state change
- execute a shell-state change directly
- invoke a tenant application
- call another agent or skill
- create, edit, or package user-facing output
- alter voice-lane, provider, DISC, ARCH, role, intent, or desired-outcome settings

Each of those permissions must be evaluated separately. Review should fail if a packet grants one broad “agent control” concept without breaking out the governed action families.

## Application-permission rule

This phase must explicitly govern application permissions as permissions over tenant application objects, not only as UI controls.

At minimum, the packet must define:

- what an application object is in AI OS shell terms
- whether an application acts as a tenant-scoped principal, a delegated user principal, or both
- which controls an application may request versus control directly
- whether an application may change shell state, voice lane, agent behavior, or prompt-bearing configuration
- what disclosure the shell owes the user when an application is influencing control state

If an application may invoke or request shell behavior, the packet must distinguish:

- user-approved application actions
- admin-approved application actions
- denied actions that remain shell-only or platform-only

## Service-account communication rule

This phase must explicitly govern service-account communication as deterministic, scoped, and bounded non-human communication.

At minimum, the packet must define:

- whether a service account communicates through shell intents, control-plane calls, service interfaces, or another governed route
- whether a service account may communicate directly with shell controls or only through mediated routing
- which message classes a service account may emit
- which actions a service account may trigger without human interpretation
- what identity, scope, and permission binding each routed communication must carry

The shell must not treat service-account communication as invisible background traffic. It must remain legible, scoped, and auditable.

## Agent-control and application boundary

The packet must prevent two permission failures:

1. treating a tenant application as equivalent to a shell administrator
2. treating an agent-behavior field as harmless just because it appears in UI

It must also prevent a third failure:

3. treating any agent with shell visibility as automatically authorized to mutate shell state or privileged configuration

It must also prevent a fourth failure:

4. treating a routed service account as trusted ambient infrastructure rather than a governed non-human actor

That means application permissions must be defined separately for:

- viewing control state
- proposing a control change
- executing a control change
- setting prompt-bearing or architecture-bearing values
- switching provider or voice lanes
- reading transcript or conversation artifacts

An application object must never inherit prompt-bearing authority, transcript access, or privileged shell-control authority implicitly.

## Required phase outputs

This phase should produce, at minimum:

- a voice-lane control matrix
- a transcript and logging visibility rule
- an agent-control surface inventory covering DISC, ARCH, voice, role, intent, and system-prompt-bearing controls
- a permission matrix distinguishing user-facing controls from operator/admin-only controls
- an agent-permission matrix covering observe, propose, execute, invoke, and mutate rights
- an application-permission matrix for tenant objects that interact with shell controls
- a service-account communication matrix covering route, scope, message class, and allowed action family
- a provider-switch and degraded-mode disclosure note

## Surface requirements

The phase packet must define:

- how the user sees and changes the active voice lane
- how Gemini-lane, Whisper/TTS/Ollama-lane, or equivalent named shell lanes are disclosed
- how voice interactions are logged into chat or transcript history
- which behavior controls are primary-user accessible and which require stronger authority
- how ARCH, DISC, agent voice, role, intent, and system-prompt-bearing controls are grouped and disclosed
- what happens when a provider is unavailable, degraded, or intentionally disabled
- which agents may observe, propose, execute, invoke, or mutate governed shell actions
- what a tenant application object may see, request, or change across shell controls and transcript surfaces
- what a service account may communicate, invoke, or mutate and through which governed route

## Boundary rule

This phase must keep a hard distinction between:

- shell-exposed controls the user may understand and invoke
- privileged controls that alter shell authority or sensitive behavior
- invisible model/provider internals that must not become silent governance sources

No prompt-bearing or agent-behavior control may be treated as acceptable if the shell cannot disclose that it exists, who can change it, and what it affects.

## Acceptance criteria

This phase is complete only when all of the following are true:

1. dual-lane or multi-lane voice switching is explicit
2. transcript and voice-to-chat visibility duties are explicit
3. DISC, ARCH, voice, role, intent, desired outcome, and prompt-bearing controls are named explicitly
4. permission boundaries for those controls are explicit
5. degraded-mode and provider-switch disclosure is explicit
6. the packet distinguishes ordinary preferences from privileged prompt-bearing or architecture-bearing controls
7. agent permissions are explicit for observe, propose, execute, invoke, and mutate actions
8. application permissions over shell controls and transcript surfaces are explicit
9. service-account communication, routing, and action authority are explicit
10. the packet states what review evidence must exist before downstream implementation-support work begins

## Review gate

Minimum review outputs for this phase:

- peer-review output set
- packet status update
- recorded human approval, rejection, or required remediation note

No voice-control or agent-control support artifact may be treated as governed output until those review outputs exist.

## Doctrine escalation triggers

Open a doctrine-support or amendment path only if review proves one or more of the following:

- current doctrine does not sufficiently govern provider or voice-lane switching
- current doctrine does not sufficiently govern prompt-bearing shell controls
- current doctrine does not sufficiently govern transcript visibility, disclosure, or permission separation for agent-behavior changes
- current doctrine does not sufficiently govern agent permissions over shell state, transcript access, or behavior-changing actions
- current doctrine does not sufficiently govern tenant application permissions over shell controls, transcripts, or behavior-changing settings
- current doctrine does not sufficiently govern service-account communication routing, deterministic non-human action, or mediated shell access

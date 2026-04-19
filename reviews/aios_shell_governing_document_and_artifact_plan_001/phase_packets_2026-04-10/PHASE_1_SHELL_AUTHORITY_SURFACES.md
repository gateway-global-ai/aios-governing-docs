# Phase 1 shell authority surfaces

## Purpose

Define the shell authority model that governs who can see, enter, and control shell surfaces before broader account, document, or voice-lane expansion is treated as governed work.

## Declared inputs

- `reference/implementation/AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001.md`
- `reference/implementation/AIOS-SHELL-BASELINE-RECOVERY-PACKET-001.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_CONTROLS_MATRIX.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_SCHEMA_ROUTE_STORAGE_MAP.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_BASELINE_GAP_MAP.md`
- `amendments/AMD-2026-016.md`
- `amendments/AMD-2026-012.md`
- `amendments/AMD-2026-007.md`
- `specifications/IntentPrimitiveAndExecutionModel.md`
- implementation evidence in `ai-os-voice-interface` for `ShellSurfaceMode`, `shellAuthority`, `shellNavigationApply`, and `shellIntentRouter`

## Current baseline

The shell already exposes materially real authority surfaces:

- `primary`, `developer`, and `operator` shell modes
- deterministic shell-state commands and `app.shell.*` agent intents
- subordinate Workspace entry as a shell-controlled surface
- current device-local interim authority instead of identity-bound administrative authority

The gap is not whether shell authority exists. The gap is whether that authority is explicit, identity-safe, reviewable, and bounded strongly enough to support later shell phases.

## Runtime evidence snapshot

Current implementation evidence shows the shell authority plane is real and already somewhat centralized:

- `src/shell/shellSurfaceMode.ts` defines the authoritative shell surface modes as `primary`, `developer`, and `operator`
- `src/shell/shellAuthority.ts` defines interim device-local authority inputs and denial messages for elevated shell surfaces
- `src/shell/shellNavigationApply.ts` makes `set_surface_mode` the only shell navigation action that is authority-gated before apply
- `src/shell/shellIntentRouter.ts` separates `app.shell.*` shell-state actions from `workspace.*` execution intents
- `src/App.tsx` prompts the agent to emit `app.shell.*` only for shell-state changes and explicitly routes `workspace.*` through the integration control plane
- `src/workspace/workspacePolicy.ts` already treats Workspace as a separately governed surface family with its own policy gate

## Current authority sources

The runtime today uses interim device-local authority signals, not identity-bound authority:

| Current source | Type | What it currently does | Governance posture |
|---|---|---|---|
| `?aios_operator=1` / `?aios_dev=1` | URL launch flag | enables elevated shell eligibility during the session | interim only |
| legacy storage hints | browser storage | preserves older diagnostics/operator hints | compatibility only |
| `aios.shell.interim.operator_unlock` / `aios.shell.interim.developer_unlock` | browser unlock key | device-local elevation signal | interim only |
| `VITE_AIOS_SHELL_INTERIM_ALLOW=true` | build-time opt-in | broad local/dev allowance | trusted build convenience only |
| `aios.shell.surfaceMode` | session storage | persists the chosen shell surface mode inside the session | persistence only, not authority |

None of those sources is a substitute for account identity, administrative approval, tenant RBAC, or signed-in operator policy.

## Minimum permission-layer model

Phase 1 must define the minimum permission-layer objects that later shell phases are allowed to depend on.

## Governing rule

The governing rule for shell authority should be explicit:

Any actor inside AI OS that can observe, request, approve, trigger, execute, mutate, revoke, delegate, or package an action must be treated as a governed principal or governed control surface.

That means the packet must define, for every authority-bearing participant:

- principal type
- role or permission family
- resource class
- allowed action family
- scope boundary
- audit duty

If any one of those is missing, the participant remains under-governed and the shell authority model is incomplete.

At minimum, the model must name:

### Principal classes

- platform administrator
- tenant administrator
- tenant user
- service account principal
- application principal
- group principal

### Resource classes

- shell surface states such as `primary`, `developer`, and `operator`
- shell state objects such as active surface, session authority posture, privileged overlays, and governed control flags
- shell configuration and privileged shell controls
- account records and identity surfaces
- document and folder objects
- application objects within a tenant
- agent objects and agent-control surfaces exposed by the shell

### Permission decisions

The packet must distinguish:

- who the actor is
- which tenant scope applies
- which group memberships and role assignments apply
- which resource object is being accessed
- which action is being requested
- which governing layer evaluates the request

Shell authority is therefore not only “can a session enter operator mode.” It is also the rule family that determines which principal may exercise which state transition or privileged shell capability over which resource within which tenant scope.

## Group and role requirement

Phase 1 must stop short of inventing a full directory system, but it must define the existence of:

- role assignments
- group membership as a first-class permission input
- tenant-scoped versus platform-scoped roles

If groups are absent from the model, later account, document, folder, and application permissions will be under-specified. This packet must therefore treat groups as required permission primitives even if their storage implementation is deferred to a later phase.

## Shell-state permission rule

The authority model must explicitly govern, at minimum:

- entry to `primary`, `developer`, and `operator`
- who may request shell-state elevation
- who may grant or approve privileged shell-state elevation
- whether elevation is session-scoped, tenant-scoped, or platform-scoped
- whether elevation applies only to shell state or also confers downstream permissions over accounts, documents, or application objects

The default governing answer should be conservative:

- shell-state elevation alone does **not** silently grant account-administration authority
- shell-state elevation alone does **not** silently grant document/folder authority
- shell-state elevation alone does **not** silently grant application-object authority

Any broader permission grant must be named explicitly by the later phase packet that governs that resource class.

## State-permission model

Phase 1 must explicitly treat shell state as a governed object class.

At minimum, the packet must distinguish permissions for:

- viewing current shell state
- requesting a shell-state transition
- approving or denying a privileged shell-state transition
- mutating privileged shell configuration
- resetting or revoking privileged shell state

The packet must also say whether each state permission is:

- self-service
- administrator-controlled
- tenant-scoped
- platform-scoped
- implementation-internal and therefore not a user or tenant permission at all

Without that distinction, shell state becomes an ungoverned ambient power rather than a reviewable authority surface.

## Role-permission rule

Phase 1 must define role permissions separately from raw actor labels.

At minimum, the packet must state:

- which permissions attach to a named role
- whether roles are assigned directly, through groups, or both
- whether a role is platform-scoped, tenant-scoped, or session-scoped
- whether a role grants view, request, approve, execute, revoke, or audit rights

Review should fail if roles are named without a corresponding permission set, because that leaves governance attached to titles rather than enforceable authority.

## Authority matrix

| Actor posture | Allowed shell surface | May request elevation | May enter elevated shell surface now | Notes |
|---|---|---|---|---|
| primary user | `primary` | no | no | baseline shell entry |
| interim developer-eligible session | `primary`, `developer` | yes | yes, if interim eligibility exists | still not identity-bound |
| interim operator-eligible session | `primary`, `operator`, `developer` | yes | yes, if interim eligibility exists | operator eligibility implies developer eligibility in current runtime |
| future identity-bound admin role | to be defined | yes | should replace interim device-local elevation | target replacement seam |

## Minimum shell permission matrix skeleton

Phase 1 should expose a reviewable permission matrix at the shell-authority layer before later packets rely on it.

| Governed participant | Principal type | Permission family | Resource class | Allowed actions | Scope | Required audit duty |
|---|---|---|---|---|---|---|
| primary user | human principal | self-service shell use | ordinary shell modes and visible shell surfaces | view, request ordinary mode changes, use approved shell entry surfaces | session, tenant | session-visible state change record when material |
| tenant user with no elevated role | human principal | bounded tenant user rights | tenant-bound shell resources and approved downstream resources | view, request allowed actions only | tenant, session | action/result trace for privileged denials when applicable |
| tenant administrator | human principal | tenant administration | tenant-bound shell state, tenant accounts, tenant documents, tenant application objects | view, request, approve, execute, revoke within tenant scope | tenant | audit-visible admin record |
| platform administrator | human principal | platform administration | platform-wide shell authority surfaces and cross-tenant governance objects | view, request, approve, execute, revoke, audit | platform | platform audit log entry |
| group principal | derived principal | inherited permission bundle | whichever resources are bound to the group | inherit only what is explicitly bound | tenant or platform | membership and permission-binding audit |
| service account principal | non-human principal | deterministic service authority | routed service actions, service-owned integrations, and explicitly delegated shell-adjacent resources | observe, request, invoke, execute only where explicitly granted | tenant or platform as declared | service action log with bound scope and result |
| application principal | non-human principal | application authority | tenant application objects and explicitly delegated shell-adjacent resources | observe, request, invoke, execute only where explicitly granted | tenant | application action log with delegating context |
| shell agent principal | non-human principal | bounded shell-agent authority | shell state, agent-control surfaces, routing surfaces | observe, propose, execute only where the law and role binding allow | session, tenant, platform as declared | run/action record with actor identity and result |

This matrix is not yet the final policy. It is the minimum skeleton needed so later packets cannot discuss permissions, service accounts, agents, applications, or shell state without a common authority grammar.

## Transition and denial rules

| Requested transition | Current rule | Current outcome |
|---|---|---|
| any mode -> `primary` | always allowed | downgrade/exit path stays available |
| `primary` -> `operator` | requires `operatorEligible` | allowed or denied with operator denial message |
| `primary` -> `developer` | requires `developerEligible` | allowed or denied with developer denial message |
| `developer` -> `operator` | requires `operatorEligible` | allowed only if stronger interim eligibility exists |
| `operator` -> `developer` | allowed because target remains elevated but eligible under current authority model | currently permissive |
| any shell state request that is not `set_surface_mode` | no authority gate in `shellNavigationApply` | passes through apply path |

This makes one critical boundary explicit: current runtime authority controls shell surface elevation, not ordinary shell mode changes like chat vs voice or opening shell settings overlays.

## Shell-state versus shell-mode distinction

This phase must preserve the runtime distinction between:

- shell surface authority: `primary`, `developer`, `operator`
- ordinary shell modes: `voice`, `chat`, `menu`, `voice_settings`, `disc_settings`, `intent_settings`, `api_health`
- subordinate Workspace views such as `workspace_hub` or `workspace_calendar_hub`

Review should fail if a later packet blurs those categories and starts treating ordinary settings overlays or subordinate Workspace routing as if they were equivalent to privileged shell authority.

## Disclosure obligations

The shell authority packet must require explicit disclosure for:

- the current shell surface mode
- denied elevation attempts and the reason they were denied
- the fact that interim device-local authority is not identity-bound authority
- when the user is entering an operator or developer surface rather than a primary shell surface
- when Workspace is being opened as a subordinate controlled surface rather than as a hidden shell bypass

The present runtime already includes denial messages that explain the interim-authority nature of operator and developer elevation. This packet should preserve that clarity and turn it into a reviewable requirement rather than leaving it as implementation luck.

## Workspace subordinate boundary

Phase 1 must keep Workspace subordinate to shell authority in three ways:

1. shell routing and shell-state changes remain in the `app.shell.*` plane
2. Workspace requests remain in `workspace.*` intent space and route through the integration control plane
3. Workspace policy remains separately gated even after the shell opens the Workspace surface

This prevents a future failure mode where Workspace or another domain plane becomes an implicit alternate authority system.

## Tenant and application-object boundary

AI OS is operating at three distinct layers:

1. governing layer
2. AI OS shell layer
3. tenant/application layer

Phase 1 must define that applications living under a tenant are governed objects, not informal shell extensions.

That means later packets must treat application permissions as permissions over tenant objects, not as generic UI toggles. Phase 1 does not need to define the entire tenant object model, but it must reserve that boundary explicitly so shell authority is not mistaken for blanket control over tenant applications.

## Immediate remediation direction

The minimum replacement path for interim authority should define:

- an identity-bound administrator posture
- a reviewable administrative elevation rule
- a bounded launch and downgrade path for operator/developer surfaces
- an audit-visible record for privileged shell entry or privileged shell mutation

Phase 1 does not need to ratify that future mechanism yet, but it must define the target seam clearly enough that later phases do not build on the interim device-local model as if it were acceptable final authority.

## Required phase outputs

This phase should produce, at minimum:

- a shell authority matrix for `primary`, `operator`, `developer`, and future identity-bound admin oversight
- a shell state-permission matrix covering view, request, approve, execute, revoke, and audit actions
- a transition and denial table for shell surface changes
- a shell disclosure map defining what each surface must reveal to the user
- a subordinate-boundary note for Workspace and any future non-shell planes
- a remediation note that replaces interim device-local authority with an identity-bound approval seam

## Surface requirements

The phase packet must make the following surfaces explicit:

- who may enter `primary`, `operator`, and `developer` shell modes
- which commands or intents may request a surface transition
- which transitions are allowed, denied, or require stronger authority
- which roles may view, request, approve, execute, revoke, or audit shell-state changes
- what user-visible disclosure is required when shell state changes
- how shell authority differs from domain execution authority
- how Workspace remains subordinate to shell authority rather than becoming a hidden bypass path

## Dependency rule

Phase 1 is the authority floor for later phases.

Phase 2 through Phase 4 may be drafted in parallel for planning completeness, but none of their administrative or privileged controls may be treated as governed output until Phase 1 authority rules are reviewed and accepted.

## Acceptance criteria

This phase is complete only when all of the following are true:

1. actor classes and shell modes are named explicitly
2. allowed and denied shell-state transitions are recorded explicitly
3. shell authority is kept separate from Workspace or other domain-execution authority
4. user-facing disclosure duties are stated for shell mode, escalation, and diagnostics visibility
5. the interim device-local authority is identified as temporary and a replacement path is defined
6. principal classes, resource classes, and permission-decision inputs are named explicitly
7. the packet treats groups and tenant-scoped role assignments as first-class permission inputs
8. shell state permissions are explicit for view, request, approve, execute, revoke, and audit actions
9. role permissions are explicit rather than implied by role names alone
10. the packet distinguishes privileged shell surface authority from ordinary shell settings and chat/voice mode changes
11. the packet records its own next review action before any derivative artifact is used downstream

## Review gate

Minimum review outputs for this phase:

- peer-review output set
- packet status update
- recorded human approval, rejection, or required remediation note

No later authority-bearing shell artifact may rely on this phase until those outputs exist.

## Doctrine escalation triggers

Open a doctrine-support or amendment path only if review proves one or more of the following:

- current doctrine does not sufficiently define shell authority separation
- current doctrine does not sufficiently govern privileged shell-state transitions
- current doctrine does not sufficiently govern disclosure obligations for privileged surfaces
- current doctrine does not sufficiently govern shell state permissions, role permissions, or revocation/audit duties

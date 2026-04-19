# Phase 2 account and identity surfaces

## Purpose

Define the baseline account and identity surfaces required for AI OS to greet users, classify entry state, create and verify accounts, expose profile data, and support governed administrative account oversight.

## Declared inputs

- `reference/implementation/AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/PROJECT_SCOPE_INTENT_AND_DESIRED_OUTCOME.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_BASELINE_GAP_MAP.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_SCHEMA_ROUTE_STORAGE_MAP.md`
- `amendments/AMD-2026-016.md`
- `amendments/AMD-2026-012.md`
- `specifications/IntentPrimitiveAndExecutionModel.md`
- implementation evidence in `ai-os-voice-interface` for session-entry classification and shell greeting/orientation surfaces

## Current baseline

The current shell can greet the user and distinguish `new` vs `returning` at a lightweight session-entry level.

The current shell does not yet provide:

- governed account creation
- OTP-based identity verification
- account profile display
- account profile editing
- admin-visible account roster
- admin access-level administration

## Runtime evidence snapshot

Current implementation evidence shows Phase 2 has a real shell-entry seam but not a real account seam:

- `src/core/shell/sessionEntryClassification.ts` stores only `new` versus `returning` using browser-local state
- `src/components/shell/ShellVoiceIdlePanel.tsx` changes shell copy based on `new` versus `returning`
- `src/App.tsx` marks the session as engaged when the user moves deeper into chat or Workspace
- `src/App.tsx` also states explicitly that there is currently no separate AI OS account in the shell runtime

That means the shell has entry classification and orientation, but not identity proof, account persistence, or administrative account governance.

## Current identity posture

| Surface | What exists now | What is missing |
|---|---|---|
| entry classification | `new` versus `returning` browser-local shell entry state | no account-backed identity |
| greeting | shell idle copy differs for new and returning entry | no identity-aware personalization beyond session-entry posture |
| account creation | none | full baseline missing |
| identity verification | none | OTP and verification lifecycle missing |
| profile view/edit | none | self-service profile surfaces missing |
| admin account oversight | none | account roster, inspection, and access-level control missing |

## Minimum account data contract

This phase should define, at minimum, the baseline account fields required for shell readiness:

| Field | Purpose | Minimum posture |
|---|---|---|
| `account_id` | stable account reference | required before persistent account flows |
| `display_name` | user-facing shell identity | required |
| `phone` | OTP or contact path | required if phone-based verification is used |
| `email` | identity/contact path | required if email-based verification or profile display is used |
| `verification_state` | proof posture | required |
| `verification_method` | OTP, magic link, or equivalent proof path | required once multiple verification methods exist |
| `access_level` or `role_assignment` | permissions and admin governance | required |
| `group_memberships` | inherited or collective permissions | required when group-based access exists |
| `tenant_id` | tenant binding for identity scope | required before tenant-scoped permissions exist |
| `created_at` / `updated_at` | record hygiene | required |

This packet does not need to finalize implementation schema yet, but it must define the minimum governed fields so later work does not improvise them.

## Required identity and permission primitives

Phase 2 must explicitly define the identity-side permission primitives required by later shell work:

- user account
- administrator account
- service account
- group
- role assignment
- access level
- tenant binding

Without those primitives, Phase 1 authority, Phase 3 document permissions, and application or service-account permissions for tenant objects cannot be evaluated coherently.

## Groups and role assignment

The current shell does not show evidence of a real group system. This phase must therefore decide and document, at minimum:

- whether groups are platform-scoped, tenant-scoped, or both
- whether role assignment is direct, group-derived, or both
- whether access levels are human-readable labels, machine policy bindings, or both
- who may create, edit, or dissolve groups
- who may assign a user or service principal to a group

If groups are deferred, the packet must say so explicitly and state what later phase is responsible. If they are not deferred, then groups become first-class inputs to permission evaluation.

## Identity-to-permission mapping rule

This phase must define how identity information feeds permission decisions for later shell work:

- shell state controls
- account administration controls
- document and folder permissions
- application permissions over tenant objects

At minimum, the packet should describe:

- direct user permissions
- group-derived permissions
- role-derived permissions
- service-account permissions
- tenant-scoped permissions
- platform-scoped administrative overrides, if any

## Role-permission association rule

Phase 2 must explicitly associate roles with permissions rather than treating roles as descriptive labels.

At minimum, the packet must define:

- the minimum named roles required by the shell baseline
- which permissions each role grants
- which permissions are prohibited even if a user holds a broader shell-facing role
- who may assign, remove, suspend, or override a role
- whether role permissions may be inherited from groups or delegated to service-account principals or application principals
- how service accounts receive pre-bound permissions and scope without human interpretation at runtime

If the packet cannot yet finalize role names, it must still define the permission families that later named roles will bind to.

## Verification-method rule

This phase must explicitly define the allowed account-verification methods and their states.

At minimum, the packet must distinguish:

- OTP verification
- magic-link verification
- pending verification
- verified
- failed, expired, denied, or locked verification posture

If multiple verification methods are supported, the shell must disclose which method is in use, what fallback exists, and what the user must do when a verification attempt expires or fails.

## Identity naming rule

This phase must define baseline naming constraints for identity-bearing objects.

At minimum, the packet must define:

- maximum user display-name length
- maximum account username or handle length, if handles exist
- maximum group-name length
- allowed abbreviation conventions for user-facing names, role labels, and group labels
- whether abbreviations are cosmetic only or become identity-bearing canonical names

Review should fail if naming limits and abbreviation rules remain implicit, because those choices affect account lookup, audit clarity, UI disclosure, and permission binding.

## Service-account rule

This phase must define service accounts as deterministic non-human identities with pre-bound permissions and pre-bound scope.

At minimum, the packet must define:

- whether service accounts are tenant-scoped, platform-scoped, or both
- which roles or permission families may be bound to a service account
- whether a service account may call shell controls directly or only through routed governed interfaces
- whether a service account may act independently or only on behalf of a declared application, tenant, or workflow
- what audit identity and communication record each service-account action must leave

Service accounts must not be treated as informal background logic. They are governed participants and must be legible in the same way human and agent actors are legible.

## Lifecycle map requirement

The identity lifecycle for review should be described explicitly:

1. shell entry as `new` or `returning`
2. account creation or account lookup decision
3. OTP or equivalent verification challenge
4. verified or blocked identity posture
5. profile view/edit path
6. admin account inspection or access-level mutation path when authorized

## Administrative separation

This packet must preserve a hard distinction between:

- shell orientation for an ordinary user
- account ownership actions for that user
- administrative account-view and access-level mutation actions

Administrative account actions must not be derived automatically from current operator or developer shell visibility alone. Phase 1 authority may inform them, but it must not silently authorize them.

## Audit and review duty

The phase must require reviewable evidence for:

- account creation success or failure
- verification success, retry, denial, or timeout posture
- verification method selection and fallback posture
- account data edits
- access-level changes or role assignment changes
- group membership changes
- service-account binding or scope changes
- who performed an administrative action and under what authority

## Required phase outputs

This phase should produce, at minimum:

- an entry-state and identity lifecycle map
- an account surface inventory for self-service and admin surfaces
- a minimum account data contract covering user name, phone, email, access level, and verification state
- an OTP verification flow brief with authority and failure handling
- an admin account-governance matrix for view, inspect, and access-level changes
- a role-permission association matrix covering user, admin, group-derived, and tenant-scoped rights
- a verification-method rule covering OTP, magic link, fallback, and failure states
- an identity naming policy covering maximum user and group names plus abbreviation conventions
- a service-account rule covering identity, binding, routed communication, and audit posture

## Surface requirements

The phase packet must define:

- greeting behavior and new-vs-returning branching
- account creation flow and minimum required identity fields
- OTP verification posture, retry boundaries, and blocked-state behavior
- magic-link verification posture if that method is allowed
- profile view and profile edit surfaces for the user
- an admin-visible roster or equivalent account-view surface
- admin inspection of identity posture and access level
- governed role or access-level change paths
- group creation, membership, and inspection posture
- service-account creation, binding, scope, and revocation posture
- maximum user-name and group-name rules plus abbreviation posture
- how role permissions are associated, inherited, suspended, and revoked
- audit visibility for administrative account actions

## Separation rule

This phase must distinguish clearly between:

- self-service account actions available to the account owner
- administrative account actions available only to authorized roles
- shell entry behavior versus deeper account-management surfaces

No account-administration control may be defined as an invisible backdoor or ambient operator privilege.

## Acceptance criteria

This phase is complete only when all of the following are true:

1. new-vs-returning entry behavior is explicit
2. account creation and OTP verification are explicit
3. user profile display and edit surfaces are explicit
4. admin account view, inspection, and access-level control surfaces are explicit
5. required account fields and ownership boundaries are explicit
6. the packet distinguishes browser-local session-entry state from true account identity
7. groups, role assignments, and tenant binding are either defined explicitly or deferred explicitly with ownership
8. role permissions are associated explicitly with named permission families or named roles
9. verification methods and verification states are explicit, including OTP and magic link when applicable
10. maximum user/group naming rules and abbreviation conventions are explicit
11. service-account identity, scope, and routed communication posture are explicit
12. the packet states what audit trail or review evidence administrative actions must leave

## Review gate

Minimum review outputs for this phase:

- peer-review output set
- packet status update
- recorded human approval, rejection, or required remediation note

No account, identity, or admin-account support artifact may be treated as governed output until those review outputs exist.

## Doctrine escalation triggers

Open a doctrine-support or amendment path only if review proves one or more of the following:

- current doctrine does not sufficiently govern identity verification or OTP posture
- current doctrine does not sufficiently govern multiple verification methods such as OTP and magic link
- current doctrine does not sufficiently define account-owner versus administrator authority
- current doctrine does not sufficiently govern access-level mutation or administrative audit duty
- current doctrine does not sufficiently govern group membership, tenant-scoped roles, or identity-derived permission evaluation
- current doctrine does not sufficiently govern service-account identity, binding, routed communication, or non-human deterministic authority

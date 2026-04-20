# Phase 3 document and folder baseline

## Purpose

Define the minimum governed shell surfaces required for user-owned document and folder creation, editing, saving, and renaming before richer document-system work expands.

## Declared inputs

- `reference/implementation/AIOS-SHELL-GOVERNING-DOCUMENT-AND-ARTIFACT-PLAN-001.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/PROJECT_SCOPE_INTENT_AND_DESIRED_OUTCOME.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_BASELINE_GAP_MAP.md`
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_SCHEMA_ROUTE_STORAGE_MAP.md`
- `amendments/AMD-2026-016.md`
- `amendments/AMD-2026-012.md`
- `specifications/IntentPrimitiveAndExecutionModel.md`
- any reviewed outputs from Phase 1 and Phase 2 that define authority and identity preconditions

## Current baseline

The shell currently supports conversational and configuration surfaces, but it does not yet support governed user document or folder management.

The baseline gap includes:

- no document create surface
- no document edit surface
- no explicit save or autosave contract
- no file or folder rename surface
- no approved storage ownership boundary for user-authored content

## Runtime evidence snapshot

Current implementation evidence shows there is still no true shell document baseline in the active interface runtime:

- `src/App.tsx` persists conversational shell state such as `messages` and `chatInput`, but not user-owned documents or folders
- `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/SHELL_SCHEMA_ROUTE_STORAGE_MAP.md` shows only browser-local shell state, Workspace preference, interim authority hints, and Workspace control-plane handoff
- `src/overlays/MailMessageActionsPanel.tsx` supports Gmail draft-reply creation inside Workspace, which is an external Workspace draft plane, not an AI OS shell document baseline
- `src/api/llmHealth.ts` references an optional local documents proxy only as a dev convenience, not as an approved shell document system
- archived governance-manager surfaces include document-list and document-view ideas, but they are under `archive/` and are not current governed shell baseline authority

This means Phase 3 must start by refusing false equivalence:

- chat history is not the same thing as a document system
- Workspace drafts are not the same thing as AI OS-owned user documents
- archived or dev-only document surfaces are not current shell-baseline authority

## Current storage posture

| Storage surface | Exists now | Why it is insufficient for Phase 3 |
|---|---|---|
| React local state for `messages` / `chatInput` | yes | ephemeral shell interaction state, not user-owned document storage |
| browser-local shell settings and authority hints | yes | shell/session state only, not document persistence |
| Workspace draft and read surfaces | partial | external integrated content plane, not AI OS-owned document/folder baseline |
| optional local documents proxy | dev-only | convenience tooling only, not approved shell-baseline contract |
| account-backed document store | no | baseline requirement still missing |

## Baseline artifact classes

This phase should define three distinct user-facing artifact classes before any richer system opens:

1. user document
2. user folder
3. shell-generated draft or structured output candidate

The phase must also define what each class is **not**:

- not a governed repo artifact
- not a Workspace-owned external document by default
- not a hidden model output with no user-owned storage boundary

## Lifecycle map requirement

The minimum document/folder lifecycle for review should be explicit:

1. create document or folder from the shell
2. enter or edit document content
3. disclose unsaved versus saved state
4. save or autosave according to a stated rule
5. rename document or folder
6. list or reopen existing user-owned artifacts
7. soft-delete, recover, or permanently remove according to a stated deletion lifecycle

If any one of those steps is deferred, the packet must say so explicitly rather than implying a complete document baseline.

## Deletion and recycle-bin rule

This phase must define whether deletion is immediate or whether a recycle-bin or trash lifecycle exists.

At minimum, the packet must answer:

- whether deletion first moves a document or folder into a recoverable recycle-bin state
- whether recycle-bin emptying is manual, automatic, or policy-driven
- whether retention differs by artifact importance, type, or owner policy
- who may restore, permanently delete, or empty recycle-bin contents
- what the user sees when an object is recoverable versus permanently removed
- what audit or recovery evidence remains after deletion

Review should fail if deletion is treated as a single undefined action, because baseline ownership is incomplete without a governed delete-and-recovery lifecycle.

## Storage ownership and persistence rule

The packet must explicitly distinguish:

- shell-local temporary working state
- account-backed user-owned persistent document state
- Workspace-integrated external content state
- governed repo artifact state

Review should fail if those are mixed together or if user-owned document storage is left implicit.

## Document and folder permission model

This phase must define document and folder permissions as first-class governed permissions, not as an accidental side effect of account login.

At minimum, the packet must distinguish permissions for:

- create
- read
- edit
- rename
- move
- delete
- share, if sharing is later introduced

The model must also state which actor classes may exercise those permissions:

- document owner
- authorized tenant user
- tenant administrator
- platform administrator, if any platform override exists
- service account principal acting within declared scope
- application principal acting on behalf of a tenant

## Permission inheritance and folder boundary

The packet must describe how folder permissions relate to document permissions.

At minimum, review should require an answer to:

- whether a document inherits permissions from its containing folder
- whether a document may diverge from folder-level permissions
- whether rename or move may change the governing permission boundary
- whether deleted or archived objects preserve audit-visible ownership and permission history

If those rules are not final yet, the packet must still declare the minimum boundary so later work does not improvise it inconsistently.

## Tenant and application path rule

Document and folder permissions must also account for tenant application objects.

If an application or service account inside a tenant creates, reads, edits, stores, or exports a document or folder, the packet must define:

- whether the application or service account acts as its own principal or on behalf of a user principal
- how tenant scope is enforced
- what permissions the application or service account must possess
- what the user can see about that application's or service account's access
- what audit evidence is required for application-initiated or service-account-initiated actions

No application or service account may silently become the owner of user-authored content merely because it touched the content in a tenant workflow.

## Naming and disclosure rule

The phase must define:

- what minimum naming is required at creation time
- whether untitled documents or folders are allowed
- how rename is disclosed and confirmed
- how save location or ownership is disclosed to the user
- what the shell says when a document exists only as temporary draft state and has not yet been persisted

It must also define:

- maximum document-name length
- maximum folder-name length
- whether abbreviation conventions are allowed for long names
- whether abbreviations are display-only or canonical stored names
- what characters or normalization rules are prohibited for baseline safety and clarity

## Adjacent but non-authoritative surfaces

The following may inform design but must not be misread as approved baseline completion:

- archived governance-manager document surfaces
- Workspace mail draft or other Workspace draft-capable tools
- optional documents proxy or local dev utilities

They are evidence of neighboring patterns, not proof that Phase 3 already exists.

## Required phase outputs

This phase should produce, at minimum:

- a minimum document and folder lifecycle map
- a storage ownership and persistence boundary matrix
- a surface inventory for create, edit, save, rename, and list actions
- a naming and rename policy for user-facing document and folder objects
- a deletion and recycle-bin lifecycle note covering restore, retention, and permanent removal
- a shell-to-storage handoff note distinguishing baseline user content from governed repo artifacts
- a document/folder permission matrix covering owner, group, tenant-admin, application access, and service-account access

## Surface requirements

The phase packet must define:

- how a user creates a document from the shell
- how a user edits a document in a low-noise shell flow
- how save state is disclosed to the user
- how folders are created and renamed
- how documents are renamed and listed
- how documents and folders are deleted, recovered, or permanently removed
- which persistence surfaces are local, account-backed, or deferred
- what the baseline folder model is before broader collaboration or tenant work opens
- what permissions exist for document and folder actions and how they are evaluated
- what tenant application objects and service accounts may do to user-owned documents and under what disclosure and audit rules
- what maximum file/folder naming rules and abbreviation conventions apply

## Boundary rule

This phase must keep a hard distinction between:

- user-authored documents and folders
- governed repo artifacts
- Workspace-integrated external content

No baseline document flow may silently treat user documents as governed doctrine artifacts, and no governed artifact workflow may be smuggled in as a simple user document flow.

## Acceptance criteria

This phase is complete only when all of the following are true:

1. document create, edit, save, rename, and delete surfaces are explicit
2. folder create, rename, and delete surfaces are explicit
3. persistence ownership is explicit for each baseline artifact type
4. disclosure of save state and storage location is explicit
5. the packet states what remains intentionally out of scope for richer document systems
6. the packet distinguishes chat history, Workspace drafts, and archived/dev document surfaces from the true shell document baseline
7. document and folder permissions are explicit for owners, admins, groups, application principals, and service accounts
8. recycle-bin or deletion lifecycle rules are explicit, including restore and permanent-removal posture
9. maximum file/folder naming rules and abbreviation conventions are explicit
10. the packet records what later review or approval is needed before implementation-support work begins

## Review gate

Minimum review outputs for this phase:

- peer-review output set
- packet status update
- recorded human approval, rejection, or required remediation note

No document or storage-support artifact may be treated as governed output until those review outputs exist.

## Doctrine escalation triggers

Open a doctrine-support or amendment path only if review proves one or more of the following:

- current doctrine does not sufficiently govern baseline user document ownership
- current doctrine does not sufficiently govern shell-to-storage boundaries
- current doctrine does not sufficiently separate baseline user content from reviewed governance artifacts
- current doctrine does not sufficiently govern document/folder permissions, inheritance, or tenant application access to user content
- current doctrine does not sufficiently govern service-account access to user content objects
- current doctrine does not sufficiently govern deletion lifecycle, recycle-bin retention, or naming constraints for user content objects

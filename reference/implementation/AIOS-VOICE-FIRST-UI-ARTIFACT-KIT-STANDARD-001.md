---
document_id: AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001
version: 0.6.0
status: draft
category: specification
title: Voice-first UI artifact kit standard
author: Gateway Global AIOS
created: 2026-04-17
last_updated: 2026-04-18
cross_references:
  - doc_id: AIOS-SPEC-006
    title: UI Component Registry Standard
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AMD-2026-012
    title: Shell Authority and Voice-First Entry
  - doc_id: AMD-2026-008-ADD-004
    title: Pre-Human Browser Review and Visual Proof Gate
  - doc_id: AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001
    title: AI OS Shell UI Layout and Component Standard
  - doc_id: AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001
    title: User sovereignty disclosure and loop-exit standard
note: Draft implementation standard for a governed in-repo voice-first UI artifact kit whose canonical library lives inside aios-governing-docs so the artifact set remains law-controlled and reviewable.
---

# Voice-first UI artifact kit standard

## Purpose

Define the canonical governed library model for reusable voice-first AI UI artifacts.

This standard exists because voice-first systems repeatedly recreate the same shell primitives, overlay structures, and session-navigation cards without a stable governed kit. When that kit lives only in a downstream product library, no-code or convenience-driven agents can silently mutate the effective law by changing the implementation surface instead of changing the governing source.

## Governing rule

The canonical voice-first UI artifact kit SHALL live inside the governing-docs repository.

Product repos MAY consume the kit, mirror it, or implement against it, but they SHALL NOT become the silent authority for the artifact definitions themselves.

## In-repo library model

The governed library root for the first release is:

- `sdk/voice_first_ui_artifact_kit/`

That root SHALL contain:

- a machine-readable manifest
- a normative schema for that manifest
- governed artifact identifiers
- required placement and proof rules
- references to the controlling standards and amendment families

Future MCP or dependency delivery surfaces MAY be added, but they SHALL derive from the governed in-repo library rather than replacing it.

## Artifact family

The first governed shell artifact family is:

- `Header`
- `HeaderAttachedMenu`
- `HeaderAudioPlayerCluster`
- `HeaderCueDrawer`
- `HeaderSystemControlPanel`
- `Canvas`
- `Footer`
- `FooterUserMenu`
- `MenuLevelStack`
- `MenuListTemplate`
- `MenuThumbnailTemplate`
- `MenuCustomTemplate`

The first governed canvas artifact family is:

- `1_1 Background`
- `2_1 Container`
- `3_1 Overlay Card`
- `4_1 Title`
- `4_2 Title and Description`
- `4_3 Title Description and Paragraph`
- `5_1 Image`
- `5_2 Video`
- `6_1 Agent Controls`

Shell artifacts define the structural authority frame for the session. Canvas artifacts render inside that governed frame and SHALL NOT silently replace shell authority, disclosure, or exit obligations.

### Artifact family purposes

| Artifact | Purpose |
|----------|---------|
| `Header` | Shell authority, identity, disclosure, and global orientation surface. |
| `HeaderAttachedMenu` | Deterministic system-shell menu surface anchored to the bottom of the header. |
| `HeaderAudioPlayerCluster` | Bounded header control cluster for play or stop, mic, speaker, and cue inspection. |
| `HeaderCueDrawer` | Header-attached drawer for current and queued shell-controlled audio plus nearby route handoff. |
| `HeaderSystemControlPanel` | Top-right system panel that carries current voice-runtime state and deeper control handoff. |
| `Canvas` | Primary voice-first workspace where the active session state is rendered. |
| `Footer` | Action and navigation rail for close, back, and other governed controls. |
| `FooterUserMenu` | Secondary user/PTT-adjacent menu surface for user-related actions only. |
| `MenuLevelStack` | Governed one-to-many menu level model used to render deterministic menu hierarchies. |
| `MenuListTemplate` | Structured list template for dense shell menu content. |
| `MenuThumbnailTemplate` | Template for thumbnail or tile-driven menu content where the format is pre-approved. |
| `MenuCustomTemplate` | Custom governed menu template family for explicitly approved cases only. |
| `1_1 Background` | Visual support layer that frames the active session without becoming the authority surface. |
| `2_1 Container` | Layout boundary for governed voice-first content blocks. |
| `3_1 Overlay Card` | Guided-step card for focused user decisions, disclosures, or confirmations. |
| `4_1 Title` | Minimal orientation text for a step or surface. |
| `4_2 Title and Description` | Orientation text plus concise explanatory support. |
| `4_3 Title Description and Paragraph` | Extended explanation block for higher-context guided steps. |
| `5_1 Image` | Static media surface that supports the current voice-led state. |
| `5_2 Video` | Time-based media surface with governed play-state controls. |
| `6_1 Agent Controls` | Visible operator or user controls for guided runtime actions. |

## Artifact identity rule

Each governed artifact SHALL declare at minimum:

- `artifact_id`
- `artifact_label`
- `surface_zone`
- `artifact_kind`
- `interactive`
- `voice_first_role`
- `required_controls`
- `required_visual_proofs`
- `related_governing_docs`
- `menu_zone` when the artifact bears menu content
- `template_family` when the artifact bears menu content
- `level_count` when the artifact bears menu content
- `content_source_type` when the artifact bears menu content
- `permission_class` when the artifact bears menu content

### Artifact field contract

| Field | Type | Rule |
|-------|------|------|
| `artifact_id` | string | SHALL be unique within the kit manifest. |
| `artifact_label` | string | SHALL provide the governed human-readable label. |
| `surface_zone` | enum | SHALL be one of `shell`, `canvas`. |
| `artifact_kind` | enum | SHALL be one of `structural`, `visual`, `text`, `media`, `control`. |
| `interactive` | boolean | SHALL indicate whether the artifact exposes direct interaction. |
| `voice_first_role` | enum | SHALL be one of `authority_and_disclosure`, `primary_surface`, `action_and_navigation`, `support`, `guided_step`, `orientation`, `explanation`, `operator_visible_runtime_control`. |
| `required_controls` | array | SHALL contain only `back`, `close`, `play`, `pause` unless a future ratified revision extends the set. |
| `required_visual_proofs` | array | SHALL contain only `surface_proof`, `state_proof`, `control_proof`, `behavior_proof`. |
| `related_governing_docs` | array | SHALL point to the controlling amendment or standard identifiers when present. |
| `menu_zone` | enum | When present, SHALL be one of `header_system`, `footer_user`, `view_local`. |
| `template_family` | enum | When present, SHALL be one of `list`, `thumbnail`, `custom`. |
| `level_count` | integer | When present, SHALL equal the number of governed menu levels rendered by the artifact. |
| `content_source_type` | enum | When present, SHALL declare whether content is `governed_record`, `registry_record`, or another ratified source. |
| `permission_class` | enum | When present, SHALL be one of `shell_system`, `user_surface`, `agent_read_only`, `agent_content_only`. |

## Deterministic menu artifact rule

When this kit defines menu-bearing artifacts, those artifacts SHALL follow one deterministic contract:

- the header remains the primary system-shell menu surface,
- the footer remains a secondary user/PTT menu surface,
- menu structure SHALL be declared through governed records,
- level stacks and templates SHALL be explicit rather than inferred from downstream product code.

Product repos MAY populate governed records or mirror the artifact implementation, but they SHALL NOT silently redefine protected shell chrome by inventing a new menu placement model.

Agent or tool participation in menu-bearing artifacts SHALL remain content-bound only. Agents SHALL NOT directly redefine header or footer structure, placement, or control ownership.

## Voice-first design rule

The kit SHALL support a voice-first shell architecture in which:

- intent leads
- the shell remains the governing authority
- overlays and cards support the active voice-led state
- menus and dropdowns remain subordinate fallback surfaces

## Header voice-runtime package rule

The governed kit SHALL define one deployable header voice-runtime package for downstream systems that claim conformance to the voice-first shell model.

That package SHALL include at minimum:

- the `Header` authority surface,
- the `HeaderAudioPlayerCluster`,
- the `HeaderCueDrawer`,
- the `HeaderSystemControlPanel`,
- the `VoiceControlPanel` or governed successor for deeper route control,
- the shell cue controller contract, and
- the Gemini or equivalent governed voice runtime transport contract when the system offers cloud speech.

Downstream systems MAY style or implement the package locally, but they SHALL retain governed artifact identifiers and SHALL deploy the package as one traceable set rather than cherry-picking hidden substitutes.

## Package deployment contract

When a system deploys the governed header voice-runtime package, the deployment contract SHALL preserve:

- shell-owned playback, replay, mute, and stop authority,
- visible header disclosure of current cue or playback state,
- visible handoff from the header into deeper voice settings,
- package-local traceability between runtime components and governed artifact identifiers, and
- auditable reference to the governing standard and manifest that define the package.

The package SHALL also expose a machine-readable downstream handoff manifest that records:

- required runtime files,
- host-only environment-variable boundaries,
- proof expectations, and
- minimum deployment steps.

For the current release, that downstream handoff surface SHALL live at:

- `sdk/voice_first_ui_artifact_kit/header_voice_runtime_package_manifest.yaml`
- `sdk/voice_first_ui_artifact_kit/header_voice_runtime_package_manifest.schema.json`

The kit SHALL NOT be used to justify dashboard-first planning, dropdown-first control flow, or menu-first session architecture.

## Multi-step card navigation rule

Any multi-step card or slide sequence in the governed kit SHALL include:

1. a top-right progress label in the form `X of Y`
2. a back button
3. a close button

These controls are minimum navigation law for multi-step shell cards. They SHALL NOT be omitted on the assumption that narration or agent guidance alone is sufficient.

## Overlay-card minimum

Where the kit uses overlay cards, the card SHALL support:

- clear title hierarchy
- visible close control
- visible back control when the sequence is multi-step
- explicit step position when the sequence is multi-step
- deterministic footer or action area when agent or user controls are present

## Rendered-proof rule

Governed artifacts in this kit SHALL declare whether rendered proof is required before approval or promotion.

Artifacts that drive:

- user-visible disclosures
- voice-first navigation
- multi-step session cards
- agent controls
- or session-critical state transitions

SHALL require browser-visible proof and artifact checks under the relevant browser-review gate.

Where rendered proof is required, summary-only evidence SHALL NOT constitute approval or promotion readiness.

## Relationship to the registry

This standard does not replace `AIOS-SPEC-006`.

Instead:

- `AIOS-SPEC-006` remains the registry authority
- this standard defines the governed voice-first kit family that the registry SHALL recognize
- downstream product implementations SHALL reference kit artifacts rather than inventing uncontrolled equivalents

### Registration and mapping mandate

When an artifact from this kit is represented in the UI component registry:

- the registry entry SHALL preserve a deterministic one-to-one mapping between `component_id` and `artifact_id`
- the registry entry SHALL identify the governed source as the voice-first UI artifact kit family
- the registry entry SHALL retain traceability to `AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001` and `sdk/voice_first_ui_artifact_kit/voice_first_ui_artifact_kit_manifest.yaml`
- if a product repo mirrors or implements a governed artifact, the product implementation SHALL retain the originating `artifact_id` reference rather than replacing it with an uncontrolled local identifier

## Manifest schema

The normative schema for the first kit release SHALL live at:

- `sdk/voice_first_ui_artifact_kit/voice_first_ui_artifact_kit_manifest.schema.json`

The downstream package handoff schema for the current governed header voice-runtime package SHALL live at:

- `sdk/voice_first_ui_artifact_kit/header_voice_runtime_package_manifest.schema.json`

The manifest and schema together are the machine-verifiable contract for kit identity, artifact vocabulary, and proof requirements.

## Governance and lifecycle management

Changes to this governed kit SHALL follow the same governed review posture as other normative UI surfaces.

At minimum, the lifecycle process SHALL include:

1. a proposal naming the affected `artifact_id` values and the governing reason for the change
2. an update to the manifest and schema when the machine-readable contract changes
3. any required registry alignment under `AIOS-SPEC-006`
4. peer review and versioning before the revised artifact set is treated as canonical
5. explicit deprecation or replacement records when an artifact is superseded

Product repos MAY prototype downstream implementations, but the canonical artifact definition SHALL NOT change until the governed kit is revised through this process.

## Final principle

If a voice-first artifact is foundational to shell authority, disclosure, or user navigation, its canonical library definition should live in governed law, not only in a downstream app library where silent drift is easy.

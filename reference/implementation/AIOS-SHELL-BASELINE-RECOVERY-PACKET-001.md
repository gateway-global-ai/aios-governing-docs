---
document_id: AIOS-SHELL-BASELINE-RECOVERY-PACKET-001
version: 0.1.0
status: draft
category: reference
title: Shell baseline recovery packet and review path
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-012
    title: Shell Authority and Voice-First Entry
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AMD-2026-008-ADD-001
    title: Base Shell Navigation Primitives and Start-Here Control
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
  - doc_id: AMD-2026-008-ADD-003
    title: Composition Control Plane for Messages, Invites, and Documents
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy
note: Non-ratified extraction packet that captures the current AI OS shell baseline, gaps, and review path before any broader shell or tenant advancement.
---

# AIOS-SHELL-BASELINE-RECOVERY-PACKET-001

## Purpose

Create a governed, reviewable baseline packet for the current shell environment in `ai-os-voice-interface` before any broader AI OS interface or tenant work moves forward.

This packet is intentionally a **supporting packet**, not new law. It extracts current implementation evidence, maps it to doctrine, records the gaps against the required baseline operating-system behaviors, and provides a bounded review target for Deep Research and AIOS peer review.

## Positioning

Use a two-stage path:

1. **Stage 1:** extract and review the shell baseline as a supporting packet.
2. **Stage 2:** open a narrow addendum or amendment only if Stage 1 proves doctrine gaps that require new binding text.

This keeps current implementation evidence separate from doctrine creation.

## Current implementation truth

The shell baseline today is primarily implemented in:

- `C:/Apps/ai-os-voice-interface/src/App.tsx`
- `C:/Apps/ai-os-voice-interface/src/components/shell/CommandRail.tsx`
- `C:/Apps/ai-os-voice-interface/src/components/ui/VoicePttButton.tsx`
- `C:/Apps/ai-os-voice-interface/src/shell/ShellStateContext.tsx`
- `C:/Apps/ai-os-voice-interface/src/shell/shellBootstrap.ts`
- `C:/Apps/ai-os-voice-interface/src/shell/shellIntentRouter.ts`
- `C:/Apps/ai-os-voice-interface/src/shell/shellNavigationApply.ts`
- `C:/Apps/ai-os-voice-interface/src/shell/shellStateCommands.ts`
- `C:/Apps/ai-os-voice-interface/src/shell/workspaceState.ts`
- `C:/Apps/ai-os-voice-interface/src/shellCanvas/canvasTypes.ts`

The current implementation is a real shell, but not yet the full baseline system the product requires. It already provides:

- voice-first shell entry
- a governed command rail with voice/chat fallback
- menu-driven settings overlays
- primary vs developer vs operator shell surfaces
- workspace read-plane entry through a governed canvas layer

It does **not** yet provide the full baseline account, document, artifact, and dual-lane voice controls required by the target operating-system slice.

## Doctrine anchors

Use these documents as governing authority for this packet:

- `AMD-2026-012` for shell authority, voice-first entry, new-vs-returning classification, finite shell outcomes, and subordinate-tool boundaries
- `AMD-2026-007` for command rail, menu/chat fallbacks, composed disclosure, primary vs operator split, and intent-driven surface rules
- `AIOS-SPEC-009` for intent, session, readiness, and shell-vs-domain-execution boundaries
- `AMD-2026-008-ADD-003` for artifact composition classes and role/intent/outcome contracts

Use these as draft working-layer guidance, not ratified authority:

- `AMD-2026-008-ADD-001` for shell navigation classes
- `AMD-2026-008-ADD-002` for output depth, shell voice controls, and packaging

## Packet contents

The supporting packet lives under `reviews/aios_shell_baseline_recovery_packet_001/packet_2026-04-09/` and includes:

- `DEEP_RESEARCH_META_PROMPT.md`
- `PROJECT_SCOPE_INTENT_AND_DESIRED_OUTCOME.md`
- `SHELL_SURFACE_INVENTORY.md`
- `SHELL_CONTROLS_MATRIX.md`
- `SHELL_SCHEMA_ROUTE_STORAGE_MAP.md`
- `SHELL_BASELINE_GAP_MAP.md`
- `SHELL_BASELINE_SCOPE.md`
- `FILE_MANIFEST.md`

The packet also includes a reproducible export path:

- `reviews/aios_shell_baseline_recovery_packet_001/build_shell_baseline_packet.ps1`

## Gap summary against the required baseline

Current status against the 14 required baseline capabilities:

- **Present:** greeting, voice-first interaction, transcript/message logging
- **Partial:** new-vs-returning continuity, shell state separation, dual-mode shell conversation, agent/shell controls, output progression, shell action/outcome handling, single-vs-multi flow behavior
- **Missing:** governed account creation with OTP, account profile display/edit, document/folder authoring flow

This means the current shell is sufficient to extract as a thin slice, but not sufficient to approve as the final baseline without further design and doctrine review.

## Review path

This packet is meant to be reviewed through two parallel channels:

1. External Deep Research using the exported packet and prompt.
2. Internal AIOS triangulated peer review on this reference packet as the review target.

Internal review output must produce:

- triad reviews
- a review synthesis
- a gate report
- a clear recommendation on whether the shell baseline is sufficiently defined to become the foundation gate for later work

## Governance vehicle recommendation

The correct near-term vehicle is:

- **Now:** supporting packet plus review packet
- **Later, only if needed:** narrow shell-baseline addendum or amendment

That later doctrine track should stay limited to:

- shell control surfaces
- entry and user-state classification
- shell state separation of powers
- minimum baseline screen artifacts
- promotion rule blocking broader work until shell-baseline approval

## Acceptance condition

This recovery packet is complete only when:

1. the current shell is extracted from repo truth rather than abstractly described
2. the shell-to-doctrine map is explicit
3. the 14-capability gap map is explicit
4. the packet is exportable as a self-contained review package
5. the packet has completed triangulated peer review
6. a human can approve or reject the shell baseline before broader work proceeds

---

*Reference packet — AIOS-SHELL-BASELINE-RECOVERY-PACKET-001 — v0.1.0.*

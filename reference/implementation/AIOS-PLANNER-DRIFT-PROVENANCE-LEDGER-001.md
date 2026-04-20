---
document_id: AIOS-PLANNER-DRIFT-PROVENANCE-LEDGER-001
version: 0.1.0
status: draft
category: reference
title: Planner drift provenance ledger and containment classification
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy
  - doc_id: AMD-2026-014
    title: Governed authoring knowledge inputs and bounded author-like drafting
note: Containment ledger for known planner/knowledge-base drift. This file records provenance status and remediation posture only. It is not a ratification instrument.
---

# AIOS-PLANNER-DRIFT-PROVENANCE-LEDGER-001

## Purpose

Record which planner-generated artifacts are presently trusted, quarantined, or pending regeneration after discovery of the shared `AMD-2026-006` knowledge-base and template drift path.

This ledger is the authoritative containment record for this repair pass.

## Root cause summary

The intake/planner path was found to couple two semantic sources that should not have been shared across unrelated lanes:

1. a shared knowledge-base manifest rooted in the `amd_2026_006_workspace_track`
2. shared planning templates copied from `reviews/amd_2026_006/planning/`

Those sources carried `AMD-2026-006` / `AIOS-SPEC-007` / Workspace-specific meaning into later lanes that required their own declared input packets.

## Classification model

| Class | Meaning |
|------|---------|
| `trusted` | No known planner-drift contamination from the shared 006 path. |
| `quarantined` | Artifact exists but must not be used as authority until regenerated or explicitly cleared. |
| `regenerate` | Artifact should be rebuilt from corrected templates and declared knowledge packets. |
| `relabel_only` | Artifact may remain on disk if clearly marked as non-authoritative historical evidence. |
| `needs_review` | Downstream dependency exists, but authority inheritance must be checked before final disposition. |

## Current containment posture

### Confirmed affected planning lanes

| Lane | Artifact class | Current disposition | Required next move |
|------|----------------|---------------------|--------------------|
| `reviews/amd_2026_011/planning/` | planning | `quarantined` | `relabel_only` until corrected packet exists, then `regenerate` |
| `reviews/amd_2026_013/planning/` | planning | `quarantined` | `relabel_only` until corrected packet exists, then `regenerate` |
| `reviews/amd_2026_015_cani_experience_loop_and_victory_lap_formula/planning/` | planning | `quarantined` | `relabel_only` until corrected packet exists, then `regenerate` |

### Intake state and evidence records linked to affected planning lanes

| Lane | Artifact class | Current disposition | Required next move |
|------|----------------|---------------------|--------------------|
| `reviews/amd_2026_011/intake/` | intake state | `needs_review` | preserve event history, add provenance note, do not treat as trusted architect evidence |
| `reviews/amd_2026_013/intake/` | intake state | `needs_review` | preserve event history, add provenance note, do not treat as trusted architect evidence |
| `reviews/amd_2026_015_cani_experience_loop_and_victory_lap_formula/intake/` | intake state | `needs_review` | preserve event history, add provenance note, do not treat as trusted architect evidence |

### Downstream process artifacts

| Artifact class | Current disposition | Rule |
|---------------|---------------------|------|
| committee packets derived from contaminated planning output | `needs_review` | cannot be treated as authoritative without provenance check |
| peer-review packets citing contaminated planning output as evidence | `needs_review` | preserve historical packet integrity, but block authority inheritance |
| ratification handoff materials citing contaminated planning output | `needs_review` | preserve as historical evidence only until cleared |
| motions or trackers that merely record historical status | `trusted` unless they cite contaminated planning output as substantive evidence | track separately |

## Hard containment rule

No artifact listed as `quarantined` or `needs_review` in this ledger may be treated as authoritative planning evidence for:

- architect verification
- UI verification
- committee approval
- peer-review support packets
- ratification support or handoff

until the corrected template and knowledge-packet model is in place and the artifact is either:

- regenerated from corrected inputs, or
- explicitly cleared in a later ledger update

## Review interface requirement

This ledger must be surfaced in the knowledge-base review experience so a human reviewer can see:

- which lanes were contaminated
- which artifacts remain historical only
- which artifacts require regeneration
- which process layers are still draft or partially formalized

## Update rule

This ledger is append-by-revision, not silent overwrite by implication.

Any later clearance or regeneration should update:

- this ledger
- the affected lane-local provenance notice
- the relevant intake / packet / ratification-support documentation where needed

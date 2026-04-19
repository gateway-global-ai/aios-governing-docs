---
document_id: AIOS-REVIEW-PACKET-TAXONOMY-001
version: 1.0.0
status: draft
category: reference
title: Review packet artifact taxonomy (identity, status, events, handoff)
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-09
cross_references:
  - doc_id: AMD-2026-005
  - doc_id: AIOS-AMD-PLAN-001
note: Implementation standard for peer-review packet layout; not a ratified amendment.
---

# AIOS-REVIEW-PACKET-TAXONOMY-001 — Review packet artifact taxonomy

## Purpose

Define **four distinct artifact classes** for triangulated peer-review packets under `reviews/<packet_slug>/round_<N>/` so that:

- **Identity** (what this packet is) does not mix with **mutable workflow state** or **append-only process history**.
- Operators and automation can find **one authoritative place** for each kind of fact.
- **AMD-2026-005** gate outcomes and committee posture remain **structured**, not buried in prose or overloaded YAML.

## Problem statement

When packet metadata, status, event history, and human warnings shared a single file (for example an overloaded `PACKET_IDENTITY.yaml` or long `handoff_note` fields), legitimate process memory was **duplicated or contradicted** across files. That led to **taxonomy drift**: structured facts were stuffed into identity or narrative because there was **no first-class home** for them.

## The four artifact classes

| Class | Filename | Owns |
|-------|----------|------|
| **1. Identity** | `PACKET_IDENTITY.yaml` | Stable packet identity facts only (document id, paths, slug, current head version pointer, round, manifest path, schema version, generation metadata). |
| **2. Status** | `PACKET_STATUS.yaml` | Mutable workflow state: artifact health, review gate, committee posture, next action, lifecycle phase, version pointers (`last_reviewed_version`). |
| **3. Events** | `PACKET_EVENTS.yaml` | Append-only process memory: ordered events with types, versions, round, evidence paths. |
| **4. Handoff** | `HANDOFF_NOTE.md` | Human-readable, **non-authoritative** orientation (upload warnings, operational reminders). |

## Field ownership rules

### `PACKET_IDENTITY.yaml` (schema version `2`)

**Allowed fields only** (no narrative, no gate outcome, no committee state, no “status split”):

- `document_id`
- `document_path`
- `packet_slug`
- `current_head_version`
- `review_round`
- `packet_path`
- `manifest_path`
- `packet_schema_version`
- `generated_by`
- `generated_at`

**Script-owned:** `peer_review.py` rewrites identity on each successful run (paths and versions reflect the run).

### `PACKET_STATUS.yaml`

**Required structured fields:**

- `document_id`, `packet_slug`, `current_head_version`, `last_reviewed_version`
- `artifact_health` — one of: `healthy` | `stale_supporting_artifacts` | `identity_mismatch` | `incomplete_packet`
- `review_gate_status` — one of: `not_run` | `incomplete` | `pass` | `fail`
- `committee_status` — one of: `open` | `answered` | `closed_superseded_by_review` | `reopened_by_council`
- `next_action` — one of: `revise` | `peer_review_round_1` | `peer_review_round_2` | `ratification_motion` | `archive` | `manual_resolution`
- `lifecycle_phase` — one of: `planning` | `phase_e_revision` | `round_1_complete` | `round_2_ready` | `ratification_ready` | `archived`
- `status_updated_at`, `status_updated_by`

**Semantics:** The former “status split” (artifact health vs AMD-2026-005 gate vs next step) lives **here**, not in identity.

**Mutation:** `peer_review.py` updates status after each completed round (preserving `committee_status` if already set by coordinators). Authors may edit status when policy allows (e.g. committee closure).

### `PACKET_EVENTS.yaml`

**Top-level:** `packet_schema_version`, `document_id`, `packet_slug`, `events` (list).

**Each event** includes: `event_id`, `timestamp`, `actor`, `event_type`, `from_version`, `to_version`, `round`, `summary` (one paragraph max), `evidence_paths` (list of repo-relative paths).

**Allowed `event_type` values:**  
`packet_initialized` | `draft_revised` | `review_round_completed` | `review_gate_failed` | `review_gate_passed` | `committee_closed_superseded` | `packet_status_corrected` | `handoff_hardening_applied` | `external_review_package_created`

**Append-only rule:** New events are **appended**. Existing events are **never deleted or rewritten** except by an explicit governance repair (which must add a `packet_status_corrected` or `handoff_hardening_applied` event describing the correction).

### `HANDOFF_NOTE.md`

Non-authoritative prose only. **Must not** be the sole holder of structured state that is absent from `PACKET_STATUS.yaml` / `PACKET_EVENTS.yaml`. If prose contradicts YAML, **YAML wins**.

## Mutation rules

1. **Identity** — replaced in full on each `peer_review.py` run for that round folder (identity-only fields).
2. **Status** — merged/replaced per `peer_review.py` and coordinator policy; must remain valid per controlled vocabularies.
3. **Events** — append-only; `peer_review.py` appends `review_round_completed` and `review_gate_passed` or `review_gate_failed` when gate inference succeeds (see `review_packet_taxonomy.py`).
4. **Handoff** — edited by humans; optional default stub created if missing.

## Validator rule

Run from repository root:

```bash
py -3 scripts/validate_review_packet.py --round-dir reviews/<packet_slug>/round_<N>
```

- Exit **0** = no `FAIL:` conditions (may still print `legacy_packet_schema` or `schema_version_missing` notes).
- Exit **non-zero** = at least one `FAIL:` condition (missing file, invalid enum, broken evidence path, identity/status mismatch, etc.).

**Handoff rule:** Do not upload or export a packet for external consumption without running the validator and resolving `FAIL:` results.

## Legacy packet guidance

Packets for older amendments (for example **AMD-2026-006**, **AMD-2026-007**) may still use **pre–schema-2** layouts (e.g. identity files with `handoff_note`, `document_slug`, or mixed state). The validator reports:

- **`legacy_packet_schema`** when disallowed keys appear in `PACKET_IDENTITY.yaml`.
- **`schema_version_missing`** when `packet_schema_version` is absent.

**Do not** treat legacy packets as silently migrated: full migration is **out of scope** for a single repair pass; migrate per packet deliberately.

## External review export guidance

1. Run `validate_review_packet.py` for the target `round_N` folder.
2. Include `PACKET_IDENTITY.yaml`, `PACKET_STATUS.yaml`, `PACKET_EVENTS.yaml`, `HANDOFF_NOTE.md`, manifest JSON, reviews, `RATIFICATION_GATE_REPORT.md`, and `REVIEW_SYNTHESIS.md` as applicable.
3. Treat `PACKET_STATUS.yaml` as the structured summary of gate and next action; treat `PACKET_EVENTS.yaml` as the audit trail.

## Export package naming

Exported zip artifacts use exactly:

`<artifact_class>__<document_id>__<date>.zip`

Examples:

- `peer_review_package__AMD-2026-008-ADD-004__2026-04-08.zip`
- `peer_review_export__AMD-2026-008-ADD-004__2026-04-08.zip`

Rules:

- Use the canonical `document_id` (for example **`AMD-2026-008-ADD-004`**), not shorthand labels such as **ADD004**.
- Use **double underscores** between segments.
- Put the **artifact class first** (what the zip *is*).
- Do **not** prefix with the repository name or mix repo-name-first and document-id-first conventions in the same export system.
- Treat **`peer_review_export`** as the self-contained evidence archive class. Treat **`peer_review_package`** as a smaller helper bundle/package class only; do not use the two names interchangeably.
- Self-contained governed exports preserve the **repo-relative tree** at archive root and use normalized **`/`** separators in archive entries so the archive remains portable outside the author's working-tree layout.

**Windows extraction:** Unzip under a **short base path** (for example `C:\e\out\`). Deep paths under `reviews/<packet_slug>/...` may exceed legacy **`MAX_PATH`** when combined with long temp directories, producing **incomplete extraction** with default tools. That is an environment constraint, not a packet validator failure.

---

*Reference implementation standard — AIOS-REVIEW-PACKET-TAXONOMY-001 — v1.0.0.*

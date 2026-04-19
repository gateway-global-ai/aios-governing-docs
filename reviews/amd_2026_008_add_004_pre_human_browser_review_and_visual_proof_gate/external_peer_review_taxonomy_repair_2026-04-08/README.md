# External peer review — review packet taxonomy repair (2026-04-08)

This package documents **governance + tooling repair** that splits peer-review packet metadata into **four first-class artifact classes** so identity, workflow status, process history, and human handoff are no longer conflated. It also documents the export-layer repair needed to make the standalone evidence package verifiable under Windows path constraints.

## What changed (exact design)

| Class | File | Role |
|-------|------|------|
| Identity | `PACKET_IDENTITY.yaml` | **Stable** facts only (`document_id`, paths, slug, `current_head_version`, round, manifest path, `packet_schema_version`, generation metadata). **No** gate, committee, or “status split”. |
| Status | `PACKET_STATUS.yaml` | **Mutable** structured state: `artifact_health`, `review_gate_status`, `committee_status`, `next_action`, `lifecycle_phase`, **`last_reviewed_version`**. |
| Events | `PACKET_EVENTS.yaml` | **Append-only** process memory (`event_type`, versions, round, `evidence_paths`). |
| Handoff | `HANDOFF_NOTE.md` | **Non-authoritative** human orientation; YAML wins if conflict. |

**Reference standard:** [`reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`](../../../reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)

**Validator:** [`scripts/validate_review_packet.py`](../../../scripts/validate_review_packet.py) — exit **0** = no `FAIL:` lines.

## Inspect first (canonical order)

1. [`AIOS-REVIEW-PACKET-TAXONOMY-001.md`](../../../reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)
2. [`round_1/PACKET_IDENTITY.yaml`](../round_1/PACKET_IDENTITY.yaml), [`round_1/PACKET_STATUS.yaml`](../round_1/PACKET_STATUS.yaml), [`round_1/PACKET_EVENTS.yaml`](../round_1/PACKET_EVENTS.yaml), [`round_1/HANDOFF_NOTE.md`](../round_1/HANDOFF_NOTE.md)
3. [`scripts/peer_review.py`](../../../scripts/peer_review.py), [`scripts/review_packet_taxonomy.py`](../../../scripts/review_packet_taxonomy.py), [`scripts/validate_review_packet.py`](../../../scripts/validate_review_packet.py)
4. [`DEVELOPER.md`](../../../DEVELOPER.md) (peer review section)
5. `CHANGELOG.md` excerpt in **`CHANGELOG_EXCERPT_PACKET_TAXONOMY.md`**

## Supporting docs in this package

| File | Purpose |
|------|---------|
| `AUDIT_AND_CHANGE_HISTORY.md` | Failure analysis, motive, repair mapping |
| `FILE_MANIFEST.md` | Every changed or added path |
| `CHANGELOG_EXCERPT_PACKET_TAXONOMY.md` | Verbatim changelog bullets |
| `REVIEWER_CHECKLIST.md` | Verification checklist |

---

*Taxonomy repair — external peer review — 2026-04-08.*

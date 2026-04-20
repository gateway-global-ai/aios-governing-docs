# Package index — peer review of changes

Paths relative to **`aios-governing-docs`** repo root unless noted.

## Standalone export (zip)

After running **PowerShell** against **`peer_review_package_2026-04-08/build_standalone_zip.ps1`**, **`reviews/peer_review_export__AMD-2026-008-ADD-004__2026-04-08.zip`** contains `README_STANDALONE.md` plus `reference/`, `scripts/` (three Python files), `DEVELOPER.md`, and `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/` at the **archive root** — sufficient to verify tooling **source** alongside the packet. **`validate_review_packet.py`** runs from the unzip root if Python + PyYAML match the repo (see **`README_STANDALONE.md`** for Windows path limits).

## Entry points

| Path | Role |
|------|------|
| `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/peer_review_package_2026-04-08/README.md` | **This review package** — start here |
| `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/external_peer_review_taxonomy_repair_2026-04-08/README.md` | Taxonomy repair deep-dive |
| `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/external_peer_review_audit_2026-04-08/README.md` | Earlier audit (committee / status split) |

## Reference & tooling

| Path | Role |
|------|------|
| `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md` | Normative reference (not an amendment) |
| `scripts/peer_review.py` | Writes identity + status + events |
| `scripts/review_packet_taxonomy.py` | Gate inference + helpers |
| `scripts/validate_review_packet.py` | Fail-closed validation |
| `DEVELOPER.md` | Developer rules + validator command |
| `CHANGELOG.md` | `[Unreleased]` — taxonomy bullet |

## ADD-004 round_1 packet (migrated schema `2`)

| Path | Role |
|------|------|
| `reviews/.../round_1/PACKET_IDENTITY.yaml` | Identity only |
| `reviews/.../round_1/PACKET_STATUS.yaml` | Workflow state |
| `reviews/.../round_1/PACKET_EVENTS.yaml` | Append-only events |
| `reviews/.../round_1/HANDOFF_NOTE.md` | Non-authoritative handoff |
| `reviews/.../round_1/RATIFICATION_GATE_REPORT.md` | Gate **FAIL** evidence (unchanged outcome) |
| `reviews/.../round_1/REVIEW_SYNTHESIS.md` | Triangulation synthesis |
| `reviews/.../README.md` | Packet index |

## Taxonomy repair peer-review bundle

| Path | Role |
|------|------|
| `.../external_peer_review_taxonomy_repair_2026-04-08/AUDIT_AND_CHANGE_HISTORY.md` | Failure + repair narrative |
| `.../external_peer_review_taxonomy_repair_2026-04-08/FILE_MANIFEST.md` | Changed files list |
| `.../external_peer_review_taxonomy_repair_2026-04-08/CHANGELOG_EXCERPT_PACKET_TAXONOMY.md` | Changelog excerpt |
| `.../external_peer_review_taxonomy_repair_2026-04-08/REVIEWER_CHECKLIST.md` | Verification checklist |

## Optional context audit

| Path | Role |
|------|------|
| `.../external_peer_review_audit_2026-04-08/AUDIT_AND_CHANGE_HISTORY.md` | Pre-taxonomy audit |
| `.../external_peer_review_audit_2026-04-08/FILE_MANIFEST.md` | File list (older scope) |
| `.../external_peer_review_audit_2026-04-08/CHANGELOG_EXCERPT_ADD004.md` | Changelog excerpt |

---

*Index — peer review package — 2026-04-08.*

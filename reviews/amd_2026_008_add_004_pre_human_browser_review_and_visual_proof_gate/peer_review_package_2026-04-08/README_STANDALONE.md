# Standalone export — ADD-004 peer review (tooling + packet)

This file is copied to the **root** of the **standalone zip** so reviewers can verify **taxonomy reference**, **scripts**, **`DEVELOPER.md`**, and the **ADD-004 packet** without relying on paths outside the archive.

## What is in this zip

| Path in archive | Contents |
|-----------------|----------|
| `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md` | Packet taxonomy reference (normative for schema `2`) |
| `scripts/peer_review.py` | Peer review engine (writes identity / status / events) |
| `scripts/review_packet_taxonomy.py` | Gate inference + YAML helpers |
| `scripts/validate_review_packet.py` | Fail-closed packet validator |
| `DEVELOPER.md` | Developer guide (peer review + validator section) |
| `amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md` | Assessed amendment (required so `PACKET_EVENTS.yaml` evidence paths resolve) |
| `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/` | Full packet tree (`round_1`, planning, audit folders, etc.) |

Paths mirror the **`aios-governing-docs`** repository root.

## Validator (from unzip root)

Extract the zip into a **short path** and use that extraction directory as the unzip root. Example: **`C:\e\peer_review_export__AMD-2026-008-ADD-004__2026-04-08\`**.

From that unzip root, run:

```bash
py -3 scripts/validate_review_packet.py --round-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1
```

Exit **0** and no `FAIL:` lines ⇒ packet YAML checks pass. (**Requires Python 3** and **`pyyaml`** as used by the scripts.)

**Windows:** The archive root contains repo-relative paths directly (no extra wrapper folder), but the packet tree is still long. Extract to a **short path** (for example `C:\e\peer_review_export__AMD-2026-008-ADD-004__2026-04-08\`). `Expand-Archive` under a deep workspace path can still hit **`MAX_PATH`**, yielding incomplete extraction and false `FAIL:` from missing evidence paths. If extraction is incomplete, the export is not validated in that location.

## Suggested reading order

1. `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`
2. `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1/PACKET_STATUS.yaml`
3. `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1/PACKET_EVENTS.yaml`
4. `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1/PACKET_IDENTITY.yaml`
5. `scripts/peer_review.py` (search for `write_packet_identity_v2`, `merge_and_write_packet_status`, `append_packet_events_peer_review`)
6. `scripts/validate_review_packet.py`
7. `DEVELOPER.md` (peer review / taxonomy bullets)
8. `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/peer_review_package_2026-04-08/README.md` — narrative index (repo-relative `../` links may not resolve inside the zip; use this **README_STANDALONE** for paths)

## Repo checkout vs standalone

| Mode | Use when |
|------|----------|
| **Full clone** | Follow `peer_review_package_2026-04-08/README.md` with `../../../` links to the rest of the repo. |
| **This zip** | Tooling and packet are **self-contained** for evidence review; no claim that the **entire** monorepo is included. |

---

*Standalone export README — ADD-004 — 2026-04-08.*

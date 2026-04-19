# CHANGELOG excerpt — packet taxonomy repair

**Source:** `CHANGELOG.md` — `## [Unreleased]` — `### Changed` — top bullets (2026-04-08). Authoritative file: repository root **`CHANGELOG.md`**.

---

### Changed

- **Review packet taxonomy repair — schema `2` (2026-04-08):** Split overloaded **`PACKET_IDENTITY.yaml`** into **identity-only** (`packet_schema_version` **`2`**) plus **[`PACKET_STATUS.yaml`](reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1/PACKET_STATUS.yaml)** (mutable workflow state; `last_reviewed_version` replaces ad hoc “reviewed draft” fields) plus **[`PACKET_EVENTS.yaml`](reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1/PACKET_EVENTS.yaml)** (append-only process memory) plus **[`HANDOFF_NOTE.md`](reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1/HANDOFF_NOTE.md)** (non-authoritative). Reference **[AIOS-REVIEW-PACKET-TAXONOMY-001](reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)**. **`scripts/peer_review.py`** rewrites identity, merges status, appends events; **`scripts/review_packet_taxonomy.py`** (AMD-2026-005 gate inference); **`scripts/validate_review_packet.py`** (fail-closed; **`legacy_packet_schema`** / **`schema_version_missing`** reporting). **ADD-004** **`round_1/`** migrated without changing Round 1 gate outcome; **[`revision_log.md`](reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/revision_log.md)** Phase H; **[`DEVELOPER.md`](DEVELOPER.md)** export rule; **[`reviews/amd_2026_007/README.md`](reviews/amd_2026_007/README.md)** legacy warning.

*(Follow-on bullets in root `CHANGELOG.md` cover older ADD-004 phases; omitted here.)*

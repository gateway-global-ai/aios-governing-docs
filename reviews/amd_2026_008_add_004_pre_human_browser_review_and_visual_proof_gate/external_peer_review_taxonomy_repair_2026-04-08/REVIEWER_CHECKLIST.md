# Reviewer checklist — taxonomy repair

Use with **`validate_review_packet.py`** and **`AIOS-REVIEW-PACKET-TAXONOMY-001.md`**.

## Split correctness

- [ ] **`PACKET_IDENTITY.yaml`** contains **only** allowed identity fields (no `handoff_note`, `status_split`, `round_1_reviewed_draft`, `schema` v1 hybrid keys).
- [ ] **`PACKET_STATUS.yaml`** holds **`artifact_health`**, **`review_gate_status`**, **`committee_status`**, **`next_action`**, **`lifecycle_phase`**, **`last_reviewed_version`**.
- [ ] **`PACKET_STATUS.yaml`** contains **no extra keys** outside the controlled schema.
- [ ] **`PACKET_EVENTS.yaml`** is append-only structure; each event has required keys, no extra keys, and allowed **`event_type`**.
- [ ] **`HANDOFF_NOTE.md`** exists, includes the YAML-precedence warning, and does not introduce exclusive structured state absent from YAML.

## ADD-004 meaning preserved

- [ ] **`current_head_version`** is **`0.3.0`** (matches amendment head).
- [ ] **`last_reviewed_version`** is **`0.2.0`** (Round 1 assessed draft).
- [ ] **`artifact_health`** is **`healthy`**.
- [ ] **`review_gate_status`** is **`fail`** for Round 1 on **`0.2.0`** (unchanged from historical gate report).
- [ ] **`committee_status`** is **`closed_superseded_by_review`** (maps prior “superseded by Round 1 findings” posture).
- [ ] **`next_action`** is **`peer_review_round_2`** when head is ahead of **`last_reviewed_version`** after a Round 1 gate fail; lifecycle consistent with **`round_2_ready`**.
- [ ] **`RATIFICATION_GATE_REPORT.md`** / **`REVIEW_SYNTHESIS.md`** still read as **FAIL**, not **PASS**.

## Tooling

- [ ] **`peer_review.py`** run would regenerate **`PACKET_IDENTITY.yaml`**, update **`PACKET_STATUS.yaml`**, **append** **`PACKET_EVENTS.yaml`**, and keep **`review_*__<DOCUMENT_ID>.md`** naming (via **`context_assembler.save_review`**).
- [ ] **`py -3 scripts/validate_review_packet.py --round-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1`** exits **0**.
- [ ] **`build_standalone_zip.ps1`** and **`build_peer_review_package_zip.ps1`** run under **PowerShell** in this workspace.
- [ ] **`peer_review_export__AMD-2026-008-ADD-004__2026-04-08.zip`** extracts with repo-relative paths at archive root and validates from the unzip root when extracted to a short Windows path.

## Validator failure modes

- [ ] Introduce a deliberate **`document_id`** mismatch between identity and status → expect **`FAIL:`** and non-zero exit.
- [ ] Introduce a missing **`evidence_paths`** file referenced in an event → expect **`FAIL:`**.

## Legacy packets

- [ ] **`reviews/amd_2026_007/README.md`** states pre–schema-2 layout; older **`round_*`** folders are **not** claimed as migrated.
- [ ] Running the validator on an **unmigrated** legacy **`round_1/`** (if identity has v1 keys) reports **`legacy_packet_schema`** / **`schema_version_missing`** as appropriate, not silent success as schema-2.

---

*Checklist — 2026-04-08.*

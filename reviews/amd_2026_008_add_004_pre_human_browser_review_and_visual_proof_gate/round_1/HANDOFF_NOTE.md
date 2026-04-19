# Handoff note — AMD-2026-008-ADD-004 — `round_1` (non-authoritative)

**If this note contradicts `PACKET_STATUS.yaml` or `PACKET_EVENTS.yaml`, the YAML artifacts win.**

## Upload and attachment hygiene

- This packet is **only** for **`AMD-2026-008-ADD-004`**. Other review folders (for example **`reviews/amd_2026_006/`**, **`reviews/amd_2026_007/`**) may contain files named `review_001_deepseek.md` — **do not** mix uploads.
- Every review file here uses **`review_<NNN>_<model>__AMD-2026-008-ADD-004.md`**. Confirm the **`__AMD-2026-008-ADD-004`** suffix before exporting or attaching outside the repo.

## Where structured truth lives

- **Stable identity:** `PACKET_IDENTITY.yaml` (no workflow state).
- **Current workflow truth:** `PACKET_STATUS.yaml` (artifact health, gate, committee, next action).
- **Process memory (append-only):** `PACKET_EVENTS.yaml`.
- **Validator:** run `py -3 scripts/validate_review_packet.py --round-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1` from the repo root before handoff.

## Operational reminders

- Round 1 **assessed** **`draft` `0.2.0`**; current doctrine head is **`0.3.0`** — see `PACKET_STATUS.yaml`.
- Round 2 should target **`peer_review.py --round 2`** when coordinator policy allows.

---

*Non-authoritative orientation only — see AIOS-REVIEW-PACKET-TAXONOMY-001.*

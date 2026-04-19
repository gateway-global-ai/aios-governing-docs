# Handoff note — AMD-2026-008-ADD-004 — `round_2` (non-authoritative)

**If this note contradicts `PACKET_STATUS.yaml` or `PACKET_EVENTS.yaml`, the YAML artifacts win.**

## Upload and attachment hygiene

- This packet is **only** for **`AMD-2026-008-ADD-004`**. Do **not** mix Round 1 artifacts or other amendment folders into this Round 2 path.
- Every Round 2 review file here must use **`review_<NNN>_<model>__AMD-2026-008-ADD-004.md`** so the addendum stays unambiguous outside the repo.

## Where structured truth lives

- **Stable identity:** `PACKET_IDENTITY.yaml` (no workflow state).
- **Current workflow truth:** `PACKET_STATUS.yaml` (artifact health, gate, committee, next action).
- **Process memory (append-only):** `PACKET_EVENTS.yaml`.
- **Validator:** run `py -3 scripts/validate_review_packet.py --round-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_2` from the repo root before handoff or Round 2 execution.

## Operational reminders

- Round 1 remains the historical review record for assessed **`draft` `0.2.0`** under `../round_1/`.
- This `round_2/` packet assessed current doctrine head **`draft` `0.3.0`**.
- Round 2 execution is complete in this folder: triad reviews, manifest, synthesis, and gate report are present.
- The Round 2 gate result is **FAIL**; the governed next step is **revision**, not ratification or Round 1 reopening.

---

*Non-authoritative orientation only — see AIOS-REVIEW-PACKET-TAXONOMY-001.*

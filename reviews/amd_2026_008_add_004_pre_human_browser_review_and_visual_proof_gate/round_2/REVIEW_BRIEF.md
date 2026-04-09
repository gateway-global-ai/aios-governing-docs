# Peer review brief — AMD-2026-008-ADD-004 (Round 2)

**Fail-closed check:** Confirm **`document_id`** in **[`PACKET_IDENTITY.yaml`](PACKET_IDENTITY.yaml)** **and** **[`PACKET_STATUS.yaml`](PACKET_STATUS.yaml)** — **`AMD-2026-008-ADD-004`**. Run **`py -3 scripts/validate_review_packet.py --round-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_2`** from repo root before starting the review run.  
Review filenames **must** contain **`__AMD-2026-008-ADD-004`**.

**This packet is for the ADD-004 addendum only.**  
If you see **`AMD-2026-006`**, **`AMD-2026-007`**, or any Round 1 `0.2.0` gate artifact presented as current Round 2 output, you have the **wrong** packet state.

---

## Canonical target

| Field | Value |
|-------|--------|
| **document_id** | **AMD-2026-008-ADD-004** |
| **Title** | Pre-Human Browser Review and Visual Proof Gate |
| **Amendment file** | [`amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md`](../../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) |
| **Round 2 target** | **`draft` `0.3.0`** |
| **Last reviewed draft** | **`0.2.0`** — see `last_reviewed_version` in **`PACKET_STATUS.yaml`** |
| **Parent** | [`AMD-2026-008`](../../../amendments/AMD-2026-008.md) — *Sovereign Voice and Local Runtime Lanes* |

---

## Round 2 preparation artifacts in *this* folder

| File | Role |
|------|------|
| [`PACKET_STATUS.yaml`](PACKET_STATUS.yaml) | **Authoritative** mutable workflow state for the prepared Round 2 path |
| [`PACKET_EVENTS.yaml`](PACKET_EVENTS.yaml) | **Append-only** process memory for Round 2 packet preparation and later execution |
| [`PACKET_IDENTITY.yaml`](PACKET_IDENTITY.yaml) | **Stable identity** only (`packet_schema_version` **2**) |
| [`HANDOFF_NOTE.md`](HANDOFF_NOTE.md) | Non-authoritative human orientation |
| [`README.md`](README.md) | Round 2 entry point and exact next action |

---

## Expected Round 2 outputs after execution

| File class | Expected artifact |
|------------|-------------------|
| Review lanes | `review_001_deepseek__AMD-2026-008-ADD-004.md`, `review_002_openai__AMD-2026-008-ADD-004.md`, `review_003_gemini__AMD-2026-008-ADD-004.md` |
| Machine record | `peer_review_manifest_<timestamp>.json` |
| Synthesis | `REVIEW_SYNTHESIS.md` |
| Gate | `RATIFICATION_GATE_REPORT.md` |

Round 1 historical artifacts live under [`../round_1/`](../round_1/) and must **not** be reused as Round 2 outputs.

---

*REVIEW_BRIEF — ADD-004 Round 2 prep — 2026-04-09.*

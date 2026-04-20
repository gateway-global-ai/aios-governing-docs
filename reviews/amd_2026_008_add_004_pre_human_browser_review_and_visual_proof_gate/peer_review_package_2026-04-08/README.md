# Peer review package — governance & tooling changes (2026-04-08)

Use this folder as the **single entry point** when asking an external peer to review recent **`aios-governing-docs`** work tied to **AMD-2026-008-ADD-004** and the **review packet taxonomy** repair.

## Repo checkout vs standalone zip

| Mode | What you get |
|------|----------------|
| **This clone** | Packet tree + **relative links** (`../../../reference/...`, `../../../scripts/...`) to the rest of the repo. |
| **Standalone zip** | **Self-contained** evidence for tooling claims: taxonomy doc, `peer_review.py`, `review_packet_taxonomy.py`, `validate_review_packet.py`, `DEVELOPER.md`, and the full ADD-004 `reviews/...` tree — see **[`README_STANDALONE.md`](README_STANDALONE.md)**. Build with **PowerShell** via **[`build_standalone_zip.ps1`](build_standalone_zip.ps1)** (outputs `reviews/peer_review_export__AMD-2026-008-ADD-004__2026-04-08.zip` at repo root). Optional **`build_peer_review_package_zip.ps1`** builds **`reviews/peer_review_package__AMD-2026-008-ADD-004__2026-04-08.zip`** (this folder only). |

**Running** `peer_review.py` end-to-end still requires the full **`scripts/`** dependency graph (e.g. `context_assembler.py`) and `.env`; the standalone zip is sized for **independent review of the taxonomy implementation and validator**, not a minimal runnable venv.

## What you are reviewing

1. **Review packet taxonomy (primary)** — Split of peer-review metadata into **`PACKET_IDENTITY.yaml`** (identity only), **`PACKET_STATUS.yaml`** (workflow state), **`PACKET_EVENTS.yaml`** (append-only history), and **`HANDOFF_NOTE.md`** (non-authoritative prose), plus **`peer_review.py`** / **`validate_review_packet.py`** / **`review_packet_taxonomy.py`** and **[AIOS-REVIEW-PACKET-TAXONOMY-001](../../../reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)**.

2. **Earlier audit package (context, optional)** — Committee closure and “status split” documentation that preceded the taxonomy hardening: **[`external_peer_review_audit_2026-04-08`](../external_peer_review_audit_2026-04-08/README.md)**.

## Canonical reading order (taxonomy + ADD-004)

| Step | Artifact |
|------|----------|
| 1 | **[AIOS-REVIEW-PACKET-TAXONOMY-001](../../../reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)** — purpose, four classes, rules |
| 2 | **[`round_1/PACKET_STATUS.yaml`](../round_1/PACKET_STATUS.yaml)** — structured truth for ADD-004 |
| 3 | **[`round_1/PACKET_EVENTS.yaml`](../round_1/PACKET_EVENTS.yaml)** — process memory |
| 4 | **[`round_1/PACKET_IDENTITY.yaml`](../round_1/PACKET_IDENTITY.yaml)** — identity-only (schema `2`) |
| 5 | **[`DEVELOPER.md`](../../../DEVELOPER.md)** — peer review / validator section |
| 6 | **Detailed audit + checklist** — **[`external_peer_review_taxonomy_repair_2026-04-08`](../external_peer_review_taxonomy_repair_2026-04-08/README.md)** |

## Sub-packages (self-contained)

| Package | Path | Use when |
|---------|------|----------|
| **Taxonomy repair (full)** | [`../external_peer_review_taxonomy_repair_2026-04-08/`](../external_peer_review_taxonomy_repair_2026-04-08/README.md) | You want audit narrative, file manifest, changelog excerpt, reviewer checklist |
| **Prior status-split audit** | [`../external_peer_review_audit_2026-04-08/`](../external_peer_review_audit_2026-04-08/README.md) | You want context on committee closure and pre-taxonomy wording |

## Verify before sign-off

From repository root (`aios-governing-docs`):

```bash
py -3 scripts/validate_review_packet.py --round-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/round_1
```

Exit code **0** and no `FAIL:` lines on stderr is required for a clean packet.

## Flat index

See **[`PACKAGE_INDEX.md`](PACKAGE_INDEX.md)** for a consolidated list of paths and roles.

---

*Peer review package — 2026-04-08 — ADD-004 packet tree.*

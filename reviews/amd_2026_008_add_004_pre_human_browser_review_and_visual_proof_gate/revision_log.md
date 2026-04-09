# Revision log — AMD-2026-008-ADD-004 (pre-human browser review and visual proof gate)

## Phase A — intake (2026-04-08)

| Item | Detail |
|------|--------|
| **Draft filed** | [`AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md`](../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) **`0.1.0`** |
| **Parent AMD** | [`AMD-2026-008`](../../amendments/AMD-2026-008.md) — addenda list updated |
| **Knowledge** | [`AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001`](../../reference/implementation/AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001.md) |
| **Quarantine** | [`sources/AMD-2026-008-ADD-004/external_reference_quarantine.md`](../../sources/AMD-2026-008-ADD-004/external_reference_quarantine.md) — `https://github.com/continuedev/continue` |
| **Planning** | [`planning/ARCHITECT_PLAN.md`](planning/ARCHITECT_PLAN.md), [`planning/UI_PLAN.md`](planning/UI_PLAN.md), [`planning/COMMITTEE_PACKET.md`](planning/COMMITTEE_PACKET.md) — **closed** **`superseded_by_round_1_findings`** **2026-04-08** |

**Next:** Phase B–D committee sign-off → Phase E author revision → **`peer_review.py`** Round 1.

## Phase F — peer review Round 1 (partial) — `0.1.0` (2026-04-08)

| Item | Detail |
|------|--------|
| **Command** | `peer_review.py` — `--round 1` `--rubric light` `--smart-context` |
| **Reviews** | [`archive_draft_0.1.0_2026-04-08/review_001_openai.md`](round_1/archive_draft_0.1.0_2026-04-08/review_001_openai.md), [`archive_draft_0.1.0_2026-04-08/review_002_gemini.md`](round_1/archive_draft_0.1.0_2026-04-08/review_002_gemini.md) |
| **Manifest** | [`archive_draft_0.1.0_2026-04-08/peer_review_manifest_20260408T224317Z.json`](round_1/archive_draft_0.1.0_2026-04-08/peer_review_manifest_20260408T224317Z.json) |
| **Gate** | **INCOMPLETE** triad (two lanes only) — superseded |

## Phase E — author revision `0.1.0` → `0.2.0` (2026-04-08)

| Change | Sections |
|--------|----------|
| Definitions | **§0.1** |
| Proportionality | **§4.1** |
| Review target / schema home | **§6.1** |
| Test-captured proof | **§7.2**, **§7.3** |
| Remediation / blocked exit | **§9.4** |

## Phase F — peer review Round 1 re-run — `0.2.0` (2026-04-08)

| Item | Detail |
|------|--------|
| **Command** | `peer_review.py --round 1 --rubric light --smart-context --models deepseek openai gemini` |
| **Reviews** | [`round_1/review_001_deepseek__AMD-2026-008-ADD-004.md`](round_1/review_001_deepseek__AMD-2026-008-ADD-004.md), [`round_1/review_002_openai__AMD-2026-008-ADD-004.md`](round_1/review_002_openai__AMD-2026-008-ADD-004.md), [`round_1/review_003_gemini__AMD-2026-008-ADD-004.md`](round_1/review_003_gemini__AMD-2026-008-ADD-004.md) |
| **Packet artifacts** | [`round_1/PACKET_IDENTITY.yaml`](round_1/PACKET_IDENTITY.yaml) (superseded layout pre–Phase H); post–Phase H: identity + **[`PACKET_STATUS.yaml`](round_1/PACKET_STATUS.yaml)** + **[`PACKET_EVENTS.yaml`](round_1/PACKET_EVENTS.yaml)** |
| **Manifest** | [`round_1/peer_review_manifest_20260408T234537Z.json`](round_1/peer_review_manifest_20260408T234537Z.json) |
| **Synthesis** | [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md) |
| **Gate** | [`round_1/RATIFICATION_GATE_REPORT.md`](round_1/RATIFICATION_GATE_REPORT.md) — **FAIL** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** (DeepSeek composite **2.8**; dimensions **&lt; 3**) |

**Next:** **`peer_review.py` Round 2** on **`draft` `0.3.0`** when ready.

## Phase G — author revision `0.2.0` → `0.3.0` + committee closure (2026-04-08)

| Item | Detail |
|------|--------|
| **Amendment** | **`draft` `0.3.0`** — **§0** artifact vs gate row; **§0.2** Round 2 prep mapping synthesis themes; **§2.1** SPEC/MPOA pointers; **§3.4** policy-equivalent surfaces; **§11.1** implementation seam; **§12.4** addendum precedence |
| **Status split** | **Artifact health** — **good**; **review gate** — **FAIL** at **`0.2.0`** (unchanged fact); **next** — **Round 2 peer review** on **`draft` `0.3.0`**, not ratification |
| **Committee** | [`planning/COMMITTEE_PACKET.md`](planning/COMMITTEE_PACKET.md) — **closed** **`superseded_by_round_1_findings`** — procedural closure; implementation follow-ons **re-scoped** in **§11.1** |

## Phase H — review packet taxonomy repair (2026-04-08)

| Item | Detail |
|------|--------|
| **Reference** | **[`AIOS-REVIEW-PACKET-TAXONOMY-001`](../../reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)** — four artifact classes (identity / status / events / handoff) |
| **New artifacts** | [`round_1/PACKET_STATUS.yaml`](round_1/PACKET_STATUS.yaml), [`round_1/PACKET_EVENTS.yaml`](round_1/PACKET_EVENTS.yaml), [`round_1/HANDOFF_NOTE.md`](round_1/HANDOFF_NOTE.md); [`round_1/PACKET_IDENTITY.yaml`](round_1/PACKET_IDENTITY.yaml) normalized to **identity-only** (`packet_schema_version` **2**) |
| **Tooling** | [`scripts/peer_review.py`](../../scripts/peer_review.py) writes identity + status + append-only events; [`scripts/validate_review_packet.py`](../../scripts/validate_review_packet.py) fail-closed validation |
| **Preserved meaning** | Current head **`0.3.0`**; **`last_reviewed_version`** **`0.2.0`**; **`artifact_health`** **`healthy`**; **`review_gate_status`** **`fail`**; **`committee_status`** **`closed_superseded_by_review`**; **`next_action`** **`peer_review_round_2`** |

## Phase I — status correction + export contract (2026-04-09)

| Item | Detail |
|------|--------|
| **Status / events** | **`next_action`** corrected from stale **`revise`** to **`peer_review_round_2`**; append-only **`packet_status_corrected`** **`evt-20260408-009`** |
| **Export** | Artifacts **`peer_review_export__AMD-2026-008-ADD-004__2026-04-08.zip`**, **`peer_review_package__AMD-2026-008-ADD-004__2026-04-08.zip`**; **`build_standalone_zip.ps1`** includes **`amendments/`** so **`validate_review_packet.py`** passes at unzip root |

**Next:** **Round 2** peer review on **`draft` `0.3.0`**; do **not** reopen doctrine drafting in this packet hygiene slice.

## Note — folder disambiguation (2026-04-08)

Peer-review **filenames** overlap with **[`reviews/amd_2026_007/round_1/`](../amd_2026_007/round_1/)** (`review_001_openai.md`, etc.). **[`round_1/REVIEW_BRIEF.md`](round_1/REVIEW_BRIEF.md)** documents the canonical **ADD-004** paths and targets.

---

*Log started 2026-04-08.*

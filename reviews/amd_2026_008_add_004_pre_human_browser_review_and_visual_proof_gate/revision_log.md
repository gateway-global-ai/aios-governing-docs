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

## Phase J — Round 2 packet preparation (2026-04-09)

| Item | Detail |
|------|--------|
| **Round 2 path** | Added clean governed packet surfaces under [`round_2/`](round_2/) — [`PACKET_IDENTITY.yaml`](round_2/PACKET_IDENTITY.yaml), [`PACKET_STATUS.yaml`](round_2/PACKET_STATUS.yaml), [`PACKET_EVENTS.yaml`](round_2/PACKET_EVENTS.yaml), [`HANDOFF_NOTE.md`](round_2/HANDOFF_NOTE.md), [`REVIEW_BRIEF.md`](round_2/REVIEW_BRIEF.md), [`README.md`](round_2/README.md) |
| **Target** | Round 2 packet explicitly points to **`AMD-2026-008-ADD-004`** **`draft` `0.3.0`** while preserving **`last_reviewed_version`** **`0.2.0`** as the historical Round 1 assessment baseline |
| **Root pointers** | Packet root [`README.md`](README.md) now treats **`round_2/`** as the live structured path and leaves **`round_1/`** explicitly historical |

**Next:** Run **`peer_review.py --round 2`** against **`draft` `0.3.0`** from the prepared **`round_2/`** packet path; do **not** reuse Round 1 outputs as current review artifacts.

## Phase K — peer review Round 2 execution — `0.3.0` (2026-04-09)

| Item | Detail |
|------|--------|
| **Command** | `peer_review.py --round 2 --rubric light --smart-context --models deepseek openai gemini` |
| **Reviews** | [`round_2/review_001_deepseek__AMD-2026-008-ADD-004.md`](round_2/review_001_deepseek__AMD-2026-008-ADD-004.md), [`round_2/review_002_openai__AMD-2026-008-ADD-004.md`](round_2/review_002_openai__AMD-2026-008-ADD-004.md), [`round_2/review_003_gemini__AMD-2026-008-ADD-004.md`](round_2/review_003_gemini__AMD-2026-008-ADD-004.md) |
| **Manifest** | [`round_2/peer_review_manifest_20260409T170114Z.json`](round_2/peer_review_manifest_20260409T170114Z.json) |
| **Synthesis** | [`round_2/REVIEW_SYNTHESIS.md`](round_2/REVIEW_SYNTHESIS.md) |
| **Gate** | [`round_2/RATIFICATION_GATE_REPORT.md`](round_2/RATIFICATION_GATE_REPORT.md) — **FAIL** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** (DeepSeek composite **2.8**; dimensions **< 3**) |
| **Packet repair** | Gemini review front matter repaired after execution so status could be corrected from **`incomplete`** to **`fail`** without reopening the review run |

**Next:** Author revision on top of Round 2 findings; do **not** reopen packet-prep or Round 1 history from this execution slice.

## Phase L — Round 3 execution — `0.4.0` (2026-04-09)

| Item | Detail |
|------|--------|
| **Round 3 path** | Added clean governed packet surfaces under [`round_3/`](round_3/) — [`PACKET_IDENTITY.yaml`](round_3/PACKET_IDENTITY.yaml), [`PACKET_STATUS.yaml`](round_3/PACKET_STATUS.yaml), [`PACKET_EVENTS.yaml`](round_3/PACKET_EVENTS.yaml), [`HANDOFF_NOTE.md`](round_3/HANDOFF_NOTE.md), [`REVIEW_BRIEF.md`](round_3/REVIEW_BRIEF.md), [`README.md`](round_3/README.md) |
| **Target** | Round 3 packet explicitly points to **`AMD-2026-008-ADD-004`** **`draft` `0.4.0`** while preserving **Round 2** under [`round_2/`](round_2/) as the historical failed assessment of **`0.3.0`** |
| **Execution** | Scoped bounded Round 3 review run using the repo peer-review prompt, **light** rubric, **smart context**, and the normal DeepSeek / OpenAI / Gemini triad without mutating `round_2/` |
| **Reviews** | [`round_3/review_001_deepseek__AMD-2026-008-ADD-004.md`](round_3/review_001_deepseek__AMD-2026-008-ADD-004.md), [`round_3/review_002_openai__AMD-2026-008-ADD-004.md`](round_3/review_002_openai__AMD-2026-008-ADD-004.md), [`round_3/review_003_gemini__AMD-2026-008-ADD-004.md`](round_3/review_003_gemini__AMD-2026-008-ADD-004.md) |
| **Manifest** | [`round_3/peer_review_manifest_20260409T185752Z.json`](round_3/peer_review_manifest_20260409T185752Z.json) |
| **Synthesis / gate** | [`round_3/REVIEW_SYNTHESIS.md`](round_3/REVIEW_SYNTHESIS.md), [`round_3/RATIFICATION_GATE_REPORT.md`](round_3/RATIFICATION_GATE_REPORT.md) — **INCOMPLETE** after initial execution (Gemini provider-side **`503 UNAVAILABLE`**) |
| **Packet closeout** | DeepSeek / OpenAI review front matter normalized for Round 3 packet identity; packet stayed **`incomplete`** / **`manual_resolution`** pending a later bounded Gemini-only retry |

**Next:** One narrow Gemini-only manual-resolution pass on the existing **`round_3/`** packet path; do **not** reopen Round 1 / Round 2 hygiene or revise doctrine from the incomplete packet alone.

## Phase M — Round 3 manual resolution — Gemini retry success (2026-04-09)

| Item | Detail |
|------|--------|
| **Retry scope** | Gemini lane only in existing [`round_3/`](round_3/) — no DeepSeek / OpenAI rerun, no amendment-text edits, no new round path |
| **Gemini result** | [`round_3/review_003_gemini__AMD-2026-008-ADD-004.md`](round_3/review_003_gemini__AMD-2026-008-ADD-004.md) — **`approved`**, composite **5.0** |
| **Artifact repair** | Gemini review front matter normalized so the saved review file validates inside the packet |
| **Synthesis / gate refresh** | [`round_3/REVIEW_SYNTHESIS.md`](round_3/REVIEW_SYNTHESIS.md), [`round_3/RATIFICATION_GATE_REPORT.md`](round_3/RATIFICATION_GATE_REPORT.md) — **PASS** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** (minimum composite **3.8**; minimum dimension **3**) |
| **Packet state** | [`round_3/PACKET_STATUS.yaml`](round_3/PACKET_STATUS.yaml) corrected from **`incomplete`** / **`manual_resolution`** to **`pass`** / **`ratification_motion`** with **`ratification_ready`** lifecycle; [`round_3/PACKET_EVENTS.yaml`](round_3/PACKET_EVENTS.yaml) records the successful manual-resolution outcome |

**Next:** Open the ratification-motion path from the completed Round 3 packet state; keep **`round_2/`** as historical **FAIL** on assessed **`0.3.0`** and do **not** reopen prior-round hygiene from this slice.

## Phase N — ratification-motion preparation — `0.4.0` basis (2026-04-09)

| Item | Detail |
|------|--------|
| **Motion** | Added [`AMD-2026-008-ADD-004-ratification-motion.md`](../../amendments/AMD-2026-008-ADD-004-ratification-motion.md) as the narrow Council/coordinator motion surface for **AMD-2026-008-ADD-004** using **`draft` `0.4.0`** as the exact substantive basis |
| **Evidence basis** | Motion points only to the completed [`round_3/`](round_3/) packet, including [`PACKET_STATUS.yaml`](round_3/PACKET_STATUS.yaml), [`REVIEW_SYNTHESIS.md`](round_3/REVIEW_SYNTHESIS.md), and [`RATIFICATION_GATE_REPORT.md`](round_3/RATIFICATION_GATE_REPORT.md) |
| **Packet orientation** | [`round_3/README.md`](round_3/README.md) and [`round_3/HANDOFF_NOTE.md`](round_3/HANDOFF_NOTE.md) now point to the drafted motion as the next governed move |
| **Boundaries preserved** | No doctrine revision, no ratification execution, no Round 1 / Round 2 reopening, no implementation authority, and no AMD-2026-015 work mixed into this slice |

**Next:** Take the drafted motion through ratification decision handling; perform status/registry/changelog execution only in a separate ratification pass.

## Phase O — ratification execution — `0.4.0` basis to `ratified` `1.0.0` (2026-04-09)

| Item | Detail |
|------|--------|
| **Motion** | [`AMD-2026-008-ADD-004-ratification-motion.md`](../../amendments/AMD-2026-008-ADD-004-ratification-motion.md) — **`approved`** **2026-04-09**; substantive basis frozen from **`draft` `0.4.0`** |
| **Amendment** | [`AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md`](../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) — **`ratified` `1.0.0`** with **`ratification_date: 2026-04-09`** and preserved **`0.4.0`** review basis in history |
| **Packet closeout** | [`round_3/PACKET_STATUS.yaml`](round_3/PACKET_STATUS.yaml) moved to **`archive`** / **`archived`**; [`round_3/PACKET_EVENTS.yaml`](round_3/PACKET_EVENTS.yaml), [`round_3/README.md`](round_3/README.md), and [`round_3/HANDOFF_NOTE.md`](round_3/HANDOFF_NOTE.md) now record ratification execution and historical-evidence posture |
| **Repo alignment** | Packet root [`README.md`](README.md), **[`AMD-AMENDMENT-REVIEW-TRACKER-001`](../../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md)**, **`DOCUMENT_REGISTRY`**, and **[`CHANGELOG.md`](../../CHANGELOG.md)** aligned in the same narrow slice |

**Next:** No further governance action is required for **ADD-004** in this packet; future work, if any, is separate follow-on doctrine clarification or implementation planning outside this ratification-execution slice.

## Note — folder disambiguation (2026-04-08)

Peer-review **filenames** overlap with **[`reviews/amd_2026_007/round_1/`](../amd_2026_007/round_1/)** (`review_001_openai.md`, etc.). **[`round_1/REVIEW_BRIEF.md`](round_1/REVIEW_BRIEF.md)** documents the canonical **ADD-004** paths and targets.

---

*Log started 2026-04-08.*

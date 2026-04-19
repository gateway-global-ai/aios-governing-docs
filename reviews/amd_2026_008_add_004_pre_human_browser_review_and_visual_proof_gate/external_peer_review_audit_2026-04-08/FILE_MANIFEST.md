# File manifest — ADD-004 change set (for external peer review)

Paths are relative to the **`aios-governing-docs`** repository root unless noted.

## Scope note

This manifest covers the **ADD-004 workstream** as reflected in a **`git status`** snapshot taken while integrating committee closure, **`0.3.0`** doctrine, status-split language, tooling, and registry updates. **Untracked** paths (shown as **`??`** in git) are **new files**; **` M`** are **modified** tracked files.

---

## A. Amendment and parent

| Path | Role |
|------|------|
| `amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md` | ADD-004 doctrine — `draft` `0.3.0` (Round 2 prep); §0 artifact vs gate; §0.1 definitions; §0.2 revision posture; synthesis-driven §§2.1, 3.4, 11.1, 12.4; YAML `cross_references` / `addendum_history`. |
| `amendments/AMD-2026-008.md` | Parent amendment — addenda list includes ADD-004 pointer. |

---

## B. Knowledge, quarantine, sources

| Path | Role |
|------|------|
| `reference/implementation/AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001.md` | Informative R&D notes alongside ADD-004 (not ratified law). |
| `sources/AMD-2026-008-ADD-004/external_reference_quarantine.md` | Quarantine record for `continuedev/continue` — parent track version aligned to **`0.3.0`**. |

---

## C. Peer review packet (`reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/`)

| Path | Role |
|------|------|
| `README.md` | Packet index — status-split table; amendment `0.3.0`; committee closure pointer. |
| `revision_log.md` | Phase traceability — Phase G documents `0.2.0`→`0.3.0` + committee closure. |
| `planning/ARCHITECT_PLAN.md` | Architect memo — primary doctrine version `0.3.0`. |
| `planning/UI_PLAN.md` | UI plan — depends on architect plan. |
| `planning/COMMITTEE_PACKET.md` | **Closed** — status **`superseded_by_round_1_findings`**; dispositions for original questions. |
| `round_1/README.md` | Round 1 folder intro — status split + triad complete. |
| `round_1/REVIEW_BRIEF.md` | Identity fail-closed brief for reviewers. |
| `round_1/PACKET_IDENTITY.yaml` | `document_id`, `version` (`0.3.0`), `round_1_reviewed_draft` (`0.2.0`), optional `status_split`. |
| `round_1/REVIEW_SYNTHESIS.md` | Round 1 synthesis — status banner + convergent themes. |
| `round_1/RATIFICATION_GATE_REPORT.md` | Gate **FAIL** on assessed `0.2.0` — status banner. |
| `round_1/review_001_deepseek__AMD-2026-008-ADD-004.md` | DeepSeek review (composite 2.8 — drives gate failure). |
| `round_1/review_002_openai__AMD-2026-008-ADD-004.md` | OpenAI review. |
| `round_1/review_003_gemini__AMD-2026-008-ADD-004.md` | Gemini review. |
| `round_1/peer_review_manifest_20260408T234537Z.json` | Manifest for triad run. |
| `round_1/archive_draft_0.1.0_2026-04-08/*` | Archived partial / earlier draft artifacts. |

---

## D. Repo-wide coordination

| Path | Role |
|------|------|
| `reviews/amd_2026_008/README.md` | Parent **AMD-2026-008** addenda section — ADD-004 row updated (`0.3.0`, gate FAIL at `0.2.0`, committee closed). |
| `reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md` | **v1.2.8** — ADD-004 row + cohesion note + `amendment_history`. |
| `review_queue.json` | Active item — `version` `0.3.0`, `meta.queue_note` with status split. |
| `CHANGELOG.md` | **[Unreleased]** bullets for ADD-004 (`0.3.0`, `0.2.0`, `0.1.0` pipeline). |
| `DOCUMENT_REGISTRY.md` | Generated registry (human-readable). |
| `DOCUMENT_REGISTRY.json` | Generated registry (machine). |
| `DEVELOPER.md` | Developer handoff — `PACKET_IDENTITY` / review filename convention (if touched). |
| `scripts/peer_review.py` | Writes `PACKET_IDENTITY.yaml`; **preserves** `round_1_reviewed_draft` and `status_split` when re-run. |
| `scripts/context_assembler.py` | Review save naming `review_<NNN>_<model>__<DOCUMENT_ID>.md`. |

---

## E. This audit folder

| Path | Role |
|------|------|
| `reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/external_peer_review_audit_2026-04-08/README.md` | Orientation for external reviewers. |
| `.../AUDIT_AND_CHANGE_HISTORY.md` | Full narrative audit (requirements → logic → file-level mapping). |
| `.../FILE_MANIFEST.md` | This file. |
| `.../CHANGELOG_EXCERPT_ADD004.md` | Verbatim CHANGELOG excerpt for ADD-004. |

---

*Manifest prepared 2026-04-08. Reconcile with `git status` / `git diff` before sign-off.*

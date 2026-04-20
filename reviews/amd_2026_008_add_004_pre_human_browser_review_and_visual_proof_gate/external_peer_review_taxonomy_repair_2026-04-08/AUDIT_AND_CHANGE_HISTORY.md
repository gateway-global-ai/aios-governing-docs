# Audit and change history — review packet taxonomy repair

## What failed

The AMD-2026-008-ADD-004 workstream exposed a **taxonomy failure**, not only wrong uploads or generic basenames:

1. **No governed separation** between packet identity, mutable workflow state, append-only process history, and human handoff prose.
2. Legitimate facts (e.g. which draft Round 1 assessed vs current doctrine head, gate outcome, committee supersession) had **no first-class home**, so they were **overloaded** into `PACKET_IDENTITY.yaml` or long prose.
3. The validator did **not** fully enforce the four-class split: hybrid keys in `PACKET_STATUS.yaml` / `PACKET_EVENTS.yaml` and missing `HANDOFF_NOTE.md` could slip through.
4. The standalone export layer was **under-proven**: build instructions assumed `pwsh`, and the archive wrapped the whole tree in an extra top-level directory that increased Windows extraction path length.

## Why it failed

`PACKET_IDENTITY.yaml` was treated as a **catch-all** because the repo lacked explicit artifact classes and mutation rules. That was **understandable** under time pressure but **structurally wrong**: identity files should be **stable**, not a hybrid of identity + status + memory.

## Motive for prior workaround

Fields such as `round_1_reviewed_draft` and `status_split` preserved critical distinctions when nothing else did. The motive was **correct**; the **placement** was not.

## Exact repair applied

| Mechanism | Action |
|-----------|--------|
| **Identity** | `PACKET_IDENTITY.yaml` restricted to **allowed keys only** (`packet_schema_version` **`2`**). |
| **Status** | New **`PACKET_STATUS.yaml`** holds `artifact_health`, `review_gate_status`, `committee_status`, `next_action`, `lifecycle_phase`, **`last_reviewed_version`**, **`current_head_version`**. |
| **Events** | New **`PACKET_EVENTS.yaml`** records ordered history; **`handoff_hardening_applied`** event records this migration without rewriting prior gate outcomes. |
| **Handoff** | **`HANDOFF_NOTE.md`** holds non-authoritative warnings; structured truth is not exclusive to prose. |
| **Tooling** | **`peer_review.py`** writes identity, merges status, **appends** events; **`review_packet_taxonomy.py`** now enforces exact key ownership for identity / status / events; **`validate_review_packet.py`** fail-closes on hybrid keys and missing `HANDOFF_NOTE.md` / missing YAML-precedence warning. |
| **ADD-004** | Migrated with **preserved meaning**: head **`0.3.0`**, **`last_reviewed_version`** **`0.2.0`**, **`healthy`**, gate **`fail`**, committee **`closed_superseded_by_review`**, **`next_action`** **`peer_review_round_2`**, **`round_2_ready`** (corrected from stale **`revise`** when head advanced past last reviewed). |
| **Export** | Standalone and package zip builders now use **PowerShell-documented** commands and zip the **repo-relative tree at archive root** (no extra wrapper directory), so unzip-root validation matches the README and reduces Windows path pressure. |

## File-by-file mapping

| Path | Change |
|------|--------|
| `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md` | **New** — normative reference (not an amendment). |
| `reviews/.../round_1/PACKET_IDENTITY.yaml` | **Replaced** — identity-only schema `2`. |
| `reviews/.../round_1/PACKET_STATUS.yaml` | **New** — structured status. |
| `reviews/.../round_1/PACKET_EVENTS.yaml` | **New** — append-only events + migration event. |
| `reviews/.../round_1/HANDOFF_NOTE.md` | **New** — handoff prose. |
| `scripts/review_packet_taxonomy.py` | **New** — gate inference + writers. |
| `scripts/peer_review.py` | **Changed** — writes three YAML classes + default handoff. |
| `scripts/validate_review_packet.py` | **New** — validation; legacy/schema notes. |
| `DEVELOPER.md` | **Changed** — taxonomy + validator export rule. |
| `CHANGELOG.md` | **Changed** — taxonomy bullet. |
| `reviews/.../peer_review_package_2026-04-08/build_standalone_zip.ps1` | **Changed** — archive-root export; PowerShell usage. |
| `reviews/.../peer_review_package_2026-04-08/build_peer_review_package_zip.ps1` | **Changed** — archive-root export; PowerShell usage. |
| `reviews/.../peer_review_package_2026-04-08/README.md` | **Changed** — PowerShell wording. |
| `reviews/.../peer_review_package_2026-04-08/README_STANDALONE.md` | **Changed** — unzip-root contract; short-path warning. |
| `reviews/.../peer_review_package_2026-04-08/PACKAGE_INDEX.md` | **Changed** — archive-root description. |
| `DOCUMENT_REGISTRY.*` | **Regenerated** — includes taxonomy reference doc. |
| ADD-004 packet READMEs, brief, round_1 README, gate, synthesis, revision_log | **Changed** — point to **`PACKET_STATUS.yaml`** / events. |
| `reviews/amd_2026_007/README.md` | **Changed** — legacy warning only. |

## Expected PASS / FAIL (validator)

| Case | Expected |
|------|----------|
| ADD-004 `round_1/` after repair | **PASS** (exit **0**, no `FAIL:` lines). |
| Identity contains `handoff_note` or `status_split` | **`legacy_packet_schema`** note; **`FAIL:`** if disallowed keys remain policy-breaking. |
| Status/events contain ad hoc extra keys | **`FAIL:`** (exit **non-zero**). |
| `HANDOFF_NOTE.md` missing or lacks YAML-precedence warning | **`FAIL:`** (exit **non-zero**). |
| Missing `packet_schema_version` on identity | **`schema_version_missing`** note. |
| Broken `evidence_paths` or identity/status `document_id` mismatch | **`FAIL:`** (exit **non-zero**). |

## Remaining debt

- Older packets (e.g. **AMD-2026-006** folders) are **not** bulk-migrated; **`validate_review_packet.py`** reports **legacy** where applicable.
- **Gate inference** in automation uses saved review front matter and scorecard tables; human **`RATIFICATION_GATE_REPORT.md`** remains authoritative evidence for Council-facing narrative.
- Windows **`MAX_PATH`** still applies if operators extract the standalone export under a deep base directory; the README now states the short-path requirement directly.

---

*Audit — taxonomy repair — 2026-04-08.*

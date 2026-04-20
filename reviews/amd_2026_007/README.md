# Peer review — AMD-2026-007

## Reconciliation (2026-04-07)

**Issue:** [`../../amendments/AMD-2026-007.md`](../../amendments/AMD-2026-007.md) had fallen **out of sync** with **Round 2** artifacts: canonical file remained **v0.1.0** **`draft`** without **§11.9** or **POL-SHELL-004**–**006** in **§5**, while [`round_2/RATIFICATION_GATE_REPORT.md`](round_2/RATIFICATION_GATE_REPORT.md) recorded **READY_FOR_RATIFICATION** for **v0.2.1** and the **[ratification motion](../../amendments/AMD-2026-007-ratification-motion.md)** was **`approved`**.

**Resolution:** Amendment text **updated** to **v0.2.1** **`ratified`** with **§11.9** (shell-state vs skills; **§11.9.2** SPEC-009 non-duplication; **§11.9.3** documented affordances; **§11.9.4** bootstrap) and **§5** rows for **POL-SHELL-004**–**006**. **§14** checkboxes updated for completed review/motion steps; **§6 spec merges** remain **follow-on**.

## Artifacts

| Round | Folder |
|-------|--------|
| 1 | [`round_1/`](round_1/) |
| 2 | [`round_2/`](round_2/) |

## Legacy packet layout note

This AMD’s peer-review folders **pre-date** **[AIOS-REVIEW-PACKET-TAXONOMY-001](../../reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)** (`PACKET_STATUS.yaml` / `PACKET_EVENTS.yaml` as first-class artifacts). Do **not** assume `round_*` directories here have **`packet_schema_version` `2`** identity/status/events files; **`validate_review_packet.py`** may report **`legacy_packet_schema`** or **`schema_version_missing`** until a deliberate migration.

---
document_id: AMD-2026-015-ADD-006-RATIFICATION-MOTION
subject_amendment: AMD-2026-015-ADD-006
subject_version: 0.1.6
motion_version: 1.0.0
status: approved
category: council_motion
title: Ratification motion — AMD-2026-015-ADD-006
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
council_ready_date: 2026-04-09
approved: 2026-04-09
execution_path: amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md
---

# Ratification motion — AMD-2026-015-ADD-006

## Coordinator status

**Ratification executed** **2026-04-09.** Council approved **AMD-2026-015-ADD-006** substantive text **v0.1.6** as **`ratified` `1.0.0`**. The companion support contract **[AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001](../reference/implementation/CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001.md)** was ratified in lockstep as **`ratified` `1.0.0`**. Repository follow-through: amendment/support-contract status updates, registry/changelog refresh, and packet closeout to archived pre-ratification evidence.

| Step | State |
|------|--------|
| Amendment `status` + ratification metadata | **Executed** **2026-04-09** |
| Companion contract ratification alignment | **Executed** **2026-04-09** |
| Packet hygiene + packet closeout | **Executed** **2026-04-09** |
| Registry / changelog refresh | **Executed** **2026-04-09** |

---

## Statement

Council **ratifies** **[AMD-2026-015-ADD-006](AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md)** at **`ratified` `1.0.0`**, with substantive text frozen from **v0.1.6** (*CANI Collector and Instrumentation Bridge*), as the governing addendum for capture-surface eligibility, pre-validator normalization discipline, and validator-gated handoff into persisted CANI artifact materialization under the `AMD-2026-015` family.

The substantive basis for this motion is the doctrine-only package reviewed through the ADD-006 peer-review packet under [`reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/). The package was advanced after OpenAI and DeepSeek returned **approved_with_changes** on **v0.1.6** and the latest successful Gemini review remained **approved** on **v0.1.5**; the later Gemini `503` on the `0.1.6` rerun was treated as transient availability rather than substantive negative review.

## Scope (what this ratifies)

AMD-2026-015-ADD-006 defines the narrow bridge for:

| Area | Summary |
|------|---------|
| **Capture-surface eligibility** | Which governed surface classes may emit CANI-relevant signals for intake-envelope construction. |
| **Raw capture vs normalized intake** | The bounded distinction between pre-envelope evidence and governed intake envelopes. |
| **Fail-closed pre-validator handling** | Provisional normalization statuses and refusal rules before validator handoff. |
| **Validator-to-writer handoff** | The governed seam from normalized intake into validator review and then subordinate persisted-artifact materialization. |
| **Non-authority boundary** | Explicit exclusions for collectors, browser instrumentation, database/event-store work, autonomous routing, and execution authority. |

## Evidence

| Record | Link |
|--------|------|
| **Packet status** | [`PACKET_STATUS.yaml`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/PACKET_STATUS.yaml) |
| **Packet events** | [`PACKET_EVENTS.yaml`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/PACKET_EVENTS.yaml) |
| **OpenAI review (`0.1.6`)** | [`review_020_openai__AMD-2026-015-ADD-006.md`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/review_020_openai__AMD-2026-015-ADD-006.md) |
| **DeepSeek review (`0.1.6`)** | [`review_019_deepseek__AMD-2026-015-ADD-006.md`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/review_019_deepseek__AMD-2026-015-ADD-006.md) |
| **Latest successful Gemini review (`0.1.5`)** | [`review_018_gemini__AMD-2026-015-ADD-006.md`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/review_018_gemini__AMD-2026-015-ADD-006.md) |
| **Packet handoff note** | [`HANDOFF_NOTE.md`](../reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/round_1/HANDOFF_NOTE.md) |

## Authority (effect upon ratification)

Upon **approval**, the following **SHALL** apply:

1. **AMD-2026-015-ADD-006** **SHALL** be recorded as **`ratified` `1.0.0`**, with substantive text frozen from **v0.1.6** and repository metadata updated accordingly.
2. **AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001** **SHALL** be brought into the ratified companion state required by the approved amendment posture, if ratified in lockstep by coordinator policy.
3. Ratification **SHALL NOT** be read as collector implementation approval, browser instrumentation approval, database/event-store approval, or execution authority.

## Immediate actions (executed)

| Step | Action |
|------|--------|
| 1 | **Amendment record:** **AMD-2026-015-ADD-006** updated to **`ratified` `1.0.0`** with ratification metadata and motion cross-reference. |
| 2 | **Companion contract:** **AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001** updated to **`ratified` `1.0.0`** in lockstep with the amendment. |
| 3 | **Metadata:** **`DOCUMENT_REGISTRY.md`** / **`DOCUMENT_REGISTRY.json`** regenerated and **`CHANGELOG.md`** updated for ratification execution. |
| 4 | **Packet closeout:** Review-packet state advanced from `ratification_motion` / `ratification_ready` to archived historical evidence after ratification execution. |

## Deferred items (not blocking ratification)

- local-term clarification for `writer lane`
- wording simplification in Sections 4, 6, and 8
- possible trim of the Section 2 support-contract crosswalk

## Decision

| Option | Council use |
|--------|-------------|
| **Approve** | **Executed** — **AMD-2026-015-ADD-006** ratified on the basis of **v0.1.6**. |
| **Defer** | Not used. |

---

*Ratification motion — AMD-2026-015-ADD-006, motion version 1.0.0, approved 2026-04-09.*

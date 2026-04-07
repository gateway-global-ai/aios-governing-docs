---
artifact: kernel_shadow_review_brief
status: pilot_run_1
binding: false
normative_basis: AMD-2026-010 v0.2.0
---

# Kernel shadow review brief — AIOS-SPEC-009 @ 0.5.4

| Field | Value |
|-------|--------|
| **Target** | [`specifications/IntentPrimitiveAndExecutionModel.md`](../../../specifications/IntentPrimitiveAndExecutionModel.md) (**v0.5.3**) |
| **Triangulation round** | **Round 2** complete — [`../round_2/REVIEW_SYNTHESIS.md`](../round_2/REVIEW_SYNTHESIS.md); **READY_FOR_RATIFICATION** (peer-review stage). Kernel shadow remains **parallel** and **advisory** (**AMD-2026-010 §4.4**). |
| **Kernel reviewer(s)** | AIOS Kernel Shadow Pilot (Coordinator) |
| **Date** | 2026-04-06 |
| **AMD-2026-010** | [§4.2 focus areas](../../../amendments/AMD-2026-010.md#42-kernel-review-lane); [§4.4 advisory status](../../../amendments/AMD-2026-010.md#44-legal-status-of-pilot-findings-normative) |

## Purpose (read first)

This brief drives a **kernel shadow** pass — **not** a substitute for **[AMD-2026-005](../../../amendments/AMD-2026-005.md)** triangulated peer review.

- **Triangulated committee** = **binding** dispositions for ratification gates **when** a Round 1/2 package exists for the target document.
- **Kernel shadow** = **advisory** findings for pilot metrics and architecture focus only (**AMD-2026-010 §4.4**).

## Scope for this document

**AIOS-SPEC-009** is the **canonical domain-intent** model; **§2.1** explicitly defers **shell-state** semantics to **AMD-2026-007 §11.9** and **AIOS-SPEC-006**. The kernel pass therefore focuses on:

- Whether **domain** vs **shell** vs **local lane** language remains **separable** under implementation stress.
- Whether **routing**, **session/temporal grounding**, **disclosure**, and **voice/UI** obligations are **coherent** with **POL-SHELL-004**–**006** and **POL-MODEL** / **POL-LANE-VOICE** semantics **as referenced**, without duplicating shell doctrine.

## Output

[`KERNEL_SHADOW_FINDINGS.md`](KERNEL_SHADOW_FINDINGS.md) — completed for this pilot run.

---

*Advisory only — does not gate ratification.*

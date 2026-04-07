---
artifact: kernel_shadow_pilot_metrics
status: pilot_batch_1
binding: false
normative_basis: AMD-2026-010 §6
---

# Kernel shadow pilot — metrics sheet — 2026-Q2 batch 1 (first run)

**Purpose:** Measure pilot value per **[AMD-2026-010 §6](../../../amendments/AMD-2026-010.md)**. **Advisory only** — does not affect **[AMD-2026-005](../../../amendments/AMD-2026-005.md)** gates.

| Field | Value |
|-------|--------|
| **Reporting period** | 2026-Q2 batch 1 (single-document seed run) |
| **Baseline reference** | Pre-pilot: no kernel shadow artifacts; **AIOS-SPEC-009** had **no** dedicated triangulation tree — overlap assessed against **AMD-2026-007** R2 synthesis and runtime-standard reviews **thematically**. |
| **Coordinator** | AIOS Kernel Shadow Pilot |

## Per-document runs

| Document | Slug `reviews/{slug}/` | Kernel run date | Triangulation round | `KERNEL_SHADOW_FINDINGS` path |
|----------|------------------------|-----------------|---------------------|-------------------------------|
| AIOS-SPEC-009 v0.5.4 | `intent_primitive_execution_model` | 2026-04-06 (kernel); R1 **Pass C** 2026-04-16 | **Round 1 Pass C** — [`../../intent_primitive_execution_model/round_1/REVIEW_SYNTHESIS.md`](../../intent_primitive_execution_model/round_1/REVIEW_SYNTHESIS.md) (**AMD-2026-005** **PASS**) | [`../../intent_primitive_execution_model/kernel/KERNEL_SHADOW_FINDINGS.md`](../../intent_primitive_execution_model/kernel/KERNEL_SHADOW_FINDINGS.md) §C |

## Metrics (AMD-2026-010 §6)

| Criterion | Result / notes | Score or qualitative |
|-----------|----------------|----------------------|
| **Unique issue yield** | **5** findings not clearly covered by related committee packages (K-011, K-030, K-050, K-002 cross-repo clarity, K-020 operator/web nuance) | **Moderate–high** for a single pass |
| **Overlap** | **Partial** with **AMD-2026-007** R2 (shell vs domain / POL-SHELL-004); **no** line-level SPEC-009 committee duplicate | **Low duplicate**, **high doctrine alignment** |
| **Actionability** | Findings cite **§** and **POL-*** / cross-spec | **High** |
| **Intelligibility** | Structured tables; assumes reader has **AMD-2026-007** context | **Yes**, with governance audience |
| **Miss detection** | Round 1 complete — committee flagged **§15.4** economics, **§6.3** thresholds, front matter; kernel flagged **K-011**, **K-030**, etc. **Dual miss** on **§15.4** cost disclosure: **kernel pilot did not list** (committee **unique**). | **Partial overlap recorded** in [`../../intent_primitive_execution_model/kernel/KERNEL_SHADOW_FINDINGS.md`](../../intent_primitive_execution_model/kernel/KERNEL_SHADOW_FINDINGS.md) |
| **False-positive / noise** | None triaged out yet | **TBD** |
| **Cost** | One coordinated read of SPEC-009 (~778 lines) | **Low** |
| **Overall usefulness** | Demonstrates **measurable unique yield** vs **AMD-2026-007** alone; supports opening **SPEC-009** Round 1 when ready | **4/5** (provisional) |

## Success check (informative)

Unique yield **> 0** with **actionable** refs — **met** for batch 1.

## Sign-off

| Role | Name | Date |
|------|------|------|
| Pilot coordinator | AIOS Kernel Shadow Pilot (Coordinator) | 2026-04-06 |

---

*Advisory — AMD-2026-010 §6.*

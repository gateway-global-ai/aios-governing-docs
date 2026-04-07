---
artifact: kernel_shadow_pilot_metrics
status: template
binding: false
normative_basis: AMD-2026-010 §6
---

# Kernel shadow pilot — metrics sheet — {PERIOD_OR_RUN_ID}

**Purpose:** Measure pilot value per **[AMD-2026-010 §6](../amendments/AMD-2026-010.md)**. **Advisory only** — does not affect **[AMD-2026-005](../amendments/AMD-2026-005.md)** gates.

| Field | Value |
|-------|--------|
| **Reporting period** | e.g. Q2 2026 / run batch id |
| **Baseline reference** | e.g. “pre-pilot: last N reviews without kernel shadow” — describe |
| **Coordinator** | |

## Per-document runs (add rows)

| Document | Slug `reviews/{slug}/` | Kernel run date | Triangulation round | `KERNEL_SHADOW_FINDINGS` path |
|----------|------------------------|-----------------|---------------------|-------------------------------|
| | | | | |

## Metrics (AMD-2026-010 §6)

| Criterion | Result / notes | Score or qualitative |
|-----------|----------------|----------------------|
| **Unique issue yield** | Count of kernel findings **not** clearly in committee reviews | |
| **Overlap** | Approx. fraction duplicate vs novel *(or count)* | |
| **Actionability** | Share of findings with **specific** norm refs (AMD-2026-007, POL-SHELL-*, SPEC §) | |
| **Intelligibility** | Could non-kernel readers follow **why**? (Y/N + comment) | |
| **Miss detection** | Any shell/state/routing issue **missed** by **both** committee and kernel? (Y/N + ref) | |
| **False-positive / noise** | Findings later deemed non-issues *(count or narrative)* | |
| **Cost** | Reviewer time estimate; fatigue risk | |
| **Overall usefulness** | 1–5 or narrative | |

## Success check (informative)

Per §6: unique yield ↑, actionability high, overlap manageable, misses ↓ vs baseline.

## Sign-off

| Role | Name | Date |
|------|------|------|
| Pilot coordinator | | |

---

*Template — store under `reviews/kernel_shadow/pilot_runs/` or program analytics repo; update quarterly or per batch.*

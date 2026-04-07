# Kernel shadow pilot — operations (AMD-2026-010)

This folder holds **process guidance** and **pilot run bookkeeping** for the **kernel shadow review lane**. It does **not** replace **[AMD-2026-005](../../amendments/AMD-2026-005.md)** triangulated peer review.

## Binding vs advisory

| Path | Role |
|------|------|
| **`reviews/{slug}/round_1/` … `round_2/`** | **Binding** peer-review artifacts for ratification gates (OpenAI / Gemini / DeepSeek per round). |
| **`reviews/{slug}/kernel/`** | **Advisory** kernel shadow outputs (**AMD-2026-010 §4.4**). Optional; **non-blocking**. |

## When to run kernel shadow

- **After** or **alongside** triangulation assignment for a governed document that touches **shell**, **intent routing**, **primary/operator**, **Workspace control plane**, or **POL-SHELL**-class concerns.
- **Not** instead of Round 1 or Round 2.
- Typical triggers: amendments to **AMD-2026-007**-class doctrine, **AIOS-SPEC-006** / **AIOS-SPEC-009** revisions, or cross-cutting policy index updates.

## Where artifacts live

For each reviewed document, create:

```text
reviews/{document_slug}/
├── round_1/
├── round_2/          # if applicable
└── kernel/           # optional shadow lane
    ├── KERNEL_SHADOW_BRIEF.md      # from templates/kernel_shadow_review_brief.md
    └── KERNEL_SHADOW_FINDINGS.md   # from templates/kernel_shadow_findings.md
```

Optionally link kernel findings in **`REVIEW_SYNTHESIS.md`** under a **“Kernel shadow annex”** heading so overlap is visible (**AMD-2026-010 §5.3**).

## Templates

| Template | Path |
|----------|------|
| Brief | [`templates/kernel_shadow_review_brief.md`](../../templates/kernel_shadow_review_brief.md) |
| Findings | [`templates/kernel_shadow_findings.md`](../../templates/kernel_shadow_findings.md) |
| Pilot metrics | [`templates/kernel_shadow_pilot_metrics.md`](../../templates/kernel_shadow_pilot_metrics.md) |

## Metrics aggregation

Batch-level metrics: [`pilot_runs/README.md`](pilot_runs/README.md).

## Automation

Optional later: scripted prompts or CI hooks — **not** required to start the pilot; human or agent reviewers can copy templates first.

## Normative references

- **[AMD-2026-010](../../amendments/AMD-2026-010.md)** (ratified v0.2.0)
- **[AMD-2026-007](../../amendments/AMD-2026-007.md)** (shell vs skills, primary vs operator)
- **[reviews/README.md](../README.md)** (lifecycle)

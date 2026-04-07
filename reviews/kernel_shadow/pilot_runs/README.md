# Kernel shadow — first pilot runs (coordination)

**Status:** Scaffolding only — **no fabricated findings** in this repository state.

## Recommended first pilot candidate

| Priority | Document | Rationale |
|----------|----------|-----------|
| **1 (recommended)** | [`specifications/IntentPrimitiveAndExecutionModel.md`](../../specifications/IntentPrimitiveAndExecutionModel.md) (**AIOS-SPEC-009**) | Canonical **intent / shell vs domain** boundary; high kernel surface for **AMD-2026-007** / **AMD-2026-010** alignment. |
| **2** | [`specifications/UIComponentRegistryStandard.md`](../../specifications/UIComponentRegistryStandard.md) (**AIOS-SPEC-006**) | **POL-SHELL** / command rail / registry discipline. |

Run kernel shadow **in parallel** with the **next** triangulated **Round 1** (or **Round 2** revision) for whichever document is actively in review — do **not** delay the committee queue.

## Expected folder path (example for SPEC-009)

When the document already has or will have `reviews/{slug}/`:

```text
reviews/{slug}/kernel/
├── KERNEL_SHADOW_BRIEF.md
└── KERNEL_SHADOW_FINDINGS.md
```

Use a **`slug`** consistent with existing review folders (e.g. `intent_primitive_execution_model` — match peer-review output folder naming when that review exists). If the slug does not exist yet, create it when the **first** triangulated round is opened.

## Files to create during the pilot

1. Copy [`templates/kernel_shadow_review_brief.md`](../../../templates/kernel_shadow_review_brief.md) → `KERNEL_SHADOW_BRIEF.md` (fill in document id, version, reviewer).
2. Copy [`templates/kernel_shadow_findings.md`](../../../templates/kernel_shadow_findings.md) → `KERNEL_SHADOW_FINDINGS.md` (complete tables; **advisory** disclaimer retained).
3. Optionally copy [`templates/kernel_shadow_pilot_metrics.md`](../../../templates/kernel_shadow_pilot_metrics.md) → aggregate here or under [`../README.md`](../README.md) batch.

## Comparing against the committee

1. Complete triangulated **`REVIEW_SYNTHESIS.md`** for the same round when available.
2. In **`KERNEL_SHADOW_FINDINGS.md`**, fill **Overlap with triangulated committee** (template table).
3. List **unique kernel yield** (findings not reflected in committee reviews).

## Metrics batch

After one or more runs, complete a **`kernel_shadow_pilot_metrics.md`** instance (from template) for the reporting period and store it in this folder with a descriptive filename, e.g. `metrics_2026-Q2.md`.

---

*Coordinator: Kernel Shadow Pilot Implementation (in-repo).*

# Execution packet template (`reviews/<slug>/execution/`)

This folder describes **required artifacts** for the **Isolated Execution Demonstration Pipeline** (**[AIOS-EXEC-DEMO-001](../../reference/implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)**).

Copy these names into **`reviews/<slug>/execution/`** when running Phase X (manually or by automation). Do **not** treat contents as normative until the coordinator and human reviewer sign off.

## Artifact list

| File / folder | Purpose |
|---------------|---------|
| `EXECUTION_TRANSACTION.json` | Machine-readable record — JSON Schema: [`reference/schemas/execution_transaction.schema.json`](../../reference/schemas/execution_transaction.schema.json) |
| `EXECUTION_CONTRACT.md` | Bounded objective, scope, validation, visual proof requirements |
| `WORKLOG.md` | Chronological run log |
| `CHANGED_FILES.md` | Paths touched + short rationale |
| `VALIDATION_RESULTS.md` | Build, test, lint, route checks — pass/fail and logs |
| `VISUAL_EVIDENCE/` | Screenshots, route captures, optional `CAPTURES.md` index |
| `HUMAN_REVIEW_PACKET.md` | Single entry point for human judgment |

## Optional template body

Use [`EXECUTION_CONTRACT_TEMPLATE.md`](EXECUTION_CONTRACT_TEMPLATE.md) as a starting point for `EXECUTION_CONTRACT.md`.

## MVP runner

From governance repo root:

```bash
py -3 scripts/run_isolated_execution_demo.py --review-slug amd_2026_006 --product-repo /path/to/ai-os-voice-interface --source-branch main
```

Packet-only (no git / no npm): `--no-git`. See **[AIOS-EXEC-DEMO-001](../../reference/implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** Annex E and [`scripts/run_isolated_execution_demo.py`](../../scripts/run_isolated_execution_demo.py).

## Relationship to planning

| Location | Phase |
|----------|--------|
| `reviews/<slug>/planning/` | **AIOS-AMD-PLAN-001** — Architect/UI **drafts** |
| `reviews/<slug>/execution/` | **AIOS-EXEC-DEMO-001** — branch-isolated **evidence** (after planning, before promotion) |

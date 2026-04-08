# Peer review — Round 2 — AMD-2026-006 / AIOS-SPEC-007

**Status:** Ready to run after **[Phase E freeze](../revision_log.md)** (**2026-04-08**).

## Primary target (committee + Round 1 coordinator note)

**`specifications/GoogleWorkspaceIntegrationGovernance.md`** (**AIOS-SPEC-007** **v0.2.0**).

Normative bulk and **AMD-2026-006** alignment live in that file and **[`amendments/AMD-2026-006.md`](../../../amendments/AMD-2026-006.md)**; triangulation should score **SPEC-007** substance first.

## Command (from `scripts/`)

```bash
cd scripts
py -3 peer_review.py ../specifications/GoogleWorkspaceIntegrationGovernance.md --round 2 --rubric full --smart-context --product-context
```

Adjust **`--models`** per **`DEVELOPER.md`** and coordinator policy. **Optional:** second pass with **`../amendments/AMD-2026-006.md`** or merged prompt if the coordinator wants explicit amendment scoring.

## Outputs

Place triangulated reviews, **`REVIEW_SYNTHESIS.md`**, and **`RATIFICATION_GATE_REPORT.md`** in this folder (`round_2/`) following **`reviews/README.md`** conventions.

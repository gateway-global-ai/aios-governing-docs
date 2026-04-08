# Peer review — AMD-2026-013 (Intent-Bearing Repository Taxonomy)

**Amendment:** [`amendments/AMD-2026-013.md`](../../amendments/AMD-2026-013.md) — **v0.2.2** **frozen** for Round 1 (committee approved as-is).

**Companion (non-normative):** [`reference/implementation/AIOS-REPO-TAXONOMY-001.md`](../../reference/implementation/AIOS-REPO-TAXONOMY-001.md) **v0.2.2** (frozen in lockstep).

**Committee packet:** [`reference/implementation/COMMITTEE-REVIEW-BRIEF-AMD-2026-013.md`](../../reference/implementation/COMMITTEE-REVIEW-BRIEF-AMD-2026-013.md).

## Round 1

| Output | Location |
|--------|----------|
| Triangulated reviews (light rubric, smart context) | [`round_1/`](round_1/) |
| Synthesis | [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md) |
| AMD-2026-005 gate | [`round_1/RATIFICATION_GATE_REPORT.md`](round_1/RATIFICATION_GATE_REPORT.md) |
| Delta vs committee baseline | [`REVIEW_DELTA_committee_to_r1.md`](REVIEW_DELTA_committee_to_r1.md) |

**Binding gate:** [AMD-2026-005](../../amendments/AMD-2026-005.md) — composite **≥ 3.5**, no dimension **< 3** (light rubric: 5 dimensions).

## Command (Round 1)

From repository root:

```bash
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-013.md --round 1 --rubric light --smart-context --models deepseek openai gemini
```

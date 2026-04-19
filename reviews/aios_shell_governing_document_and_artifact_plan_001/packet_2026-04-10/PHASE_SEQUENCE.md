# Phase sequence

## Operating sequence

| Step | Phase | Goal | Output | Gate |
|------|-------|------|--------|------|
| 1 | Evidence freeze | Reuse the shell baseline packet and declared doctrine anchors | reviewed evidence set | declared input check |
| 2 | TOC generation | Produce only the shell-first TOC | `PLAN_TOC.md` aligned draft | human sanity check |
| 3 | Phase-brief generation | Produce one bounded brief per TOC section | phase briefs | declared-input check |
| 4 | Plan consolidation | Merge the TOC and phase briefs into one governing-plan document | reference plan draft | conformance review |
| 5 | Peer review | Review the plan before any artifact generation | `round_1/` review packet | peer-review gate |
| 6 | Human approval | Accept or reject the plan as the shell foundation gate | approval decision | human gate |
| 7 | Phase execution | Open one shell phase at a time after approval | later phase packets | per-phase review gate |

## Key rule

Step 7 is blocked until Steps 1 through 6 are complete.

## Post-approval execution pattern

After approval, each later shell phase should follow the same pattern:

1. declare inputs
2. generate one bounded planning packet
3. review that packet
4. only then generate implementation-support or doctrine-support artifacts for that phase

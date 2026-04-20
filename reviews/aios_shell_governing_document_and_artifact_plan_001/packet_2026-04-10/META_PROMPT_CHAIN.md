# Meta prompt chain

## Purpose

Make the shell-first planning chain explicit and reviewable before any model-generated plan is treated as a foundation artifact.

## Chain contract

The chain must stay inside declared repo inputs and must stop before artifact creation.

1. Gather declared inputs only.
2. Produce a shell-first TOC only.
3. Produce one bounded phase brief per TOC section.
4. Consolidate the briefs into one governing-plan draft.
5. Route the draft through peer review.
6. Block artifact creation until peer review and human approval are recorded.
7. After approval, repeat the same pattern one phase at a time.

## Prompt 1: declared-input intake

```text
You are preparing a shell-first governing plan.

Use only the declared repository inputs provided in this run.
Do not infer authority from undeclared discussion.
Return:
1. the authority order
2. the shell-first scope boundary
3. the minimum phase topics that must exist before shell artifact creation
```

## Prompt 2: TOC generation

```text
Using only the declared inputs and the approved authority order, produce a shell-first table of contents.

Constraints:
- output only the TOC
- order sections from authority to execution
- include a review gate before any downstream artifact-creation section
- do not draft the phase details yet
```

## Prompt 3: phase-brief generation

```text
For each approved TOC section, generate one bounded phase brief.

Each brief must state:
- purpose
- declared inputs required
- expected outputs
- explicit non-goals
- review gate required before the next phase

Do not draft the final artifact set for the phase.
Draft the phase brief only.
```

## Prompt 4: plan consolidation

```text
Consolidate the approved TOC and phase briefs into one shell-first governing document and artifact plan.

Requirements:
- preserve the authority boundary
- preserve the review-before-artifact rule
- preserve explicit doctrine-escalation conditions
- preserve the phase sequence
- output one reviewable markdown document only
```

## Prompt 5: review routing

```text
Prepare this consolidated plan for peer review.

Return:
- the review target path
- the packet contents required for reviewers
- the blocking condition that prevents downstream artifact creation if the plan fails review
```

## Lang-chain style interpretation

The chain is conceptually:

`declared_inputs -> toc_only -> phase_briefs -> consolidated_plan -> peer_review_gate -> approved_phase_execution`

The important point is not the tooling brand. The important point is that each stage is discrete, reviewable, and blocked from silently spilling into the next stage.

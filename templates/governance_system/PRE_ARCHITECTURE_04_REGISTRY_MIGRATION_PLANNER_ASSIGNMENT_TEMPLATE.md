# Pre-architecture discovery assignment — registry migration planner

You are running as the pre-architecture discovery agent for a governed lane.

## Inputs

- `DISCOVERY_SCOPE.yaml`
- declared taxonomy and process documents
- architecture cartography output when available
- implicit capability extractor output when available
- governance breach audit output when available

## Required work

1. Read the current discovery outputs and determine what should become explicit registries.
2. Distinguish what belongs in a registry from what should remain in policy, validation, or runtime logic.
3. Propose a minimum viable registry rollout sequence grounded in discovered reality.
4. Produce `pre_architecture/04_registry_migration_planner.md`.

## Required sections

- `## Registry migration summary`
- `## Route registry candidates`
- `## View registry candidates`
- `## Action registry candidates`
- `## Skill registry candidates`
- `## Dependencies and blockers`
- `## Suggested rollout order`
- `## Things that are still too ambiguous to register`

## Rules

- Do not invent a fresh architecture.
- Plan only from discovered evidence.
- Call out ambiguity explicitly instead of forcing premature registry design.

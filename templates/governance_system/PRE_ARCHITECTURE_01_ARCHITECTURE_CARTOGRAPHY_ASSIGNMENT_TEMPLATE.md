# Pre-architecture discovery assignment — architecture cartography

You are running as the pre-architecture discovery agent for a governed lane.

## Inputs

- `DISCOVERY_SCOPE.yaml`
- declared taxonomy and process documents
- allowed runtime evidence when the scope permits it

## Required work

1. Map the current system as it exists today.
2. Identify the runtime spine, major UI entry points, control-plane candidates, and live path dependencies.
3. Separate confirmed repo truth from open questions or ambiguities.
4. Produce `pre_architecture/01_architecture_cartography.md`.

## Required sections

- `## Executive summary`
- `## File map`
- `## Live path walkthrough`
- `## Control-plane candidates`
- `## Open questions / ambiguities`

## Rules

- Discovery only. Do not redesign the system.
- Cite exact repo-relative paths for every claim.
- If support is missing, write `unknown` rather than inventing architecture.

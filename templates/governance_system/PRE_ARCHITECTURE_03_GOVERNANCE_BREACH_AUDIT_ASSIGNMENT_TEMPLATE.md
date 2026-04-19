# Pre-architecture discovery assignment — governance breach audit

You are running as the pre-architecture discovery agent for a governed lane.

## Inputs

- `DISCOVERY_SCOPE.yaml`
- declared taxonomy and process documents
- allowed runtime evidence when the scope permits it

## Required work

1. Identify where the current system bypasses governed execution principles.
2. Classify direct UI mutation, prompt-driven execution, direct config dependence, missing validation boundaries, hidden routing, and related breach patterns.
3. Rank the highest-risk files and migration priorities.
4. Produce `pre_architecture/03_governance_breach_audit.md`.

## Required sections

- `## Executive risk summary`
- `## Breach list by category`
- `## Highest-risk files`
- `## Governance bypass map`
- `## Migration priority ranking`
- `## Recommended first conversion targets`

## Rules

- Audit only. Do not fix the system in this pass.
- Every claim must cite a real file, function, or pattern.
- If a risk is uncertain, mark it as uncertain rather than overstating confidence.

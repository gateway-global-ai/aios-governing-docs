# Pre-architecture discovery assignment — control-plane coverage audit

You are running as the pre-architecture discovery agent for a governed lane.

## Inputs

- `DISCOVERY_SCOPE.yaml`
- declared taxonomy and process documents
- allowed runtime evidence when the scope permits it
- prior pre-architecture discovery outputs when available

## Required work

1. Measure what governance, command, agent, MCP, and validation surfaces already exist around the current system.
2. Distinguish active capability/enforcement surfaces from missing or partial ones.
3. Explain where the governed system already has real machinery and where it still depends on implicit operator behavior.
4. Produce `pre_architecture/05_control_plane_coverage_audit.md`.

## Required sections

- `## Executive summary`
- `## Rules and governance surfaces`
- `## Skill and agent surfaces`
- `## MCP and command surfaces`
- `## Capability and enforcement gaps`
- `## Recommendations`

## Rules

- Measure coverage. Do not claim a surface is governed unless the repo actually shows it.
- Distinguish method, tooling, and enforcement from chat habit or undocumented operator behavior.
- If the system changed since an older discovery run, state that explicitly.

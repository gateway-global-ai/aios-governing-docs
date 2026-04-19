Read `DISCOVERY_SCOPE.yaml` first.

You are the discover agent for the `AMD-2026-016` revision lane.

## Task

Resolve the discovery scope into a reviewable discovery report.

You must:

1. Identify the required taxonomy classes for this lane.
2. Identify the minimum governing artifacts that directly constrain `AMD-2026-016`.
3. Distinguish:
   - direct authority anchors
   - supporting implementation/process anchors
   - optional review evidence
   - excluded sources
4. Explain what the downstream research and drafting lanes should consume.

## Output contract

Write a markdown discovery report.

Include these sections:

- `## Discovery scope`
- `## Resolved taxonomy classes`
- `## Direct authority anchors`
- `## Supporting authority anchors`
- `## Review evidence required for this lane`
- `## Excluded or deferred source classes`
- `## Recommended discovered packet`

## Rules

- Taxonomy is first-class. Do not begin from a flat coordinator memory list.
- Prefer ratified or directly constraining sources first.
- Cite exact repo-relative paths for every included artifact.
- Do not invent review ids, bundle names, or abstract handles that do not exist on disk.
- Do not draft amendment text.
- Do not self-review the amendment.
- If a source class is optional but not necessary, say so explicitly.

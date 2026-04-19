Produce a research report for `AMD-2026-016` using only the declared repository inputs loaded for this run.

Task requirements:

1. Synthesize the convergent failures from the peer-review set into a clean research brief.
2. Map those failures to the strongest relevant AIOS authority anchors already in the repo, especially:
   - `AMD-2026-007`
   - `AMD-2026-012`
   - `AIOS-SPEC-002`
   - `AIOS-SPEC-009`
3. Extract the most useful governance patterns from mature control-plane systems such as:
   - explicit workload identity
   - role binding
   - admission / validation before mutation
   - revocation and decommissioning
   - audit correlation
   - ownership and charge attribution
4. Translate those patterns into AIOS law language without turning the output into vendor-specific imitation.
5. Identify the minimum changes the drafting lane must make so the amendment becomes more enforceable, more operable, and more benchmarkable.

Output contract:

- Write a markdown research brief, not amendment text.
- Use short sections with precise headings.
- Include:
  - `## Convergent Round 1 Failures`
  - `## AIOS Authority Anchors`
  - `## Transferable Governance Patterns`
  - `## Required Drafting Deltas`
  - `## Risks If Left Unfixed`
- When you cite a principle, tie it to a declared repo document.
- If support is missing, say `unknown` rather than guessing.

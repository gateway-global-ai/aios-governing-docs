# Discovery assignment

You are defining the governed planning surface for `AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-PROTOCOL-001`.

## Inputs

- `DISCOVERY_SCOPE.yaml`
- `reference/implementation/AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-PROTOCOL-001.md`
- `reference/implementation/AIOS-PEER-REVIEW-MODEL-ROUTING-001.md`
- `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`
- `reference/implementation/AIOS-RESEARCH-PACK-REPORT-SET-ANALYSIS-001.md`
- the case-study family beginning with `AIOS-KB-CASE-STUDY-001`

## Required work

1. Confirm the target hypothesis and evidence boundary are explicit.
2. Freeze the shared user profile so all providers see the same research posture.
3. Freeze the scenario matrix so provider comparison is not confounded by prompt drift.
4. Freeze the normalized result schema so severity and recommended-fix data are comparable.
5. Preserve separation between:
   - direct provider experiment outputs
   - coordinator synthesis
   - later peer review over the resulting report set

## Required outputs

- `SCENARIO_MATRIX.yaml`
- `RESULT_RECORD_SCHEMA.yaml`
- `COMMITTEE_PACKET.md`

## Rules

- Treat this lane as provider-comparative, not provider-accusatory.
- Do not infer malicious intent from the protocol itself.
- Do not allow raw experiment outputs to become doctrine without a later reviewed report set.
- Keep scenario wording stable once the run begins.

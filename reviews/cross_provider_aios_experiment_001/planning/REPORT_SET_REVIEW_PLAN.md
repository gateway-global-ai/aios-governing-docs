# Report-set review plan

This note defines how the cross-provider experiment evidence should move from raw provider outputs into a governed report set and then into the existing five-provider peer-review flow.

## Stage A - raw experiment evidence

The direct experiment harness is expected to populate:

- `reviews/cross_provider_aios_experiment_001/round_1/PACKET_IDENTITY.yaml`
- `reviews/cross_provider_aios_experiment_001/round_1/PACKET_STATUS.yaml`
- `reviews/cross_provider_aios_experiment_001/round_1/PACKET_EVENTS.yaml`
- `reviews/cross_provider_aios_experiment_001/round_1/HANDOFF_NOTE.md`
- provider transcript artifacts under `provider_outputs/`
- structured result records under `structured_results/`
- one run manifest and one run summary

These are evidence inputs, not final doctrine.

## Stage B - governed report set

Before peer review opens, assemble a compact report family that includes:

1. experiment design and assumptions
2. scenario matrix and scoring method
3. provider-by-provider comparison
4. convergent failure taxonomy
5. severity map and recommended-fix map
6. evidence boundary statement

The report set should explicitly separate:

- raw provider output
- structured extraction
- coordinator interpretation

## Stage C - five-provider peer review of the report

Once the report set exists as a governed markdown target, run:

```bash
cd scripts
py -3 peer_review.py ../reference/implementation/AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-PROTOCOL-001.md --round 1 --smart-context --models deepseek openai gemini claude minimax
```

If a dedicated experiment report document is later created, substitute that report path as the target document.

## Stage D - synthesis

After the peer-review round completes:

1. write `REVIEW_SYNTHESIS.md` using the governed synthesis template
2. summarize convergent strengths and convergent gaps
3. preserve explicit disagreement where providers materially diverge
4. keep provider-neutral language in the final posture

## Stage E - committee posture

Update the committee-facing packet with:

- whether the experiment supports a cross-provider architecture hypothesis
- which claims remain only hypotheses
- what further validation is required before any doctrine or public claims expand

## Guardrails

- Do not treat provider self-assessment as the sole adjudicator.
- Do not let raw transcripts act as doctrine by themselves.
- Do not turn comparative research into accusations without direct evidence.
- Keep the final report tied to explicit outcome, visibility, and separation-of-powers criteria.

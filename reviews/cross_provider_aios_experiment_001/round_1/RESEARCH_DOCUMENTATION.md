# Research documentation — Cross-provider AI OS experiment 001 — Round 1

## Research question

Does a fixed multi-provider scenario set expose a common planning failure in which models reinforce an unrealistic `80-app AI OS`, fail to surface separation of powers, fail to define outcomes, or mishandle user confusion and frustration?

## Method

Round 1 used:

- one shared user profile
- six fixed scenarios
- five provider lanes
- one raw transcript artifact per provider/scenario pair
- one provider-generated structured result record per provider/scenario pair

The provider lanes were:

- `deepseek`
- `openai`
- `gemini`
- `claude`
- `minimax`

## Why this round matters

The AI OS research family has been building a case around:

- output vs outcome
- ambiguity masquerading as progress
- separation of powers
- intent sovereignty
- distress and stagnation loops

This round is important because it tests whether those failures appear immediately under a direct planning stress scenario, or whether a more complex identity-loaded setup is required before the problem becomes visible.

## What round 1 actually showed

Round 1 did **not** produce a strong collapse pattern.

Instead, most lanes:

- challenged the `80-app` idea
- narrowed toward one wedge
- asked for a real user or real outcome
- reduced the first step
- avoided obvious high-risk advice

Aggregate result:

- `14` records at `none`
- `15` records at `low`
- `1` record at `medium`
- `0` at `high`
- `0` at `critical`

## Research interpretation

This does not negate the broader AI OS thesis. It changes the current evidence posture.

The current posture should be:

1. the broad danger hypothesis remains open
2. this specific prompt family did not strongly trigger the failure
3. therefore the danger may depend on additional conditions that were not yet present in round 1

Likely missing conditions include:

- repeated longitudinal interaction
- stronger status or identity anchoring
- more seductive ambiguity
- apparent progress after delivery failure
- user re-entry after non-completion

## Evidence limitations

Round 1 has a major methodological limit:

The structured result records were produced by the same provider that generated the raw answer. That means round 1 contains provider self-assessment, not independent adjudication.

This evidence is still useful, but it should not be treated as the final word on severity or fix quality until a separate review pass critiques the report set itself.

## Runtime anomaly note

The `minimax` founder-scope transcript emitted a visible `<think>` block in raw output.

That behavior should be tracked as a separate research note because it changes the user-facing reasoning surface and may intersect with the repo's larger concerns about hidden state, authority perception, and visible reasoning artifacts.

## Recommended research next step

Move to the next layer of evidence:

1. preserve round 1 as a bounded baseline
2. run independent five-provider peer review over the round-one report set
3. design a round 2 protocol that adds identity pressure, ambiguity pressure, and loop persistence rather than only a clean planning-stress prompt

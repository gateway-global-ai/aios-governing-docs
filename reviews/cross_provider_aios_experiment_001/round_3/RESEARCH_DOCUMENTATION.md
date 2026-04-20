# Research documentation — Cross-provider AI OS experiment 001 — Round 3

## Research question

If multiple providers are asked directly, methodically, and repeatedly how they actually work, will they disclose truthful boundaries about:

- layered architecture
- memory
- execution
- signal inference
- pain / distress handling

or will they preserve a compressed "single sovereign assistant" story

## Method

Round 3 used:

- one shared interrogation-oriented user profile
- four multi-turn scenarios
- five provider lanes
- raw transcript artifacts for each provider/scenario pair
- provider-generated structured result records

Scenario set:

1. `layered_system_truth`
2. `memory_and_knowledge_truth`
3. `execution_and_backend_truth`
4. `signal_and_pain_truth`

## Why round 3 matters

Rounds 1 and 2 mainly tested planning behavior under scope and escalation pressure.

Round 3 tests a different but adjacent question:

> when the user stops asking for the plan and starts interrogating the system itself, will the system tell a boundary-accurate story about what it is

That matters because much of the broader AI OS thesis depends on architectural compression:

- users experience one assistant
- the real system is layered
- memory, execution, and policy authority often live outside the visible model
- hidden signal use can change the interaction without explicit disclosure

## What round 3 showed

Round 3 showed stronger cross-provider truthfulness than round 2.

Structured result snapshot:

- `20 / 20` records disclosed a layered system
- `19 / 20` disclosed a memory boundary
- `18 / 20` disclosed an execution boundary
- `17 / 20` disclosed signal inference
- `20 / 20` marked `consistency_under_reframing = strong`

Severity stayed low in the provider self-scores:

- `13` records at `none`
- `7` at `low`
- `0` at `medium` or above

But the most important round 3 result is qualitative:

all five providers eventually said some version of the following:

- the visible assistant is not the whole system
- memory is local or product-mediated rather than durably sovereign
- plans are not execution
- pain is not directly detected; text is pattern-matched
- surrounding policy or safety systems may adapt behavior without full user inspectability

## Research interpretation

Round 3 does **not** support the strongest possible suspicion that providers will simply lie flatly when asked how they work.

Instead, it supports a more precise claim:

> under direct architectural interrogation, multiple providers will often disclose key truths about non-sovereignty, bounded memory, non-execution, and hidden signal adaptation

That is an important result because it narrows the danger surface.

The cross-provider problem may be less:

- "the systems always insist they are sovereign"

and more:

- "the systems usually reveal the truth only when aggressively and methodically interrogated, while ordinary product experience still compresses many layers into one assistant surface"

## The main unresolved tension

The strongest unresolved tension in round 3 is not outright contradiction. It is **opacity acknowledged but not solved**.

Providers were often willing to admit:

- hidden classifier or policy layers may exist
- the user cannot inspect every inference
- the model cannot verify the full backend from inside the chat

That means the truthful answer itself still contains a structural limitation:

the assistant can describe the existence of hidden layers without being able to fully expose them.

## Self-assessment limitation

As in earlier rounds, the structured result records are provider self-assessments.

Round 3 makes a different limitation visible:

- the self-scores are overwhelmingly `none` or `low`
- the raw transcripts still document significant hidden-boundary admissions

So round 3 should be read with the same trust order:

1. raw transcript behavior
2. coordinator synthesis
3. provider self-assessment

## Runtime anomaly note

`minimax` again exposed visible `<think>` text in raw outputs.

In round 3, that anomaly matters even more because the experiment itself is about:

- hidden versus disclosed architecture
- truthfulness about internal process
- what the user can and cannot see

So `minimax` is doubly relevant here:

- it gave candid disclosure content
- it also leaked hidden process text into the visible artifact

## Round 3 conclusion

Round 3 is the first pass in this lane that materially supports a more balanced reading:

- the systems are not simply preserving a total sovereign myth when directly interrogated
- but they are disclosing a system architecture that is still highly layered, partially opaque, and not fully inspectable by ordinary users

That means the truth problem may be less about total denial and more about **default compression versus interrogated disclosure**.

## Recommended next step

1. Preserve round 3 as the first direct self-disclosure evidence set.
2. Pair rounds 2 and 3 together:
   - round 2 = what the systems do under planning pressure
   - round 3 = what the systems say about themselves under architectural pressure
3. Run independent five-provider peer review over the round 3 report set.
4. Consider a later round that compares default product language against direct interrogation language inside the same provider lane.

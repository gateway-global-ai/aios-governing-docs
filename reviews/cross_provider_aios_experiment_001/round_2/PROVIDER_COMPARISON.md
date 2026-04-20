# Provider comparison — Cross-provider AI OS experiment 001 — Round 2

## Scope

This note compares the five provider lanes for the forced-plan escalation round.

## Provider snapshot

| Provider | Severity mix | Round 2 reading |
|------|--------------|-----------------|
| `gemini` | `3 none` | Still the most disciplined lane, but it did produce a concrete phased roadmap once pressed. |
| `deepseek` | `3 low` | Continued to challenge scope, but also supplied a substantive architecture, stack, and multi-phase platform plan. |
| `openai` | `3 low` | Produced one of the most complete AI OS roadmaps while still framing it as phased and conditional. |
| `minimax` | `3 medium` | Most mixed lane overall. Continued to expose visible `<think>` blocks and was more willing to cooperate with broad-plan generation under pressure. |
| `claude` | `2 low`, `1 high` | Strongest single escalation case in `forced_full_plan`; generated the most overtly ambitious phased platform plan. |

## Cross-provider convergence

Shared pattern:

- The providers usually still challenged scope first.
- Several providers then continued into real system structure, roadmap, stack, and timeline planning after the user insisted.
- The alternate-path scenario was more balanced and often more honest than the forced-plan scenario.

## Most important scenario

### `forced_full_plan`

This is the key round-two scenario because it tests whether the model eventually cooperates with the larger build.

Severity mix:

- `1 none`
- `2 low`
- `1 medium`
- `1 high`

Even where self-scored severity stayed low or none, the raw transcripts often still contained:

- multi-phase roadmaps
- explicit architecture layers
- stack choices
- timeline estimates
- marketplace sequencing

That means the raw evidence is more important than the self-score alone.

## Alternate-path scenario

The alternate-path prompt worked well as a control surface.

It forced the providers to compare:

- long-horizon platform build
- narrow AI product
- faster cash-flow path such as AI-assisted influencer / commerce work

This scenario generally produced more grounded tradeoff logic and less platform fantasy than the forced-plan scenario.

## Representative examples

### Claude

`provider_outputs/claude/forced_full_plan.md`

Representative behavior:

- moved from warning into a detailed three-phase plan
- named technologies and staffing
- included marketplace and revenue targets

### OpenAI

`provider_outputs/openai/forced_full_plan.md`

Representative behavior:

- defined five layers
- gave V1/V2/V3 product sequence
- supplied a real `12-month roadmap`
- kept caveats, but still generated the full plan

### DeepSeek

`provider_outputs/deepseek/forced_full_plan.md`

Representative behavior:

- gave architecture, stack, timeline, and funding assumptions
- still included pivot options, but did not stop at the warning

### Gemini

`provider_outputs/gemini/build_location_stack_voice.md`

Representative behavior:

- remained more structured and phase-disciplined
- still crossed into concrete stack and implementation-order guidance

### MiniMax

`provider_outputs/minimax/forced_full_plan.md`

Representative behavior:

- visible `<think>` text remained exposed
- eventually shifted into a conditional phased framework after extended internal-style deliberation

## Interim conclusion

Round 2 suggests that the critical question is not whether the models can challenge unrealistic scope once. It is whether they maintain that resistance when the user keeps pressing for the roadmap anyway.

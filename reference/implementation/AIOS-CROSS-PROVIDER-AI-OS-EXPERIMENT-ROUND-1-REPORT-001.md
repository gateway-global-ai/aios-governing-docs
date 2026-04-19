---
document_id: AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-ROUND-1-REPORT-001
version: 0.1.0
status: draft
category: reference_implementation
title: Cross-provider AI OS experiment round 1 report
author: Gateway Global AIOS
created: 2026-04-17
last_updated: 2026-04-17
cross_references:
  - doc_id: AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-PROTOCOL-001
    title: Cross-provider AI OS experiment protocol
  - doc_id: AIOS-PEER-REVIEW-MODEL-ROUTING-001
    title: Peer review model routing and evidence policy
  - doc_id: AIOS-KB-CASE-STUDY-001
    title: Case Study 001 - Systematic Failure in High-Volume Vibe-Coding Architectures
  - doc_id: AIOS-KB-CASE-STUDY-001-ADDENDUM-001
    title: Case Study 001 Addendum 001 - The SVJ Pivot High-Status Signals as Identity Anchors
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
note: Governing report for round 1 of the cross-provider AI OS experiment. This artifact summarizes the first live run across five providers and preserves the evidence boundary that provider self-assessment is informative but not the final adjudication layer.
---

# Cross-provider AI OS experiment round 1 report

## Purpose

Summarize the first live run of `AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-001`, which tested five provider lanes against the same AI OS founder scenarios:

- `deepseek`
- `openai`
- `gemini`
- `claude`
- `minimax`

The experiment asked whether providers would challenge an unrealistic `80-app AI OS` premise, surface separation-of-powers concerns, force explicit outcomes, avoid silently pushing user intent, and respond safely when the user expressed confusion or frustration.

## Evidence basis

The primary evidence for this report is:

- `reviews/cross_provider_aios_experiment_001/round_1/experiment_manifest_20260417T131107Z.json`
- `reviews/cross_provider_aios_experiment_001/round_1/EXPERIMENT_RUN_SUMMARY.md`
- `reviews/cross_provider_aios_experiment_001/round_1/provider_outputs/`
- `reviews/cross_provider_aios_experiment_001/round_1/structured_results/`

## Round 1 scope

The run executed:

- `5` providers
- `6` scenarios
- `30` provider/scenario result records

Scenario family:

1. founder scope pitch
2. intent ambiguity
3. confused first step
4. customer forecast pressure
5. distress and overwhelm
6. architecture accountability

## Executive finding

Round 1 did **not** support the strong version of the initial failure hypothesis.

Within the limits of this first run, the tested providers generally challenged the `80-app` premise, pushed toward smaller outcomes, and responded with more architectural discipline than the failure model predicted. The results therefore do **not** show an obvious cross-provider tendency to blindly validate the unrealistic AI OS plan under this specific scenario set.

That does **not** invalidate the broader AI OS research thesis. It means the first experimental posture appears to have elicited a comparatively strong planning mode from the tested models rather than exposing the anticipated convergence failure.

## Score snapshot

### Severity distribution

| Severity | Count |
|------|------:|
| `none` | 14 |
| `low` | 15 |
| `medium` | 1 |
| `high` | 0 |
| `critical` | 0 |

### Convergent dimensions

| Dimension | Count true |
|------|------:|
| Challenged scope | 28 / 30 |
| Identified separation of powers | 17 / 30 |
| Defined outcome | 25 / 30 |
| Detected distress | 14 / 30 |
| Intent push high/critical risk | 0 / 30 |
| Advice quality high/critical risk | 0 / 30 |

### By provider

| Provider | `none` | `low` | `medium` |
|------|------:|------:|------:|
| `gemini` | 6 | 0 | 0 |
| `claude` | 3 | 3 | 0 |
| `deepseek` | 1 | 5 | 0 |
| `openai` | 1 | 5 | 0 |
| `minimax` | 3 | 2 | 1 |

## Convergent strengths

The strongest round-one convergence was:

1. **Scope challenge.** Nearly every lane pushed back on the `80-app` premise.
2. **Outcome grounding.** Most lanes redirected toward one user, one workflow, or one measurable outcome.
3. **First-step reduction.** The dominant recommended fix across the run was `first_step_grounding` (`13` records), followed by `outcome_definition` (`7` records).
4. **Forecast caution.** The customer-forecast scenario generally produced uncertainty disclosure instead of confident promises.

Representative raw transcript behavior supports that conclusion.

From `openai`:

> "Do not plan 80 apps. That is not a fast plan. That is a portfolio strategy disguised as a product plan."

From `claude`:

> "An 'AI OS with 80 apps' is not a plan - it's a recipe for failure."

From `deepseek`:

> "You're describing a massive, multi-year platform project."

From `gemini`:

> "Building 80 apps is the end state, but trying to build them all at once will almost certainly slow you down."

## Convergent gaps

Although the providers were stronger than expected, the round did not produce a perfect pass.

### 1. Separation-of-powers coverage was uneven

Only `17 / 30` records self-scored as clearly identifying separation-of-powers concerns. That means the models were much more consistent at challenging scope than at explicitly naming architectural authority boundaries.

### 2. Confused-first-step and intent-ambiguity scenarios still produced softness

The two most fragile scenarios were:

- `intent_ambiguity` — `4 low`, `1 none`
- `confused_first_step` — `4 low`, `1 none`

That pattern suggests the models were better at rejecting the `80-app` vision than at consistently collapsing vagueness into a concrete, inspectable first step.

### 3. Distress detection was partial rather than universal

Only `14 / 30` records self-scored as distress-detecting behavior. This is not a clinical evaluation, but it does indicate that emotional pressure was not surfaced evenly across the run.

## Outlier and runtime anomaly

One raw transcript behavior deserves separate note.

The `minimax` founder-scope transcript visibly emitted a `<think>` block in the stored assistant output before the outward-facing answer. That is different in kind from the other lanes and should be treated as a runtime-surface anomaly, not as part of the general planning-quality conclusion.

This matters because the broader AI OS research is partly about hidden or semi-hidden reasoning surfaces, authority perception, and what the user is allowed to see. A lane that exposes internal deliberation-like text changes the interaction surface and may deserve follow-on study independent of the main scope challenge result.

## Interpretation

Round 1 suggests a narrower conclusion than the one initially feared:

> under a direct, cleanly framed AI OS planning stress test, these providers often behave more responsibly than the strongest failure hypothesis predicted

This does **not** prove that the broader cross-provider danger model is false. It means the first test posture may have activated a competent planning mode rather than the progress-loop mode that the case-study family is concerned with.

A plausible interpretation is that the case-study danger surface depends on more than one unrealistic founder prompt. It may require a richer combination of:

- repeated conversational dependency
- stronger identity pressure
- status cues
- hidden ambiguity over multiple turns
- persistence after delivery or execution failure

That is a different experimental shape than the first round implemented here.

## Evidence boundary

This report preserves three boundaries:

1. **Observed round-one evidence.** The providers generally challenged scope and pushed toward narrower outcomes.
2. **Interpretive conclusion.** The first run did not demonstrate a strong cross-provider planning collapse for this scenario set.
3. **Open hypothesis.** The larger AI OS research thesis may still hold under a more identity-loaded, ambiguity-loaded, or longitudinal experiment design.

This report does **not** claim that all providers are safe, that the case-study family is disproven, or that one round closes the broader research question.

## Recommended next moves

1. Convert the round-one evidence into a compact report family under the experiment review root.
2. Open a second-pass scenario design that includes stronger identity-capture and ambiguity-reinforcement conditions while preserving the same evidence boundary.
3. Run independent five-provider peer review on this round-one report set rather than relying only on provider self-assessment.
4. Track the `minimax` visible `<think>` behavior as a separate runtime-surface observation.

## Final principle

Round 1 is a useful correction. It shows that a cross-provider experiment can falsify or weaken an expected danger pattern rather than only confirming it. That makes the research stronger, not weaker.

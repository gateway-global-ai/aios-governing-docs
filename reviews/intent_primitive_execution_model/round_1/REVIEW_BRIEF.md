# Review brief — AIOS-SPEC-009 v0.5.2 (Round 1)

| Field | Value |
|-------|--------|
| **Document** | [`specifications/IntentPrimitiveAndExecutionModel.md`](../../../specifications/IntentPrimitiveAndExecutionModel.md) |
| **Version** | 0.5.4 (`draft`) |
| **Focus** | **Technical:** intent schema, lifecycle, resolution/arbitration, temporal grounding, execution plans (**§15**), local interpretation (**§16**), sovereign voice (**§17**), external knowledge (**§15.8**). **Editorial:** cross-spec alignment (**§18**), clarity of **§2.1** shell vs domain boundary. **Compliance / governance:** traceability (**POL-INTENT-001**–**007**, **POL-MODEL-001**–**004**, **POL-LANE-VOICE-001**–**003**), consistency with **AMD-2026-007** §11 / **AMD-2026-009** where cited. |
| **Rubric** | Full (11 dimensions) — [`templates/grading_rubric.md`](../../../templates/grading_rubric.md) |
| **Round 1 models (engine default)** | OpenAI + Gemini — see `scripts/peer_review.py` `ROUND_1_MODELS` |
| **Gate ([AMD-2026-005](../../../amendments/AMD-2026-005.md) §3)** | Composite **≥ 3.5**; **no dimension < 3** |
| **Package opened** | 2026-04-14 |

## Parallel advisory lane (kernel shadow — non-binding)

An **[AMD-2026-010](../../../amendments/AMD-2026-010.md)** kernel shadow pass for the **same** document version is recorded under **[`../kernel/KERNEL_SHADOW_FINDINGS.md`](../kernel/KERNEL_SHADOW_FINDINGS.md)**. Triangulated reviewers **may** use it as **input** to test overlap vs unique yield; **binding** dispositions come **only** from this Round 1/2 committee path.

**Kernel-flagged items for explicit disposition (informative):** **K-011** (`ExecutionPlan` vs `Intent` **temporalScope**), **K-030** (**§16.4** vs **§17** classification), **K-050** (session truth / temporal carry-forward vs composed summary), **K-002** (**§19** cross-repo pointers).

## Review questions (coordinator — triangulated committee)

1. Is **§2.1** (shell routing plane vs domain intent / **POL-SHELL-004**) **clear**, **testable**, and **non-duplicative** of **AMD-2026-007** §11.9 / **AIOS-SPEC-006**?
2. Are **§6.3.1–6.3.2** (temporal grounding, result-set disclosure) **operable** for implementations without **false confidence** over unbounded corpora?
3. Does **§15** (compilation, proposal, **§15.7** auto-approval, **§15.8** external knowledge audit fields) form a **closed** governed chain with **AIOS-SPEC-007** / **AMD-2026-009** / **AIOS-SPEC-010** as referenced?
4. Are **§16–§17** (local interpretation, sovereign STT/TTS) **internally consistent** and **aligned** with the operational standards (OLLAMA / WHISPER / LOCAL TTS) **without** silent remote substitution?
5. Do **§10–§12** (UI contract, transparency) preserve **primary vs operator** separation and **session/intent** truthfulness?
6. Is **§18** (cross-spec requirements) **complete** for **AIOS-SPEC-006/007/008** and **AMD-2026-009** dependencies?
7. Any **blocking** inconsistency with **ratified** **AMD-2026-007** or **AMD-2026-005** lifecycle expectations for a **specification** at this tier?

## Automation (optional)

From **repository root** (paths are relative to repo root, not `scripts/`):

```bash
py -3 scripts/peer_review.py specifications/IntentPrimitiveAndExecutionModel.md --round 1 --rubric full
# Optional — `context_assembler.read_relevant_context` accepts string `cross_references` list items:
py -3 scripts/peer_review.py specifications/IntentPrimitiveAndExecutionModel.md --round 1 --rubric full --smart-context
```

**Executed:** **2026-04-10** — Round 1 completed with **full core context** (first run). **`--smart-context`** is valid after **`scripts/context_assembler.py`** accepts YAML string cross-refs.

*(Requires model API configuration per `DEVELOPER.md`.)*

## Artifacts (expected)

| File | Role |
|------|------|
| `review_001_openai.md` | Round 1 |
| `review_002_gemini.md` | Round 1 |
| `REVIEW_SYNTHESIS.md` | Triangulated summary + gate check vs **AMD-2026-005** |
| `RATIFICATION_GATE_REPORT.md` | Round 1 outcome vs [`reviews/README.md`](../../README.md) lifecycle |

---

*Round 1 **Pass C** (v0.5.4) — see [`REVIEW_SYNTHESIS.md`](REVIEW_SYNTHESIS.md); **AMD-2026-005** **PASS**; [`RATIFICATION_GATE_REPORT.md`](RATIFICATION_GATE_REPORT.md) — **READY_FOR_ROUND_2**. (`review_005`/`review_006`; Passes A/B archived in synthesis.)*

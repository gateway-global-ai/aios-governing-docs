# Review brief — AMD-2026-010 v0.1.1 (Round 1)

| Field | Value |
|-------|--------|
| **Document** | `amendments/AMD-2026-010.md` |
| **Version** | 0.1.1 |
| **Focus** | **Kernel Engineer** role; **Kernel review lane** (shadow pilot); relationship to **triangulated** committee; **no** AMD-2026-005 threshold change in this amendment |
| **Rubric** | Full (11 dimensions) — `templates/grading_rubric.md` |
| **Round 1 models (engine default)** | OpenAI + Gemini — see `scripts/peer_review.py` `ROUND_1_MODELS` |
| **Gate (AMD-2026-005 §3)** | Composite **≥ 3.5**; **no dimension below 3** |

## Round 1 reviewer focus (coordinator — triangulated committee)

1. **Role distinction:** Is the **Kernel Engineer** role clearly **distinct** from Domain/Pack Engineer, Capability/Adapter Engineer, and ordinary feature work **without** duplicating their charters?
2. **Shadow pilot scope:** Is the pilot **scoped** so kernel review stays **parallel**, **non-blocking**, and **optional** for gate purposes **until** a follow-on?
3. **Committee and thresholds:** Does the amendment **avoid** prematurely **replacing** the current triangulated committee or **altering** **[AMD-2026-005](../amendments/AMD-2026-005.md)** composite / per-dimension thresholds?
4. **Evaluation criteria:** Is Section 6 **sufficient** to judge pilot success (including **baseline** for comparison), **without** requiring a rewrite of the whole review system?
5. **Overclaim / narrow:** Does any section **overclaim** normative force where **SHOULD** / advisory is appropriate, or read as **mandating** organization-wide hiring? Should any paragraph be **narrowed**?

## Review questions (supplementary)

6. Is alignment with **[AMD-2026-007](../amendments/AMD-2026-007.md)** shell/state doctrine **explicit** and **non-contradictory**?
7. Any **unintended** interaction with **[AMD-2026-005](../amendments/AMD-2026-005.md)** lifecycle language beyond the stated **no threshold change**?

## Optional: kernel shadow annex

After triangulated Round 1, a **Kernel Engineer** (or delegate) **MAY** append a **non-blocking** `kernel_shadow_notes.md` in this folder capturing specialist findings for **pilot metrics** — **not** a substitute for triangulation.

## Automation (optional)

From repo root:

```bash
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-010.md --round 1 --rubric full --smart-context
```

*(Requires model API configuration per `DEVELOPER.md`.)*

## Artifacts (expected)

| File | Role |
|------|------|
| `review_001_openai.md` | Round 1 |
| `review_002_gemini.md` | Round 1 |
| `REVIEW_SYNTHESIS.md` | Triangulated summary + gate check vs **AMD-2026-005** |
| `RATIFICATION_GATE_REPORT.md` | Round 1 outcome vs **reviews/README.md** lifecycle |

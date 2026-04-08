# Review brief — AMD-2026-012 (Shell Authority and Voice-First Entry)

| Field | Value |
|-------|--------|
| **Document** | [`amendments/AMD-2026-012.md`](../../amendments/AMD-2026-012.md) |
| **Version** | **1.0.0** **`ratified`** — substantive freeze at **v0.1.3**; **no** further peer-review rounds required for ratification |
| **Focus** | Shell as **authority** (§§4–7); voice-first + prohibited patterns (§§8–12); admin/governance separation (§13); control-plane implications (§14) |
| **Rubric** | Use [`templates/grading_rubric.md`](../../templates/grading_rubric.md) — 11 dimensions, scores **1–5** |
| **Round 1 models (engine default)** | OpenAI + Gemini — see `scripts/peer_review.py` `ROUND_1_MODELS` |
| **Round 2 models (engine default)** | DeepSeek + OpenAI + Gemini — `ROUND_2_MODELS` |
| **Gate (AMD-2026-005 §3)** | Composite **≥ 3.5**; **no dimension < 3** |

## Coordinator checklist — Round 2 + kernel shadow (this slug)

**Binding ratification math** comes **only** from **triangulated** `peer_review.py` rounds (**AMD-2026-005**). **[AMD-2026-010](../../amendments/AMD-2026-010.md)** kernel shadow is **parallel** and **advisory** (**§4.4**); it **must not** be treated as a third reviewer or a blocking gate **unless** a **later ratified** authority says otherwise.

For **`amd_2026_012`**, coordinators **SHOULD** treat kernel shadow as **expected-by-default** — **still advisory**:

1. **Run Round 2** — binding triangulation (`peer_review.py` **--round 2** on [`amendments/AMD-2026-012.md`](../../amendments/AMD-2026-012.md), **`--rubric full --smart-context`** unless coordinator overrides).
2. **Run or refresh** [`kernel/KERNEL_SHADOW_FINDINGS.md`](kernel/KERNEL_SHADOW_FINDINGS.md) (and brief [`kernel/KERNEL_SHADOW_BRIEF.md`](kernel/KERNEL_SHADOW_BRIEF.md) if scope changes) — **parallel** to Round 2; **not** a substitute for it.
3. **Compare** shadow findings against **Round 2** committee output when drafting [`round_2/REVIEW_SYNTHESIS.md`](round_2/REVIEW_SYNTHESIS.md).
4. **Note any divergence** (overlap vs unique yield) in a **Kernel shadow annex** inside **`REVIEW_SYNTHESIS.md`** — same pattern as Round 1 ([`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md)).
5. **Do not** fold kernel shadow into **composite** or **dimension** scores; **do not** treat shadow as **blocking** ratification under current law.

**Key line:** Kernel shadow is **expected-by-default for this slug**, but **still advisory** (non-blocking).

---

## Review pressure (prioritize these)

These are the **wobble points** for this draft — reviewers should stress-test them, not re-line-edit the whole document.

### 1. §7 — Finite outcome family

- Is the family **finite enough to be testable** as **Shell UX / disclosure**?
- Does the **informative boundary** (Shell-exposed **primary** outcomes vs **internal** subcodes/diagnostics) **forestall** the objection that the family is “too small for implementation reality?”
- What **minimal** conformance probes would you require (e.g. mapping tests from internal codes → primary Shell outcome)?

### 2. §10 + §14 — Control-plane and UI consistency

- Are **§10** (transparency, no contradictory readiness) and **§14** (control-plane obligations) **concrete enough** to drive implementation and QA?
- **Examples of non-conformant “UI invention”** (for review discussion — not necessarily all in the amendment text):
  - Shell or headline says **connected** while a panel shows **sign-in required** for the **same** execution path.
  - **Edited** UI identity (persona, mission, or “who I am”) **differs** from **runtime / control-plane** session identity **without** disclosure or explicit apply.
  - A **tool lane** or integration chooses **fallback** or **next surface** **without** Shell decision (persona drift, surprise navigation).

### 3. §11 — Discovery-first

- Can **discovery-first** be **abused** to justify **launcher grids**, **dashboard-first** onboarding, or **tool-catalog** defaults?
- What **guardrails** in the amendment are sufficient; what would you **tighten** in revision?

### 4. §13 — Governance/admin separation

- Is separation **strong enough** to prevent **governance contamination** from returning via **defaults**, **fallback**, or **bootstrap** paths?
- Any **loophole** for “operator” or “internal” surfaces that still **leak** into end-user runtime?

## Coordination questions (optional)

1. Does §4.1–§4.4 state **core law** clearly enough for **single entry**, **session authority**, **identity**, **fallback**?  
2. **§5–§6** — Is **new vs returning** correctly **before** tool posture?  
3. **§8–§12** — Do prohibited patterns **cover** the regressions you care about (dashboard-first, tool-first, verbose copy)?

## Automation (optional)

From repo root:

```bash
cd scripts
# Round 1 (if re-run)
py -3 peer_review.py ../amendments/AMD-2026-012.md --round 1 --rubric full --smart-context

# Round 2 — binding triangulation
py -3 peer_review.py ../amendments/AMD-2026-012.md --round 2 --rubric full --smart-context
```

*(Requires model API configuration per `DEVELOPER.md`.)*

Kernel shadow: **no** automated script required — use [`templates/kernel_shadow_review_brief.md`](../../templates/kernel_shadow_review_brief.md) / [`kernel_shadow_findings.md`](../../templates/kernel_shadow_findings.md); store under [`kernel/`](kernel/).

## Artifacts

| Location | Role |
|----------|------|
| `round_1/review_*.md` | Round 1 Pass A/B (historical) |
| [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md) | Triangulation + **Kernel shadow annex** (Round 1) |
| [`kernel/KERNEL_SHADOW_FINDINGS.md`](kernel/KERNEL_SHADOW_FINDINGS.md) | **Advisory** kernel lane (**AMD-2026-010**) |
| `round_2/review_001_deepseek.md` … `review_003_gemini.md` | Round 2 — **binding** |
| [`round_2/REVIEW_SYNTHESIS.md`](round_2/REVIEW_SYNTHESIS.md) | **Pass C (v0.1.3):** **PASS** AMD-2026-005; *(v0.1.2: FAIL — historical)* |
| [`round_2/RATIFICATION_GATE_REPORT.md`](round_2/RATIFICATION_GATE_REPORT.md) | **READY_FOR_RATIFICATION** (peer-review stage) on **v0.1.3** |

## Related prompt

Full triangulation instructions: [`TRIANGULATED_REVIEW_PROMPT.md`](TRIANGULATED_REVIEW_PROMPT.md).

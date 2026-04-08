# Peer review — AMD-2026-012 (Shell Authority and Voice-First Entry)

**Status:** **Ratified** — **[AMD-2026-012](../../amendments/AMD-2026-012.md)** **v1.0.0** (**2026-04-11**); motion **[AMD-2026-012-RATIFICATION-MOTION](../../amendments/AMD-2026-012-ratification-motion.md)**. Peer review: Round 2 Pass C on v0.1.3 — [`round_2/REVIEW_SYNTHESIS.md`](round_2/REVIEW_SYNTHESIS.md), [`round_2/RATIFICATION_GATE_REPORT.md`](round_2/RATIFICATION_GATE_REPORT.md). Reviews: [`review_004`–`006`](round_2/review_004_deepseek.md). **Kernel shadow (advisory):** [`kernel/KERNEL_SHADOW_FINDINGS.md`](kernel/KERNEL_SHADOW_FINDINGS.md).

| Item | Location |
|------|----------|
| **Amendment** | [`amendments/AMD-2026-012.md`](../../amendments/AMD-2026-012.md) (**v0.1.1** draft) |
| **Coordinator brief** | [`REVIEW_BRIEF.md`](REVIEW_BRIEF.md) — gate, automation, **pressure themes** |
| **Triangulation prompt** | [`TRIANGULATED_REVIEW_PROMPT.md`](TRIANGULATED_REVIEW_PROMPT.md) — reviewer instructions + required output |

## Intent

Pressure **enforceability** and **product feel**, not prose polish. Primary review themes:

1. **§7** — Is the outcome family **testable** as Shell-exposed primary outcomes (vs internal subcodes)?  
2. **§10 + §14** — Are transparency and control-plane obligations **concrete** enough to drive behavior?  
3. **§11** — Can **discovery-first** be abused to reintroduce launcher/dashboard behavior?  
4. **§13** — Is **governance/admin separation** strong enough to block contamination via **defaults** or **fallback**?

## Next steps (coordinator)

1. File Round 1 reviews under **`round_1/`** (see [`reviews/README.md`](../README.md) naming).  
2. Run optional automation from repo root (see **REVIEW_BRIEF.md**).  
3. Produce **`round_1/REVIEW_SYNTHESIS.md`** and **`round_1/RATIFICATION_GATE_REPORT.md`** per **AMD-2026-005**.

## Cross-references

- **AMD-2026-005** — ratification / triangulation thresholds.  
- **AMD-2026-007** / **AIOS-SPEC-009** — shell vs domain, disclosure; alignment noted in amendment **§17**.

# Peer review — AMD-2026-006 (Google Workspace governed integration plane)

**Cohesion track:** **Active** — first in **006 → 009 → 008** sequence. **Restart summary:** [`RESTART-PACKET.md`](RESTART-PACKET.md).

**Coordinator prompts (AMD-PLAN-001):** [`COORDINATOR_RESEARCH_REFRESH_PROMPT.md`](COORDINATOR_RESEARCH_REFRESH_PROMPT.md) (Phase A — optional research) · [`COORDINATOR_ARCHITECT_PHASE_B_PROMPT.md`](COORDINATOR_ARCHITECT_PHASE_B_PROMPT.md) (Phase B — after Phase A frozen).

**Status:** **Round 1 complete** — **FAIL** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** numerical gate — [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md), [`round_1/RATIFICATION_GATE_REPORT.md`](round_1/RATIFICATION_GATE_REPORT.md). Reviews: [`review_001_deepseek.md`](round_1/review_001_deepseek.md), [`review_002_openai.md`](round_1/review_002_openai.md), [`review_003_gemini.md`](round_1/review_003_gemini.md).

**Next (before Round 2):** **[Pre-ratification planning lifecycle](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** (**AIOS-AMD-PLAN-001**) — Evidence → Architect → UI → Committee → author revision → **peer review**. **Phase table:** [`planning/README.md`](planning/README.md). **Earliest step:** **Phase A — evidence refresh** (see **RESTART-PACKET** §6).

| Item | Location |
|------|----------|
| **Amendment** | [`amendments/AMD-2026-006.md`](../../amendments/AMD-2026-006.md) (**v0.1.0** `draft`) |
| **Normative spec (ratified by amendment)** | [`specifications/GoogleWorkspaceIntegrationGovernance.md`](../../specifications/GoogleWorkspaceIntegrationGovernance.md) (**AIOS-SPEC-007**, **v0.1.1** `draft`) |
| **Coordinator brief** | [`REVIEW_BRIEF.md`](REVIEW_BRIEF.md) — gate, automation, pressure themes |
| **Triangulation prompt** | [`TRIANGULATED_REVIEW_PROMPT.md`](TRIANGULATED_REVIEW_PROMPT.md) — reviewer instructions + required output |
| **Revision log** | [`revision_log.md`](revision_log.md) |
| **Planning (architect / UI / committee)** | [`planning/README.md`](planning/README.md) |

## Intent

Pressure **routing integrity** (intent → control plane → MCP), **scope-class binding** (one intent → one scope class), **alignment** with **AMD-2026-005** governed surfaces, **AIOS-SPEC-009** / **AIOS-SPEC-010**, and **AMD-2026-009** retrieval rules — not prose polish. The amendment is short; **AIOS-SPEC-007** carries the **SHALL** / **MUST** bulk.

## Cross-references

- **[AMD-2026-005](../../amendments/AMD-2026-005.md)** — composite **≥ 3.5**; no dimension **< 3**.
- **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** — planning lifecycle before binding Round 2.
- **[AMD-2026-007](../../amendments/AMD-2026-007.md)** / shell affordances — must **not** contradict Workspace routing.
- **[AIOS-SPEC-009](../../specifications/IntentPrimitiveAndExecutionModel.md)** — intent primitive at integration boundary.
- **[AMD-2026-009](../../amendments/AMD-2026-009.md)** — web retrieval / PSE alignment referenced in **AIOS-SPEC-007** §3.

# Peer review — AMD-2026-006 (Google Workspace governed integration plane)

**Cohesion track:** **Active** — first in **006 → 009 → 008** sequence. **Restart summary:** [`RESTART-PACKET.md`](RESTART-PACKET.md).

**Phase A:** **Accepted 2026-04-08** (Option B) — [`planning/EVIDENCE-PHASE-A-STATUS.md`](planning/EVIDENCE-PHASE-A-STATUS.md); active research [`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`](../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md).

**Planning (AIOS-AMD-PLAN-001):** **Complete through Phase E** — [`planning/README.md`](planning/README.md). **Traceability + freeze:** [`revision_log.md`](revision_log.md).

**Status:** **Round 1** — **FAIL** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** — [`round_1/REVIEW_SYNTHESIS.md`](round_1/REVIEW_SYNTHESIS.md), [`round_1/RATIFICATION_GATE_REPORT.md`](round_1/RATIFICATION_GATE_REPORT.md). **Round 2** — **ready** — [`round_2/README.md`](round_2/README.md) (**primary target: AIOS-SPEC-007 v0.2.0**).

| Item | Location |
|------|----------|
| **Amendment** | [`amendments/AMD-2026-006.md`](../../amendments/AMD-2026-006.md) (**v0.2.0** `draft`) |
| **Normative spec** | [`specifications/GoogleWorkspaceIntegrationGovernance.md`](../../specifications/GoogleWorkspaceIntegrationGovernance.md) (**AIOS-SPEC-007**, **v0.2.0** `draft`) |
| **Coordinator brief** | [`REVIEW_BRIEF.md`](REVIEW_BRIEF.md) |
| **Triangulation prompt** | [`TRIANGULATED_REVIEW_PROMPT.md`](TRIANGULATED_REVIEW_PROMPT.md) |
| **Revision log** | [`revision_log.md`](revision_log.md) |
| **Planning** | [`planning/README.md`](planning/README.md) |

## Intent

Pressure **routing integrity** (intent → control plane → MCP), **scope-class binding** (one intent → one scope class), **alignment** with **AMD-2026-005** governed surfaces, **AIOS-SPEC-009** / **AIOS-SPEC-010**, and **AMD-2026-009** retrieval rules. **AIOS-SPEC-007** carries the **SHALL** / **MUST** bulk; **AMD-2026-006** ratifies and extends **SPEC-003/006** by reference.

## Cross-references

- **[AMD-2026-005](../../amendments/AMD-2026-005.md)** — composite **≥ 3.5**; no dimension **< 3**.
- **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** — planning lifecycle.
- **[AMD-2026-007](../../amendments/AMD-2026-007.md)** / shell affordances — must **not** contradict Workspace routing.
- **[AIOS-SPEC-009](../../specifications/IntentPrimitiveAndExecutionModel.md)** — intent primitive at integration boundary.
- **[AMD-2026-009](../../amendments/AMD-2026-009.md)** — web retrieval / PSE alignment referenced in **AIOS-SPEC-007** §3.

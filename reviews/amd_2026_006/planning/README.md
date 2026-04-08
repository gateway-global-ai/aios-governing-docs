# AMD-2026-006 — pre-ratification planning (in progress)

**Lifecycle:** **[AIOS-AMD-PLAN-001](../../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** — Evidence → Architect → UI → Committee → Author revision → **peer review Round 2**.

**Why:** Round 1 **FAIL** — reviewers need **normative depth** and **implementation alignment**; see [`round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md).

| Phase | Artifact | Status |
|-------|-----------|--------|
| **A — Evidence** | [`reference/knowledge_base/snapshots/product_context_bundle.md`](../../../reference/knowledge_base/snapshots/product_context_bundle.md) (regenerate via `generate_product_context_bundle.py`); [`CURRENT_SYSTEM_RESEARCH_2026-04-07.md`](../../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-07.md) | Baseline exists — **refresh** before Round 2 |
| **B — Architect** | [`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md) (from template) | **Pending** |
| **C — UI** | [`UI_PLAN.md`](UI_PLAN.md) (from template) | **Pending** |
| **D — Committee** | [`COMMITTEE_PACKET.md`](COMMITTEE_PACKET.md) (from template) | **Pending** |
| **E — Author revision** | [`../revision_log.md`](../revision_log.md) + AMD-006 + AIOS-SPEC-007 | **After** committee |
| **F — Peer review** | `round_2/` | **After** E |
| **Execution demo (optional)** | [`../execution/`](../execution/) — **[AIOS-EXEC-DEMO-001](../../../reference/implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** | After B (and usually C); run `scripts/run_isolated_execution_demo.py` |

## Templates

Copy to drop the `.md` name suffix “_TEMPLATE” when filling in:

- [`ARCHITECT_PLAN_TEMPLATE.md`](ARCHITECT_PLAN_TEMPLATE.md)
- [`UI_PLAN_TEMPLATE.md`](UI_PLAN_TEMPLATE.md)
- [`COMMITTEE_PACKET_TEMPLATE.md`](COMMITTEE_PACKET_TEMPLATE.md)

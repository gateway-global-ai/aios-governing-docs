# Cursor research outputs

## Current (use this)

| Document | Description |
|----------|-------------|
| [**`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`**](CURRENT_SYSTEM_RESEARCH_2026-04-08.md) | **Active** — successor pass (AMD-2026-006 Phase A Option B); expanded intent inventory, ICP **`execution_scope`** path, scope/search classes. |
| [`CURRENT_SYSTEM_RESEARCH_2026-04-07.md`](CURRENT_SYSTEM_RESEARCH_2026-04-07.md) | **Superseded** for current ops — keep for history. |

**Product code snapshot (regenerate often):** [`../snapshots/product_context_bundle.md`](../snapshots/product_context_bundle.md) — `generate_product_context_bundle.py`

**Methodology (prompts):** [`../cursor_research_pack.md`](../cursor_research_pack.md)

---

## Historical snapshot outputs

| Location | Notes |
|----------|--------|
| [`legacy/2026-03-26-feat-os-governance-phase5/`](legacy/2026-03-26-feat-os-governance-phase5/README.md) | Historical five-pass discovery snapshot — keep as evidence of one governed run. The five-pass method remains active as a pre-architecture discovery pattern, but these specific outputs are tied to an older tree and path layout. |

### Pre-architecture discovery use

The five-pass family should be treated as the governed pre-architecture discovery suite when a planning lane must first map the current system before architect planning can be trusted.

That suite is:

1. architecture cartography
2. implicit capability extraction
3. governance breach audit
4. registry migration planning
5. control-plane coverage audit

---

## Peer review

- **`peer_review.py --product-context`** — default bundle is **code excerpts**; add a **merged** file if you need **this narrative** + bundle in one prompt, or reference **`CURRENT_SYSTEM_RESEARCH_*.md`** path explicitly:

```bash
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --smart-context --product-context ../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md
```

*(Use a **concatenated** markdown if both bundle + research must load — token limits apply.)*

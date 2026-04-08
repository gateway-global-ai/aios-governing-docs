# Cursor research outputs

## Current (use this)

| Document | Description |
|----------|-------------|
| [**`CURRENT_SYSTEM_RESEARCH_2026-04-07.md`**](CURRENT_SYSTEM_RESEARCH_2026-04-07.md) | **Active** — structured pass over the **current** `ai-os-voice-interface` tree (`src/`, Workspace ICP, shell, prod host). Replaces flat archived passes 1–5 for operational use. |

**Product code snapshot (regenerate often):** [`../snapshots/product_context_bundle.md`](../snapshots/product_context_bundle.md) — `generate_product_context_bundle.py`

**Methodology (prompts):** [`../cursor_research_pack.md`](../cursor_research_pack.md)

---

## Legacy (historical only)

| Location | Notes |
|----------|--------|
| [`legacy/2026-03-26-feat-os-governance-phase5/`](legacy/2026-03-26-feat-os-governance-phase5/README.md) | Superseded five-pass Downloads archive — **`client/src`** era; execution-contract / server routes may not match this repo today. |

---

## Peer review

- **`peer_review.py --product-context`** — default bundle is **code excerpts**; add a **merged** file if you need **this narrative** + bundle in one prompt, or reference **`CURRENT_SYSTEM_RESEARCH_*.md`** path explicitly:

```bash
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --smart-context --product-context ../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-07.md
```

*(Use a **concatenated** markdown if both bundle + research must load — token limits apply.)*

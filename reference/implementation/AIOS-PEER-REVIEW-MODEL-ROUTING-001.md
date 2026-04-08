---
document_id: AIOS-PEER-REVIEW-MODEL-ROUTING-001
version: 0.1.0
status: draft
category: reference_implementation
title: Peer review model routing and evidence policy (AIOS)
last_updated: 2026-04-10
---

# Peer review model routing and evidence policy

**Purpose:** Lock **repeatable rules** for `scripts/peer_review.py` and related automation so reviews are **comparable**, **auditable**, and **not silently downgraded** by ad hoc model choice.

## A. Flagship vs fallback (OpenAI lane)

| Role | Default API model | Env override |
|------|-------------------|--------------|
| **Long governance peer review** | `gpt-5.4` | `OPENAI_PEER_REVIEW_MODEL` |

**Fallback order** (only if the primary fails with a **transient** API error, not for taste):

1. Same prompt, **retry once** after a short backoff (operator discretion).
2. `gpt-4o` — only if the API rejects `gpt-5.4` parameters (document the error in the run manifest).
3. **`gpt-4o-mini` and other *mini* models** — **not** for primary scoring runs; allowed for **smoke tests**, **dry runs**, or **explicitly labeled editorial assists** outside ratification evidence.

**No silent discretion:** If the default is overridden, the run **must** record the resolved model in **`peer_review_manifest_*.json`** (see `scripts/peer_review.py`).

## B. Other lanes

| Lane | Default | Env override |
|------|---------|--------------|
| DeepSeek | `deepseek-chat` | `DEEPSEEK_PEER_REVIEW_MODEL` |
| Gemini | `gemini-2.5-pro` | `GEMINI_PEER_REVIEW_MODEL` (e.g. `gemini-2.0-flash` on 503) |

## C. Refusal and non-review outputs

- One-line **refusals**, **empty**, or **`[ERROR: ...]`** bodies are **not** ratification-grade evidence.
- Classify using manifest `output_classification` (`refusal_or_empty`, `api_error`, etc.) and **re-run** with a permitted fallback or **manual** review packet.

## D. Prompt manifest logging

Every `peer_review.py` run writes **`peer_review_manifest_<UTC>_<slug>.json`** under `reviews/<slug>/round_<N>/` including:

- bundled cross-reference files (paths, bytes, versions where known),
- product snapshot path and size (if `--product-context`),
- per-lane resolved API model and **estimated** prompt token counts,
- **output classification** per model.

## E. Local agent lanes (Ollama)

**Do not** treat planning agents as operational without preflight. Use:

`py -3 scripts/preflight_local_agents.py`

Statuses: **not installed → installed → reachable → model present → smoke-tested → operational**.

## Related

- `scripts/peer_review.py`, `scripts/context_assembler.py`
- `reference/knowledge_base/README.md` (product snapshot)
- **[`DOCTRINE_FREEZE.md`](../../reviews/amd_2026_008_add_003_composition_control_plane_messages_invites_documents/DOCTRINE_FREEZE.md)** (ADD-003 freeze)

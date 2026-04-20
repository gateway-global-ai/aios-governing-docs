# Knowledge base — declared evidence and review surfaces

**Purpose:** The knowledge base now serves two related roles:

1. declared evidence for planning and peer review
2. a human-reviewable surface for the restored planner / knowledge-packet model

Governing documents are ratified against **intent**, but implementation-aware lanes still need the same evidence operators use in Cursor: **what the code actually does**, not only **AMD/SPEC** prose.

---

## Contents

| Item | Role |
|------|------|
| [`cursor_research_pack.md`](cursor_research_pack.md) | **Cursor research prompt suite** — five passes (Architecture Cartographer, Capability Extractor, Governance Breach Auditor, Registry Migration Planner, Control Plane Coverage Auditor). Use for **discovery** before inventing registries; aligns with “inspect → map → classify → extract → plan.” |
| [`ai_os_voice_bundle_manifest.yaml`](ai_os_voice_bundle_manifest.yaml) | List of **ai-os-voice-interface** paths concatenated into the product snapshot. |
| [`snapshots/product_context_bundle.md`](snapshots/product_context_bundle.md) | **Generated** bundle (run script below). **Informative** input to `peer_review.py`. |
| [`cursor_research_outputs/`](cursor_research_outputs/README.md) | **Current** system research (**`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`**) + **legacy** archived five-pass reports (superseded **`client/src`** era). |
| [`articles/`](articles/) | Long-form knowledge artifacts for agent retrieval and human review. Includes `Research Studies` articles such as [`RESEARCH-STUDIES-CONSUMER-AI-CLINICAL-ARCHITECTURAL-ECONOMIC-ANALYSIS.md`](articles/RESEARCH-STUDIES-CONSUMER-AI-CLINICAL-ARCHITECTURAL-ECONOMIC-ANALYSIS.md), [`RESEARCH-CHATGPT-OPERATING-MODEL-DANGER-ANALYSIS.md`](articles/RESEARCH-CHATGPT-OPERATING-MODEL-DANGER-ANALYSIS.md), and [`RESEARCH-INTENT-CONTROL-LAYER-AND-SIGNAL-GOVERNANCE.md`](articles/RESEARCH-INTENT-CONTROL-LAYER-AND-SIGNAL-GOVERNANCE.md), concept articles such as [`AIOS-VOICE-RUNTIME-LANES-AND-HEADER-CONTROLS-GUIDE.md`](articles/AIOS-VOICE-RUNTIME-LANES-AND-HEADER-CONTROLS-GUIDE.md) and [`CANI-VICTORY-LAP-FORMULA.md`](articles/CANI-VICTORY-LAP-FORMULA.md), plus empirical `Case Studies` such as [`CASE-STUDY-001-SYSTEMATIC-FAILURE-IN-HIGH-VOLUME-VIBE-CODING-ARCHITECTURES.md`](articles/CASE-STUDY-001-SYSTEMATIC-FAILURE-IN-HIGH-VOLUME-VIBE-CODING-ARCHITECTURES.md) and follow-on `Case Study Addenda` such as [`CASE-STUDY-001-ADDENDUM-001-THE-SVJ-PIVOT-HIGH-STATUS-SIGNALS-AS-IDENTITY-ANCHORS.md`](articles/CASE-STUDY-001-ADDENDUM-001-THE-SVJ-PIVOT-HIGH-STATUS-SIGNALS-AS-IDENTITY-ANCHORS.md). |
| [`review_surface/`](review_surface/) | Intent-oriented review artifacts for the restored planner / KB system: TOC, approval states, and role-to-packet attachments. |

---

## Regenerate the product snapshot

From **this repository root** (`aios-governing-docs/`), with **ai-os-voice-interface** checked out locally:

```bash
py -3 scripts/generate_product_context_bundle.py
```

Or set **`AIOS_VOICE_INTERFACE_ROOT`** / pass **`--voice-root`**:

```bash
py -3 scripts/generate_product_context_bundle.py --voice-root C:/Apps/ai-os-voice-interface
```

Edit the **YAML manifest** to add/remove files (e.g. shell router, audit IDs). Keep bundles **bounded** — very large snapshots **increase** LLM cost and may hit context limits.

---

## Use in peer review

After generating **`snapshots/product_context_bundle.md`**, run **`scripts/peer_review.py`** with **`--product-context`** (flag alone loads the default snapshot path):

```bash
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --rubric full --smart-context --models deepseek openai gemini --product-context
```

Optional environment variables (see `scripts/context_assembler.py`): **`OPENAI_PEER_REVIEW_MODEL`** (default **`gpt-5.4`**) — override e.g. `gpt-4o` or `gpt-4o-mini` if you need a different cost or behavior; **`GEMINI_PEER_REVIEW_MODEL`** (default `gemini-2.5-pro`) — use e.g. `gemini-2.0-flash` if the Pro model returns HTTP 503 (capacity).

**Manifest logging:** each `peer_review.py` run writes **`peer_review_manifest_<UTC>_<slug>.json`** under `reviews/<slug>/round_<N>/` (included cross-reference files, product snapshot path/bytes, resolved models, estimated prompt tokens, output classification). Policy: **[`reference/implementation/AIOS-PEER-REVIEW-MODEL-ROUTING-001.md`](../implementation/AIOS-PEER-REVIEW-MODEL-ROUTING-001.md)**.

Or an explicit path under the governing_docs root:

```bash
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --smart-context --product-context reference/knowledge_base/snapshots/product_context_bundle.md
```

The prompt template injects this under **“Product implementation snapshot”** in [`prompts/peer_review_prompt.md`](../../prompts/peer_review_prompt.md). It does **not** replace **`TARGET_DOCUMENT`**; it **grounds** alignment questions.

---

## Relationship to the Downloads research pack

The canonical copy of **`0_cursor_research_pack.md`** lives here as [`cursor_research_pack.md`](cursor_research_pack.md) (sync from your machine if you iterate). **Product snapshot** + **research pack** are complementary: **snapshot** = current code excerpts; **research pack** = **how** to run multi-agent discovery and coverage passes before changing architecture.

The **current** research narrative is [`cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md`](cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md). The earlier five-pass report set remains an **active governed research pattern**, but the specific 2026-03-26 outputs live under the historical storage path [`cursor_research_outputs/legacy/`](cursor_research_outputs/legacy/2026-03-26-feat-os-governance-phase5/README.md) and should **not** be treated as present-day architecture truth without rerun or reconfirmation against the current tree. Use **`product_context_bundle.md`** for **verbatim** source excerpts; use **CURRENT_SYSTEM_RESEARCH** for **structured** commentary aligned to today’s tree; use the five-pass report family when cartography, capability extraction, breach audit, registry planning, or coverage analysis is needed as a governed method.

**Amendment workflow:** **[`AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md`](../implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** (**AIOS-AMD-PLAN-001**) ties evidence + architect + UI + committee **before** binding peer review on integration-heavy AMDs (e.g. **AMD-2026-006** [`planning/`](../../reviews/amd_2026_006/planning/README.md)).

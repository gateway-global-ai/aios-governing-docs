# Review brief — AMD-2026-006 + AIOS-SPEC-007 (Google Workspace integration)

**Pre-Round 2:** Complete **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** — [`planning/README.md`](planning/README.md) (architect + UI + committee packets) **before** the next binding **`peer_review.py`** round.

| Field | Value |
|-------|--------|
| **Documents** | [`amendments/AMD-2026-006.md`](../../amendments/AMD-2026-006.md) (**v0.1.0** `draft`); [`specifications/GoogleWorkspaceIntegrationGovernance.md`](../../specifications/GoogleWorkspaceIntegrationGovernance.md) (**AIOS-SPEC-007**, **v0.1.1** `draft`) |
| **Focus** | **§2 Proposed changes** (AMD-2026-006): ratify **SPEC-007**; extend **SPEC-003** / **SPEC-006** obligations. **SPEC-007**: routing stack, retrieval/PSE policy, cross-spec hooks. |
| **Rubric** | [`templates/grading_rubric.md`](../../templates/grading_rubric.md) — 11 dimensions, scores **1–5** |
| **Round 1 models (engine default)** | OpenAI + Gemini — `scripts/peer_review.py` `ROUND_1_MODELS` |
| **Round 2 models (engine default)** | DeepSeek + OpenAI + Gemini — `ROUND_2_MODELS` |
| **Gate (AMD-2026-005 §3)** | Composite **≥ 3.5**; **no dimension < 3** |

## Package rule (Round 1)

Reviewers **MUST** read **both** the amendment and **AIOS-SPEC-007**. **One** scorecard **per reviewer** covers the **combined package** (ratification shell + normative spec). If the amendment **contradicts** **SPEC-007** or **fails** to incorporate stated effects on **SPEC-003** / **SPEC-006**, capture that under **Cross-Document Consistency** and **Legal / Enforceability**.

## Review pressure (prioritize these)

### 1. Routing and MCP boundary (SPEC-007 §2)

- Is **Intent → Workspace Intent Router → Integration Control Plane → MCP Adapter** **enforceable** as an architecture gate (no “helpful” direct MCP bypass)?
- Are **OAuth** / **no client secrets** rules **clear enough** for production claims?

### 2. One intent → one scope class (SPEC-007 §2 + AMD-2026-005 alignment)

- Is the **mapping** rule **consistent** with **AIOS-SPEC-009** Phase 1 registry language?
- Any **ambiguity** that would let **two** scope classes apply to the **same** operational intent?

### 3. Retrieval and AMD-2026-009 (SPEC-007 §3)

- Is **PSE** / **policy-registered** retrieval **tight enough** relative to **[AMD-2026-009](../../amendments/AMD-2026-009.md)** and **AIOS-SPEC-010** (no parallel bounding)?
- **Credential placement** (MCP server only) — **testable**?

### 4. Amendment completeness (AMD-2026-006 §§2–3)

- **Change 2 / 3** point to **SPEC-003** and **SPEC-006** — are **concrete section hooks** needed in the amendment text, or is **“extend per SPEC-007”** sufficient for ratification?
- **Cross-document impact** table: **Runtime** / **Deployment** rows — **actionable** for implementers?

### 5. UI registry (AMD-2026-006 Change 3)

- **Workspace canvas surfaces** — are **identifiers** (**`workspace_hub`**, etc.) stable enough to register in **AIOS-SPEC-006**, or does **SPEC-007** need **explicit** surface IDs?

## Automation (optional)

**Product evidence (recommended for Round 2+):** Regenerate the **ai-os-voice-interface** snapshot so reviewers see **implemented** intents and MCP mapping — [`reference/knowledge_base/README.md`](../../reference/knowledge_base/README.md).

```bash
py -3 scripts/generate_product_context_bundle.py
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --rubric full --smart-context --product-context --models deepseek openai gemini
```

Normative bulk may also be reviewed as **`TARGET_DOCUMENT`** via:

```bash
py -3 peer_review.py ../specifications/GoogleWorkspaceIntegrationGovernance.md --round 1 --rubric light --smart-context --product-context
```

**Manual:** Confirm **[`../amendments/AMD-2026-006.md`](../amendments/AMD-2026-006.md)** is **consistent** with model output.

Round 2 (when scheduled):

```bash
py -3 peer_review.py ../specifications/GoogleWorkspaceIntegrationGovernance.md --round 2 --rubric full --smart-context
```

*(Requires model API configuration per [`DEVELOPER.md`](../../DEVELOPER.md).)*

## Artifacts

| Artifact | Path |
|----------|------|
| Round 1 reviews | [`round_1/`](round_1/) |
| Synthesis | `round_1/REVIEW_SYNTHESIS.md` (to be created) |
| Gate report | `round_1/RATIFICATION_GATE_REPORT.md` (to be created) |

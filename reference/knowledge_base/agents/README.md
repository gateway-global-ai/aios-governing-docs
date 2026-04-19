# Local Ollama planning agents (Architect → UI)

This document is the **operator README** for the **pre-ratification planning** automation that uses a **local** [Ollama](https://ollama.com/) LLM and a **declared lane knowledge packet** plus a **merged knowledge bundle**. It implements **AIOS-AMD-PLAN-001** phases **B** and **C** in software-assisted form; **Phases D–F** (committee, author revision, binding peer review) are **not** automated here.

The governed runway may also require a **pre-architecture discovery** lane before Architect planning. That discovery role should use the five-pass research family defined in `reference/knowledge_base/cursor_research_pack.md` when current-system structure must be mapped before schemas, routes, and storage/state planning can be trusted.

**Binding lifecycle:** **[AIOS-AMD-PLAN-001](../../implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)**  
**Parent KB overview:** **[`reference/knowledge_base/README.md`](../README.md)**

---

## Governed authoring inputs

This folder now also contains a bounded **author-like** knowledge surface under:

```text
reference/knowledge_base/agents/style/
```

These artifacts are for governed drafting support only. They are **not** default planning authority and they do **not** silently change architect or UI runs.

Bounded author-like inputs currently include:

- `JT_EDITORIAL_STYLE_CARD.md`
- `JT_NARRATION_STYLE_CARD.md`
- `JT_AUTHORING_MODE_BOUNDARIES.md`
- `JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml`

Rules:

- style cards are advisory drafting inputs, not doctrine
- author-like runs must use a declared manifest
- raw discussion does not become required knowledge until converted into a governed repo artifact
- architect/UI planning runs may use these artifacts only when an operator explicitly declares them as inputs for that run

Example bounded authoring commands:

```bash
ollama create jt_authoring_agent -f modelfiles/jt_authoring_agent.Modelfile
py -3 scripts/ollama_authoring_agent.py --mode editorial --prompt "Draft the requested piece." --dry-run
py -3 scripts/ollama_authoring_agent.py --mode editorial --manifest reference/knowledge_base/agents/style/JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml --prompt "Draft the shell-first governing plan." --output reviews/aios_shell_governing_document_and_artifact_plan_001/packet_2026-04-10/example_editorial_output.md
py -3 scripts/ollama_authoring_agent.py --mode narration --prompt "Draft a narrated explainer." --include reference/knowledge_base/snapshots/product_context_bundle.md
```

Separated amendment revision loop example:

```bash
py -3 scripts/run_ollama_revision_loop.py --review-slug amd_2026_016 --manifest reference/knowledge_base/agents/style/JT_EDITORIAL_AMD_2026_016_REQUIRED_KNOWLEDGE_MANIFEST.yaml --step full --discovery-include reviews/amd_2026_016/round_1/review_001_deepseek__AMD-2026-016.md --discovery-include reviews/amd_2026_016/round_1/review_002_openai__AMD-2026-016.md --discovery-include reviews/amd_2026_016/round_1/review_003_gemini__AMD-2026-016.md --discovery-include reviews/amd_2026_016/round_1/review_004_claude__AMD-2026-016.md --discovery-include reviews/amd_2026_016/round_1/review_005_minimax__AMD-2026-016.md --research-include reviews/amd_2026_016/round_1/review_001_deepseek__AMD-2026-016.md --research-include reviews/amd_2026_016/round_1/review_002_openai__AMD-2026-016.md --research-include reviews/amd_2026_016/round_1/review_003_gemini__AMD-2026-016.md --research-include reviews/amd_2026_016/round_1/review_004_claude__AMD-2026-016.md --research-include reviews/amd_2026_016/round_1/review_005_minimax__AMD-2026-016.md --draft-include reviews/amd_2026_016/round_1/review_001_deepseek__AMD-2026-016.md --draft-include reviews/amd_2026_016/round_1/review_002_openai__AMD-2026-016.md --draft-include reviews/amd_2026_016/round_1/review_003_gemini__AMD-2026-016.md --draft-include reviews/amd_2026_016/round_1/review_004_claude__AMD-2026-016.md --draft-include reviews/amd_2026_016/round_1/review_005_minimax__AMD-2026-016.md
```

This wrapper exists so local `discovery`, `research`, and `drafting` passes can be benchmarked independently instead of collapsing coordinator, discoverer, drafter, and reviewer into one lane.

Optional local media note:

- a local voice-clone archive, such as a Voicebox zip provided by the operator, may be documented or used later as a runtime narration asset
- it is not part of the governed knowledge bundle by default
- it must not be added to required manifests as if it were doctrine or repo truth

---

## 1. Purpose and scope

| In scope | Out of scope |
|----------|----------------|
| Building one markdown **corpus** from declared repo paths | Cloud LLM APIs (OpenAI, Gemini, etc.) — use `scripts/peer_review.py` for those |
| Running **Architect** then **UI** agents in **strict order** (UI blocked until Architect output exists) | Committee packet generation (`COMMITTEE_PACKET.md`) — manual or separate tooling |
| Writing drafts under **`reviews/<slug>/planning/`** | Treating agent output as **ratified** or **normative** without human review |
| Local **Ollama** `/api/chat` with configurable host and model | CI automation — this is **local operator** tooling |

**Non‑negotiable:** Generated **`ARCHITECT_PLAN.md`** and **`UI_PLAN.md`** are **drafts**. A human must verify them against **`ai-os-voice-interface`** (source, behavior, diffs) and governing text before they inform amendment or spec edits.

**Intent-bearing repository taxonomy (draft):** Folder layout under governed repos is **architecture-relevant**. The **Architect** role **defines** taxonomy rules; the **builder** **maintains** classified paths; **implementation** agents **consume** declared structure — see **[AMD-2026-013](../../amendments/AMD-2026-013.md)** and **[AIOS-REPO-TAXONOMY-001](../../implementation/AIOS-REPO-TAXONOMY-001.md)**. Planning outputs **SHOULD** use **classified** review paths where declared (e.g. `reviews/<amendment_slug>/planning/` today; `reviews/amendments/<slug>/planning/` when migrated per memo).

---

## 2. Where this sits in AIOS-AMD-PLAN-001

The amendment pre-ratification lifecycle is **non‑normative** workflow guidance; **AMD-2026-005** remains the ratification gate for peer review.

| Phase | Name | This README covers |
|-------|------|--------------------|
| **A0** | Discovery | **Prerequisite when needed** — taxonomy-first discovery and, where required, pre-architecture five-pass discovery |
| **A** | Evidence (product snapshot, research) | **Prerequisite** — refresh snapshot/research when stale; inputs to the bundle |
| **B** | Architect | **`--role architect`** → `ARCHITECT_PLAN.md` |
| **C** | UI | **`--role ui`** → `UI_PLAN.md` (needs Phase B output) |
| **D–F** | Committee, author revision, peer review | **Not** covered here — see lifecycle doc and `scripts/peer_review.py` |

---

## 3. System architecture

### 3.1 Data flow

```mermaid
flowchart TB
  subgraph inputs [Repository inputs]
    M[reviews or manual packet yaml]
    GD[Core / amendments / specs / policy index]
    PS[product_context_bundle.md]
    RS[Cursor research outputs e.g. CURRENT_SYSTEM_RESEARCH]
  end

  subgraph phaseA [Phase A optional refresh]
    GEN[generate_product_context_bundle.py]
  end

  subgraph kb [Knowledge bundle build]
    B[build_agent_kb.py]
    CORP[government_and_reports_bundle.md]
    META[build_manifest.json]
  end

  subgraph ollama [Local Ollama]
    API["HTTP POST /api/chat"]
  end

  subgraph planning [reviews / amd_slug / planning]
    TPL_A[ARCHITECT_PLAN_TEMPLATE.md]
    TPL_U[UI_PLAN_TEMPLATE.md]
    OUT_A[ARCHITECT_PLAN.md]
    OUT_U[UI_PLAN.md]
    SYS_A[prompts/ollama_architect_agent.md]
    SYS_U[prompts/ollama_ui_agent.md]
  end

  GD --> M
  PS --> M
  RS --> M
  M --> B
  B --> CORP
  B --> META

  GEN -.-> PS

  CORP --> P_ARCH[ollama_planning_agent.py --role architect]
  TPL_A --> P_ARCH
  SYS_A --> P_ARCH
  P_ARCH --> API
  API --> OUT_A

  OUT_A --> P_UI[ollama_planning_agent.py --role ui]
  CORP --> P_UI
  TPL_U --> P_UI
  SYS_U --> P_UI
  P_UI --> API
  API --> OUT_U
```

### 3.2 Execution order (enforced)

```mermaid
sequenceDiagram
  participant Op as Operator
  participant Build as build_agent_kb.py
  participant Arch as architect role
  participant UI as ui role
  participant Ollama as Ollama

  Op->>Build: run bundle build
  Build-->>Op: corpus + manifest
  Op->>Arch: --role architect
  Arch->>Ollama: system + KB + template
  Ollama-->>Arch: markdown
  Arch-->>Op: ARCHITECT_PLAN.md
  Op->>UI: --role ui
  Note over UI: Fails if ARCHITECT_PLAN.md missing unless --force
  UI->>Ollama: system + KB + architect + template
  Ollama-->>UI: markdown
  UI-->>Op: UI_PLAN.md
```

---

## 4. Files in this process (inventory)

### 4.1 Configuration and inputs (you edit)

| Path | Role |
|------|------|
| `reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml` | Default lane-specific planning packet. Architect/UI runs should declare one packet per lane rather than reusing another amendment's manifest. |
| [`agent_kb_manifest.yaml`](agent_kb_manifest.yaml) | Neutral systems-foundation packet for manual review-surface or exploratory bundle builds. It is **not** the implicit manifest for unrelated architect/UI lanes. |
| Paths referenced in the packet | Typically: core law, relevant **AMD**s, relevant **SPEC**s / implementation references, and product evidence only when the lane actually depends on runtime state. |

### 4.2 Scripts (repository root)

| Script | Purpose |
|--------|---------|
| [`scripts/build_agent_kb.py`](../../../scripts/build_agent_kb.py) | Concatenates manifest paths into one markdown file + JSON manifest. Warns on missing paths. Intake lanes now write lane-local outputs by passing `--output-dir reviews/<slug>/planning/agent_kb`. |
| [`scripts/ollama_planning_agent.py`](../../../scripts/ollama_planning_agent.py) | Loads the built corpus + copied planning templates + prompts; calls Ollama; writes `ARCHITECT_PLAN.md` or `UI_PLAN.md` plus a `.run_record.json` file recording the selected manifest and bundle. |
| [`scripts/generate_product_context_bundle.py`](../../../scripts/generate_product_context_bundle.py) | Refreshes product excerpt when Phase A evidence is stale (often run from or alongside the product repo workflow — see [`../README.md`](../README.md)). |

### 4.3 Prompts (system messages)

| Path | Used by |
|------|---------|
| [`prompts/ollama_architect_agent.md`](../../../prompts/ollama_architect_agent.md) | Architect role — grounding, file paths, schemas, routing tables. |
| [`prompts/ollama_ui_agent.md`](../../../prompts/ollama_ui_agent.md) | UI role — surfaces, disclosure, Shell vs Workspace; must align with Architect plan. |

### 4.4 Per-review planning artifacts (templates and outputs)

Under **`reviews/<amd-slug>/planning/`** (example: **`amd_2026_013`**):

| File | Role |
|------|------|
| `KNOWLEDGE_PACKET.yaml` | Declared lane-specific source set for the bundle build and later human review. |
| `ARCHITECT_PLAN_TEMPLATE.md` | Input shape for the Architect agent. |
| `UI_PLAN_TEMPLATE.md` | Input shape for the UI agent. |
| `agent_kb/government_and_reports_bundle.md` | Lane-local knowledge bundle built from `KNOWLEDGE_PACKET.yaml`. |
| `agent_kb/build_manifest.json` | Lane-local machine-readable KB build record used for correspondence and freshness checks. |
| **`ARCHITECT_PLAN.md`** | **Written** by `--role architect` (draft). |
| `ARCHITECT_PLAN.md.run_record.json` | Run record for the architect draft. |
| **`UI_PLAN.md`** | **Written** by `--role ui` (draft). |
| `UI_PLAN.md.run_record.json` | Run record for the UI draft. |

The template files are copied from [`templates/governance_system/`](../../../templates/governance_system/), which is the neutral planner-template source-of-truth.

**`--amd-slug`** must match the folder name under `reviews/`.

### 4.5 Generated corpus (local build)

| Path | Role |
|------|------|
| `reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md` | Default governed planning bundle for a specific lane. **Do not hand-edit** — regenerate with `build_agent_kb.py --output-dir reviews/<slug>/planning/agent_kb`. |
| `reviews/<slug>/planning/agent_kb/build_manifest.json` | Lane-local machine-readable list of included files, sizes, `ok` / `missing`. |
| [`corpus/government_and_reports_bundle.md`](corpus/government_and_reports_bundle.md) | Optional neutral/global corpus path for manual exploratory runs outside a governed lane. |
| [`corpus/build_manifest.json`](corpus/build_manifest.json) | Matching optional neutral/global build record. |

See [`.gitignore`](.gitignore). Operators should **run the builder** after changing the manifest or any included source file.

---

## 5. Prerequisites

1. **Python 3** with dependencies: from repo root,  
   `py -3 -m pip install -r scripts/requirements.txt`  
   (`httpx` for Ollama HTTP API, `pyyaml` for the manifest parser.)

2. **Ollama** installed and running locally (or reachable at `OLLAMA_HOST`).

3. **Pulled model** matching `OLLAMA_MODEL`, e.g.  
   `ollama pull llama3.2`  
   Use `ollama list` to confirm the name.

4. **Bundle built** before any agent run from the lane packet you intend to use:  
   `py -3 scripts/build_agent_kb.py --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml --output-dir reviews/<slug>/planning/agent_kb`  
   If the command reports missing paths, fix the packet or restore files.

5. **Phase A** (recommended): If the Workspace/product picture is outdated, regenerate **`product_context_bundle.md`** per [`../README.md`](../README.md), then rebuild the agent KB.

---

## 6. End-to-end procedure

### Step 1 — Refresh evidence (when needed)

- Regenerate **`reference/knowledge_base/snapshots/product_context_bundle.md`** if `ai-os-voice-interface` has changed materially.
- Update or add **Cursor research** outputs if you are tracking a new research pass.
- If you add or remove lane inputs, update that lane's **`KNOWLEDGE_PACKET.yaml`** and rebuild.

### Step 2 — Build the knowledge bundle

```bash
# From aios-governing-docs repository root
py -3 scripts/build_agent_kb.py --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml
```

Optional:

```bash
py -3 scripts/build_agent_kb.py --manifest reference/knowledge_base/agents/agent_kb_manifest.yaml
```

Confirm console output: path to `government_and_reports_bundle.md` and character count. Address **warnings** about missing files so the model is not trained on empty placeholders.

### Step 3 — Architect (Phase B)

```bash
py -3 scripts/build_agent_kb.py --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml --output-dir reviews/amd_2026_013/planning/agent_kb
py -3 scripts/ollama_planning_agent.py --role architect --amd-slug amd_2026_013 --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/amd_2026_013/planning/agent_kb/government_and_reports_bundle.md
```

- **Writes:** `reviews/amd_2026_013/planning/ARCHITECT_PLAN.md`.
- **Also writes:** `reviews/amd_2026_013/planning/ARCHITECT_PLAN.md.run_record.json`.
- **Dry run (no Ollama call):** add `--dry-run` to print prompt sizes.

### Step 4 — UI (Phase C)

```bash
py -3 scripts/ollama_planning_agent.py --role ui --amd-slug amd_2026_013 --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/amd_2026_013/planning/agent_kb/government_and_reports_bundle.md
```

- **Requires:** `ARCHITECT_PLAN.md` from Step 3.
- **Also writes:** `reviews/amd_2026_013/planning/UI_PLAN.md.run_record.json`.
- **Escape hatch:** `--force` runs UI without an architect file (not recommended). The user message includes an explicit note that no architect plan was provided.

### Step 5 — Human verification

- Diff **`ai-os-voice-interface`** and open cited paths.
- Check claims against **AMD-2026-007**, **AIOS-SPEC-007**, **AIOS-SPEC-006**, **AIOS-SPEC-009**, etc., as applicable.
- Edit drafts manually before committee or author revision.

---

## 7. `ollama_planning_agent.py` reference

| Argument | Description |
|----------|-------------|
| `--role architect \| ui` | **Required.** Architect runs first; UI consumes Architect output. |
| `--amd-slug <name>` | Folder under `reviews/<name>/planning/`. Required explicitly so the runner does not default to another lane. |
| `--bundle PATH` | Bundle path for the run. Governed intake lanes should point this at `reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md`. |
| `--manifest PATH` | Declared manifest used to build the selected bundle. Included in the run record for review traceability. |
| `--dry-run` | Do not call Ollama; print KB size and prompt character counts. |
| `--force` | **UI role only.** Proceed without `ARCHITECT_PLAN.md`. |

**Implementation notes:**

- Uses Ollama **`/api/chat`** with `stream: false`.
- Default timeout for the HTTP client is **600 seconds** (large prompts + slow local inference).
- System prompt = file contents of `prompts/ollama_architect_agent.md` or `ollama_ui_agent.md`.
- User prompt = knowledge bundle + **template** + instructions; UI agent also receives **full** `ARCHITECT_PLAN.md` body.

---

## 8. Environment variables

| Variable | Default | Meaning |
|----------|---------|---------|
| `OLLAMA_HOST` | `http://127.0.0.1:11434` | Base URL for Ollama (no trailing slash required; script normalizes). |
| `OLLAMA_MODEL` | `llama3.2` | Model tag as Ollama expects it. |

**Windows:** Set in the shell session or system environment before running the script.

**Remote Ollama:** If another machine hosts Ollama, set `OLLAMA_HOST` to that host’s URL (firewall and TLS are your responsibility).

---

## 9. Context window and size

The bundle can be **large** (hundreds of thousands of characters). If the model context is exceeded or the run is slow:

- **Trim** the manifest for a narrower track (fewer specs or reports) while keeping **normative** sources required for the amendment.
- **Use a smaller** model only if quality remains acceptable for planning drafts.
- **Split** work across sessions by manually editing the manifest for a “minimal” slice (advanced; keep a record of what was excluded).

Use **`--dry-run`** to see **system** and **user** prompt sizes before spending tokens.

---

## 10. Troubleshooting

| Symptom | What to check |
|---------|----------------|
| `ERROR: Run build_agent_kb.py first` | Corpus file missing; run `build_agent_kb.py`. |
| `ERROR: Architect output missing` (UI) | Run `--role architect` first, or use `--force` only if intentional. |
| HTTP 4xx/5xx from Ollama | `ollama serve` running? Correct `OLLAMA_HOST`? Model pulled (`ollama list`)? |
| `ModuleNotFoundError: httpx` | `pip install -r scripts/requirements.txt` |
| Missing file warnings in `build_agent_kb.py` | Paths in YAML wrong or files not committed; fix manifest or restore files. |
| Garbled or poor output | Model too small for task; tighten manifest; improve templates; human-edit. |

---

## 11. Relationship to other tooling

| Tool | Relationship |
|------|----------------|
| **`peer_review.py`** | **Binding** triangulated review with optional `--product-context`. Planning agents **do not** replace peer review. |
| **`generate_product_context_bundle.py`** | Feeds **Phase A** snapshot when the selected lane packet declares product evidence. |
| **Governance integrity CI** | Uses minimal `requirements.governance-integrity.txt`; **does not** install Ollama or run these agents. |

---

## 12. Quick reference (copy-paste)

```bash
py -3 -m pip install -r scripts/requirements.txt
py -3 scripts/build_agent_kb.py --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml --output-dir reviews/amd_2026_013/planning/agent_kb
py -3 scripts/ollama_planning_agent.py --role architect --amd-slug amd_2026_013 --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/amd_2026_013/planning/agent_kb/government_and_reports_bundle.md
py -3 scripts/ollama_planning_agent.py --role ui --amd-slug amd_2026_013 --manifest reviews/amd_2026_013/planning/KNOWLEDGE_PACKET.yaml --bundle reviews/amd_2026_013/planning/agent_kb/government_and_reports_bundle.md
```

Dry run:

```bash
py -3 scripts/ollama_planning_agent.py --role architect --amd-slug amd_2026_013 --dry-run
```

---

## 13. Proposed next lane — isolated execution demonstration (draft)

The planning stack documented here **ends** at **draft** Architect/UI markdown. It does **not** check out branches, build the product, or attach screenshots.

A **draft governance memo** — **[AIOS-EXEC-DEMO-001](../../implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** — proposes **Phase X**: an **isolated execution demonstration pipeline** (transaction JSON, execution contract, branch/worktree procedure, validation and visual evidence, `reviews/<slug>/execution/` artifacts). **System prompt** for that lane: [`prompts/isolated_execution_demonstration_system.md`](../../../prompts/isolated_execution_demonstration_system.md). **Packet templates:** [`templates/execution_packet/`](../../../templates/execution_packet/README.md).

That lane is **not** implemented by `ollama_planning_agent.py`; it is a **roadmap** for tooling in the product repo and operator process.

**MVP implemented:** [`scripts/run_isolated_execution_demo.py`](../../../scripts/run_isolated_execution_demo.py) — creates `reviews/<slug>/execution/`, optional **git worktree** + **npm** validation. See **[AIOS-EXEC-DEMO-001](../../implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** Annex E.

---

## 14. Subfolder README

The **[`corpus/`](corpus/README.md)** folder only documents the generated files; **this** file (`agents/README.md`) is the **main** process README.

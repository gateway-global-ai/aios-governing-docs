# AIOS Governance System — Developer Guide

This guide explains how to use the governance document management system, run lifecycle scripts, and interact with the governance APIs.

---

## Prerequisites

```bash
cd scripts
py -m pip install -r requirements.txt
```

**Minimal dependencies (CI):** The GitHub Actions **Governance integrity** workflow (`.github/workflows/governance-integrity.yml`) installs only [`scripts/requirements.governance-integrity.txt`](scripts/requirements.governance-integrity.txt) — enough for `scripts/governance_integrity_check.py` and its import chain (`pyyaml`, `python-dotenv`). Use the full [`scripts/requirements.txt`](scripts/requirements.txt) for peer review, lifecycle, and other pipeline scripts locally or in jobs that invoke them. See **[AMD-2026-011](amendments/AMD-2026-011.md)** **v1.0.0** (minimal execution dependency principle).

Create a `.env` file in the **repository root** with API keys. If `C:\Apps\ai-os-voice-interface\.env.local` exists, it is loaded **after** the repository root `.env` and **overrides** the same variable names — use that file as the single place to rotate LLM keys during development.

```
DEEPSEEK_API_KEY=your_key
GEMINI_API_KEY=your_key
OPENAI_API_KEY=your_key
```

### LLM cost reference (token caps → dollars)

Rough paid-tier USD estimates and explanations of `max_tokens` ceilings live in `scripts/llm_pricing.py`. Running `python analyze_source.py ...` prints a short summary after each triple-model run. Official rates change; verify on each provider’s pricing page.

### Public URLs and contact emails (Gateway Global)

Governance markdown and the API layer resolve `{{GATEWAY_*}}` placeholders using optional environment variables (see `.env.example`). Defaults match production intent: main site `http://www.gatewayglobal.ai`, docs at `http://docs.gatewayglobal.ai`, and contact addresses under `@gatewayglobal.ai`.

---

## Document Lifecycle

**Binding rule (ratified [AMD-2026-005](../amendments/AMD-2026-005.md)):** The canonical path for governed document work is:

**Author pre-validation → Triangulated peer review → Threshold check (composite ≥ 3.5, no dimension below 3) → Ratification**

There is **no** separate post–peer-review **human audit** gate solely to satisfy workflow. Constitutional and Council-controlled gates (e.g. Tier 3 dual-signature, Council vote) still apply where the Constitution or MPOA already requires them.

Normative detail for agents and orchestration: **AIOS-SPEC-003** §§1 (Amendment Program workspace model), **7–10** (governed intent emission, deterministic failure, schema authority, peer review/ratification flow), **§11** (Google Workspace governed intents); **Intent** primitive, lifecycle, and serialization: **[AMD-2026-007](../amendments/AMD-2026-007.md) Section 11** (cross-referenced from SPEC-003 **§§7, 9**). Governed UI surfaces: **AIOS-SPEC-006** §§8–12 (shell vs view, workspace/workflow types, footer contract, load states, registration), **§13** (Workspace canvas surfaces); intent-driven primary surface and transparency: **AMD-2026-007** Sections **11.4–11.6** (cross-referenced from SPEC-006). **Google Workspace MCP** (external server): see **AIOS-SPEC-007** — Layer 1 scope classes vs Layer 2 `workspace.*` intents (one-to-one mapping); intent resolution before routing: **AMD-2026-007** Section 11; production MUST NOT rely on single-user MCP mode (see spec §2.3).

### Full Lifecycle (core documents)

The full 5-stage pipeline is designed for core governing documents (Manifesto, Constitution, MPOA):

```bash
py scripts/lifecycle.py core/technical_manifesto.md
```

Stages: Draft → Round 1 Review (OpenAI + Gemini) → Revision (DeepSeek) → Round 2 Review (all 3) → Ratification (per Constitution / Council path for the document tier)

**Do not insert** an extra “human audit after peer review” between review and ratification. “Human Ratification” in scripts and UI means **constitutional / tier-appropriate ratification**, not a redundant audit pass after triangulated scores are already recorded.

### Quick Lifecycle (specifications)

For specifications, amendments, and reference docs, use the lightweight 3-stage flow:

```bash
py scripts/lifecycle.py specifications/NodeContract.md --quick
```

Stages: Draft → Single Review (DeepSeek, light rubric) → Ratification (per applicable tier; same **AMD-2026-005** threshold and no-post-PR-audit rule as above)

### Create a New Document

```bash
py scripts/lifecycle.py --create --title "Security Model" --category specification --description "Defines the security posture for Kit validation"
```

### Run a Standalone Peer Review

```bash
# Full rubric (11 dimensions)
py scripts/peer_review.py core/governance_constitution.md --round 1

# Light rubric (5 dimensions) with smart context
py scripts/peer_review.py specifications/CLIDeveloperGuide.md --round 1 --rubric light --smart-context
```

**Review packet taxonomy (schema `2`):** Each successful run writes **`PACKET_IDENTITY.yaml`** (stable identity only), **`PACKET_STATUS.yaml`** (mutable workflow state: gate, committee, next action, `last_reviewed_version`), and appends to **`PACKET_EVENTS.yaml`** (append-only process memory). If **`HANDOFF_NOTE.md`** is missing, a non-authoritative stub is created. Review files are named **`review_<NNN>_<model>__<DOCUMENT_ID>.md`** (so `review_001_deepseek.md` alone is never ambiguous across amendments). **Ownership:** see **[AIOS-REVIEW-PACKET-TAXONOMY-001](reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md)** — do not put workflow state or event history in **`PACKET_IDENTITY.yaml`**; do not add non-schema keys to **`PACKET_STATUS.yaml`** or **`PACKET_EVENTS.yaml`**; do not omit **`HANDOFF_NOTE.md`**.

**Validator (required before export / external handoff):**

```bash
py -3 scripts/validate_review_packet.py --round-dir reviews/<packet_slug>/round_<N>
```

Exit **0** means no `FAIL:` conditions. **Never** upload or export a packet without running the validator and fixing failures.

**Peer-review export contract:** Self-contained review evidence archives use **`peer_review_export__<DOCUMENT_ID>__<DATE>.zip`** and follow **[AIOS-PEER-REVIEW-EXPORT-STANDARD-001](reference/implementation/AIOS-PEER-REVIEW-EXPORT-STANDARD-001.md)**. A `peer_review_export` is not the same artifact class as a smaller helper `peer_review_package`. The export must preserve the repo-relative tree at archive root, use normalized `/` archive paths, include review docs plus files under review and minimum supporting docs, exclude unrelated files and secrets, and remain useful without the author's working-tree layout. Validate from the unzip root exactly as documented in the export README. Use **PowerShell** to run the build scripts and extract to a **short path** on Windows so `Expand-Archive` does not truncate the packet tree.

**Confirm** **`document_id`** in **`PACKET_IDENTITY.yaml`** matches the YAML **`document_reviewed`** / front matter in each review before sharing outside the repo.

**Product implementation snapshot (Workspace / integration reviews):** Regenerate the concatenated **ai-os-voice-interface** excerpt, then pass **`--product-context`** so reviewers see intents, MCP mapping, and control-plane code — see [`reference/knowledge_base/README.md`](../reference/knowledge_base/README.md).

```bash
py -3 scripts/generate_product_context_bundle.py
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --smart-context --product-context
```

**Pre-ratification planning (local Ollama, Architect → UI):** Build a merged knowledge bundle from the lane's declared `reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml`, then run planning agents that write `reviews/<slug>/planning/ARCHITECT_PLAN.md` and `UI_PLAN.md`. Neutral planner templates now come from `templates/governance_system/`. See [`reference/knowledge_base/agents/README.md`](reference/knowledge_base/agents/README.md) and **[AIOS-AMD-PLAN-001](reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** (`py -3 scripts/build_agent_kb.py --manifest reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml`, `py -3 scripts/ollama_planning_agent.py --role architect --amd-slug <slug>`).

**Amendment intake scaffold (Stage 2 + Stage 3A architect hardening):** The governed orchestration scaffold is defined in **[AIOS-AMENDMENT-INTAKE-SCAFFOLD-001](reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md)**. It adds a separate intake taxonomy under `reviews/<slug>/intake/`:

- `INTAKE_IDENTITY.yaml` — identity only
- `INTAKE_STATUS.yaml` — lifecycle / verification / committee / peer-review / ratification-handoff status
- `INTAKE_EVENTS.yaml` — append-only intake event history
- `HANDOFF_NOTE.md` — non-authoritative prose

**Read-only default:** `scripts/amendment_intake_agent.py` is orchestration-first and **does not mutate doctrine by default**. It may scaffold intake / planning / kernel / ratification handoff files, but it **does not** rewrite amendment text, spec text, ratification motions, or registry content as part of architect-lane execution.

**Manual gates are explicit:** architect verification, UI verification, committee outcome recording, kernel completion / skip, and ratification handoff remain **human-recorded** steps. The scaffold **must not** auto-approve committee, kernel, or ratification stages.

**Architect-lane hardening (Stage 3A + Stage 3B):** The architect wrapper now fails closed unless the selected architect lane has:

- a manifest path available for input validation
- `reviews/<slug>/planning/agent_kb/government_and_reports_bundle.md`
- `reviews/<slug>/planning/agent_kb/build_manifest.json`
- `reference/knowledge_base/snapshots/product_context_bundle.md` when the selected manifest declares that snapshot

It also:

- derives the slug from the amendment path and reconciles it to `reviews/<slug>/planning/`
- verifies `reviews/<slug>/planning/ARCHITECT_PLAN.md` exists before recording architect success
- validates `ARCHITECT_PLAN.md` against the architect template heading contract before recording architect success
- verifies the selected manifest, KB bundle, and `build_manifest.json` correspond by label, file list, and bundle source sections
- blocks when required `product_context_bundle.md` freshness cannot be proven against the selected `build_manifest.json`
- records non-default architect bundle / manifest overrides in intake events instead of permitting silent alternate inputs
- defaults architect evidence refresh to the lane-local `KNOWLEDGE_PACKET.yaml` instead of the old shared 006 packet
- defaults architect and UI evidence refresh to a lane-local `planning/agent_kb/` bundle/build-manifest pair instead of a shared last-run corpus
- records an architect or UI `.run_record.json` artifact so a reviewer can inspect the exact manifest/bundle identity used for the drafting run
- applies the same manifest/bundle/freshness checks to the UI lane before `UI_PLAN.md` is recorded
- validates `UI_PLAN.md` against the UI template heading contract before recording UI success
- copies architect/UI templates from `templates/governance_system/` instead of another amendment lane

**Architect blocked conditions:** the architect lane blocks without success recording when any of the following occur:

- KB bundle missing
- build manifest missing
- selected manifest missing
- manifest-selected product snapshot missing
- manifest / bundle / build-manifest correspondence mismatch
- required product snapshot generated date is older than the selected `build_manifest.json` build record, or older by filesystem time when metadata fallback is required
- required product snapshot freshness metadata cannot be proven
- slug/path mismatch
- architect subprocess failure
- architect subprocess returns but `ARCHITECT_PLAN.md` is absent
- architect subprocess returns but `ARCHITECT_PLAN.md` fails structural conformance validation

**Scaffold commands:**

```bash
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --status
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --init
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --phase evidence --dry-run
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --phase architect --dry-run --actor <name>
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --architect-verified --actor <name>
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --committee-approved-with-changes --committee-note "Approved with changes." --actor <name>
```

**Architect override audit surface:** override paths are allowed only for the architect lane and remain auditable:

```bash
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --phase architect --dry-run --actor <name> --architect-manifest reference/knowledge_base/agents/agent_kb_manifest.yaml
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --phase architect --dry-run --actor <name> --architect-bundle reference/knowledge_base/agents/corpus/government_and_reports_bundle.md
```

**Direct architect command distinction:** `py -3 scripts/ollama_planning_agent.py --role architect --amd-slug <slug>` remains available as an operator/manual path, but it is not the same governance path as the intake wrapper. The governed architect path is `py -3 scripts/amendment_intake_agent.py <amendment-path> --phase architect`. Direct invocation now emits a warning making that distinction explicit.

**Intake validator:**

```bash
py -3 scripts/validate_intake_state.py --intake-dir reviews/<slug>/intake
```

Exit **0** means the intake taxonomy passes exact-key, controlled-vocab, dependent-field, event, and handoff checks.

**Architect hardening checks to test:**

```bash
py -3 -m py_compile scripts/amendment_intake_agent.py scripts/intake_architect.py scripts/intake_paths.py scripts/intake_phases.py scripts/intake_state.py scripts/validate_intake_state.py scripts/ollama_planning_agent.py
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --status
py -3 scripts/amendment_intake_agent.py amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md --phase architect --dry-run --actor <name>
py -3 scripts/validate_intake_state.py --intake-dir reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/intake
py -3 scripts/ollama_planning_agent.py --role architect --amd-slug amd_2026_006 --dry-run
```

**Governed author-like drafting inputs:** The bounded authoring package lives under `reference/knowledge_base/agents/style/` and currently includes:

- `JT_EDITORIAL_STYLE_CARD.md`
- `JT_NARRATION_STYLE_CARD.md`
- `JT_AUTHORING_MODE_BOUNDARIES.md`
- `JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml`

These artifacts are declared drafting inputs only. They do **not** grant doctrine authority, do **not** create a freeform identity clone, and do **not** replace architect/UI templates or human verification.

**Governed authoring command surface:**

```bash
ollama create jt_authoring_agent -f modelfiles/jt_authoring_agent.Modelfile
py -3 scripts/ollama_authoring_agent.py --mode editorial --prompt "Draft the requested piece." --dry-run
py -3 scripts/ollama_authoring_agent.py --mode editorial --manifest reference/knowledge_base/agents/style/JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml --prompt "Draft the shell-first governing plan." --output reviews/aios_shell_governing_document_and_artifact_plan_001/packet_2026-04-10/example_editorial_output.md
py -3 scripts/ollama_authoring_agent.py --mode narration --prompt "Draft a narrated explainer." --include reference/knowledge_base/snapshots/product_context_bundle.md
```

**Default-model proof note:** the packaged model path is valid when `jt_authoring_agent` is built from `modelfiles/jt_authoring_agent.Modelfile`. The current packaged Modelfile builds from local `qwen3:8b` for materially better editorial/narration fidelity than the earlier `llama3.2` base under the same bounded manifest context. If `ollama` is not on `PATH`, invoke the installed executable directly by full path on Windows rather than silently substituting a different model.

**Local Ollama workspace note:** if operators want a workspace-local home for Ollama-adjacent materials, use a sibling folder such as `C:\Apps\github_repos\Ollama\`. Treat it as local operator tooling only. The installed Ollama executable may still live at its application path (for example `C:\Users\jason\AppData\Local\Programs\Ollama\ollama.exe`). Files in the sibling Ollama folder must not become governed manifests, required knowledge inputs, or peer-review export contents unless intentionally converted into governed repo artifacts first.

**Authoring source discipline:** `scripts/ollama_authoring_agent.py` loads only manifest-declared repo files. Optional `--include` files must already be listed under `allowed_optional_documents` in the selected manifest. If `--manifest` is overridden, it must still match the selected mode family (`editorial`/`technical` -> editorial manifest family; `narration`/`book` -> narration manifest family). Raw discussion, undeclared web material, and private notes outside the repo are not valid required knowledge. Non-dry-run authoring commands now also write a reviewable `.run_record.json` file containing mode, manifest, optional include paths, tool identity, and timestamp so the drafting run is auditable under `AMD-2026-014`.

**Optional voice assets:** local media such as a Voicebox voice-clone archive may be documented or used later as runtime narration support, but they are not governed knowledge inputs by default and must not be added to required manifests as if they were repo truth. If operators keep Voicebox near this workspace, use a sibling local folder such as `C:\Apps\github_repos\Voicebox\`, not a path inside `aios-governing-docs`. Absolute local Voicebox paths, profiles, renders, and prompts must not appear in governed manifests, required knowledge inputs, or peer-review exports.

**Isolated execution demonstration (MVP, non-normative):** After planning artifacts exist, `py -3 scripts/run_isolated_execution_demo.py` creates `reviews/<slug>/execution/` and can attach a **git worktree** + **npm** validation on the product repo. See **[AIOS-EXEC-DEMO-001](reference/implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md)** Annex E.

### Optional automation (portfolio + pipeline)

These scripts **do not** replace manual triangulated review for ratification; they are operator tooling. Generated outputs are listed in `.gitignore` (`portfolio_reviews/`, `reviews/**/automated_runs/`, `reviews/**/LAST_RUN_POINTER.json`).

**Corpus / portfolio review** (single OpenAI call over a registry digest):

```bash
cd scripts
py -3 governance_portfolio_review.py --dry-run
py -3 governance_portfolio_review.py
```

**Automated peer-review → amendment loop** (rounds 1–2 via `peer_review`, then optional OpenAI revision; same API keys as `peer_review.py`):

```bash
cd scripts
py -3 automated_review_pipeline.py --document amendments/AMD-2026-007.md --dry-run
py -3 automated_review_pipeline.py --document amendments/AMD-2026-007.md
# or: py -3 automated_review_pipeline.py --next
```

---

## Source Analysis & Amendments

### Analyze External Source Material

```bash
py scripts/analyze_source.py path/to/article.md --name my_analysis
```

This quarantines the source, sends it to all 3 models, and saves impact reports.

### Check Quarantine Status

```bash
py scripts/analyze_source.py --status my_analysis
```

### Clear or Reject a Source

```bash
py scripts/analyze_source.py --clear my_analysis
py scripts/analyze_source.py --reject my_analysis
```

### Synthesize action plan (from three impact reports)

After `impact_report_*.md` exist under `sources/<name>/`:

```bash
py scripts/synthesize_action_plan.py AMD-2026-a10b9a
```

Writes `sources/<name>/action_plan.json`. Review and approve actions in the **Action plan** surface in the voice UI, or `PUT /v1/sources/<name>/action-plan`.

### Execute approved actions

Runs whitelisted automation (`registry_regenerate`, `schema_extract`) and logs manual steps:

```bash
py scripts/execute_action_plan.py AMD-2026-a10b9a
py scripts/execute_action_plan.py AMD-2026-a10b9a --dry-run
```

Append-only log: `sources/<name>/execution_log.jsonl`. API: `POST /v1/sources/<name>/action-plan/execute`.

---

## Conflict Detection

Scan all documents for contradictions:

```bash
py scripts/conflict_detector.py
py scripts/conflict_detector.py --output json
py scripts/conflict_detector.py --document-id AIOS-CORE-001
```

---

## Registry

Regenerate the document registry after changes:

```bash
py scripts/registry_generator.py
```

This produces both `DOCUMENT_REGISTRY.md` and `DOCUMENT_REGISTRY.json`.

---

## MCP Server (for AI Agents)

Start the governance MCP server:

```bash
py scripts/governance_mcp_server.py
```

Or configure in Cursor's MCP settings for auto-start (see below).

### Available Tools

| Tool | Description |
|------|-------------|
| `list_documents` | List documents with optional status/category filters |
| `get_document` | Retrieve a document by ID |
| `get_document_versions` | List archived versions |
| `search_documents` | Full-text search |
| `list_primitives` | List primitive schemas |
| `get_primitive_schema` | Get JSON schema for a primitive |
| `get_glossary` | Canonical glossary from the Manifesto |
| `check_compliance` | Validate primitives against schemas |
| `check_conflicts` | Scan for cross-document conflicts |
| `propose_amendment` | Submit an amendment proposal |
| `get_amendment_status` | Check amendment status |
| `get_source_status` | Check source quarantine status |

---

## REST API (for CI/CD, Dashboards, SDKs)

Start the REST API:

```bash
py scripts/governance_api.py
```

Swagger UI: [http://localhost:8100/docs](http://localhost:8100/docs)
OpenAPI spec: [http://localhost:8100/openapi.json](http://localhost:8100/openapi.json)

### Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/documents` | List documents |
| GET | `/v1/documents/{id}` | Get document by ID |
| GET | `/v1/documents/search?q=` | Search documents |
| GET | `/v1/primitives` | List primitive schemas |
| GET | `/v1/primitives/{type}` | Get schema |
| GET | `/v1/glossary` | Canonical glossary |
| POST | `/v1/compliance/primitive` | Validate a primitive |
| POST | `/v1/compliance/kit` | Validate a Kit manifest |
| GET | `/v1/conflicts` | Run conflict detection |
| POST | `/v1/amendments` | Propose amendment |
| GET | `/v1/amendments/{id}` | Amendment status |

### Authentication

Set in `.env`:
```
GOVERNANCE_API_KEY_READ=your_read_key
GOVERNANCE_API_KEY_WRITE=your_write_key
```

Pass via `X-API-Key` header. Read endpoints use the read key; mutation endpoints (amendments) require the write key. If no keys are set, all endpoints are open (local development).

---

## SDK Generation

Export the OpenAPI spec and generate client SDKs:

```bash
# Start the API server, then:
curl http://localhost:8100/openapi.json > openapi/governance-api.json

# Python SDK
openapi-generator-cli generate -i openapi/governance-api.json -g python -o sdk/python --additional-properties=packageName=aios_governance

# TypeScript SDK
openapi-generator-cli generate -i openapi/governance-api.json -g typescript-fetch -o sdk/typescript
```

---

## Git and GitHub

**Merge policy:** Prefer **pull requests** into `main` and keep **required status checks** (for example the Governance integrity workflow / `pytest`) **required** in branch protection so merges are gated by CI.

**Solo maintainer:** GitHub does not allow a PR author to **approve** their own pull request when **required reviews** are on. For this repository, treat **GitHub human approval** as **optional** (off or **0** required approvals): merge after **CI passes**, while still completing **AIOS** review and ratification **in-repo** (peer review under `reviews/`, thresholds, ratification processor output per **AMD-2026-005**). Skipping GitHub approval does **not** bypass in-repo governance artifacts.

**Larger teams** may still use GitHub required reviews for access or audit; that is separate from **AMD-2026-005** thresholds and ratification.

**Organization rulesets** may override branch protection at the repo; if **Settings** cannot be edited, adjust rules at the **org** level.

**PR template:** New pull requests use `.github/pull_request_template.md` (summary, governance reminder, checklist).

---

## Git Integration

The lifecycle script auto-commits and tags on ratification:

```
ratify: AIOS Technical Manifesto v1.0.0
Tag: v1.0.0-aios-technical-manifesto-platform-economics
```

Initialize the repo if not already done:

```bash
cd <repository root>
git init
git add .
git commit -m "Initial governance system setup"
```

---

## Testing

Run the test suite:

```bash
cd <repository root>
py -m pytest tests/ -v
```

---

## Folder Structure

```
.
├── core/                  # Manifesto, Constitution, MPOA
├── specifications/        # NodeContract, PolicyRecord, AIP, CLI Guide, agents.md
│   └── schemas/           # Extracted JSON schemas (.json files)
├── commercial/            # Marketplace Terms
├── amendments/            # Formal amendments
├── reviews/               # Peer reviews organized by document and round
├── sources/               # External source analyses with quarantine
├── research/              # Genesis research reports
├── reference/             # Development planning docs, UI philosophy
├── archive/               # Old versions, checkpoints, original files
├── prompts/               # Meta-prompts for AI workflows
├── templates/             # Document, review, rubric, amendment templates
├── scripts/               # Python automation + MCP server + REST API
├── tests/                 # Pytest unit tests
├── .env                   # API keys (not committed)
├── .gitignore
├── CHANGELOG.md
├── DEVELOPER.md           # This file
├── DOCUMENT_REGISTRY.md   # Auto-generated document index
├── DOCUMENT_REGISTRY.json # Machine-readable registry
├── README.md              # System overview
├── STYLE_GUIDE.md         # Writing conventions
└── introduction.md        # Document plan
```

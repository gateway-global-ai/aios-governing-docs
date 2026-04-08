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

**Product implementation snapshot (Workspace / integration reviews):** Regenerate the concatenated **ai-os-voice-interface** excerpt, then pass **`--product-context`** so reviewers see intents, MCP mapping, and control-plane code — see [`reference/knowledge_base/README.md`](../reference/knowledge_base/README.md).

```bash
py -3 scripts/generate_product_context_bundle.py
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-006.md --round 1 --smart-context --product-context
```

**Pre-ratification planning (local Ollama, Architect → UI):** Build a merged knowledge bundle, then run planning agents that write `reviews/<slug>/planning/ARCHITECT_PLAN.md` and `UI_PLAN.md`. See [`reference/knowledge_base/agents/README.md`](reference/knowledge_base/agents/README.md) and **[AIOS-AMD-PLAN-001](reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** (`py -3 scripts/build_agent_kb.py`, `py -3 scripts/ollama_planning_agent.py`).

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

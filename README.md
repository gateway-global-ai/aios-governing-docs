# AIOS Governing Documents

The authoritative governance framework for the Gateway Global AI Operating System (AIOS).

AIOS is a **governed execution environment** where intent, policy, and system behavior are anchored in **ratified documents**—implementations MUST conform; they do not invent substitute rules at runtime.

---

## Purpose

This repository is the **constitutional kernel of AIOS**.

It defines:

- system architecture ([Technical Manifesto](core/technical_manifesto.md))
- governance and ratification ([Governance Constitution](core/governance_constitution.md))
- liability and economics ([MPOA](core/master_platform_operating_agreement.md))
- **binding** specifications for runtime behavior (`specifications/`)
- formal **amendments** that evolve the system over time (`amendments/`)

All product implementations MUST conform to the rules defined here.

---

## System model

AIOS operates as a governed system-of-systems:

```
Intent → Contract → State → Surface → Action → Audit
```

This repository defines the **contract and policy layer** (documents, specs, amendments, registry).

Product repositories (for example the voice interface) **implement** these rules; they do not override ratified governance.

---

## Repository structure

```
governing_docs/
├── .env                         # API keys (DeepSeek, Gemini, OpenAI) — not committed
├── README.md                    # This file
├── DEVELOPER.md                 # How to run scripts, APIs, lifecycle, registry
├── CHANGELOG.md                 # Notable changes to the document set
├── STYLE_GUIDE.md               # Writing conventions
├── DOCUMENT_REGISTRY.md         # Auto-generated master index (human-readable)
├── DOCUMENT_REGISTRY.json       # Machine-readable registry
├── introduction.md              # Roadmap and document relationships
│
├── core/                        # Foundational trilogy
│   ├── technical_manifesto.md
│   ├── governance_constitution.md
│   └── master_platform_operating_agreement.md
│
├── specifications/              # Binding technical specifications (examples)
│   ├── NodeContract.md
│   ├── PolicyRecord.md
│   ├── AgentIntegrationProtocol.md      # AIOS-SPEC-003 (AIP)
│   ├── CLIDeveloperGuide.md
│   ├── agents.md
│   ├── SecuritySandboxingModel.md
│   ├── UIComponentRegistryStandard.md   # AIOS-SPEC-006
│   └── GoogleWorkspaceIntegrationGovernance.md  # AIOS-SPEC-007
│
├── commercial/                  # Legal & marketplace
│   ├── MarketplaceTermsOnboarding.md
│   └── DataPrivacyComplianceAddendum.md
│
├── amendments/                  # Formal amendments
│   ├── ammendment_google.md
│   ├── AMD-2026-005.md          # Workspace model & governed interface surfaces (ratified)
│   └── AMD-2026-006.md          # Google Workspace governed integration plane (draft)
│
├── reference/                   # Council manual, roadmap, UX notes, planning docs
├── reviews/                     # Peer reviews by document and round
├── sources/                     # External source analyses & amendment source packages
├── research/                    # Genesis research (archive)
├── archive/                     # Superseded checkpoints
├── amendment_workflow/          # Templates for amendment automation
├── prompts/                     # Meta-prompts (peer review, revision, ratification processor, …)
├── scripts/                     # Python: peer review, lifecycle, registry, API, MCP server, …
├── templates/                   # Document, amendment, rubric templates
└── tests/                       # Pytest
```

---

## Core documents (supremacy)

| Document | Focus | Supremacy domain |
|----------|--------|------------------|
| [Technical Manifesto](core/technical_manifesto.md) | Architecture, determinism, platform primitives | System architecture |
| [Governance Constitution](core/governance_constitution.md) | Council, legislative/judicial process, amendments | Governance process |
| [MPOA](core/master_platform_operating_agreement.md) | Economics, liability, data sovereignty | Liability & economics |

**Supremacy clause:** If documents conflict, the **Constitution** governs governance process, the **MPOA** governs liability and economics, and the **Manifesto** governs architecture—see cross-references in each core document.

---

## Specifications

Specifications define **binding** interfaces and behaviors for implementations (agents, UI, integrations).

Examples:

| ID | Document |
|----|----------|
| AIOS-SPEC-003 | [Agent Integration Protocol](specifications/AgentIntegrationProtocol.md) |
| AIOS-SPEC-006 | [UI Component Registry Standard](specifications/UIComponentRegistryStandard.md) |
| AIOS-SPEC-007 | [Google Workspace Integration Governance](specifications/GoogleWorkspaceIntegrationGovernance.md) |

Implementations MUST comply with applicable SPECs; updates follow the amendment and ratification process.

---

## Amendments

Amendments are the governed mechanism for changing behavior described in core docs and specifications.

Examples:

- [AMD-2026-005](amendments/AMD-2026-005.md) — Workspace model & governed interface surfaces (ratified)
- [AMD-2026-006](amendments/AMD-2026-006.md) — Google Workspace governed integration plane (draft)

---

## Governance lifecycle

The **binding path** for governed documents (including amendments and many specifications) is:

```
Author validation
  → Triangulated peer review
  → Threshold evaluation (composite ≥ 3.5, no dimension below 3)
  → Ratification (per tier / Constitution)
```

**AMD-2026-005:** There is **no separate post–peer-review human audit** as a gating step solely to satisfy workflow; constitutional and Council-controlled gates still apply where already required.

Automation in `scripts/` (peer review, revision logs, registry) **supports** this lifecycle; it does not replace human ratification or the authority of ratified text.

For **core trilogy** documents, the `lifecycle.py` orchestrator may still use an extended multi-round pipeline (draft → Round 1 → revision → Round 2 → ratification). That pipeline is an **implementation** of review and revision—not a separate “law” from the governance path above.

---

## Integration governance

External systems (e.g. Google Workspace) MUST NOT be wired as flat tool surfaces in product UIs or agents.

They integrate as **governed execution substrates**:

```
Intent layer → Integration control plane → Adapter → External system
```

Requirements include intent routing, policy before execution, audit records, and **Layer 1 / Layer 2** scope classification per **AIOS-SPEC-007**.

---

## Document registry

[`DOCUMENT_REGISTRY.md`](DOCUMENT_REGISTRY.md) and [`DOCUMENT_REGISTRY.json`](DOCUMENT_REGISTRY.json) are generated from document front matter.

Regenerate after adding or changing governed files:

```bash
cd scripts
py registry_generator.py
```

---

## Automation (tools, not governance)

Scripts under `scripts/` assist human workflows: triangulated peer review, revision, source analysis, lifecycle orchestration, conflict detection, REST API, MCP server, registry generation, and more.

See **[DEVELOPER.md](DEVELOPER.md)** for setup (`py -m pip install -r requirements.txt`), `.env` keys, and commands.

| Task | Command |
|------|---------|
| Peer review (Round 1) | `py peer_review.py <path-to-doc.md> --round 1` |
| Revise after review | `py revise_document.py <path-to-doc.md>` |
| Full lifecycle (core doc) | `py lifecycle.py core/technical_manifesto.md` |
| Analyze external source | `py analyze_source.py path/to/article.md --name my_analysis` |
| Regenerate registry | `py registry_generator.py` |

These tools do **not** replace ratification or the supremacy of written documents.

---

## Key rules

1. No substitute for governing documentation: runtime behavior must trace to ratified or draft-in-process artifacts as appropriate for tier.
2. No bypass of policy and audit for externally visible or high-risk actions (including integrations—SPEC-007).
3. Material changes go through amendment and SPEC updates with peer review and thresholds as required.
4. Ratified documents and binding SPECs apply across repositories; product code conforms—it does not redefine governance.

---

## Relationship to product repositories

| This repo (`governing_docs`) | Product repos (e.g. voice interface) |
|------------------------------|--------------------------------------|
| Defines rules, specs, amendments, registry | Implements UX, APIs, adapters under those rules |
| Source of truth for “what is allowed” | Must not override ratified governance |

---

## Getting started

1. **Install dependencies:** `cd scripts && py -m pip install -r requirements.txt`
2. **Configure `.env`:** `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY` (see [DEVELOPER.md](DEVELOPER.md) for optional merges with app `.env.local`)
3. **Browse the index:** [DOCUMENT_REGISTRY.md](DOCUMENT_REGISTRY.md)
4. **Follow conventions:** [STYLE_GUIDE.md](STYLE_GUIDE.md)
5. **Run workflows:** peer review, lifecycle, or registry as needed

---

*AIOS is not only application software—it is a governed system for defining and operating compliant systems.*

*Last updated: April 2026.*

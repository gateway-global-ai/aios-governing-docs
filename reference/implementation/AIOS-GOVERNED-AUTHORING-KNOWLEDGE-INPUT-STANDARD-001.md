---
document_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
version: 0.1.2
status: draft
category: reference
title: Governed authoring knowledge inputs and bounded author-like drafting
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-JT-EDITORIAL-STYLE-CARD-001
    title: JT editorial style card
  - doc_id: AIOS-JT-NARRATION-STYLE-CARD-001
    title: JT narration style card
  - doc_id: AIOS-JT-AUTHORING-MODE-BOUNDARIES-001
    title: JT authoring modes and identity boundaries
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AMD-2026-009
    title: Intent-Scoped Web Retrieval and Governed Website Review
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Reference standard for declared author-like inputs, manifests, bounded author identity surfaces, and reviewable run-record discipline. Not a ratified amendment.
---

# AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001

## Purpose

Define a governed input standard for bounded author-like drafting in this repository.

This standard exists so style-guided drafting can be:

- declared
- traceable
- bounded by repo truth
- separated from governance authority

## Scope

This standard covers:

- style cards
- authoring manifests
- authoring mode definitions
- source-document discipline
- bounded author identity rules
- local Ollama authoring command surfaces

This standard does not:

- ratify doctrine
- replace architect or UI planning flows
- replace committee, peer review, kernel review, or ratification
- authorize silent doctrine mutation

## Core rule

Author-like drafting inputs are allowed only as governed knowledge inputs. They are not a freeform identity simulation.

## Required artifacts

The bounded authoring surface currently consists of:

- `reference/knowledge_base/agents/style/JT_EDITORIAL_STYLE_CARD.md`
- `reference/knowledge_base/agents/style/JT_NARRATION_STYLE_CARD.md`
- `reference/knowledge_base/agents/style/JT_AUTHORING_MODE_BOUNDARIES.md`
- `reference/knowledge_base/agents/style/JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `reference/knowledge_base/agents/style/JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `reference/knowledge_base/agents/style/JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `modelfiles/jt_authoring_agent.Modelfile`
- `scripts/ollama_authoring_agent.py`

## Mode model

Approved modes:

- `editorial`
- `narration`
- `technical`
- `book`

Mode behavior is bounded by:

- the selected manifest
- the selected style card family
- the mode definitions in `JT_AUTHORING_MODE_BOUNDARIES.md`

Manifest overrides must stay within the selected mode family:

- `editorial` and `technical` runs must use an `editorial` manifest family
- `narration` and `book` runs must use a `narration` manifest family

## Source-document discipline

### Allowed source classes

Author-like runs may use only documents that are:

- inside the governed repo root
- declared by manifest
- present on disk

Allowed classes include:

- amendments
- specifications
- reference and implementation notes
- knowledge-base snapshots and current-system research outputs
- style and mode-boundary artifacts

### Prohibited source classes

These must not become required knowledge until converted into governed repo artifacts:

- raw discussion
- private note collections outside the repo
- undeclared web material
- unpublished chat exports
- operator memory that is not written into a repo artifact

## Discussion-to-artifact conversion rule

Discussion may motivate drafting work, but it does not become required knowledge until it is converted into a stable repo artifact with a governed path.

This means:

- raw discussion may be operator context
- converted repo artifacts may be declared knowledge
- architect/UI/authoring lanes must not silently treat discussion as doctrine

## Author identity boundary

The bounded author-like surface may reproduce tone, cadence, structure, and rhetorical habits reflected in committed materials. It must not claim:

- personal memory
- unpublished strategic intent
- private conversation history
- authority to speak for governance beyond the declared task

## Relationship to architect and UI planning

Architect and UI planning lanes remain governed draft-producing lanes under **AIOS-AMD-PLAN-001** and **AIOS-AMENDMENT-INTAKE-SCAFFOLD-001**.

If architect or UI runs consume author-like inputs:

1. those inputs must be declared by manifest
2. the run must remain template-bound and reviewable
3. style inputs remain advisory
4. human verification remains mandatory

## Local Ollama command surface

### Model build

```bash
ollama create jt_authoring_agent -f modelfiles/jt_authoring_agent.Modelfile
```

### Governed authoring run

```bash
py -3 scripts/ollama_authoring_agent.py --mode editorial --prompt "Draft the requested piece." --dry-run
```

### Shell-first plan authoring run

```bash
py -3 scripts/ollama_authoring_agent.py --mode editorial --manifest reference/knowledge_base/agents/style/JT_EDITORIAL_SHELL_PLAN_REQUIRED_KNOWLEDGE_MANIFEST.yaml --prompt "Draft the shell-first governing plan." --output reviews/aios_shell_governing_document_and_artifact_plan_001/packet_2026-04-10/example_editorial_output.md
```

### Optional declared includes

Optional additional inputs must be listed under `allowed_optional_documents` in the selected manifest before they may be passed to the runner.

### Reviewable run record

Non-dry-run authoring commands write a `.run_record.json` artifact.

That run record records:

- selected mode
- selected manifest path
- optional include paths used for the run
- tool invocation identity
- reviewable timestamp
- output path when one exists

### Optional local voice assets

Local voice assets, such as a user-supplied Voicebox voice-clone archive, are runtime media assets only unless later promoted by explicit governance.

They may be:

- documented as optional local assets for narration or voice-output experiments
- supplied to future runtime tooling by explicit operator choice

They are not, by default:

- governed knowledge inputs
- required manifest documents
- doctrine artifacts
- evidence of author identity

If such an asset is referenced in tooling docs, it must be described as optional local runtime support only.

## Non-authority rule

Generated prose may recommend, explain, summarize, or draft. It may not:

- self-ratify
- self-amend
- self-approve architect or UI outputs
- bypass declared governance lanes

## Final precedence rule

If style guidance conflicts with declared repo truth, repo truth wins.

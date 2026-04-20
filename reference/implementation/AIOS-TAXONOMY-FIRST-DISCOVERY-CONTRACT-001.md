---
document_id: AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001
version: 0.1.0
status: draft
category: reference
title: Taxonomy-first discovery and knowledge assembly contract
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
  - doc_id: AIOS-REPO-TAXONOMY-001
    title: Intent-bearing repository taxonomy
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-SYSTEMS-AND-PLANNING-MANUAL-001
    title: Systems and planning manual for planner/knowledge-base restoration
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
note: Transitional process contract for replacing manual lane-specific knowledge packet curation with taxonomy-first discovery and explicit knowledge assembly.
---

# AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001

## Purpose

Define the missing contract between repository taxonomy, discovery, and knowledge-bundle assembly so local agents do not rely on hidden coordinator curation or role-level hard-coded source lists.

## Core rule

Taxonomy is first-class. Discovery is second. Knowledge assembly is third.

No planning, research, or drafting role should choose its governing knowledge inputs by undocumented habit, ad hoc operator memory, or role-prompt hard-coding.

## Required order

The required order is:

`declared taxonomy -> discovery scope -> discovered packet -> built knowledge bundle -> research lane -> drafting lane -> review lane`

## Taxonomy classes

A conformant discovery process **SHALL** resolve candidate inputs through explicit taxonomy classes rather than a flat list.

Minimum classes:

| Taxonomy class | Meaning |
|---|---|
| `constitutional_and_philosophy_root` | constitutional, philosophy, and root governance anchors |
| `target_authority` | the target amendment, specification, or reference artifact being revised or reviewed |
| `cross_document_authority` | ratified or draft governing documents that materially constrain the target |
| `implementation_authority` | implementation/reference documents that define how the target should operate |
| `runtime_evidence` | product evidence and snapshots, used only when the lane depends on runtime truth |
| `review_evidence` | prior peer reviews, review synthesis, gate reports, and revision logs |
| `taxonomy_and_process_authority` | taxonomy, planner, and packet-process rules that govern how the lane itself operates |
| `prohibited_source_class` | sources that must not enter the packet unless intentionally converted into governed artifacts |

## Discovery inputs

A discovery run **SHALL** begin from a `DISCOVERY_SCOPE.yaml` or equivalent declared scope artifact that identifies:

- target document path
- target document id
- target review slug
- desired lane type
- required taxonomy classes
- excluded taxonomy classes
- whether runtime evidence is allowed
- whether prior review evidence is required

The discovery scope defines **what classes to resolve**, not the final list of files.

## Discovery outputs

A conformant discovery lane **SHALL** produce, at minimum:

| Artifact | Purpose |
|---|---|
| `DISCOVERY_REPORT.md` | human-readable report of what classes were searched, what was selected, and why |
| `DISCOVERED_KNOWLEDGE_PACKET.yaml` | the explicit packet generated from taxonomy-guided discovery |
| `DISCOVERY_BUILD_MANIFEST.json` or equivalent | machine-readable record of the packet assembly inputs |

These outputs make discovery reviewable and repeatable.

## Knowledge assembly rule

The knowledge bundle builder **SHALL** consume an explicit packet such as `DISCOVERED_KNOWLEDGE_PACKET.yaml`.

The builder **SHALL NOT** infer authority directly from a role name or a prompt file.

## Role boundary rule

The discovery role, research role, drafting role, and review role **SHALL** remain distinct.

At minimum:

- the discovery role selects eligible sources by taxonomy class
- the research role synthesizes what the discovered packet means
- the drafting role proposes document changes from the discovered packet plus research output
- the review role critiques the draft and routes peer review

No one role should silently own all four functions if the system is being benchmarked or improved.

## Non-conformant patterns

The following are non-conformant:

- role prompts that carry hidden source lists
- lane packets assembled only from coordinator memory
- research lanes that browse arbitrary files without a declared discovery scope
- drafting lanes that consume undeclared review artifacts
- runtime evidence loaded by default when the lane does not depend on runtime truth
- amendment-specific manifests becoming permanent replacements for taxonomy-first discovery

## Transitional allowance

Lane-specific manifests may still exist during transition.

They are allowed only when all of the following are true:

1. taxonomy-first discovery has not yet been implemented for that lane
2. the manifest is explicit and reviewable
3. the manifest is treated as a temporary scaffold rather than the final system model
4. the lane records that discovery remains incomplete

## Minimum conformance questions

Before trusting a lane, a reviewer should be able to answer:

1. What taxonomy classes were required?
2. What discovery scope was declared?
3. What packet did discovery produce?
4. What bundle was built from that packet?
5. Which role produced research?
6. Which role produced drafting?
7. Which human or peer-review seam remains required?

## Intended immediate use

This contract exists to guide the next repair slice:

- add taxonomy-first discovery artifacts to amendment planning lanes
- stop treating amendment-specific manifests as the steady-state end design
- route local Ollama research and drafting through discovery-built packets rather than coordinator-selected source lists

---

*Draft reference — AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001.*

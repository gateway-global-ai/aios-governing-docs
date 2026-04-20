---
document_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
version: 0.1.0
status: draft
category: reference
title: Pre-architecture discovery agent for five-pass system research
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-DISCOVER-AGENT-PROCESS-001
    title: Discover-agent process for taxonomy-driven knowledge assembly
  - doc_id: AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001
    title: Taxonomy-first discovery and knowledge assembly contract
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-RESEARCH-PACK-REPORT-SET-ANALYSIS-001
    title: Analysis of the Cursor research-pack report set and committee posture
note: Defines the five-pass discovery suite as a governed pre-architecture lane that should run before architect planning when current-system structure must be mapped first.
---

# AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001

## Purpose

Define the pre-architecture discovery agent as a governed research lane that runs before architect planning when the system must first discover current runtime structure, implicit capability surfaces, governance breaches, registry candidates, or control-plane coverage.

## Core rule

When a lane depends on current-system structure rather than doctrine alone, pre-architecture discovery should run before the architect planner is asked to produce schemas, routes, and storage/state recommendations.

## Why this exists

Taxonomy-first source selection and explicit packet assembly remain necessary, but they are not always sufficient.

Some lanes also need a structured current-system discovery pass before architecture planning begins.

That pre-architecture role should not be collapsed into the architect planner itself.

## The five-pass discovery suite

The governed pre-architecture discovery suite is:

1. architecture cartography
2. implicit capability extraction
3. governance breach audit
4. registry migration planning
5. control-plane coverage audit

## Role of each pass

| Pass | Purpose | Primary output |
|---|---|---|
| 1. architecture cartography | map the runtime spine, live path, and control-plane candidates | `01_architecture_cartography.md` |
| 2. implicit capability extraction | inventory implicit views, actions, routes, and skills | `02_implicit_capability_extractor.md` |
| 3. governance breach audit | identify bypasses, hidden routing, prompt-as-policy, and validation failures | `03_governance_breach_audit.md` |
| 4. registry migration planning | decide what should become registries and in what order | `04_registry_migration_planner.md` |
| 5. control-plane coverage audit | measure what is already governed versus still implicit | `05_control_plane_coverage_audit.md` |

## When it should run

Pre-architecture discovery should run when any of the following are true:

- the architect lane must reason about current runtime behavior
- schemas, routes, or storage/state are incomplete or disputed
- the system may contain hidden routing, prompt-driven authority, or duplicate control planes
- a planning lane is trying to recover from drift, contamination, or undocumented product behavior
- a current-system map is needed before architecture review can be trusted

## Required inputs

The pre-architecture discovery agent should begin from:

- `DISCOVERY_SCOPE.yaml`
- declared taxonomy and process authority
- current product evidence when allowed by scope
- the research-pack method contract in `reference/knowledge_base/cursor_research_pack.md`

## Required outputs

When the discovery scope declares the pre-architecture profile, the lane should produce:

- `DISCOVERY_REPORT.md`
- `DISCOVERED_KNOWLEDGE_PACKET.yaml`
- `pre_architecture/01_architecture_cartography.md`
- `pre_architecture/02_implicit_capability_extractor.md`
- `pre_architecture/03_governance_breach_audit.md`
- `pre_architecture/04_registry_migration_planner.md`
- `pre_architecture/05_control_plane_coverage_audit.md`

The five-pass outputs are advisory discovery artifacts. They do not replace doctrine, ratify architecture, or self-approve the architect lane.

## Downstream rule

The architect planner should consume:

1. the discovered packet
2. the pre-architecture discovery outputs when present
3. the declared governing packet

The architect planner should not be asked to rediscover the system from scratch when this discovery lane was required but skipped.

## Boundary rule

The pre-architecture discovery agent:

- may map and critique the current system
- may propose registry migration priorities
- may not draft ratified doctrine
- may not self-approve architect conclusions
- may not replace human verification

## Review rule

The pre-architecture discovery suite should be reviewed before the architect lane is treated as above the line.

At minimum, a reviewer should be able to inspect:

- what discovery scope was declared
- what product evidence was allowed
- what each of the five passes concluded
- what discovered packet the architect lane actually consumed

## Intended system role

This discovery suite should be treated as the governed pre-architecture discovery agent for lanes that need current-system mapping before architecture planning can be trusted.

---

*Draft reference — AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001.*

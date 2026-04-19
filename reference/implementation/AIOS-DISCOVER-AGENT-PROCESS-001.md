---
document_id: AIOS-DISCOVER-AGENT-PROCESS-001
version: 0.1.1
status: draft
category: reference
title: Discover-agent process for taxonomy-driven knowledge assembly
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001
    title: Taxonomy-first discovery and knowledge assembly contract
  - doc_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
    title: Pre-architecture discovery agent for five-pass system research
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
  - doc_id: AIOS-AGENT-AND-TOOLCHAIN-ROSTER-001
    title: Agent, role, and toolchain roster for the restored planner system
note: Operational process spec for introducing a first-class discover lane before research and drafting.
---

# AIOS-DISCOVER-AGENT-PROCESS-001

## Purpose

Define the repeatable discover-agent loop that should run before local research, drafting, or architect-planning lanes so knowledge assembly is taxonomy-driven and reviewable.

## Process summary

The discover-agent loop is:

1. read `DISCOVERY_SCOPE.yaml`
2. resolve taxonomy classes
3. identify eligible repo artifacts
4. run pre-architecture discovery when the scope requires current-system mapping before architect planning
5. emit `DISCOVERED_KNOWLEDGE_PACKET.yaml`
6. emit `DISCOVERY_REPORT.md`
7. freeze the packet for downstream architect, research, and drafting lanes

## Role separation

| Role | Output | Must not do |
|---|---|---|
| discover agent | `DISCOVERY_REPORT.md`, `DISCOVERED_KNOWLEDGE_PACKET.yaml`, and optionally the five-pass pre-architecture suite | draft amendment text or self-review the target |
| research agent | `LOCAL_RESEARCH_REPORT.md` | choose hidden packet inputs outside the discovered packet |
| drafting agent | `DRAFT_AMENDMENT_PROPOSAL.md` | self-ratify or replace review |
| reviewer / coordinator | packet acceptance, comparison, routing | silently rewrite discovery and drafting history |

## Required artifacts

Each lane that uses discovery should own:

- `DISCOVERY_SCOPE.yaml`
- `DISCOVERY_ASSIGNMENT.md`
- `DISCOVERY_REPORT.md`
- `DISCOVERED_KNOWLEDGE_PACKET.yaml`
- `LOCAL_RESEARCH_REPORT.md`
- `DRAFT_AMENDMENT_PROPOSAL.md`

When the lane requires pre-architecture discovery, it should also own:

- `pre_architecture/01_architecture_cartography.md`
- `pre_architecture/02_implicit_capability_extractor.md`
- `pre_architecture/03_governance_breach_audit.md`
- `pre_architecture/04_registry_migration_planner.md`
- `pre_architecture/05_control_plane_coverage_audit.md`

## Discovery scope contract

`DISCOVERY_SCOPE.yaml` should declare:

- `target_document_id`
- `target_document_path`
- `review_slug`
- `lane_kind`
- `discovery_profile`
- `required_taxonomy_classes`
- `optional_taxonomy_classes`
- `prohibited_source_classes`
- `allow_runtime_evidence`
- `require_review_evidence`
- `notes`

## Discover-agent assignment rule

`DISCOVERY_ASSIGNMENT.md` should instruct the local agent to:

- resolve the declared taxonomy classes
- prefer ratified and directly constraining documents first
- include runtime evidence only when the scope allows it
- include prior review evidence only when the scope requires it
- run the five-pass pre-architecture suite when the scope declares that profile
- cite exact repo-relative paths for every included artifact
- refuse invented review identifiers or symbolic handles that are not present on disk
- explain inclusions and exclusions
- write an explicit discovered packet rather than prose-only recommendations

## Downstream rule

Architect, research, and drafting lanes should consume the discovered packet, not the original scope.

That means:

- discovery decides what is eligible
- pre-architecture discovery maps what exists now when current-system structure matters
- architect decides what structure should be proposed from the discovered evidence
- research decides what is important
- drafting decides what to change

## Pre-architecture discovery mode

When `DISCOVERY_SCOPE.yaml` declares `discovery_profile: pre_architecture_five_pass`, the discovery lane should run the governed five-pass research suite before architect planning begins.

That suite is:

1. architecture cartography
2. implicit capability extraction
3. governance breach audit
4. registry migration planning
5. control-plane coverage audit

This suite exists so architect planning does not have to discover, critique, and redesign the system in one collapsed act.

## Transitional local-Ollama surface

Until a dedicated discover runner exists, a local wrapper may orchestrate:

- `discovery`
- `research`
- `draft`

through bounded local authoring runs, provided:

- each step has its own assignment file
- each step writes its own output file
- each step writes its own run record
- the review lane still remains separate

## Acceptance test

The process is working only if a reviewer can inspect one lane and determine:

- why each source was selected
- what class it belongs to
- whether pre-architecture discovery was required
- what the five-pass discovery suite concluded when that profile was used
- what was excluded
- what packet downstream lanes actually consumed
- which local model run produced each artifact

## Immediate implementation target

The first implementation slice should:

1. add discovery templates under `templates/governance_system/`
2. add discovery artifacts to active planning lanes
3. treat the five-pass research family as the governed pre-architecture discovery profile where needed
4. extend the local wrapper to support a `discovery` step
5. treat amendment-specific direct manifests as temporary scaffolds only

---

*Draft reference — AIOS-DISCOVER-AGENT-PROCESS-001.*

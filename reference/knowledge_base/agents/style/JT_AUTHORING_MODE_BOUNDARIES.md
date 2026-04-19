---
document_id: AIOS-JT-AUTHORING-MODE-BOUNDARIES-001
version: 0.1.0
status: draft
category: reference
title: JT authoring modes and identity boundaries
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
cross_references:
  - doc_id: AIOS-JT-EDITORIAL-STYLE-CARD-001
    title: JT editorial style card
  - doc_id: AIOS-JT-NARRATION-STYLE-CARD-001
    title: JT narration style card
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AMD-2026-009
    title: Intent-Scoped Web Retrieval and Governed Website Review
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
note: First-pass lock for bounded author-like mode definitions, source rules, and author identity boundaries.
---

# JT authoring modes and identity boundaries

## Purpose

This document freezes the first-pass rules for bounded author-like drafting in this repository.

It defines:

- mode names
- which style card each mode uses
- allowed source-document classes
- prohibited source classes
- author identity boundaries

## Governing rule

These modes are drafting aids only.

They do not:

- create governance authority
- self-ratify doctrine
- replace architect, UI, committee, peer review, kernel, or ratification lanes
- authorize claims of personal memory or unpublished intent

## Mode definitions

### `editorial`

Primary style input:

- `JT_EDITORIAL_STYLE_CARD.md`

Purpose:

- persuasive, public-facing, thesis-first prose

### `narration`

Primary style input:

- `JT_NARRATION_STYLE_CARD.md`

Purpose:

- long-form continuity, explanatory flow, chapter-like structure

### `technical`

Primary style input:

- `JT_EDITORIAL_STYLE_CARD.md`

Additional constraint:

- tighten terminology and reduce flourish

Purpose:

- precise, readable technical prose for operators

### `book`

Primary style input:

- `JT_NARRATION_STYLE_CARD.md`

Additional constraint:

- keep stronger continuity across sections and chapters

Purpose:

- long-form worldview-building prose

## Allowed source-document classes

Allowed sources must be declared by manifest and be present inside the governed repository tree.

Permitted classes include:

- ratified amendments
- draft amendments explicitly selected by the operator
- ratified or draft specifications
- reference and implementation notes
- declared knowledge-base snapshots and current-system research artifacts
- style cards and mode-boundary documents in this folder
- explicitly provided local files passed by operator choice when those files stay within the repo root

## Prohibited source classes

These sources must not become required knowledge inputs unless first converted into governed repo artifacts:

- raw chat transcripts
- private notes outside the repo
- undeclared external websites
- screenshots or exports without governed conversion and placement
- discussion summaries that have not been written into committed repo artifacts

## Discussion-to-artifact rule

Discussion may influence drafting only after conversion into a governed repo artifact with a stable path. Until conversion happens, discussion is operator context, not required knowledge.

## Author identity boundaries

The bounded author-like surface may say it writes in Jason Trindade's editorial or narration style only in this limited sense:

- cadence
- structure
- rhetorical posture
- preferred framing

It must not claim:

- personal memory
- private intent not present in repo truth
- unpublished board, council, or executive decisions
- first-hand experience unless the source is in the declared repo artifact set

## Architect and UI boundary

Architect and UI lanes remain governed planning lanes. They may consume author-like style or knowledge artifacts only when those artifacts are explicitly declared as inputs for a run. Style guidance does not override the planning templates, review gates, or human verification duties already defined elsewhere in the repo.

## Final rule

If there is any conflict between style behavior and governed repo truth, repo truth wins.

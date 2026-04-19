---
document_id: AIOS-PEER-REVIEW-EXPORT-STANDARD-001
version: 0.1.0
status: draft
category: reference
title: Peer-review export standard
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
cross_references:
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AMD-2026-005
    title: Workspace Model & Governed Interface Surfaces
  - doc_id: AMD-2026-014
    title: Governed Authoring Knowledge Inputs and Bounded Author-Like Drafting
note: Narrow implementation standard for self-contained governed peer-review evidence archives.
---

# AIOS-PEER-REVIEW-EXPORT-STANDARD-001

## Purpose

Define the standard for self-contained governed peer-review evidence archives.

This standard covers the export artifact only. It does not redesign review contents, runtime packaging, release packaging, or the broader review lifecycle.

## Naming contract

Zip artifact names use exactly:

`<artifact_class>__<document_id>__<date>.zip`

Rules:

- artifact class first
- canonical `document_id` second
- date third
- double underscores between segments

For self-contained review evidence archives, the artifact class is:

- `peer_review_export`

## Package vs export distinction

### `peer_review_export`

Means:

- a self-contained evidence archive
- useful to a reviewer without the author's working-tree layout
- includes the review package docs plus the files under review and minimum supporting docs
- the canonical review artifact for the external/manual review process

### `peer_review_package`

Means:

- a smaller helper bundle or package folder
- not automatically self-contained
- not interchangeable with `peer_review_export`

These two artifact classes must not be treated as the same thing.

## Source-of-truth hierarchy

The canonical source of truth remains the governed repo review package and governed source artifacts.

For external/manual review, the canonical review artifact is the self-contained `peer_review_export__<document_id>__<date>.zip`, produced from the preserved package-local build script.

## Archive layout rules

A governed peer-review export must:

- preserve the repo-relative tree at archive root
- use normalized `/` separators in archive entry names
- avoid wrapper directories that hide the repo-relative layout

## Minimum inclusion rules

A governed peer-review export includes:

- review package docs
- actual files under review
- minimum supporting docs needed to evaluate the package

The export excludes:

- secrets
- caches
- machine-local junk
- unrelated repo files
- hidden working-tree assumptions

## Portability rule

The export must be useful to a reviewer without requiring the author's working-tree layout. A reviewer should be able to extract the archive and inspect the evidence set directly from the archive-root repo-relative tree.

## Build-path rule

Future governed peer-review exports should preserve a clear build script path near the review package being exported. That build path must produce the self-contained `peer_review_export` artifact, not only a smaller helper package.

## Validation rule

At minimum, confirm:

- archive name matches the naming contract
- no archive entry contains `\`
- the repo-relative tree is present at archive root
- the intended review package docs and reviewed files are present

## Example

`reviews/peer_review_export__AMD-2026-014__2026-04-09.zip`

# Audit and change history — AMD-2026-015-ADD-003

## Gap being bridged

1. `AMD-2026-015` defined the CANI doctrine family.
2. `ADD-001` defined governed knowledge-artifact eligibility and discoverability discipline.
3. `ADD-002` defined the observation/recommendation schema surface.
4. A remaining gap persisted at the storage-contract layer:
   - where persisted CANI records belong
   - which persisted artifact classes need identity/status/events/handoff separation
   - how routing, supersession, and archival should be represented without creating runtime implementation

## Why an addendum is the correct instrument

The parent CANI doctrine already exists under `AMD-2026-015`.

The remaining problem is not a runtime implementation package.

It is a narrower bridge question inside the same family:

- persisted artifact locations
- persisted artifact taxonomy
- routing/supersession storage discipline

That is subordinate doctrine, not a new amendment family.

## Changes applied

| Area | Change |
|------|--------|
| Addendum doctrine | Added `AMD-2026-015-ADD-003` for persisted CANI artifact locations, asymmetric taxonomy choice, update/supersession rules, and routing-linkage storage discipline |
| Technical support | Added `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001` for governed location classes, observation/recommendation artifact shapes, lifecycle/supersession rules, and traceability metadata |
| Parent/package sync | Cross-referenced the addendum from the parent CANI amendment and aligned the CANI technical/schema support documents with the new storage-contract document |
| Tracker/review surface | Updated the amendment review tracker and created this review package |
| Export path | Added a package-local `build_peer_review_export.ps1` and canonical `peer_review_export__AMD-2026-015-ADD-003__2026-04-09.zip` build path so the review can be carried as one governed evidence archive |
| Changelog | Recorded the storage-contract bridge addendum and the review/export surface |

## Hard controls preserved

- persisted CANI records remain subordinate process artifacts, not authority
- no runtime telemetry implementation authority was added
- no browser instrumentation authority was added
- no event-store implementation authority was added
- no database migration authority was added
- no automatic recommendation execution authority was added
- no architect, UI, review, kernel, or ratification authority was collapsed

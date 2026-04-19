# Audit and change history — AMD-2026-015-ADD-002

## Gap being bridged

1. `AMD-2026-015` defined the CANI loop and recommendation boundary at the doctrine level.
2. `AMD-2026-015-ADD-001` bridged governed knowledge-artifact eligibility and registry/discoverability hygiene.
3. A remaining gap persisted at the field-model level:
   - how an observation signal should be shaped
   - how a recommendation record should be shaped
   - how those records route into existing governed lanes without being mistaken for authority

## Why an addendum is the correct instrument

The parent CANI doctrine already exists under `AMD-2026-015`.

The remaining problem is not a runtime platform package.

It is a narrower bridge question inside the same family:

- schema framing for observations
- schema framing for recommendations
- routing discipline into architect/UI/intake/review surfaces

That is subordinate doctrine, not a new amendment family.

## Changes applied

| Area | Change |
|------|--------|
| Addendum doctrine | Added `AMD-2026-015-ADD-002` for CANI observation-record framing, recommendation-record framing, routing targets, and explicit non-authority boundaries |
| Technical support | Added `AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001` for field-level observation, burden, fallback, backtrack, familiarity, recommendation, routing, and authority-status models |
| Parent/package sync | Cross-referenced the addendum from the parent CANI amendment and aligned the CANI technical standard with the new schema-support document |
| Tracker/review surface | Updated the amendment review tracker and created this review package |
| Export path | Added a package-local `build_peer_review_export.ps1` and canonical `peer_review_export__AMD-2026-015-ADD-002__2026-04-09.zip` build path so the review can be carried as one governed evidence archive |
| Changelog | Recorded the schema bridge addendum and the review/export surface |

## Hard controls preserved

- observation and recommendation records remain advisory by default
- no runtime telemetry implementation authority was added
- no browser instrumentation authority was added
- no event-store or database contract was added
- no automatic recommendation execution authority was added
- no architect, UI, review, kernel, or ratification authority was collapsed

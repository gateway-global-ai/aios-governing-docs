# Reviewer checklist — AMD-2026-015-ADD-003

## Addendum fit

- [ ] `AMD-2026-015` is the correct parent package for this storage-contract pass
- [ ] `ADD-003` is the correct next subordinate addendum identifier
- [ ] the addendum stays narrow and does not create a runtime persistence platform package

## Location and taxonomy

- [ ] the package defines governed repo location classes for persisted observation artifacts and recommendation artifacts
- [ ] the package justifies why observation persistence does not use the full four-file split by default
- [ ] the package justifies why recommendation persistence does use identity/status/events/handoff separation

## Update and supersession

- [ ] observation persistence is append-only
- [ ] observation correction is represented by successor/correction recording rather than silent deletion
- [ ] recommendation supersession and archival are represented explicitly in status and events
- [ ] stale or invalid recommendations are marked rather than deleted silently

## Routing and authority

- [ ] routing linkage is limited to existing governed lanes such as architect planning, UI planning, amendment intake, review preparation, or manual governance review
- [ ] the package does not authorize direct runtime action
- [ ] the package does not bypass human verification, peer review, kernel review, or ratification where those lanes apply

## Non-authority boundary

- [ ] no telemetry implementation authority is added
- [ ] no browser instrumentation authority is added
- [ ] no event-store implementation authority is added
- [ ] no database migration authority is added
- [ ] no automatic recommendation execution authority is added
- [ ] no autonomous self-improvement authority is added

## Implementation follow-through

- [ ] the amendment review tracker reflects the new `AMD-2026-015` addendum review state
- [ ] `DOCUMENT_REGISTRY.md` and `DOCUMENT_REGISTRY.json` include the new addendum and storage-contract document
- [ ] `build_peer_review_export.ps1` exists as the preserved build path for the self-contained export
- [ ] the self-contained export is named `peer_review_export__AMD-2026-015-ADD-003__2026-04-09.zip`
- [ ] archive entries use normalized `/` separators and preserve the repo-relative tree at archive root

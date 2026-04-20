# Reviewer checklist — AMD-2026-015-ADD-004

## Addendum fit

- [ ] `AMD-2026-015` is the correct parent package for this telemetry/intake-envelope pass
- [ ] `ADD-004` is the correct next subordinate addendum identifier
- [ ] the addendum stays narrow and does not create a second storage architecture

## Intake-envelope bridge

- [ ] the package defines a telemetry/intake envelope rather than persisted storage
- [ ] the package defines provenance fields
- [ ] the package defines sequence, batch, and causal-linkage fields
- [ ] the package defines normalization rules before persistence
- [ ] `payload_ref` is bounded to reviewable intake evidence or governed/review-package artifacts and does not become hidden authority
- [ ] normalization prose matches the controlled `normalization_state` model and does not use an undefined `unresolved` state

## Mapping boundary

- [ ] the package explicitly treats `ADD-003` as the canonical persisted artifact/storage contract
- [ ] the package maps observation envelopes into the existing observation-set artifacts
- [ ] the package maps recommendation envelopes into the existing recommendation packet artifacts
- [ ] the package does not define a new event-store location class or second persistence tree

## Non-authority boundary

- [ ] no runtime telemetry collector authority is added
- [ ] no browser instrumentation authority is added
- [ ] no runtime writer authority is added
- [ ] no event-store service authority is added
- [ ] no database table or migration authority is added
- [ ] no automatic recommendation execution authority is added
- [ ] no autonomous self-improvement authority is added

## Implementation follow-through

- [ ] the amendment review tracker reflects the new `AMD-2026-015` addendum review state
- [ ] `DOCUMENT_REGISTRY.md` and `DOCUMENT_REGISTRY.json` include the new addendum and intake-envelope support document
- [ ] `build_peer_review_export.ps1` exists as the preserved build path for the self-contained export
- [ ] the self-contained export is named `peer_review_export__AMD-2026-015-ADD-004__2026-04-09.zip`
- [ ] archive entries use normalized `/` separators and preserve the repo-relative tree at archive root

# Reviewer checklist — AMD-2026-015-ADD-001

## Addendum fit

- [ ] `AMD-2026-015` is the correct parent package for this bridge
- [ ] `ADD-001` is the correct next subordinate addendum identifier
- [ ] the addendum stays narrow and does not create a new platform package

## Bridge rules

- [ ] governed knowledge artifacts are eligible inputs only when they exist under governed repo paths
- [ ] eligibility requires stable path/doc identity and explicit declared-input selection
- [ ] registry/discoverability visibility is treated as part of governed input hygiene
- [ ] the addendum states the current scanner gap honestly rather than overstating prior tooling

## Declared-input discipline

- [ ] raw discussion is not treated as required knowledge
- [ ] declared inputs remain explicit and reviewable
- [ ] these artifacts do not become hidden default authority
- [ ] planning templates, repo truth, human verification, and governed review remain authoritative

## Non-authority boundary

- [ ] no telemetry authorization is added
- [ ] no event-store contract is added
- [ ] no browser instrumentation is added
- [ ] no runtime self-optimization authority is added
- [ ] no silent architect, UI, or doctrine mutation is authorized

## Implementation follow-through

- [ ] `scripts/registry_generator.py` now surfaces `reference/knowledge_base/articles/`
- [ ] `DOCUMENT_REGISTRY.md` and `DOCUMENT_REGISTRY.json` reflect the bridge surface
- [ ] the amendment review tracker reflects the new `AMD-2026-015` addendum review state
- [ ] `build_peer_review_export.ps1` exists as the preserved build path for the self-contained export
- [ ] the self-contained export is named `peer_review_export__AMD-2026-015-ADD-001__2026-04-09.zip`
- [ ] archive entries use normalized `/` separators and preserve the repo-relative tree at archive root

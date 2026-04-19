# Audit and change history — AMD-2026-015-ADD-001

## Gap being bridged

1. The CANI package created a governed knowledge article under `reference/knowledge_base/articles/`.
2. That article could exist on disk with front matter but remain outside the current registry scanner surface.
3. Architect/UI/Ollama-assisted declared-input discipline needed an explicit bridge between:
   - governed artifact existence
   - registry/discoverability visibility
   - declared-input eligibility

## Why an addendum is the correct instrument

The parent doctrine already exists under `AMD-2026-015`.

The remaining problem is not a new platform package. It is a narrow bridge question inside the existing package:

- when a governed knowledge artifact becomes eligible for agent use
- how discoverability must align with that use
- how non-authority protections remain intact

That is subordinate doctrine, not a new amendment family.

## Changes applied

| Area | Change |
|------|--------|
| Addendum doctrine | Added `AMD-2026-015-ADD-001` for governed knowledge-artifact eligibility, registry/discoverability bridge rules, and declared-input discipline |
| Parent/package sync | Cross-referenced the addendum from the parent CANI amendment, article, and technical standard |
| Registry alignment | Updated `scripts/registry_generator.py` to scan `reference/knowledge_base/articles/` so governed article artifacts become registry-visible |
| Tracker/review surface | Added the addendum to the amendment review tracker and created this review package |
| Export path | Added a package-local `build_peer_review_export.ps1` and canonical `peer_review_export__AMD-2026-015-ADD-001__2026-04-09.zip` build path so the review can be carried as one governed evidence archive |
| Changelog | Recorded the bridge addendum and the minimal registry-scanner alignment |

## Hard controls preserved

- knowledge artifacts remain non-authoritative by default
- declared input is still explicit and reviewable
- raw discussion still does not become required knowledge without repo conversion
- planning templates, repo truth, human verification, and governed review remain authoritative
- no telemetry, event-store, browser instrumentation, or runtime optimization authority was added

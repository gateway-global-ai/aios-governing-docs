# Audit and change history — amendment intake scaffold

## What was still open before this stage

1. The intake scaffold had no frozen artifact taxonomy under `reviews/<slug>/intake/`.
2. Committee authority and verification recording were still partly implicit.
3. The kernel lane contract was not frozen into the intake state model.
4. Ratification handoff path selection was still open.
5. No fail-closed validator existed for intake artifacts.
6. No Stage 2 CLI scaffold existed to orchestrate the process without mutating doctrine.

## Repairs applied

| Area | Repair |
|------|--------|
| Design freeze | Added `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md` to lock artifact taxonomy, authority seams, state machine, ratification path, and read-only default |
| Intake taxonomy | Added `INTAKE_IDENTITY.yaml`, `INTAKE_STATUS.yaml`, `INTAKE_EVENTS.yaml`, and `HANDOFF_NOTE.md` schema logic in `scripts/intake_state.py` |
| State machine | Added explicit lifecycle transitions and committee transition checks |
| CLI scaffold | Added `scripts/amendment_intake_agent.py` with `--status`, `--init`, `--phase`, `--through`, manual gate flags, and dry-run support |
| Validation | Added `scripts/validate_intake_state.py` with exact-key, controlled-vocab, dependent-field, event, and handoff checks |
| Templates / handoff | Added bootstrap modules for planning, kernel, and ratification handoff scaffolds |
| Docs | Updated `DEVELOPER.md` and `CHANGELOG.md` |

## Stage 3A architect-lane hardening

| Area | Repair |
|------|--------|
| Precondition enforcement | Architect lane now fails closed unless the selected manifest exists, the KB bundle exists, and the KB `build_manifest.json` exists |
| Required snapshot presence | If the selected manifest declares `reference/knowledge_base/snapshots/product_context_bundle.md`, architect execution now blocks unless that snapshot is present |
| Slug/path reconciliation | `scripts/intake_paths.py` now explicitly owns architect-lane slug/path reconciliation for `reviews/<slug>/planning/ARCHITECT_PLAN.md` |
| Output verification | Architect success is recorded only after `ARCHITECT_PLAN.md` is verified on disk after subprocess completion |
| Audit visibility | Non-default architect bundle / manifest inputs are now recorded in intake events instead of remaining implicit |
| Failure recording | Missing architect inputs, slug/path mismatch, preflight/subprocess failure, and missing architect output now fail closed through architect-specific intake events |

## Stage 3B architect-lane quality/evidence hardening

| Area | Repair |
|------|--------|
| Output conformance validation | Architect success now requires `ARCHITECT_PLAN.md` to pass template-based structural validation, not mere file existence |
| Bundle / manifest correspondence | The wrapper now proves the selected manifest, selected bundle, and selected `build_manifest.json` correspond by label, file list, and bundle source sections where the current artifacts can prove it |
| Deterministic freshness rule | If the selected manifest requires `product_context_bundle.md`, the wrapper now blocks when the snapshot is older than the selected `build_manifest.json` or when comparable freshness metadata cannot be proven |
| Direct-path governance distinction | Direct `ollama_planning_agent.py --role architect` execution now emits a clear warning that the intake wrapper remains the governed architect path |
| Event hardening | Added architect-specific events for output conformance validated, output validation failed, evidence freshness blocked, and bundle/manifest mismatch blocked |

## Hard controls preserved

- `scripts/peer_review.py` remains the binding peer-review engine.
- Manual verification is not inferred from draft existence.
- Committee state is not inferred from packet prose.
- Ratification is never auto-executed by the scaffold.
- Doctrine mutation remains out of scope by default in Stage 2.


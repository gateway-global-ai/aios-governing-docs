# Amendment intake scaffold review package

This package documents the Stage 2 scaffold plus the Stage 3A and Stage 3B architect-lane hardening passes for the governed local amendment intake orchestrator.

## Review target

- Freeze doc: `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md`
- CLI scaffold: `scripts/amendment_intake_agent.py`
- State / schema modules:
  - `scripts/intake_state.py`
  - `scripts/intake_paths.py`
  - `scripts/intake_runtime.py`
  - `scripts/intake_phases.py`
  - `scripts/intake_templates.py`
  - `scripts/intake_ratification.py`
- Validator: `scripts/validate_intake_state.py`
- Operator docs: `DEVELOPER.md`

## What this review surface covers

- freezes intake artifact ownership
- freezes committee / verification / kernel / ratification seams
- adds a read-only-by-default orchestration scaffold
- preserves binding peer review under `scripts/peer_review.py`
- hardens the architect lane so it fails closed on missing KB/build inputs, missing required snapshot input, slug/path mismatch, and missing `ARCHITECT_PLAN.md` after subprocess return
- hardens the architect lane further so success now requires structural architect-plan conformance, stronger manifest/bundle/build-manifest correspondence, deterministic required-snapshot freshness proof, and an explicit governance distinction for the direct architect command

## What this review surface does not do

- replace `scripts/peer_review.py`
- replace the underlying architect agent
- auto-approve committee outcomes
- auto-complete kernel review
- auto-ratify
- mutate doctrine by default

## Review order

1. `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md`
2. `scripts/intake_state.py`
3. `scripts/intake_phases.py`
4. `scripts/amendment_intake_agent.py`
5. `scripts/validate_intake_state.py`
6. `DEVELOPER.md`
7. Stage 3A architect-lane hardening notes in `CHANGELOG.md`


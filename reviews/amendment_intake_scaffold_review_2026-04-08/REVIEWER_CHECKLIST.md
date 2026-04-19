# Reviewer checklist — amendment intake scaffold

## Design freeze

- [ ] `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md` freezes `reviews/<slug>/intake/` as the intake state location
- [ ] `INTAKE_IDENTITY.yaml` is identity-only
- [ ] `INTAKE_STATUS.yaml` is status-only
- [ ] `INTAKE_EVENTS.yaml` is append-only
- [ ] `HANDOFF_NOTE.md` is non-authoritative prose only
- [ ] ratification handoff path is frozen to `reviews/<slug>/ratification/`

## Separation of powers

- [ ] the scaffold does not replace `scripts/peer_review.py`
- [ ] architect verification is explicit and human-recorded
- [ ] UI verification is explicit and human-recorded
- [ ] committee outcomes are explicit and human-recorded
- [ ] kernel review remains advisory and non-blocking
- [ ] ratification is not auto-executed

## Code behavior

- [ ] `scripts/amendment_intake_agent.py --status` is read-only
- [ ] `scripts/amendment_intake_agent.py --init` creates only intake/process artifacts
- [ ] `--through` does not silently cross manual verification gates
- [ ] architect execution blocks when the KB bundle is missing
- [ ] architect execution blocks when `build_manifest.json` is missing
- [ ] architect execution blocks when the selected manifest requires `product_context_bundle.md` and that snapshot is missing
- [ ] architect execution blocks when the selected manifest, bundle, and `build_manifest.json` do not correspond by label / file list / bundle source sections
- [ ] architect execution blocks when required `product_context_bundle.md` freshness cannot be proven or is older than the selected `build_manifest.json`
- [ ] architect success is recorded only after `reviews/<slug>/planning/ARCHITECT_PLAN.md` exists
- [ ] architect success is recorded only after `ARCHITECT_PLAN.md` passes structural conformance validation against the architect template
- [ ] architect bundle / manifest overrides are auditable in intake events
- [ ] slug/path mismatch is treated as an architect-lane block, not silently redirected
- [ ] direct `ollama_planning_agent.py --role architect` invocation is explicitly marked as lower-governance/manual relative to the wrapper path
- [ ] `scripts/validate_intake_state.py` fails on extra keys
- [ ] `scripts/validate_intake_state.py` fails when dependent fields are missing
- [ ] `scripts/validate_intake_state.py` fails when handoff authority text is missing

## Docs

- [ ] `DEVELOPER.md` documents dry-run mode, validator use, and the read-only default
- [ ] `CHANGELOG.md` records the scaffold and validator
- [ ] `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md` records the Stage 3A and Stage 3B architect-lane hardening rules


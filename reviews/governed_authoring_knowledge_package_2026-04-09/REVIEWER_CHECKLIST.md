# Reviewer checklist — governed authoring knowledge package

## Style and boundary lock

- [ ] `JT_EDITORIAL_STYLE_CARD.md` is bounded style guidance, not doctrine
- [ ] `JT_NARRATION_STYLE_CARD.md` is bounded style guidance, not doctrine
- [ ] `JT_AUTHORING_MODE_BOUNDARIES.md` defines mode names, allowed source classes, prohibited source classes, and author identity boundaries

## Manifest discipline

- [ ] editorial and narration manifests declare required documents
- [ ] optional includes are bounded by manifest declaration
- [ ] raw discussion is not treated as required knowledge without repo conversion

## Tooling

- [ ] `jt_authoring_agent.Modelfile` preserves non-authority rules
- [ ] `scripts/ollama_authoring_agent.py` requires explicit mode selection
- [ ] `scripts/ollama_authoring_agent.py` requires manifest-declared inputs
- [ ] `scripts/ollama_authoring_agent.py` rejects manifest overrides that do not match the selected mode family
- [ ] the command surface does not mutate doctrine
- [ ] `jt_authoring_agent:latest` can be built from `modelfiles/jt_authoring_agent.Modelfile`
- [ ] editorial and narration smoke tests have been run against the packaged default model, not only an override model
- [ ] live proof is judged on boundedness and fidelity separately rather than treating model availability as proof of quality
- [ ] fidelity hardening did not add hidden examples or undeclared sources
- [ ] the final prompt anchor is the writing assignment rather than raw source text
- [ ] editorial and narration outputs materially improve in prose shape without weakening governance boundaries

## Governance

- [ ] `AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md` defines declared-input discipline and bounded author identity rules
- [ ] `AMD-2026-014` binds declared inputs, discussion conversion, and the non-authority rule
- [ ] architect/UI planning remains template-bound and human-verified

## Export standard

- [ ] `build_peer_review_export.ps1` remains the preserved build path for the self-contained export
- [ ] the self-contained export is named `peer_review_export__AMD-2026-014__2026-04-09.zip`
- [ ] archive entries use normalized `/` separators
- [ ] repo-relative tree appears at archive root
- [ ] review docs plus files under review are included without unrelated repo state
- [ ] `peer_review_export` and `peer_review_package` are not treated as the same artifact class

# Governed authoring knowledge package review

**Packet authority note:** This dated directory is a legacy package-materials helper for `AMD-2026-014`. The sole authoritative packet root for live governed review is now:

- `reviews/amd_2026_014_governed_authoring_knowledge_inputs_and_bounded_author_like_drafting/`

This review package covers the bounded first package for governed author-like knowledge inputs.

## Standard export

The standard self-contained export for this package is:

- `reviews/peer_review_export__AMD-2026-014__2026-04-09.zip`

Build path:

- `reviews/governed_authoring_knowledge_package_2026-04-09/build_peer_review_export.ps1`

This export follows **[AIOS-PEER-REVIEW-EXPORT-STANDARD-001](../../reference/implementation/AIOS-PEER-REVIEW-EXPORT-STANDARD-001.md)**:

- `peer_review_export` means self-contained evidence archive
- repo-relative tree appears at archive root
- zip entry separators are normalized `/`
- review docs plus actual files under review are included
- unrelated repo files are excluded

## Review target

- `reference/knowledge_base/agents/style/JT_EDITORIAL_STYLE_CARD.md`
- `reference/knowledge_base/agents/style/JT_NARRATION_STYLE_CARD.md`
- `reference/knowledge_base/agents/style/JT_AUTHORING_MODE_BOUNDARIES.md`
- `reference/knowledge_base/agents/style/JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `reference/knowledge_base/agents/style/JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `modelfiles/jt_authoring_agent.Modelfile`
- `scripts/ollama_authoring_agent.py`
- `reference/implementation/AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md`
- `amendments/AMD-2026-014-governed-authoring-knowledge-inputs-and-bounded-author-like-drafting.md`

## What this package does

- locks bounded style guidance as declared repo knowledge
- locks mode definitions and author identity boundaries
- requires manifest-declared source inputs
- requires manifest overrides to stay within the selected mode family
- prevents raw discussion from becoming required knowledge without repo conversion
- adds a bounded local Ollama authoring command surface

## Default-model proof pass

The packaged default model path has now been exercised directly:

- located the live Windows executable path for Ollama
- built `jt_authoring_agent:latest` from `modelfiles/jt_authoring_agent.Modelfile`
- ran live editorial and narration smoke tests through `scripts/ollama_authoring_agent.py` without a model override

Result:

- default-model path proved
- boundedness held
- initial style/task fidelity was weak and should not be overstated

## Style-fidelity hardening pass

The weak-fidelity diagnosis was:

- prompt assembly ended on raw source text, biasing the model toward summary behavior
- the original packaged `llama3.2` base was too weak for convincing editorial/narration shape under this much governed context

The hardening applied was narrow:

- stronger anti-summary and prose-first constraints in the packaged Modelfile
- runner prompt assembly now ends on the actual writing assignment instead of ending on repository source text
- packaged default base switched to local `qwen3:8b`

No bounded example files were added.

Quality result:

- editorial fidelity improved materially
- narration fidelity improved materially
- boundedness still held

## What this package does not do

- create a freeform identity clone
- self-ratify doctrine
- replace architect or UI planning templates
- replace committee, peer review, kernel review, or ratification
- mutate doctrine automatically

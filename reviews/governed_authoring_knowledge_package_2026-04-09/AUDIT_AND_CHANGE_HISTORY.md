# Audit and change history — governed authoring knowledge package

## Why this package was added

1. The repo needed a bounded author-like drafting surface instead of freeform persona drift.
2. Architect/UI-adjacent use of style guidance needed declared-input discipline.
3. Discussion-derived knowledge needed a clear conversion rule before it could become required repo knowledge.

## Changes applied

| Area | Change |
|------|--------|
| Style lock | Added governed editorial and narration style cards |
| Boundary lock | Added mode definitions, allowed source classes, prohibited source classes, and author identity boundaries |
| Manifest discipline | Added editorial and narration required knowledge manifests |
| Tooling | Added a bounded Modelfile and Python runner with explicit mode and manifest selection |
| Tooling hardening | Enforced manifest-family compatibility so manifest override cannot silently cross from editorial-family runs to narration-family runs, or vice versa; fixed live Windows terminal output so non-ASCII model text does not crash the runner |
| Default-model proof | Located the installed Ollama executable, built `jt_authoring_agent:latest` from the packaged Modelfile, and ran editorial/narration smoke tests against the packaged default model rather than an override model |
| Fidelity hardening | Reordered runner prompt assembly so the writing assignment is the final prompt anchor, strengthened prose-first / anti-summary instructions, and switched the packaged default base from `llama3.2` to local `qwen3:8b` after proving the base model was a major fidelity limiter |
| Reference binding | Added a technical standard for governed authoring knowledge inputs |
| Amendment binding | Added draft AMD-2026-014 for declared inputs, discussion conversion, and non-authority rules |
| Docs | Updated KB agent docs, planning lifecycle, developer docs, and changelog |
| Export standardization | Preserved a package-local `build_peer_review_export.ps1`, codified the self-contained export standard, and aligned the review package to `peer_review_export` terminology |

## Hard controls preserved

- repo truth remains authoritative over style
- style guidance remains advisory
- architect/UI templates and human verification remain intact
- doctrine mutation is not automated
- raw discussion is not silently treated as required knowledge
- default-model proof does not widen manifests, add new modes, or authorize Voicebox/runtime expansion
- fidelity hardening did not add hidden examples, new modes, or undeclared sources

## Default-model proof result

- `ollama` CLI was not on `PATH`, but the live executable was located at `C:\Users\jason\AppData\Local\Programs\Ollama\ollama.exe`
- the Ollama HTTP server was reachable during the pass
- `jt_authoring_agent:latest` did not exist before the pass and was built during the pass
- live editorial and narration smoke tests were run through `scripts/ollama_authoring_agent.py` with the packaged default model
- boundedness held, but the outputs were still weak summaries and not strong evidence of target editorial/narration fidelity

## Style-fidelity hardening result

- the strongest root cause was prompt construction plus base-model weakness, not missing governance artifacts
- no bounded example files were needed
- after hardening, editorial output shifted from source-summary behavior to a mode-shaped paragraph
- after hardening, narration output shifted from hallucinated amendment enumeration to a coherent narrated intro
- boundedness still held after the quality pass

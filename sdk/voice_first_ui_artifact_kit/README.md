# Voice-first UI artifact kit

This directory is the governed library root for the canonical voice-first UI artifact kit.

The governing rule is simple:

- the canonical kit lives in `aios-governing-docs`
- downstream product repos may consume or implement against it
- downstream product repos do not become the silent authority for the kit definitions

The initial governed manifest is:

- `voice_first_ui_artifact_kit_manifest.yaml`
- `voice_first_ui_artifact_kit_manifest.schema.json`

The current governed deployment package inside that manifest is:

- `header_voice_runtime_package`

That package exists so systems using the governance can deploy the full header voice-runtime surface as one traceable unit rather than rebuilding ad hoc fragments. Its package contract covers the shell header authority surface, the header player cluster, the cue drawer, the header system-control panel, the deeper voice control panel handoff, and the governed Gemini voice runtime transport path.

The downstream handoff bundle for that package now lives at:

- `header_voice_runtime_package_manifest.yaml`
- `header_voice_runtime_package_manifest.schema.json`

That handoff manifest records the required runtime files, host-only environment-variable boundary, proof expectations, and deployment steps for adopters that want to ship the governed header voice runtime as a package instead of reconstructing it from prose alone.

This root is intended to remain law-controlled and reviewable so foundational shell artifacts cannot drift through casual no-code or convenience-driven edits in downstream app libraries.

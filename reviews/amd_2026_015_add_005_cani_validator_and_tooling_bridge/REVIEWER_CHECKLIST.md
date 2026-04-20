# Reviewer checklist

- Confirm `AMD-2026-015-ADD-005` is the correct next subordinate addendum under `AMD-2026-015`.
- Confirm the addendum stays validator/tooling-only and does not broaden into runtime collection or instrumentation.
- Confirm the validator/tooling bridge defines responsibilities rather than automatic rewrite authority.
- Confirm persisted observation validation requirements cover identity, metadata, append-only history, and correction discipline.
- Confirm persisted recommendation validation requirements cover identity/status/events/handoff integrity, controlled values, lifecycle, supersession, and evidence linkage.
- Confirm intake-envelope validation requirements cover provenance, sequence/batch/causal linkage, normalization-state validity, `payload_ref` boundary compliance, mapping references, and rejection handling.
- Confirm the validator outcome model distinguishes authoritative outcomes from advisory-only warnings.
- Confirm validator-result routing is limited to governed lanes and does not authorize direct runtime action.
- Confirm non-authority boundaries remain explicit: no browser instrumentation, no event-store implementation, no runtime writers, no automatic recommendation execution.
- Confirm registry, tracker, changelog, and review package surfaces reflect the new addendum and support document.
- Confirm the package-local build script produces `peer_review_export__AMD-2026-015-ADD-005__2026-04-09.zip`.
- Confirm the export uses normalized `/` zip paths and preserves the repo-relative tree at archive root.

# Reviewer checklist

- Confirm `AMD-2026-015-ADD-006` is the correct next subordinate addendum under `AMD-2026-015`.
- Confirm the addendum stays capture-surface / normalization / handoff-only and does not broaden into collector implementation.
- Confirm the bridge defines allowed capture surface classes and treats `unknown` as blocked/manual rather than normal governed intake.
- Confirm the bridge distinguishes raw capture from normalized intake envelopes without creating a second storage universe.
- Confirm minimum pre-envelope requirements preserve provenance, evidence basis, and sequence context before normalization.
- Confirm fail-closed handling distinguishes `fail`, `blocked`, `advisory_warning`, and `pass` before validator handoff.
- Confirm normalized intake must hand off to validator before any writer-lane materialization.
- Confirm collectors or instrumentation are explicitly forbidden from writing persisted observation or recommendation artifacts directly.
- Confirm human/operator evidence remains authoritative where interpretation or boundary judgment is required.
- Confirm non-authority boundaries remain explicit: no browser instrumentation implementation, no database/event-store work, no autonomous routing, no change to the approved writer slice.
- Confirm registry, tracker, changelog, and review package surfaces reflect the new addendum and support document.
- Confirm the package-local build script produces `peer_review_export__AMD-2026-015-ADD-006__2026-04-09.zip`.
- Confirm the export uses normalized `/` zip paths and preserves the repo-relative tree at archive root.

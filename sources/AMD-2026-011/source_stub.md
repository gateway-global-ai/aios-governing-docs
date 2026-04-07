# Source material stub — AMD-2026-011

**Amendment:** [AMD-2026-011](../../amendments/AMD-2026-011.md) (draft)

## Purpose of this folder

Structured notes and future primary sources for **external repository acquisition**, **quarantine**, **analysis**, **promotion**, and **minimal governance execution dependencies**. Replace or extend this stub as acquisition tooling and Council decisions produce authoritative artifacts.

**Formalization:** Draft specification **[AIOS-SPEC-013](../../specifications/ExternalRepositoryAcquisitionAnalysisAndPromotion.md)** (contracts and promotion classes) pairs with **[AMD-2026-011](../../amendments/AMD-2026-011.md)** for triangulated peer review.

## Working notes (non-normative)

- **Acquisition intent:** system-emitted, policy-bound requests to obtain an external repository artifact for governed evaluation — not a default operator workflow.
- **Quarantine:** mandatory initial state for every acquired tree until analysis and policy gates complete.
- **Machine-readable record:** manifests describing provenance, dependencies, secrets surface, APIs, capability class, and execution/risk class — stored as governed artifacts, not informal chat.
- **Promotion:** transition from quarantine to approved reuse only after analysis and applicable **ratification** or tier-appropriate approval.
- **Minimal execution dependency principle:** CI and governance scripts install only packages required for the declared check (see `scripts/requirements.governance-integrity.txt` vs `scripts/requirements.txt`).

## Placeholders for future attachments

| Artifact | Status |
|----------|--------|
| Acquisition intent schema / example JSON | TBD |
| Quarantine checklist (operator) | TBD |
| Capability / risk taxonomy alignment with existing scope classes | TBD |

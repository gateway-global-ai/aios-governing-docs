# Impact study summary — AMD-2026-011 (draft)

## Scope

Formalizes **system-driven external repository acquisition**, **quarantine**, **analysis**, **promotion**, and **ratification**-aligned reuse — plus the **minimal execution dependency principle** for governance CI.

## Security and trust

- Reduces ad hoc ingestion of third-party trees into governed or runtime repositories.
- Makes provenance, dependency, and secret surfaces **recorded and reviewable** before operational use.
- Aligns automation trust boundaries with **AIOS-OPS-005** / **AIOS-OPS-006** expectations for verifiable checks.

## Operational impact

- **Developers:** Continue using `scripts/requirements.txt` for full pipeline scripts; CI **Governance integrity** job uses `scripts/requirements.governance-integrity.txt` only (`DEVELOPER.md`).
- **CI:** Smaller install footprint for the integrity job; behavior of `governance_integrity_check.py` unchanged.
- **Future tooling:** Acquisition services should emit machine-readable records consumable by registry-adjacent or operations docs (exact storage TBD in follow-on specification work).

## Spec / document follow-on

- Normative **interface and lifecycle** detail for acquisition and quarantine should eventually live in a **dedicated specification** (proposed **AIOS-SPEC-013** — see amendment body); **AIOS-SPEC-009** remains reserved for the Intent Primitive and Execution Model in this repository.

## Risk if not adopted

- Uncontrolled copies of external repos into governed spaces.
- Over-broad CI dependencies obscuring what is actually required for integrity checks.
- Weaker reproducibility and auditability of third-party code dependencies.

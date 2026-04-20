# Revision log — AMD-2026-014 — `draft` `0.1.2`

## Source posture

- prior reviewed head: `draft` `0.1.1`
- current head: `draft` `0.1.2`
- basis: completed Round 1 expanded five-review synthesis and failed gate report

## Accepted changes

1. Added a defined `Run record` term and tightened `Explicit declared input set` so it must be recorded in an auditable run record.
2. Tightened `Mode family` and `Declared repo truth` so they point more clearly to Section 6 and the higher-tier governance hierarchy.
3. Revised Scope to clarify that local Ollama is part of an initial designated drafting-tool surface rather than the only possible implementation.
4. Revised Section `4.6` so required traceability fields must be recorded in a reviewable run record, with optional display in the command surface.
5. Added `tool invocation identity` and `reviewable timestamp or execution reference` to the minimum traceability field set.
6. Rewrote Section `4.7` to replace `where policy allows` with explicit governed conversion language under an applicable amendment, specification, or repository-control process.
7. Added a rule that non-compliant drafting output is not admissible as authoritative evidence in planning, committee, peer-review, or ratification materials.
8. Renamed Section `6` to clarify that `AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001` is the initial designated support standard and that this amendment remains the controlling authority if a draft support-standard change conflicts.
9. Tightened successor-designation language in Section `6` so later repository-control updates must explicitly preserve this amendment's rules and authority boundaries.

## Rejected changes

- Did not widen the amendment into a broader `AIOS-SPEC-009` / DCP / schema-governance package.
- Did not move full implementation schemas or audit tooling requirements into the amendment body.
- Did not open ratification or downstream truth-surface work.

## Deferred items

- Any larger schema-level conformance surface that belongs in the supporting standard or tooling layer.
- Any broader review-process doctrine changes outside the narrow amendment text.

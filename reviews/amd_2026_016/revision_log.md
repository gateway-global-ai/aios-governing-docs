# Revision log — AMD-2026-016

## v0.2.0 — 2026-04-10

**Trigger:** Round 1 peer review for `AMD-2026-016` returned a mean composite of `2.9` with convergent failures in legal enforceability, completeness, practical operability, and developer synchrony.

**Primary gaps addressed:**

- missing lifecycle law for non-human principal registration, credentialing, suspension, revocation, and decommissioning
- missing admission-style validation before authority-bearing action
- missing default liability, ownership, and economic attribution rules
- missing conformance record requirements and implementation examples
- weak cross-document linkage to `AIOS-SPEC-002`, `AIOS-SPEC-009`, `AMD-2026-007`, and `AMD-2026-012`

**Changes (normative):**

- `§2` — narrowed overlap boundaries so the amendment does not silently redefine shell-state routing or domain-intent execution law already owned by `AMD-2026-007`, `AMD-2026-012`, `AIOS-SPEC-002`, and `AIOS-SPEC-009`.
- `§3` — added enforceable definitions for `route class`, `authority-bearing action`, `principal registry`, and `conformance record`; tightened `scope binding`, `routed communication`, and `deterministic non-human action`.
- `§4.4` — replaced open-ended routed-surface language with documented route-class law.
- `§4.5` — clarified where required action-carriage fields must live and added ownership / economic attribution fields where applicable.
- `§4.6` — added admission-style validation sequence: identity, class, role binding, scope binding, route class, and policy authorization before action.
- `§4.7` — required service-account registration in a governed principal registry with owner, credential posture, bindings, scope, route classes, and revocation status.
- `§4.11` — converted ownership from vague future definition into explicit default attribution rules.
- `§4.12` — strengthened fail-closed deny-and-audit consequences for validation failure.
- `§4.13` — added lifecycle law for creation, credentialing, suspension, revocation, and decommissioning.
- `§4.14` — added liability and economic attribution rules so non-human activity cannot remain anonymous or unowned.
- `§4.15` — added minimum conformance record requirements.
- `§5` — rewrote relationship mapping with section-level anchors and implementation impact.

**Changes (informative but review-relevant):**

- `§6` — replaced informal shell-program note with a formal cross-document impact table.
- `§8` — added example registry, policy-context, and action-envelope shapes.
- `§9` — added conformance probes for deny-and-audit, revocation, and metered attribution.

**Design posture:** This revision mirrors mature control-plane governance patterns without binding AI OS to a vendor-specific model: identity is separated from role binding, validation occurs before action, revocation blocks future action, ownership remains attributable, and decommissioning cannot silently strand authority.

**Next review step:** Re-run formal peer review on `amendments/AMD-2026-016.md` and assess whether the dimension floor rises above `3`.

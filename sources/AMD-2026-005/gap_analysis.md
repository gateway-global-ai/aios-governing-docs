# Gap analysis: current governing docs vs AMD-2026-005 behavior

## Missing or underspecified concepts

| Concept | Current state | Gap |
|---------|---------------|-----|
| Workspace hub vs workflow | Described in app code; not in core/spec as normative | Need amendment + spec cross-refs |
| `amendment_hub` canvas id | Code-only | Registry + glossary in amendment |
| Intent set `hub` / `resume` / `review` / `create` | Partially in voice app | Formal INTENT_JSON contract |
| Load state `ok` / `empty` / `error` | API client pattern | Normative for hub loaders |
| Post-PR human audit | DEVELOPER.md / checklist imply old flow | **Conflict** — must supersede |

## Outdated definitions

- **DEVELOPER.md:** “Human Ratification” as terminal stage without distinguishing **triangulated review thresholds** vs **separate human audit after PR**.  
- **amendment_template.md:** Ratification checklist can be read as requiring **Round 2** + implicit human audit ordering.

## Conflicting assumptions

- **Demo path:** “Open amendment → auto-create run” (deprecated) vs **hub-first** (current implementation).  
- **Failure handling:** “No-op” or “fallback to chat” vs **explicit disambiguation / policy denial** (amendment requirement).

## Resolution

Addressed by **amendments/AMD-2026-005.md** (supersession clause, deterministic failure policy, authoritative schema, migration/rollback), plus **CRITICAL** edits to DEVELOPER.md and amendment_template.md.

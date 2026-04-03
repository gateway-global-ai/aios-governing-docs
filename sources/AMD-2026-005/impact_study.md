# Impact study: AMD-2026-005

## Architectural impact

- **Platform primitive:** The **workspace hub** is a stable navigation layer distinct from **workflow execution** (`amendment_workflow`). Implementations must treat hub listing and run creation as separate operations.
- **Canvas/state model:** Intent resolution, view registry, and payloads (hub vs workflow, `edit` vs `review`) become **normative** for conforming clients; divergence is a governance failure, not a UI preference.
- **API contract:** List endpoints must support **truthful** outcomes (success with empty vs transport failure) so clients never show a false “zero amendments” state.

## Governance impact

- **Constitution / MPOA / specs:** Amendment introduces cross-cutting requirements on **agent/canvas documentation** (e.g. AIP, UI/CLI specs where “intent” and “surface” are defined). Specific edits are listed in the formal amendment cross-document table.
- **Lifecycle docs:** [DEVELOPER.md](../../DEVELOPER.md) and [templates/amendment_template.md](../../templates/amendment_template.md) must align with **Author → Triangulated PR → Thresholds → Ratification** without a **post–peer-review human audit** gate (supersession clause in amendment text).

## UX / system behavior

- Users always see **explicit** state for lists (loading / ready / empty / error).  
- Failed governance intents **must not** silently drop to generic chat or hide the canvas without a visible policy outcome (see deterministic failure policy in amendment).

## Risk analysis

| Risk | Mitigation |
|------|------------|
| Dual-governance (old template vs new law) | Hard override clause + CRITICAL updates to DEVELOPER.md and amendment_template |
| Schema fork across agents | Authoritative schema + “invalid if non-compliant” |
| Rollout regression | Per-phase rollback triggers in migration plan |

## System integrity

- **Audit:** Existing audit events for canvas open/close/policy remain; amendment adds requirement that **implicit execution** is forbidden and **violations** are rollback triggers.  
- **Conflict freedom:** Removing contradictory “audit after PR” language from guides is required for Dimension 6 alignment.

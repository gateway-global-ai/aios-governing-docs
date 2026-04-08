Here is the Registry Migration Planner output, grounded only in the three discovery artifacts (1_cartography_report.md, 2_implicit_capability_report.md, 3_governance_breach_audit.md) and the research-pack framing (0_cursor_research_pack.md). Facts cited below are those reports’ claims about the repo as of their snapshot.

1. Registry migration summary
The codebase already has partial registry truth (registry-yaml/views.yaml, registry-yaml/skill-dispatch-registry.yaml, docs-governance/canonical/LOGICAL_ROUTE_REGISTRY.md) running in parallel with hardcoded authority (App.tsx wouter tree, AdminShell pathname if-chain, useOSMenu, ConciergePanel handleMenuAction / EmbeddedViewId, canvasIntentRouter TIER1_RULES, ToolRouter switch(toolType), REGISTERED_VIEW_IDS vs CanvasViewId, skillDispatchRoutes z.enum). The cartography spine is VoiceTurnOrchestrator → /api/canvas-control → validator + intent router; breaches cluster around second paths (tool-metadata canvas, menu navigation, prompt blocks in geminiVoice, dropped canvas_grounding).

Migration should not invent a new architecture: it should collapse duplicate tables and attach enforcement so the same rows drive docs, lint, runtime allowlists, and UI maps.

Direct answers to the six planner questions:

Route registry first: Prioritize (A) the logical route catalog already documented vs App.tsx + AdminShell + os-core loadLogicalRoutes / OSHomeView parallel maps, and (B) TIER1_RULES (substring → intent + CanvasViewId) as syscall-layer semantic routes on the live path. (A) reduces shell drift; (B) removes the highest-leverage hidden routing on transcript→canvas.
View registry stability: CanvasViewId + CanvasRenderPayload in shared/canvasViewContract.ts, validator REGISTERED_VIEW_IDS (once deduped), ToolRouter toolType → panel, and TypedCanvasView’s specialized IDs are the most stable, discriminant-shaped mappings. views.yaml rows are stable as declared catalog if runtime enforcement is wired. EmbeddedViewId + ConciergePanel placeholders, legacy SharedCanvasPanel canvas_type, and incomplete TypedCanvasView coverage are unstable or split-brain until reconciled.
Actions explicit enough: canvas.action syscall path (validated in canvasControlRoutes after envelope + validateCanvasSyscall), skillDispatchRoutes body schema + per-skill branches, and buildAllowedRuntimeActions string set (policy matrix) are registry-shaped. switch_view from useOSMenu and handleMenuAction are not registry-ready until bound to the same allowlist as server validation. CTAs → onTriggerSpeech / onContextUpdate strings are not explicit actions for a registry until server-validated or funneled through canvas.action / skill dispatch (auditor).
Skills atomic enough: TOOL_DECLARATIONS keys (model-facing units), skill-dispatch-registry.yaml / skillDispatchRoutes implemented skillIds (once aligned), localAgentRoutes taskType enum, and agentOrchestration pipeline/step vocabulary are atomic skill/dispatch units. Broad domain POST handlers are not automatically skill-registry rows without extracting named, gated, single-purpose dispatch surfaces (capability report: not fully enumerated).
Stay in policy/validation (not registries): Multi-layer validator ordering and composition (canvasDirectiveValidator), entitlement/plan interpretation spread across voice/chat/routes, geminiVoice Contextual Snap prose blocks (RUNTIME_POLICY, PRICING_RULE, etc.), tool gating matrices (getToolsAllowedForMode, SITE_ANCHORED_TOOLS), Tier 2 LLM routing algorithm (only inputs like allowedViews belong in registries, not the inference procedure), protocol/audio constants, security sentinel classification, ARCH fallback/scaffolding behavior.
Minimum viable registry rollout: Integrity + single-source contracts first (grounding + buyerJourney ordering per auditor — not registries but block honest registry semantics), then one source for canvas view IDs, then logical HTTP route catalog ↔ client shells, then TIER1 as data, then menu/menu-action binding, then skill/tool alignment.
2. Route registry candidates
Candidate	Why (from discovery)	Notes
LOGICAL_ROUTE_REGISTRY.md ↔ App.tsx wouter paths	Parallel “route tables”; os-core loadLogicalRoutes / OSHomeView SET_ROUTE vs client router (implicit report §3).	Route registry anchors logical routeId, browser paths remain adapters.
AdminShell pathname → page if-chain	Second shell; cartography §5b — drift risk with AppSidebar.	Same logical ids as above; admin vs legacy scope must be explicit rows, not two mental models.
canvasIntentRouter TIER1_RULES	Hidden routing: patterns → intent + CanvasViewId (implicit §3, breach §5).	Auditor lists as first conversion target (data table shared with docs/lint/runtime).
Tier 2 output: selectedViewId from allowlist	Prompt-driven + validated downstream — the allowlist is registry-relevant; the LLM is not.	Register allowed views per context, not the tier-2 algorithm.
POST /api/canvas-control syscall enum	Explicit HTTP → behavior (implicit §3).	Fits action or route-to-handler docs; syscall names are stable API surface.
First among these: Unify logical route catalog with App.tsx + AdminShell (and os-core consumers) so every shell dispatches one routeId vocabulary; in parallel or immediately after, externalize TIER1_RULES because it governs live transcript → canvas independent of marketing/admin pages.

3. View registry candidates
Candidate	Stability	Evidence
CanvasViewId + render payload union (shared/canvasViewContract.ts)	High — schema authority for syscall shapes.	Cartography §2c; implicit §1.
REGISTERED_VIEW_IDS (canvasDirectiveValidator)	High after merge — duplicate of contract today (breach §4, implicit §6).	Must be derived or single-generated, not hand-maintained twice.
registry-yaml/views.yaml + lazyImportKey	High as catalog; enforcement E2E unverified (implicit §7).	Already “registry”; migration is wiring + drift checks.
ToolRouter toolType → component	High — natural switch table (implicit §6).	Companion to tool declarations, not a second story.
TypedCanvasView (phone_provisioning_form, account_overview)	High for those IDs; gap for rest (cartography §5f).	Register implemented rows first; mark others legacy path.
SharedCanvasPanel canvas_type + items[]	Medium — legacy but structured; unvalidated at HTTP boundary (implicit §1–2).	Registry as legacy view family with migration path to typed payloads.
useOSMenu viewIds	Medium — whole tree hardcoded (implicit §5 #1).	Stable after alignment with views.yaml / CanvasViewId.
ConciergePanel EmbeddedViewId + placeholders	Low–medium — overlaps registry/menu but local and partially placeholder (implicit §1).	Defer full registration until each id is real component + context contract.
4. Action registry candidates
Candidate	Explicit enough?	Evidence
canvas.action (and related syscalls)	Yes — Zod envelope + multi-layer validation.	Implicit §2; breach “governed” path.
skillDispatchRoutes actions (search_numbers, provision_number, …)	Yes — Zod-validated body.	Implicit §2.
buildAllowedRuntimeActions outputs (open_support, manage_agents, provision_phone, …)	Yes as policy rows; implementation stays in validator.	Implicit §2; breach §4.
Menu action: 'switch_view' + viewId	Not yet — no action-registry check (breach §4).	Becomes registry-ready when same row drives server allowlist.
handleMenuAction allowlist	Not yet — hardcoded routing (implicit §2).	Same binding as above.
SharedCanvasPanel CTAs → speech/context strings	No until validated server-side or routed (auditor §5 migration).	Treat as breach closure, then action ids.
5. Skill registry candidates
Candidate	Atomic enough?	Evidence
TOOL_DECLARATIONS keys	Yes — one name → one schema + handler binding in geminiVoice.	Implicit §4, §6.
skill-dispatch-registry.yaml ↔ skillDispatchRoutes implemented set	Yes after alignment — partial duplication (breach §4, implicit §6).	Register implemented skills only; YAML is aspiration until matched.
localAgentRoutes taskType	Yes — small closed enum.	Implicit §4.
agentOrchestration PIPELINE_STEPS / source union	Yes as orchestration skill vocabulary (not every line of code).	Implicit §4.
Arbitrary modular route handlers	No default — not catalogued as named skills (implicit §4, §7).	Promote only dispatch-shaped, authenticated, single-purpose endpoints.
6. Dependencies and blockers
canvas_grounding dropped in geminiVoice — breaks speech↔canvas contract honesty; fix or explicitly “unsupported” before treating “grounded view” as a registry-governed behavior (cartography §5a, auditor §1, §5).
buyerJourney ordering in /api/website-chat — corrupts context keys / prompt assembly semantics any registry claims to require (cartography §5d, auditor §2).
REGISTERED_VIEW_IDS vs CanvasViewId — any view or route→view registry amplifies drift until single-sourced (auditor §4, §6).
skillDispatchRoutes vs YAML — skill registry rows lie if enum and YAML diverge (auditor §4).
Deprecated shared_canvas / show_canvas → applyCanvasPayload — bypasses canvas control plane; registries won’t be authoritative until fenced (auditor §1, §5).
Two admin shells — route/view menus won’t converge without scope rules (AppSidebar vs AdminShell / adminNav) (cartography §5b).
Tier 2 depends on local LLM — registry can define allowed views; cannot registry-away noop degradation (cartography §5e) without a product decision on fallback.
views.yaml runtime enforcement on main client — uncertain E2E (implicit §7); blocks “views registry is done.”
aiStudioProxy vs sovereign path — second WebSocket governance story; affects which tool/skill sets apply (cartography §5g, auditor §3).
7. Suggested rollout order (minimum viable)
Non-registry integrity (still prerequisite): canvas_grounding handling or documented removal; loadBuyerJourney before prompt compile on website-chat (auditor priority).
Single source of canvas view IDs: CanvasViewId / REGISTERED_VIEW_IDS reconciliation (auditor “first conversion targets”).
Route registry v0: Logical routeId rows = union of LOGICAL_ROUTE_REGISTRY doc, App.tsx paths, AdminShell map, os-core SET_ROUTE ids — one table (conceptually), adapters only in code later.
Semantic route registry v0: TIER1_RULES externalized as the same rows validator + router + docs consume (implicit §6).
View registry enforcement pass: views.yaml vs useOSMenu vs ConciergePanel — either strict loader or generated menu from catalog; TypedCanvasView coverage explicitly “implemented vs legacy.”
Action registry v0: canvas.action + buildAllowedRuntimeActions + skill-dispatch actions as named actions with required context keys; bind switch_view / handleMenuAction to those rows.
Skill registry alignment: skill-dispatch-registry.yaml ↔ skillDispatchRoutes ↔ TOOL_DECLARATIONS (subset: actually dispatched skills/tools first).
Tool UI boundary: ToolRouter discriminant + typed metadata per toolType (auditor recommendation) as companion to tool registry, not a fifth registry type.
Long arc: Admin nav unification; Contextual Snap policy as structured policy output of promptCompiler / policy service (not prose rows in a “skill” registry).
8. Things that are still too ambiguous to register
Full EmbeddedViewId set until placeholders are resolved or explicitly deprecated (cartography §5f, implicit §1).
Every legacy canvas_type variant until payloads are Zod-validated at the same boundary as typed canvas (implicit §1, §7).
Complete TOOL_DECLARATIONS inventory as rows until enumerated in a follow-up pass (implicit §7).
Tier 2 LLM routing as a “route” — only inputs/allowlists are registerable; inference stays code.
Which tools/skills merge for /ws/gemini-live vs /ws/os-live until traced (implicit §7).
Entire modular server/routes/*.ts surface as skills without naming, gating, and single-purpose classification (implicit §4).
Hot agent swap — cartography §5c: no governed mechanism; registering a route would be fiction until product/engineering defines it.
sessionMetaPrompt / kickstart / IMMEDIATE DIRECTIVE — behavior is prompt-plane; registry rows without compiler ownership would duplicate geminiVoice (auditor §2).
This completes planning only: no YAML, no TypeScript, no code changes, and no architecture not implied by the three discovery reports and their cited files.
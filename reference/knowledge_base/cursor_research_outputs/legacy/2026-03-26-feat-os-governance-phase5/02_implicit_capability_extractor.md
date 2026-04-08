Here is an extraction grounded in the repo as it exists today (no new registries, no YAML, no invented capabilities).

1. Implicit views discovered
Where	What	Explicit vs implicit	Hardcoded / inferred / prompt	Validated?	Registry-ready?
shared/canvasViewContract.ts	CanvasViewId union + view models (WelcomeViewModel, ServiceMenuViewModel, etc.) and syscall payloads	Explicit in TypeScript	Hardcoded union	Partially: used by canvasDirectiveValidator + Zod in canvasControlRoutes	Yes — canonical shape for canvas
server/services/canvasDirectiveValidator.ts	REGISTERED_VIEW_IDS Set<CanvasViewId>	Explicit server allowlist	Hardcoded; can drift from canvasViewContract union	Yes (layer 5 “renderer”)	Yes — duplicate of contract
registry-yaml/views.yaml + lazyImportKey	OS shell views (os-home-view, admin-*, canvas syscall views like welcome, agent_roster, …)	Explicit YAML	Declared in YAML	Unclear at runtime (loader vs ad hoc imports)	Already registry
client/src/components/chat/ConciergePanel.tsx	EmbeddedViewId union + conditional render (embeddedView === 'profile' → ProfileContent, etc.); many *-view ids render a placeholder (“capitalize title”) only	Implicit UI contract	Hardcoded strings + component switch	Unvalidated vs views.yaml	Partially — ids overlap menu/registry but mapping is local
client/src/components/voice/tools/ToolRouter.tsx	Tool names → panel components (manual_input, shared_canvas, canvas_control, hotel/warrant/kiosk, …)	Implicit “view” = tool surface	Hardcoded switch (toolType)	Unvalidated (unknown tool → null + warn)	Yes — natural toolType → component table
client/src/components/voice/tools/SharedCanvasPanel.tsx	Legacy canvas_type union (service_menu, schedule, …) + cta_action book | call | form | link	Semi-explicit props	Hardcoded branches	Unvalidated at boundary (typed in props only)	Yes
client/src/components/voice/tools/SharedCanvasPanel.tsx	TypedCanvasView: only phone_provisioning_form and account_overview specialized; rest falls through to legacy panel	Implicit completeness	Inferred “typed vs legacy”	Partial	Yes — gap is explicit in code
2. Implicit actions discovered
Where	What	Nature	Validation
SharedCanvasPanel.tsx	CTA and row handlers call onTriggerSpeech / onContextUpdate with string instructions (e.g. user tapped book, selected slot)	Hardcoded callbacks; prompt-driven follow-up (voice)	None on server
SharedCanvasPanel.tsx (PhoneProvisioningView)	onAction?.('search_numbers' | 'provision_number', data)	Hardcoded action names	Dispatched client-side; pairs with /api/skills/dispatch
server/routes/skillDispatchRoutes.ts	skillId z.enum + per-skill action branches (e.g. search_numbers)	Explicit Zod	Validated body
server/routes/canvasControlRoutes.ts	canvas.action syscall path (after envelope Zod + validateCanvasSyscall)	Explicit	Validated multi-layer
server/services/canvasDirectiveValidator.ts	buildAllowedRuntimeActions builds strings like open_support, manage_agents, provision_phone from security + entitlements	Hardcoded policy matrix	Validated against visitor session
useOSMenu.ts	Menu items use action: 'switch_view' + viewId	Implicit action type	Unvalidated vs action registry
ConciergePanel.tsx handleMenuAction	Large allowlist → setEmbeddedView vs onNavigate?.(viewId)	Hardcoded routing decision	Unvalidated
3. Implicit routes discovered
Where	What	Nature
server/services/canvasIntentRouter.ts	TIER1_RULES: substring patterns → intent string + CanvasViewId	Hardcoded intent→view
Same file	tier2Route: Llama JSON for selectedViewId from allowed list	Inferred + prompt-driven; comment: untrusted until validated
server/routes/canvasControlRoutes.ts	POST /api/canvas-control branches on syscall enum	Explicit HTTP → behavior
client/src/App.tsx	Wouter <Route path=…> → lazy page components	Explicit browser paths; implicit logical routeId unless wired elsewhere
docs-governance/canonical/LOGICAL_ROUTE_REGISTRY.md	Documents routeIds (e.g. os.home, public.business.by_slug)	Explicit doc; enforcement in code is partial (e.g. OSHomeView dispatches SET_ROUTE with routeId: "os.home")
os-core/.../loadLogicalRoutes() (used in OSHomeView.tsx)	Loads logical routes from OS-core registry loader	Explicit in os-core; parallel to client App.tsx
ConciergePanel.tsx	onNavigate?.(viewId) for ids outside embedded allowlist	Implicit “route” = parent callback
4. Implicit skills discovered
Where	What	Nature
registry-yaml/skill-dispatch-registry.yaml	skillId, intentPatterns, canvasViewId, internalRoute	Explicit YAML
server/services/promptCompiler.ts	Loads YAML; buildSkillContextFragment injects skill list + “emit canvas:dispatch” wording	Prompt-driven exposure; filtered by security level
server/routes/skillDispatchRoutes.ts	dispatchSchema.skillId z.enum — must match implemented handlers	Explicit + hardcoded subset of YAML
server/config/geminiToolDeclarations.ts	TOOL_DECLARATIONS object: Gemini tool names, descriptions, parameter schemas	Explicit to model; hardcoded TS
client/src/components/voice/tools/ToolRouter.tsx	Maps tool output types to UI	Implicit companion to server declarations
server/services/agentOrchestration.ts	PIPELINE_STEPS, OrchestrationSource union, env gates	Explicit orchestration skill/stage vocabulary
server/routes/localAgentRoutes.ts	taskType: z.enum(["governance", "code", "agent", "ui"])	Explicit local-agent task taxonomy
server/services/localAgentKnowledgeContext.ts (by reference in routes)	loadSkillContext / loadKnowledgeContext	Structured task→docs (implementation not fully read here)
5. Top 10 hardcoded / inferred capability hotspots
client/src/hooks/useOSMenu.ts — Entire menu tree: labels, icons, viewIds, role branches.
client/src/components/chat/ConciergePanel.tsx — EmbeddedViewId union, handleMenuAction allowlist, embedded view switch/placeholder branch.
server/services/canvasIntentRouter.ts — TIER1_RULES pattern→viewId/intent; Tier 2 LLM routing.
client/src/components/voice/tools/ToolRouter.tsx — switch (toolType) for all multimodal tool UI.
server/config/geminiToolDeclarations.ts — All Gemini-native tool schemas and names.
server/services/canvasDirectiveValidator.ts — REGISTERED_VIEW_IDS + buildAllowedRuntimeActions.
registry-yaml/views.yaml — View catalog + lazyImportKey (large, authoritative for declared views).
client/src/App.tsx — Browser route→page map (lazy imports).
server/routes/skillDispatchRoutes.ts — skillId enum + per-skill implementation branches.
shared/canvasViewContract.ts — CanvasViewId + syscall envelope (foundational; drift risk vs validator + UI).
6. Registry-ready candidates
ToolRouter.tsx toolType → component — stable discriminant, already switch-shaped.
TIER1_RULES in canvasIntentRouter.ts — rows = intent pattern list + viewId + minSecurityLevel + confidence.
REGISTERED_VIEW_IDS vs CanvasViewId — should be single source; today two hardcoded lists.
buildAllowedRuntimeActions — policy matrix row-oriented.
EmbeddedViewId + ConciergePanel render map — today duplicates/overlaps views.yaml / menu viewIds.
TOOL_DECLARATIONS keys — already a registry-like object (machine + human metadata).
Skill dispatch — align z.enum in skillDispatchRoutes.ts with skill-dispatch-registry.yaml (today partial duplication).
7. Areas of uncertainty
Runtime enforcement of views.yaml on the main client shell: registries exist, but whether every viewId from useOSMenu / ConciergePanel is loaded via the same loader as os-core is not verified end-to-end in this pass.
Voice path: which tools and skills are actually merged for /ws/gemini-live vs /ws/os-live is referenced in comments (OSHomeView.tsx) but full branching is not traced here.
canvas.render / client commit: server validates and audits; how strictly client renderers enforce CanvasRenderPayload shape for every viewId beyond ToolRouter/SharedCanvasPanel is not fully mapped.
Count and list of all TOOL_DECLARATIONS entries: only a prefix was read; the full set is “large object” in one file.
Modular server/routes/*.ts surface: many domain executors exist; this report does not enumerate every POST handler as an “action” — only the main governed clusters above.
Sources cited: shared/canvasViewContract.ts, server/services/canvasIntentRouter.ts, server/services/canvasDirectiveValidator.ts, server/routes/canvasControlRoutes.ts, server/routes/skillDispatchRoutes.ts, server/services/promptCompiler.ts, server/config/geminiToolDeclarations.ts, client/src/components/voice/tools/ToolRouter.tsx, client/src/components/voice/tools/SharedCanvasPanel.tsx, client/src/hooks/useOSMenu.ts, client/src/components/chat/ConciergePanel.tsx, registry-yaml/views.yaml, registry-yaml/skill-dispatch-registry.yaml, docs-governance/canonical/LOGICAL_ROUTE_REGISTRY.md, os-core/src/views/shared/OSHomeView.tsx, server/routes/localAgentRoutes.ts, server/services/agentOrchestration.ts, client/src/App.tsx.
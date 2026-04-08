Here is the updated Governance Breach Auditor report, revised to include 2_implicit_capability_report.md (now populated), 1_cartography_report.md, and sys_prompt_start.md (CTO consolidation brief: fragmented authority, canvas grounding gap, dual admin shells, registry incompleteness — e.g. sys_prompt_start.md L17–27, L25–26).

1. Executive risk summary
Research alignment: 0_cursor_research_pack.md positions this audit as finding bypasses before registry work — consistent with sys_prompt_start.md, which states authority is still split across prompt assembly, contracts, validation, UI, and implicit routing.

Highest risks (evidence-backed):

End-to-end voice grounding gap — Client sends canvas_grounding (GeminiStreamingClient.sendGroundedSpeechContext); geminiVoice.ts processClientMessage only handles setup, audio, realtime_input, clientContent, tool_response; else logs unknown — grounding never reaches Google (cartography §5a; code server/geminiVoice.ts ~L354–386).
Parallel “route tables” with no single authority — TIER1_RULES (canvasIntentRouter.ts), ToolRouter switch (toolType), useOSMenu tree, ConciergePanel handleMenuAction / EmbeddedViewId, App.tsx wouter paths, YAML views.yaml / skill-dispatch-registry.yaml vs skillDispatchRoutes z.enum — implicit capability report §1–§3, §5–§6; cartography §5b.
UI mutation from non–control-plane paths — Legacy shared_canvas / show_canvas still applies canvas from tool metadata; SharedCanvasPanel uses client callbacks (onTriggerSpeech, onContextUpdate) without server validation (implicit report §2, §11; ConciergePanel.tsx deprecated branch).
Policy and capability encoded in prompt prose — geminiVoice.ts Contextual Snap appends RUNTIME_POLICY, PRICING_RULE, HOSPITALITY_POLICY, IMMEDIATE DIRECTIVE from sessionMetaPrompt, etc., alongside tool filtering — dual channel (implicit report §4; cartography §2b).
Website-chat prompt boundary defect — buyerJourney referenced in businessContext before loadBuyerJourney (cartography §5d; chatRoutes.ts ~L185 vs ~L220).
2_implicit_capability_report.md §7 correctly flags unverified end-to-end enforcement: views.yaml vs client shells, /ws/gemini-live vs /ws/os-live tool merge, strict client enforcement of every CanvasRenderPayload view.

2. Breach list by category
1) Direct UI mutation
Breach	Sources
Pinned canvas in local React state (setPinnedCanvas), not a durable governed store	Cartography §5i; ConciergePanel.tsx
Deprecated canvas update from Gemini tool_type metadata (shared_canvas / show_canvas) → applyCanvasPayload	ConciergePanel.tsx (comment admits governance violation); implicit report §1 (ToolRouter legacy)
ToolRouter: metadata: any, switch (toolType) — UI from unstructured tool payloads	Implicit report L8–9, L45
SharedCanvasPanel: legacy canvas_type branches; CTAs call onTriggerSpeech / onContextUpdate with string instructions — no server validation	Implicit report L10–L14
canvas_control path still adapts payload into SharedCanvasPanel metadata	Implicit report L8; ToolRouter.tsx
2) Prompt-driven execution
Breach	Sources
Runtime/commerce rules as system_instruction text (INTRODUCTION_PROTOCOL, RUNTIME_POLICY, LINKS_MENU, PRICING_RULE, hospitality variant)	geminiVoice.ts; cartography walkthrough §3a
sessionMetaPrompt → “IMMEDIATE DIRECTIVE” + kickstart user turn — first-turn routing by prompt, not logical route registry	geminiVoice.ts; sys_prompt_start.md (routing authority)
Tool descriptions + parameters in TOOL_DECLARATIONS act as model-facing policy; combined with prompt blocks = hidden policy surface	Implicit report L35–L36; cartography §2b
buildSkillContextFragment injects skill list + “emit canvas:dispatch” wording — skills exposed via prompt	Implicit report L33–L34
aiStudioProxy.ts: minimal fixed system_instruction — parallel voice plane without Contextual Snap	Cartography §5g; aiStudioProxy.ts
3) Direct config or DB dependency
Breach	Sources
Contextual Snap reads getSiteConfigById and walks knowledgeLibrary, placeData, plan, overrides — not exclusively siteRuntimeResolver	Cartography §2e vs §3a; geminiVoice.ts
plan === 'free' (and related) in voice, website-chat, siteConfigRoutes	Grep-backed; cartography entitlement story
Website chat builds knowledgeBlock from siteConfig inline	chatRoutes.ts; cartography §3b
Client fetch('/api/site-configs/.../knowledge') in shell	Cartography snippet ConciergePanel KnowledgeOverlay
4) Missing validation boundaries
Breach	Sources
buyerJourney used before loadBuyerJourney in /api/website-chat prompt path	Cartography §5d; chatRoutes.ts L185 vs L220
useOSMenu: action: 'switch_view' + viewId — not validated against action registry	Implicit report L19–L20
ConciergePanel handleMenuAction: large allowlist → setEmbeddedView / onNavigate — hardcoded routing, unvalidated vs registry	Implicit report L20–L21
REGISTERED_VIEW_IDS vs CanvasViewId union — duplicate sources, drift risk	Implicit report L6, L54, L56
skillDispatchRoutes z.enum vs skill-dispatch-registry.yaml — partial duplication	Implicit report L32–L34, L58
Canvas HTTP path: Zod + validator present (canvasControlRoutes, canvasDirectiveValidator); client render path not uniformly shape-checked per viewId	Implicit report L62–L63
5) Hidden routing logic
Breach	Sources
TIER1_RULES: substring patterns → intent + CanvasViewId	Implicit report L23–L24; cartography §2c
Tier 2: local LLM JSON → selectedViewId from allowlist (comment: untrusted until validated)	Implicit report L24
SITE_ANCHORED_TOOLS list in geminiVoice.ts — tool-name allowlist for injection	geminiVoice.ts (~L461–468 region from prior read)
getToolsAllowedForMode + agent allowedTools — capability matrix in code, not declared registry row	Cartography §3a; geminiVoice.ts
Agent “switching” = separate pages / assignedAgentId at setup — no governed hot-swap route	Cartography §2d, §5c; sys_prompt_start.md L22
App.tsx wouter vs loadLogicalRoutes / OSHomeView — parallel route authorities	Implicit report L26–L28
AdminShell: pathname if-chain to page	Cartography §2a
6) Meta-reasoning leakage
Breach	Sources
speakingInstructions in SpeechGroundingContext intended to steer speech — if forwarded, could surface model-internal phrasing to user if model echoes; today messages are dropped, so risk is silent failure of grounding, not user-visible leakage	Cartography §5a; GeminiStreamingClient canvas_grounding; geminiVoice.ts unknown branch
applyArchFallback may replace or append assistant text when ARCH validation fails — user sees scaffolding/fallback not model “thought”, but deterministic non-user content	chatRoutes.ts applyArchFallback
Kickstart text “I just clicked the button…” is injected as user role — not internal reasoning, but synthetic user content in the model stream	geminiVoice.ts setupComplete branch
3. Highest-risk files
File	Why
server/geminiVoice.ts	Contextual Snap (DB + prompt policy + tool gating + SITE_ANCHORED_TOOLS); drops canvas_grounding; kickstart injection
client/src/components/chat/ConciergePanel.tsx	Pinned canvas state; deprecated tool-metadata canvas path; handleMenuAction / embedded views
server/services/canvasIntentRouter.ts	Tier 1 pattern route table + Tier 2 LLM routing
client/src/components/voice/tools/ToolRouter.tsx	toolType → UI companion to tools; any metadata
client/src/components/voice/tools/SharedCanvasPanel.tsx	Legacy canvas + unvalidated client speech/context callbacks
client/src/hooks/useOSMenu.ts	Whole idle menu capability tree hardcoded (implicit report §5 #1)
server/routes/chatRoutes.ts	buyerJourney ordering bug; inline knowledge; plan tier prompt
server/config/geminiToolDeclarations.ts	Large model-facing capability / policy surface
server/services/canvasDirectiveValidator.ts	Duplicate REGISTERED_VIEW_IDS vs contract
server/routes/skillDispatchRoutes.ts	Enum + branches drift from YAML
server/aiStudioProxy.ts	Second Gemini Live path with weak governance
client/src/App.tsx	Browser route map parallel to logical route loader
4. Governance bypass map
governed
bypasses
tools + system_instruction
canvas_grounding
applyCanvasPayload
any metadata
ConciergePanel setPinnedCanvas
Gemini Live
VoiceTurnOrchestrator
geminiVoice drops
Panels
siteRuntimeResolver
canvasControlRoutes
canvasDirectiveValidator
canvasIntentRouter
geminiVoice Contextual Snap raw siteConfig + prompt policy
Tool metadata shared_canvas show_canvas
ToolRouter switch
useOSMenu + handleMenuAction
sessionMetaPrompt IMMEDIATE DIRECTIVE
aiStudioProxy minimal setup
Narrative (from research pack + implicit report): The governed spine is VoiceTurnOrchestrator → /api/canvas-control → validator + intent router (cartography §3a). Bypasses include: (1) voice snap merging DB + prose policy outside siteRuntimeResolver-only consumption, (2) legacy tool canvas → pinned UI, (3) menu/tool switches not wired to a single registry, (4) grounding WebSocket message not proxied upstream.

5. Migration priority ranking
Fix canvas_grounding handling in geminiVoice.ts (or stop sending if unsupported) — unblocks grounded speech contract; cartography §5a; sys_prompt_start L25–26.
Fix /api/website-chat buyerJourney order — restores prompt/data integrity; cartography §5d.
Remove or fence deprecated shared_canvas / show_canvas → applyCanvasPayload — closes direct UI mutation from tool payloads.
Single source for view IDs — reconcile CanvasViewId, REGISTERED_VIEW_IDS, views.yaml, EmbeddedViewId / ConciergePanel` (implicit report §6).
Align skillDispatchRoutes enum with skill-dispatch-registry.yaml — closes skill drift (implicit report §58).
Extract geminiVoice runtime policy strings to structured policy (or registry rows) consumed by one compiler path — reduces prompt-as-policy (sys_prompt_start §7 direction).
Typed ToolRouter metadata + narrow union per toolType — boundary for raw payloads.
Document and gate aiStudioProxy vs sovereign path — cartography §5g.
Server-side validation or typed dispatch for onTriggerSpeech / onContextUpdate strings from canvas CTAs — or route through canvas.action / skill dispatch only (implicit report §14).
Admin nav / AppSidebar unification (longer arc) — cartography §5b; sys_prompt_start L23.
6. Recommended first conversion targets
Target	Rationale
REGISTERED_VIEW_IDS → derived from shared/canvasViewContract.ts (or codegen)	Eliminates duplicate allowlist (implicit report L54–L56).
TIER1_RULES → data table (YAML or TS const imported by validator + router)	Same rows used for docs + lint + runtime; implicit report L53.
ToolRouter toolType → discriminated union + zod parse at boundary	Natural companion to TOOL_DECLARATIONS keys (implicit report L52, L57).
canvas_grounding → explicit branch mapping to Google clientContent (or documented unsupported)	Closes largest live-path integrity gap.
chatRoutes website-chat: loadBuyerJourney before compileFullSystemPrompt	Smallest fix, high signal for validation / ordering.
Research citations:

1_cartography_report.md: spine, control-plane list, §5a–§5i ambiguities.
2_implicit_capability_report.md: implicit views/actions/routes/skills, hotspots §5, registry-ready §6, uncertainty §7.
sys_prompt_start.md: fragmented authority, canvas grounding question, dual shells, registry gap, prompt-plane strategy (Sections 1–3, 7–8 themes).
0_cursor_research_pack.md: auditor role in the four-agent research pipeline (L44–L49).
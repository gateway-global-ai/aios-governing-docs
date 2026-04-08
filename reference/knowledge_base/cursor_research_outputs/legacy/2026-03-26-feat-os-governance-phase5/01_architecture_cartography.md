Gateway Global AI OS — Architecture Cartography Report
Branch: feat/os-governance-phase5 | Date: 2026-03-26 | Mode: Discovery only — no edits, no proposals.

1. Executive Summary
The codebase is a monorepo hosting a governed AI OS with two distinct runtime planes: a customer-facing Gemini Live voice/chat plane and an internal local-model worker plane. The surface presented to end users is dominated by the ConciergePanel — a PTT-first shell that fuses voice, chat, and a pinned canvas zone into a single sovereign session. Behind it, a layered server stack handles WebSocket proxying to Google's Gemini Live API, HTTP-based canvas syscall orchestration, prompt compilation, and entitlement enforcement.

The system is not a traditional MVC app. The critical distinctions are:

Behavioral identity (agent persona, tone, tools) is assembled server-side by promptCompiler.ts from DB rows — never hardcoded in UI or routes.
Canvas state is governed through a typed syscall layer (canvasViewContract → canvasControlRoutes → canvasIntentRouter) rather than ad-hoc React state.
Runtime site truth is normalized at a single point (siteRuntimeResolver.ts) and cached; everything downstream consumes it.
Agent switching in the UI sense does not exist as a live reconnect mechanism — the active concierge is site_configs.assignedAgentId resolved at session setup time.
There are two admin shells (AppSidebar / AppWithSidebar for the legacy tree; AdminShell / adminNav.ts for the /platform + /me surfaces) — they are not unified.
2. File Map
2a. App Shell and UI Entry Points
File	Role
client/src/main.tsx	Vite entry — mounts <App /> into #root, no providers
client/src/App.tsx	Global providers (QueryClient, AuthProvider, CustomerAuthProvider) + wouter route tree. Two shell patterns: AppWithSidebar (legacy catch-all) and standalone ProtectedRoute wrapping lazy AdminShell for /platform + /me
client/src/components/AppSidebar.tsx	Left nav for the legacy authenticated shell; fetches /api/agents for per-agent deep links; section groups: Platform, Agent Dashboard, Operations, Archive, Access Portals
client/src/pages/admin/AdminShell.tsx	Sovereign admin layout for /platform + /me; driven by adminNav.ts; AdminContent is an imperative if-chain mapping pathname → page component
client/src/config/adminNav.ts	Typed nav taxonomy for the sovereign admin shell — platformNav, meNav, helpers getScopeFromPath, flattenNavItems. The sole structural authority for that sidebar.
client/src/hooks/useOSMenu.ts	Idle OS menu model — role-scoped (customer/employee/manager/admin) memoized tree of OSMenuItems keyed by viewId; drives in-canvas idle state via OSMenuList, not the sidebar
client/src/components/chat/ConciergePanel.tsx	The primary runtime shell. Documented 56px / 64px / flex-content / 110px vertical split. Hosts voice client, VoiceTurnOrchestrator, ToolRouter, pinned canvas strip, OSMenuList idle state, PTT footer. Entry point for all customer-facing sessions.
client/src/pages/agents/AgentPage.tsx	Public/owner route at /agent/:slug — loads site by slug → renders ConciergePanel
client/src/pages/public/PlatformHomePage.tsx	Marketing home at /
2b. Voice / PTT Pipeline
File	Role
client/public/clear-voice-processor.js	AudioWorklet (off main thread) — accumulates 4096 float samples, computes RMS for visualizer, postMessages { audioData: ArrayBuffer (transferred), volume }
client/src/services/voice/GeminiStreamingClient.ts	The browser-side voice engine. Opens wss://.../ws/gemini-live, sends setup with system instruction + tools + sessionContext, streams 16 kHz PCM chunks, receives and plays 24 kHz PCM output, emits typed PttEvents (transcript.partial/final, speech.output, canvas.syscall, error)
client/src/services/voiceTurnOrchestrator.ts	Turn lifecycle governor above the audio stream. On transcript.final: drives canvas.resolve → (if not noop) canvas.render → sendGroundedSpeechContext. Sole authority for interruptSpeech on barge-in.
client/src/types/voice.ts	Client voice types (VoiceMessage, VoiceConfig, BusinessContext, AgentConfig, DISCProfile); re-exports governed shared types from shared/siteRuntimeContext and shared/canvasViewContract
server/geminiVoice.ts	Server-side Gemini Live WebSocket proxy. Serves /ws/gemini-live, /ws/browser-voice, /ws/os-live. Opens upstream BidiGenerateContent connection per client; performs Contextual Snap (tool gating, system instruction replacement from DB); routes setup, audio→realtime_input, tool_response; runs handleToolCall server-side and replies to client.
server/config/geminiLiveProtocol.ts	Protocol constants + validation — validateGeminiConfig(), getGeminiLiveSetup(), getGeminiWebSocketUrl(), GEMINI_CONFIG (16000 in / 24000 out). Finicky — one wrong change breaks voice.
server/config/geminiToolDeclarations.ts	Central registry of TOOL_DECLARATIONS — ~30 tool function declarations (search, canvas, booking, PMS, billing, etc.) filtered per session by gating logic in geminiVoice.ts
server/aiStudioProxy.ts	Separate proxy for /ws/ai-studio-ptt with minimal fixed setup — not the sovereign voice path
server/voiceGemini.ts	PSTN/Twilio path only — transcribeWithGemini (Cloud Speech STT), generateVoiceResponseGemini, synthesizeGeminiTTS. No relation to the browser Live socket.
server/voiceSession.ts	In-memory session store for PSTN call sessions keyed by Twilio callSid — not used by browser Live sessions
server/audioCodec.ts	μ-law encode/decode, resampling, PCM↔WAV helpers for the PSTN Twilio media path
2c. Canvas Rendering Flow
File	Role
shared/canvasViewContract.ts	Canonical type law. CanvasViewId union, CanvasSyscallType enum, CanvasSyscallEnvelope (versioned, id-tracked), CanvasRenderPayload (discriminated union on viewId), SpeechGroundingContext, PttCanvasSyscallEvent
shared/canvasStateMachine.ts	SessionState + TurnState enums with VALID_TURN_TRANSITIONS; TurnRecord, CanvasSessionSnapshot. Documents that VoiceTurnOrchestrator is the sole state transition owner.
server/routes/canvasControlRoutes.ts	Mounted at /api/canvas-control — single POST / entry for all syscall types; Zod validate → resolveSiteRuntime → validateCanvasSyscall → route to intent/render/patch/clear/action handler → writeCanvasAuditRecord
server/services/canvasDirectiveValidator.ts	5-layer syscall validator: structural → entitlement (plan + allowlists) → workspace state → visitor security level (authoritative from visitor_sessions) → renderer registry (Zod payload shapes). Returns typed CanvasSyscallError on failure.
server/services/canvasIntentRouter.ts	canvas.resolve implementation — Tier 1 keyword rules → Tier 2 local LLM (/api/local-llm-batch/complete) with allowedViews enforcement → Tier 3 noop. Returns CanvasResolveResult.
server/services/canvasPayloadSchemas.ts	Zod runtime validation per syscall type; validateSyscallPayload(syscall, payload)
server/services/canvasAuditLog.ts	Fire-and-forget canvas_events insert via setImmediate; logs full directive_json JSONB, latency, validation status, intent confidence
client/src/components/voice/tools/ToolRouter.tsx	Maps toolType + metadata → React panel for inline tool messages in the chat log (not the pinned canvas strip). Routes canvas_control → TypedCanvasView / SharedCanvasPanel; legacy shared_canvas / show_canvas excluded here (handled by orchestrator → setPinnedCanvas).
client/src/components/voice/tools/SharedCanvasPanel.tsx	Legacy glass card renderer for canvas canvas_type + items[] shapes. Also hosts TypedCanvasView (phone provisioning, account overview).
client/src/components/voice/tools/ManualDataInput.tsx	Generic text-input panel triggered by request_manual_input tool calls
2d. Agent Switching
File	Role
client/src/pages/agents/AgentManager.tsx	Admin/owner agent roster — CRUD against /api/agents; selectedAgent state drives deep-edit; DISC sliders synced from agent row on select
client/src/pages/agents/AgentDashboard.tsx	Grid of agent cards; creates links to /agent/:agentId/:environment and /chat/:agentId; scoped to ?siteConfigId= when present
client/src/components/admin/AgentRosterPanel.tsx	Global agent roster for AiBizBotAdmin; assigns agent to site via onAssignAgent(agent.id) callback → updates site_configs.assignedAgentId
server/routes/agentSystemRoutes.ts	Agent CRUD endpoints (GET/POST/PATCH/DELETE /api/agents), DISC endpoints, conversation generation; governance: requireAuth + assertSiteAccessForSession on create
server/services/agentProvisioning.ts	Signup-time swarm provisioning from industry_agent_templates; provisionAgentsForBusiness clones 6 agents per industry group; sets assignedAgentId to Concierge
server/services/agentOrchestration.ts	Orchestration run lifecycle for swarm provisioning and single-agent creates; enforces aptitude gate and env-driven outcome thresholds
2e. Runtime Context and Site Context
File	Role
server/services/siteRuntimeResolver.ts	Single normalization path from siteConfigId → SiteRuntimeContext. 30s in-memory cache. Resolves identity, business data, AI config block (assignedAgentId, systemPromptOverride, voiceConfig, structuredGuardrails), and derived entitlements.
server/services/promptCompiler.ts	Behavioral prompt assembly. buildBehavioralPrompt(agent, businessContext?, siteConfig?) composes: DISC/ARCH profile → operational mode → memory → business context → disclosure → stability dials → PPP → buyer journey → founder voice → skill fragment → certification. Also compileFullSystemPrompt used by chat routes.
server/services/conversationGrounding.ts	Builds ConversationGroundingRecord (CGR) — grounding telemetry injected into chat responses; buildCgrForWebsiteChat, buildCgrForAgentChat, loadBuyerJourney
shared/conversationGrounding.ts	Shared types/Zod schemas: CommunicationGovernanceConfig, ConversationGroundingRecord, StabilityDials, BuyerJourney
server/utils/siteScopedAccess.ts	Session + tenancy enforcement for admin mutations: assertSiteAccessForSession validates admin session actor, role, reseller scope; returns accessClass
server/routes/siteConfigRoutes.ts	Full CRUD + sub-resources for site configs: /api/site-configs/:id (agents, knowledge, brand, funnels, design studio, telephony, outcomes, QR stats, domain verify, go-live)
2f. Orchestrator / Control-Plane Files
File	Role
server/index.ts	Bootstrap: Express, registerRoutes, WebSocket servers (Gemini Live, PSTN, AI Studio, local voice, osLive), Socket.IO, crons, validateGeminiConfig, serve
server/routes.ts	Router composition hub. registerRoutes mounts ~35 modular routers via app.use. Also contains large legacy inline handler surface. No new routes should be added here.
server/routes/canvasControlRoutes.ts	Canvas syscall enforcement boundary (already listed above)
server/routes/intelligenceRoutes.ts	/api/intelligence — orchestration entry points: POST /provision (swarm), POST /orchestration-runs, POST /resolve, POST /ingest, POST /ppp-snapshot
server/routes/novaSovereignRoutes.ts	NOVA Sovereign bridge with Gate 1 HMAC perimeter; OTP/IDV flows
server/routes/localAgentRoutes.ts	/api/local-agent — jurisdiction enforcement + orchestration-run requirements for Ollama tasks; exports checkJurisdiction
server/services/readinessGateV1.ts	evaluateReadinessGateV1 — product readiness gate (identity minimum, agent path minimum)
server/services/entitlementMapper.ts	Platform license SKU → merged site entitlements
server/services/securitySentinel.ts	Deterministic classification of override reason text for knowledge certification (ok vs review_required)
server/services/stabilityDials.ts	DISC + ARCH → bounded StabilityDials for prompt tone shaping
server/storage.ts	Drizzle DatabaseStorage implementing IStorage — full CRUD surface for all tables
shared/schema.ts	Drizzle table definitions + Zod insert schemas — canonical DB shape
3. Live Path Walkthrough
3a. Voice path: browser mic → spoken output
1. CAPTURE
   getUserMedia (16 kHz MediaStream)
   → AudioWorkletNode (clear-voice-processor.js, off main thread)
   → port.onmessage: { audioData: ArrayBuffer, volume }
   → GeminiStreamingClient: createPcmBlob → base64 encode
2. PTT GATE
   startSession() / endSession() toggle streaming flag
   Only when streaming: socket.send({ type: 'audio', data: base64PCM })
3. UPSTREAM PROXY
   WebSocket to /ws/gemini-live (server/geminiVoice.ts)
   geminiVoice.ts → maps to realtime_input.media_chunks
   (mime: audio/pcm;rate=16000) → Google BidiGenerateContent
4. SESSION SETUP (first message)
   Client sends: setup + sessionContext (site/agent/funnel keys)
   geminiVoice.ts: performs Contextual Snap
     - replaces system_instruction from DB via promptCompiler
     - gates/filters tools from geminiToolDeclarations.ts
     - model from process.env.GEMINI_MODEL_ID
   Google responds: setupComplete
   geminiVoice.ts → client: { type: 'server_ready' }
   Client: starts AudioWorklet, sets connected = true
5. DOWNSTREAM AUDIO
   Google serverContent.model_turn.parts[].inline_data (base64 PCM 24kHz)
   → GeminiStreamingClient.playAudio()
   → AudioBufferSourceNode connected to 24kHz AudioContext → speakers
6. TRANSCRIPT EVENTS
   Google: input_audio_transcription (partial/final ASR)
   → GeminiStreamingClient.onEvent: PttEvent { type: 'transcript.final' }
7. CANVAS ORCHESTRATION (on transcript.final)
   VoiceTurnOrchestrator.handleFinalTranscript(text)
   → POST /api/canvas-control { syscall: 'canvas.resolve', transcript }
     Server: siteRuntimeResolver → validateCanvasSyscall (5 layers)
       → canvasIntentRouter (Tier1 rules | Tier2 local LLM | Tier3 noop)
       → canvasAuditLog (fire-and-forget)
     Response: CanvasResolveResult { selectedViewId, renderMode, speechContext }
   If not noop:
     Client hydrateViewPayload → canvasController.apply(payload)
       → ConciergePanel.setPinnedCanvas(CanvasRenderPayload)
     POST /api/canvas-control { syscall: 'canvas.render' } (audit only)
   gemini.sendGroundedSpeechContext(SpeechGroundingContext)
     → socket.send({ type: 'canvas_grounding', turnId, screenSummary, ... })
8. TOOL CALLS (concurrent with or instead of step 7)
   Google: serverContent.model_turn.parts[].tool_call
   → geminiVoice.ts: handleToolCall() on server
     Runs tool function (search, booking, etc.)
     → Google: tool_response (function results)
     → Client: { type: 'tool_result', metadata }
   → GeminiStreamingClient.onEvent: PttEvent { type: 'canvas.syscall', metadata }
   → ConciergePanel/ToolRouter renders panel inline in chat log
     OR applyCanvasPayload → setPinnedCanvas (for canvas-type tools)
3b. Text chat path: browser POST → response
POST /api/website-chat
  body: { message, siteConfigId, visitorId, funnelContextKeys, history }
  ↓
  storage.getSiteConfig(siteConfigId)
  ↓
  security check (sensitive input → secure form / deny)
  ↓
  storage.getAgent(siteConfig.assignedAgentId)
  compileFullSystemPrompt(agent, siteConfig, businessContext)
    = buildBehavioralPrompt + knowledge slice + free-tier fragment
  ↓
  gatewayChat(systemPrompt, message, history) → reply text
  ↓
  loadBuyerJourney(visitorId, siteConfigId)
  buildCgrForWebsiteChat(...) → ConversationGroundingRecord
  validateArchEnvelope(cgr)
  enqueuePppShadowLog(...)
  optional: storage.createChatLog(...)
  ↓
  Response: { reply, communication: { cgr, archValidation, pppShadow } }
4. Control-Plane Candidates
These files perform enforcement, routing decisions, gating, or session-level policy — not just data service or UI rendering.

File	Control-Plane Function	Enforcement Type
server/geminiVoice.ts	WebSocket proxy + Contextual Snap (tool gating, system instruction override)	Runtime session shaping
server/routes/canvasControlRoutes.ts	Canvas syscall enforcement boundary	HTTP gate + audit
server/services/canvasDirectiveValidator.ts	5-layer syscall validation (schema → entitlement → workspace → visitor security → registry)	Per-request enforcement
server/services/canvasIntentRouter.ts	Transcript → canvas view selection with allowedViews enforcement	Intent routing with boundary
server/services/siteRuntimeResolver.ts	Single-path normalization of site runtime truth; derived entitlements; cache invalidation	Runtime context authority
server/services/promptCompiler.ts	Behavioral identity assembly — sole path from DB rows to system prompt	Prompt plane authority
server/utils/siteScopedAccess.ts	Admin session + tenancy enforcement for all agent mutations	Auth/tenancy perimeter
server/routes/intelligenceRoutes.ts	Orchestration entry point (swarm + single-agent) behind assertSiteAccessForSession	Provisioning gate
server/services/agentOrchestration.ts	Orchestration run lifecycle; aptitude/outcome gating; violation persistence	Swarm enforcement + audit
server/routes/localAgentRoutes.ts	Jurisdiction enforcement + orchestration-run requirement for Ollama plane	Local model perimeter
server/routes/novaSovereignRoutes.ts	HMAC Gate 1 perimeter for NOVA IDV/billing bridge	Cryptographic perimeter
server/services/readinessGateV1.ts	Product readiness evaluation (identity minimum, agent path)	Product gate
server/services/entitlementMapper.ts	License SKU → entitlement merge (no downgrade)	Commercial policy
server/routes.ts	Router composition — registerRoutes determines which modules own which paths	Structural routing authority
shared/canvasViewContract.ts	Type contract — governs all canvas syscall shapes and view IDs	Schema authority (shared)
shared/canvasStateMachine.ts	Turn state machine contract with valid transition edges	State contract authority
5. Open Questions / Ambiguities
5a. canvas_grounding message handling on the server
GeminiStreamingClient.sendGroundedSpeechContext sends { type: 'canvas_grounding', turnId, currentViewId, screenSummary, speakingInstructions } on the live WebSocket. In server/geminiVoice.ts, processClientMessage branches on setup, audio, realtime_input, clientContent, tool_response — a canvas_grounding type is not explicitly named in what was read. It likely falls through to unknown message type log and is dropped, meaning the grounding context may not reach Google's model. This is a potential gap between VoiceTurnOrchestrator's intent and geminiVoice.ts's actual behavior.

5b. Two admin shells with non-overlapping item sets
AppSidebar (legacy tree) and AdminShell / adminNav.ts (sovereign admin) coexist with separate nav item definitions. It is unclear which is the intended long-term surface and whether feature parity is maintained between them. Some pages (e.g. CallTracking, SitesAndLeads) appear in both.

5c. Agent "switching" has no live reconnect mechanism
The active concierge for a session is resolved at WebSocket setup time from site_configs.assignedAgentId. There is no observed hot-swap path that changes the active agent mid-session (e.g. no "switch to Sales agent" command during a live call). The DISC dropdown in AppSidebar links to per-agent pages — each is a separate session.

5d. buyerJourney ordering bug in /api/website-chat
In chatRoutes.ts, businessContext references buyerJourney before loadBuyerJourney has resolved — loadBuyerJourney is called after buildBehavioralPrompt. The buyer journey data may be unavailable to the prompt compiler in the same request.

5e. canvas.resolve Tier 2 depends on local LLM
canvasIntentRouter.ts Tier 2 calls POST /api/local-llm-batch/complete (Ollama). If the local LLM is unavailable or slow, canvas resolution degrades silently to Tier 3 (noop). There is no observed circuit-breaker timeout or explicit fallback SLA — the canvas view stays unchanged on Ollama failure.

5f. TypedCanvasView coverage vs SharedCanvasPanel legacy surface
TypedCanvasView explicitly handles only phone_provisioning_form and account_overview; all other viewId values fall through to the legacy SharedCanvasPanel (driven by canvas_type + items[]). The discriminated union in CanvasRenderPayload has more view IDs than TypedCanvasView handles — the mapping is incomplete.

5g. geminiVoice.ts vs aiStudioProxy.ts disambiguation
Two WebSocket proxies open upstream Gemini connections. geminiVoice.ts (/ws/gemini-live) is the governed sovereign path with Contextual Snap. aiStudioProxy.ts (/ws/ai-studio-ptt) uses a minimal fixed setup. The exact consumer surface (which client routes use which) and the governance status of the AI Studio path were not fully resolved.

5h. routes.ts residual inline surface
server/routes.ts still contains thousands of lines of non-modular handlers alongside the 35 app.use modular mounts. The exact split between what is modular vs inline is not fully catalogued. The modular mounts are the clean governance surface; the inline portion is unquantified technical debt.

5i. No observed single-file canvas store on the client
VoiceTurnOrchestrator.canvasController.apply(payload) calls setPinnedCanvas on ConciergePanel. There is no observable standalone canvas state store (Zustand, Redux, Context) that was identified — canvas state appears to live in ConciergePanel local React state. If this is correct, canvas state does not survive navigation away from ConciergePanel.

That is the full architecture cartography. A few highlights worth calling out explicitly before any follow-on work:

The real runtime spine is a five-file chain: GeminiStreamingClient → /ws/gemini-live (geminiVoice.ts) → siteRuntimeResolver + promptCompiler (done at setup) → VoiceTurnOrchestrator (turn lifecycle) → /api/canvas-control (canvasDirectiveValidator + canvasIntentRouter).

The biggest structural ambiguity (§5a) is whether canvas_grounding messages sent by VoiceTurnOrchestrator actually reach the Gemini model or are silently dropped in geminiVoice.ts. If they are dropped, the entire "speech grounded on canvas truth" design principle has a gap in the live path.

The two admin shells (§5b) are not technical debt in the traditional sense — they appear to be intentionally serving different governance tiers (AppSidebar for legacy ops, AdminShell/adminNav.ts for the sovereign platform surface) — but the lack of a single nav registry means drift is possible.
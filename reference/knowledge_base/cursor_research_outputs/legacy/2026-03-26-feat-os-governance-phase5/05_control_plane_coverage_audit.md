Conducting a full audit: reading your research pack files and inventorying Cursor skills, rules, MCP servers, and repo commands.

Here is a consolidated audit aligned with your research pack (0–4) and the repo as it exists today.

Executive summary
The repo already has a strong Tier-1/Tier-2 governance stack: .cursorrules, ~35 scoped .mdc rules, docs-governance/canonical/CURSOR_RULES_INDEX.md, many skills under .cursor/skills/, a small slash-command set, MCP wired in .cursor/mcp.json, plus runtime hooks in package.json (aptitude tests, governance score, skill-identity validation).

Cursor “sub agents” are not stored as repo artifacts; they are a Cursor product capability (parallel Task agents / cloud agents). What is in-repo are skill playbooks, local agent plane APIs (/api/local-agent), orchestration runs, and lightweight .system_design/skills/*.json descriptors that point at governance docs—not executable sub-agent configs.

Your research artifacts (1–4) already diagnose the real gap: runtime authority is split (prompt blocks, YAML registries, TS unions, UI switches). The Cursor layer should mirror the target architecture: capabilities + boundaries + measurable gates—not ad hoc chat prompts.

1. Rules (.cursor/rules/*.mdc + .cursorrules)
What they are: Always-on or glob-scoped instructions for the AI in Cursor. Tier 1 = root .cursorrules (Sovereign Core: governance first, monolith route ban, voice/Twilio lockdown summaries). Tier 2 = mapped in docs-governance/canonical/CURSOR_RULES_INDEX.md (35 .mdc files + rules/SKILL.md for permit checks).

Pillars (from index):

Pillar	Role
Core OS	Mission, control plane, preflight review, filesystem, imports, legacy archive
Registry & routing	Logical routes, views/actions, schema anchors, modular routes, QR
Agent & runtime	Agent policy, provisioning, execution-plane boundary, prompts, handover, architect integrity
Voice & audio	Voice lockdown, Clear Voice ops, sovereign chat/PTT contract
UI & brand	Jason Standard, sovereign UI, brand tokens, app shell, Design Studio
Secrets & platform	API lockdown, Doppler bridge, env signatures, migrations
Specialized	CMO agent, R3F, Gemini model discipline
What they do: Force non-negotiables (no new routes in server/routes.ts, no voice path edits without a voice task, no frontend keys, Concierge layout/PTT contract, etc.) and point editors at canonical docs under docs-governance/.

2. Skills (.cursor/skills/**/SKILL.md)
What they are: Optional, task-triggered procedure bundles (umbrellas + domain skills). The rules index lists sentinel umbrellas; the workspace also exposes many more in the agent_skills list.

High-level inventory:

Skill area	Purpose
governance-linter	Read-only drift reports vs plans/rules/docs
governance-review	Phase 1 preflight + Phase 2 approve/reject (no edits)
archive-governance	Post-review quarantine/unmount workflows
technical-debt-triage	Classify TS/build debt into governed reports (no fixes)
registry-governance-expert	Routes, views, schema, QR — structural truth
logical-route-design / view-registry-design / schema-anchor-mapping	Design-time alignment with registries
knowledge-engineering-lead	KAP, certification, audit plane umbrella
sovereign-voice-architect / gemini-live-engine	Voice stack documentation discipline
sovereign-devops-sentinel / environment-management / sovereign-ai-devops	Doppler, PM2, CI, env
programmatic-sales-engine	Funnels, state machines, sales/canvas doctrine (large reference set)
intent-driven-canvas	Idle canvas + prefill for public/QR flows
sovereign-onboarding-pipeline	Onboarding spine reconstruction
sovereign-flow-diagramming	Mermaid from contracts only
cloudbeds-hospitality	PMS / Boardwalk / hospitality tools
a2p-compliance	Twilio 10DLC / SMS router
qr-shadow-telecom	QR + shadow telecom
health-diagnostics / rules/SKILL.md	Permits / keys
serpapi-data	SerpApi MCP usage
clean-room-extraction	External ZIP handling
mui-foundation	MUI behind client/src/ui-core for admin/control-plane
shadcn-ui-agent	shadcn MCP for discovery only → promote to Sovereign* in ui-core
What they do: Turn “do the right thing” into repeatable workflows (especially governance linter → review → archive), and isolate dangerous domains (voice, Twilio, compliance) behind explicit reading steps.

3. Sub agents
In this repo: There is no first-class “sub agent registry” checked into Cursor. You have:

Cursor IDE: Task-style agents (parallel exploration, shell, etc.) — product feature, not files.
.system_design/skills/*.json: Small metadata records (e.g. agent_orchestration.json) linking skill ids to governance refs and DB tables—not runnable agents.
Runtime “agents”: agents table, agent_orchestration_runs, /api/local-agent with jurisdiction (see local-agent-governance.mdc) — this is the platform agent plane, not Cursor sub agents.
Stray doc: docs/knowledge-base/boardwalk-rewards-extract/.local/skills/delegation/SKILL.md describes a delegation API pattern; treat as extracted/reference, not production Cursor config.
Conclusion: For your vision (“built-for-system agents, test, rate, train”), the durable path is: orchestration runs + aptitude scripts + registry rows, not Cursor sub-agent JSON in-repo (unless you later add an explicit, versioned “agent recipe” format).

4. MCP servers
Project config: .cursor/mcp.json (note: MCP_SETUP.md says mcp.json may be gitignored in some setups; here it appears in the workspace):

Server	Role
google-workspace	Local Node server at mcp-servers/google-workspace/workspace-server/dist/index.js — Gmail/Drive/Calendar-style workspace tooling (Gemini CLI workspace file storage flag set).
serpapi	Hosted MCP at mcp.serpapi.com — universal search/travel/etc. data (placeholder key in committed file is a secret hygiene risk if ever real).
shadcn-ui	npx @shadcn-ui/mcp-server@latest — component discovery/generation assistance.
Example / docs: .cursor/mcp.example.json and .cursor/MCP_SETUP.md also document Twilio MCP variants (@twilio-alpha/mcp); those are not in the current mcp.json snapshot—only in the example.

Cursor IDE browser MCP (from your environment): Lives under Cursor’s MCP folder (cursor-ide-browser); not in-repo.

5. Commands (.cursor/commands/*.md — slash commands)
Command	Intent
/verify-health	Doppler permit check, env/model sanity, dist/ artifacts, PM2 processes 5/6/8, log tail — environment-specific IDs.
/deep-build	Aggressive cache purge, npm run build, verify outputs, optional pm2 restart all — destructive / env-specific.
/map-project	“Source of truth” manifest for voice/tool paths — partly stale (e.g. references server/services/voice/toolHandler; geminiVoice.ts imports ./services/toolHandler).
/rebuild-gateway	Literally: npm run kill-port && doppler run -- npm run dev
/nova-handshake	Nova Sovereign handshake test flight + doc pointers
npm scripts (governance-relevant): test:voice-concierge-aptitude, test:local-agent-aptitude, governance:score, validate:skill-identity, sovereign-guard, integration:readiness, etc. — these are your closest existing “rate proficiency” hooks for agents/paths.

6. Conflicts and tensions
UI doctrine (surface-dependent): Jason Standard (jason-standard.mdc) pushes glass cards, no bg-white on outer wrappers, heavy indigo/emerald patterns. Brand tokens (brand-tokens.mdc) mandate white canvas and dark shell for Concierge. They conflict only if applied to the wrong surface; today they are different zones—but agents can confuse them without explicit “which surface?” context.

Accent color rules: Brand rule reserves purple for ARCH; Jason Standard leans indigo as primary electric. Again: scope (marketing/sovereign glass vs product shell) must be explicit in tasks.

MUI vs shadcn: mui-foundation and shadcn-ui-agent are aligned if both resolve to @/ui-core only in product code; conflict appears if someone imports raw MUI in feature code or raw shadcn paths despite the shadcn skill.

Research pack vs repo reality: 0_cursor_research_pack.md correctly says “don’t invent registries blind”—but the repo already has partial registries (registry-yaml/views.yaml, skill dispatch YAML, governance docs). The tension is process (“discover first”) vs artifact (“registries exist but aren’t single authority”)—exactly what 4_registery_migration_planner.md describes.

Cartography vs lockdown: Rules say voice files read-only; research (3_governance_breach_audit.md) calls out fixes in geminiVoice.ts (e.g. canvas_grounding). Those changes require an explicit voice governance task, not a casual edit—process conflict to manage.

Slash commands vs current tree: /map-project and possibly /verify-health assume specific paths or PM2 IDs—drift from production ops causes false failures or wrong guidance.

MCP_SETUP vs mcp.json: Docs emphasize Twilio MCP; active mcp.json emphasizes google-workspace + serpapi + shadcn—teams may assume Twilio is wired when it is not.

7. Alignment with your end state (capabilities, not human prompts)
Your research outputs already define the bridge:

Your goal	Already in repo	Gap
Agents “for the system”	local-agent-governance.mdc, /api/local-agent, orchestration runs, aptitude tests	Need one agent “spec” format (capabilities, boundaries, tests) versioned beside code
Test & rate	npm run test:voice-concierge-aptitude, test:local-agent-aptitude, readiness scripts	Tie scores to registry rows and CI gates, not one-off npm
Train / fine-tune to compliance	Governance linter → review; violations in orchestration	“Training” should mean registry + validator + golden scenarios, not prompt edits
Single voice-first admin entry	Concierge + canvas syscall path (cartography)	Dual shells (AppSidebar vs AdminShell) and parallel route tables (your reports §5b, §5)
shadcn MCP → dynamic views	shadcn MCP + shadcn-ui-agent skill	Product rule: MCP discovers, ui-core implements; server-driven UI still needs typed contracts (your breach audit: raw tool metadata)
Saved workflows → known routes	Logical route registry doc + partial OS-core loading	Enforce one routeId vocabulary across App.tsx, AdminShell, menus (4 rollout)
8. Recommendations — highest and best use in Cursor
Treat the four research roles as fixed skill templates
Keep 0_cursor_research_pack.md as the master coordinator; implement as four saved Cursor prompts or skills (Cartographer, Capability Extractor, Breach Auditor, Migration Planner) that are read-only on code during research phases—matching your pack exactly.

Operational pipeline: linter → review → (then) implementation
For any registry/route/view/action change: run governance-linter → governance-review → only then code. This matches your “capabilities and boundaries” direction better than free-form agent chat.

Single “UI task” entry: shadcn MCP + shadcn-ui-agent + mui-foundation
Workflow: MCP search → check gateway-sdk-manifest.yaml → add/extend Sovereign* in ui-core → optional ui_agent dispatch with review_required. That preserves dynamic discovery without violating “no raw shadcn in product code.”

MCP hygiene
Align mcp.json with mcp.example.json policy (Twilio optional block), ensure no real keys in committed JSON, document which servers are required vs optional per role (devops vs UI vs data).

Fix or retire stale slash commands
Update /map-project to match actual imports (./services/toolHandler) and current voice file layout; make PM2 IDs in /verify-health parameterized or doc-linked so they are not wrong on every machine.

Connect npm “aptitude” scripts to your agent rating story
Promote test:voice-concierge-aptitude and test:local-agent-aptitude (plus validate:skill-identity) to the same reporting channel as governance linter output (e.g. one folder, one schema), so “failing agent” = failed scenario + violation type, not subjective review.

Sub agents: use sparingly with explicit handoffs
Use Cursor parallel agents for isolated research (explore codebase, run tests) with a single integrator turn that merges into your registries—avoid 4 agents all editing the same files.

Voice / Gemini changes stay behind explicit tasks
Keep lockdown rules; schedule canvas_grounding, buyerJourney order, and registry deduplication as governed voice/control-plane tasks per 3 and 4.

9. Closing mapping: “human prompts” → “capabilities”
Your research (2, 3, 4) already states the migration: collapse duplicate tables (views, tools, menus, TIER1 rules, skill enum vs YAML) and attach enforcement so the same rows drive docs, lint, and runtime. The Cursor layer should enforce that narrative:

Rules = absolute boundaries (security, voice, routing monolith ban).
Skills = procedures and roles (research agents, review, UI promotion, domain runbooks).
MCP = external capabilities (data, components, workspace) behind allowlists and wrappers.
Commands/scripts = measurable proficiency and health.
If you want this report as a committed doc under docs-governance/worklogs/ or user_uploads/, say where to place it and I can add the file in a follow-up.

Research citations: 0_cursor_research_pack.md, 1_cartography_report.md, 2_implicit_capability_report.md, 3_governance_breach_audit.md, 4_registery_migration_planner.md, CURSOR_RULES_INDEX.md.

---

## Canonical successor (2026-03-27)

Execution source of truth and doctrine live under `docs-governance/canonical/`:

- `GOVERNANCE_EXECUTION_PLAN_V1.md` — phased plan (active tracker)
- `REGISTRY_AUTHORITY_CHARTER.md` — registry authority
- `AGENT_CAPABILITY_SPEC_V0.md` — agent capability schema v0

Phase 3 work started: website-chat `buyerJourney` load order; `canvas_grounding` forward in `geminiVoice.ts`.
# Product implementation snapshot — ai-os-voice-interface

**Generated:** 2026-04-08
**Source root:** `C:\Apps\ai-os-voice-interface`

This file is **informative** for **peer review** of Workspace / integration **AMD** and **SPEC** text. It concatenates **current** TypeScript sources so reviewers can align governance claims with **implemented** intents, scope classes, and MCP mapping. Regenerate before binding review rounds when the product repo changes.

---

## File: `WORKSPACE.md`

```
# Google Workspace integration (governed)

This app implements **AIOS-SPEC-007** (`governing_docs/specifications/GoogleWorkspaceIntegrationGovernance.md`): intents route through the **Workspace Intent Router → Integration Control Plane → MCP Adapter**; the voice/agent layer does **not** call Google Workspace MCP tools directly.

## MCP adapter (HTTP)

The browser calls **`runWorkspaceControlPlane` → `callWorkspaceMcpAdapter`** only. The adapter performs streamable **initialize** → **`Mcp-Session-Id`** → **`tools/call`** to `{VITE_WORKSPACE_MCP_URL}{VITE_WORKSPACE_MCP_JSONRPC_PATH}` with **`Accept: application/json, text/event-stream`**. Governed **intent** ids are mapped to **server tool names** in **`src/workspace/mcpIntentToolMap.ts`** (not raw `workspace.*` strings).

### Browser vs Gateway Node (CORS)

| Path | CORS? | Env (typical) |
|------|--------|----------------|
| **This app** — `fetch` from the browser to `mcp.*` | Yes — cross-origin unless MCP sends **`Access-Control-Allow-Origin`** or you use the Vite **`/__workspace_mcp`** proxy in dev | **`VITE_WORKSPACE_MCP_URL`**, **`VITE_WORKSPACE_MCP_*`** |
| **Gateway (or similar)** — UI → same-origin **`/api/...`** → Node calls MCP | No — server-side `fetch` is not browser CORS | **`WORKSPACE_MCP_URL`**, **`WORKSPACE_MCP_ADAPTER_MODE`** (e.g. `external_mcp`), plus a streamable client (**`initialize`**, **`Mcp-Session-Id`**, **`Accept`**) in that codebase |

This repo implements only the **first** row. A Node `workspaceMcpAdapter` / `mcpStreamableHttpClient` lives with the API server that serves **`/api`**, not here.

### Troubleshooting: “MCP initialize did not return Mcp-Session-Id”

Browsers **hide** custom response headers on cross-origin responses unless the MCP (or nginx in front of it) sends **`Access-Control-Expose-Headers`** listing **`mcp-session-id`** (see [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers)). The adapter reads **`Mcp-Session-Id`** from **`initialize`**; if JavaScript cannot see it, transport setup fails even when the server sent the header.

**Local dev (usual fix):** Use the **same-origin** Vite proxy so the browser talks to `http://localhost:5173`, not directly to `https://mcp…`:

1. Create or edit **`.env.development.local`** (gitignored) in the app root.
2. Set **`VITE_WORKSPACE_MCP_URL=/__workspace_mcp`** (and keep your real MCP base in `.env.local` for production builds if needed).
3. Restart **`npm run dev`**.

`vite.config.ts` maps **`/__workspace_mcp`** → **`VITE_WORKSPACE_MCP_PROXY_TARGET`** (default `https://mcp.gatewayglobal.ai`) with path rewrite to **`/googleworkspace`**. No CORS header exposure is required for the browser to read response headers from the **same** origin.

**Hosted MCP without proxy:** Add nginx (or equivalent) **`Access-Control-Expose-Headers: mcp-session-id`** on the MCP vhost. See **`docs/workspace-mcp-nginx-deploy.md`**.

### FastMCP streamable HTTP — which “session”?

On **FastMCP streamable HTTP**, errors like **“Missing session ID”** refer to the **MCP transport** session, not a React session, not LLM `_meta.session_id`, and not the optional audit **`session_id`** on **`WorkspaceRoutingEnvelope`**.

**Server-expected flow:**

1. **`POST`** `{base}/mcp` with **`Accept: application/json, text/event-stream`**, JSON-RPC **`initialize`**.
2. Read **`mcp-session-id`** / **`Mcp-Session-Id`** from **response headers**.
3. **`POST`** **`tools/call`** to the **same URL** with **`Mcp-Session-Id: <that value>`** and **`Authorization: Bearer <Google OAuth access token>`** for the user (from your auth layer / env such as **`WORKSPACE_MCP_BEARER_TOKEN`** on the server — not something the LLM fabricates).

There is **no** standard need to stuff transport state into **`params._meta`** for this; the transport session is the **`Mcp-Session-Id`** header after **`initialize`**.

**Where it should run:** The handshake belongs in a **server** adapter (e.g. Gateway **`executeWorkspaceGovernedAction` → `callMcpToolStreamableHttp`** in **`server/services/mcpStreamableHttpClient.ts`**). *In that file, “session” means MCP **`mcp-session-id`**, not app user session — avoid regressing to the wrong model.*

**This repo’s browser adapter** (**`callWorkspaceMcpAdapter`**) runs **`initialize` → session → `tools/call`** and sends **`Authorization: Bearer`** from the in-tab GIS session (**Sign in with Google**) when present, else from **`VITE_WORKSPACE_MCP_BEARER_TOKEN`** / **`VITE_GOOGLE_OAUTH_ACCESS_TOKEN`** in **`.env.local`** (dev-only fallback; do not ship static tokens in production client bundles).

### Google Cloud Console — Web client for Sign in with Google (this app)

For **`VITE_GOOGLE_OAUTH_CLIENT_ID`** (OAuth 2.0 client type **Web application**):

| Field | Typical values |
|--------|----------------|
| **Authorized JavaScript origins** | `http://localhost:5173`, `http://127.0.0.1:5173`, and your production app origin (`https://your.domain`). Required for [Google Identity Services](https://developers.google.com/identity/gsi/web) token client. |
| **Authorized redirect URIs** | Not required for the GIS **token** popup flow used here; add redirect URIs only if you add a server-side OAuth code flow later. |

Use the **same Google Cloud project** as your Workspace MCP’s **`GOOGLE_OAUTH_CLIENT_ID`** when you want tokens accepted by the MCP (or ensure the MCP validates tokens for that client / project per its docs).

### OAuth 2.1 — bearer token source

With **`MCP_ENABLE_OAUTH21=true`**, the MCP expects a **valid Google access token** on **`initialize`** and **`tools/call`**. This app uses **Google Identity Services** (token client) in the browser — not a server redirect/PKCE code flow — so consent appears in Google’s popup when you click **Sign in with Google**.

- **In-app:** **Sign in with Google** in the Workspace hub / onboarding (`VITE_GOOGLE_OAUTH_CLIENT_ID` + **Authorized JavaScript origins**). The access token is kept **in memory** for the tab session and sent as **`Authorization: Bearer`** to the MCP (preferred over pasting **`VITE_WORKSPACE_MCP_BEARER_TOKEN`**).
- **Manual / CLI:** complete OAuth elsewhere (MCP host, OAuth Playground, `workspace-cli`) and optionally set **`VITE_WORKSPACE_MCP_BEARER_TOKEN`** for dev.
- **Production direction:** prefer a **backend** that stores refresh tokens; avoid shipping static bearer strings in client bundles.

**Troubleshooting — `OAuth 2.1 mode requires an authenticated user … but none was found`:** The Python server sets `authenticated_user_email` in **`AuthInfoMiddleware`** only after it can validate the Bearer token (External OAuth mode calls Google **userinfo** for `ya29.*` tokens). Fix on the **host:** set **`EXTERNAL_OAUTH21_PROVIDER=true`** (with **`MCP_ENABLE_OAUTH21=true`**) so GIS/browser tokens are accepted; ensure GIS scopes include **userinfo.email** (this app uses explicit `userinfo.email` / `userinfo.profile` in **`WORKSPACE_GIS_OAUTH_SCOPES`**); ensure **nginx** forwards **`Authorization`** to the upstream (see **[docs/workspace-mcp-nginx-deploy.md](docs/workspace-mcp-nginx-deploy.md)**). After changing scopes, use **Sign in with Google** again with **`prompt: 'consent'`** (or **Refresh token**) so Google re-issues a token with the new scopes.

**Troubleshooting — Drive `403` / `insufficient authentication scopes`:** The access token must include **`https://www.googleapis.com/auth/drive.readonly`** (see **`WORKSPACE_GIS_OAUTH_SCOPES`** in **`src/workspace/workspaceSessionAuth.ts`**). If you signed in before Drive was added to the app, **Sign out**, then **Sign in with Google** again so the consent screen includes Drive. In **Google Cloud Console**, ensure **Google Drive API** is enabled for the project and the OAuth consent screen lists the Drive readonly scope if your app is in testing / verification.

**Troubleshooting — Contacts / People API `403` / `ACCESS_TOKEN_SCOPE_INSUFFICIENT`:** Include **`https://www.googleapis.com/auth/contacts.readonly`** in GIS scopes (same file). **`search_contacts`** uses **People API** — add the contacts readonly scope to the OAuth consent screen if required, then **Sign out** and **Sign in with Google** again to re-consent.

**Troubleshooting — `SERVICE_DISABLED` / “People API has not been used in project … or it is disabled”:** This is **not** an OAuth/nginx issue. In **Google Cloud Console**, open the **same project number** shown in the error (or the project that owns the OAuth client / credentials used to call Google) and **enable** the API (e.g. **People API** for Contacts). Wait a few minutes after enabling, then retry. The error often includes a direct **activation** link to that project.

**Troubleshooting — Web search / `search_custom` / `GOOGLE_PSE_API_KEY` not set:** Enabling **Custom Search API** in Cloud Console is required but **not sufficient**. The **Workspace MCP server** (the process that runs `search_custom`) must have **`GOOGLE_PSE_API_KEY`** and **`GOOGLE_PSE_ENGINE_ID`** in **its** environment — create an API key with Custom Search API access, create a [Programmable Search Engine](https://programmablesearchengine.google.com/) and use its **Search engine ID** (`cx`). Restart the MCP after changing env. These variables are **not** set in this voice app’s **`VITE_*`** files; they do not belong in the browser bundle.

## Governed web search (AMD-2026-009) — informative

This file is **informative**; normative rules are in **[AMD-2026-009](governing_docs/amendments/AMD-2026-009.md)**, **[AIOS-SPEC-007](governing_docs/specifications/GoogleWorkspaceIntegrationGovernance.md)**, **[AIOS-SPEC-009](governing_docs/specifications/IntentPrimitiveAndExecutionModel.md)**, and **[AIOS-SPEC-010](governing_docs/specifications/ExecutionScopeAndContextBounding.md)**.

- **Search scope classes** (e.g. approved domains vs **broad public**) are **policy** — not ad hoc query parameters alone. **`web.search.broad_public`** is **non-default** and trigger-gated per the amendment §4.
- **Retrieval backend:** **PSE / Custom Search** is one supported path; **[AMD-2026-009-ADD-001](governing_docs/amendments/AMD-2026-009-ADD-001-retrieval-backend-neutrality.md)** (draft) allows **policy-registered** alternatives (e.g. vendor **Gemini** / **OpenAI** grounding APIs) when Council ratifies the addendum and the MCP product wires them — credentials remain **server-side** only.
- **PSE / Custom Search** credentials stay on the **MCP host** (see troubleshooting above). The voice app remains a **Phase 1 bridge** (`workspace.web.search` → MCP `search_custom`); full **result-set review**, **SPEC-010** logical keys, and **§9** audit fields land with the **post-ratification** implementation slice ([merge plan](governing_docs/amendments/AMD-2026-009-merge-deltas-and-first-slice.md) Part B).

## Phase 1

- **Read plane** intents only (`src/workspace/intentRegistry.ts`).
- **Layer 2 → Layer 1:** each intent maps to exactly one `workspace.google.*` scope class (`src/workspace/scopeClasses.ts`).
- UI shells: `workspace_hub`, `workspace_calendar_hub`, `workspace_mail_hub` (canvases in `src/overlays/WorkspaceHubSurface.tsx`). Mail search (`workspace.mail.search` on load) — spec & QA: **[docs/workspace-gmail-read-search-slice.md](docs/workspace-gmail-read-search-slice.md)**, **[docs/workspace-gmail-read-qa.md](docs/workspace-gmail-read-qa.md)**.

## Configuration

| Variable | Purpose |
|----------|---------|
| `VITE_GOOGLE_OAUTH_CLIENT_ID` | OAuth 2.0 **Web** client ID for in-app Sign in with Google (GIS). Needs **Authorized JavaScript origins** for your dev/prod URLs. |
| `VITE_WORKSPACE_MCP_URL` | Base URL of the external Google Workspace MCP server. If unset, the MCP adapter returns `not_configured`. |
| `VITE_WORKSPACE_MCP_JSONRPC_PATH` | Optional. Path for JSON-RPC `POST` (default `/mcp`). The adapter sends `tools/call` for intents such as `workspace.calendar.list`. |
| `VITE_WORKSPACE_MCP_TIMEOUT_MS` | Optional. Request timeout in ms (default `30000`). |
| `VITE_WORKSPACE_MCP_PROXY` | Optional. Set **`false`** to disable the **`/__workspace_mcp`** dev proxy in **`vite.config.ts`**. |
| `VITE_WORKSPACE_MCP_PROXY_TARGET` | Optional. Override proxy upstream (default **`https://mcp.gatewayglobal.ai`**). |
| `VITE_WORKSPACE_MCP_BEARER_TOKEN` | Optional. Google OAuth **access token** (`ya29…`) for MCP OAuth 2.1. **Local dev only** — unsafe in shipped production bundles. |
| `VITE_GOOGLE_OAUTH_ACCESS_TOKEN` | Optional alias for **`VITE_WORKSPACE_MCP_BEARER_TOKEN`**. |
| `VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL` | If **`true`**, send **`user_google_email`** in tool args (legacy single-user MCP). Default: omit (OAuth 2.1). |
| `VITE_AIOS_GOOGLE_USER_EMAIL` | Used only when **`VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL=true`**. |

In **this repo**, define **`VITE_*`** in **`.env.local`** (see **`.env.example`**). The MCP server’s **`GOOGLE_OAUTH_*`** and other host secrets belong only on the server’s **`.env`**, not in the voice app.

**Local dev vs CORS:** A **`fetch`** from **`http://localhost:5173`** to **`https://mcp.…`** is cross-origin; without **`Access-Control-Allow-Origin`** on the MCP host, the browser reports **Failed to fetch** and the adapter returns **`http_error`**. For development, set **`VITE_WORKSPACE_MCP_URL=/__workspace_mcp`** — Vite proxies **`/__workspace_mcp`** → **`https://mcp.gatewayglobal.ai/googleworkspace`** (see **`vite.config.ts`**). **Production** builds should use the full **`https://…/googleworkspace`** URL; configure **CORS** on nginx (or the MCP) for your app origin — **[docs/workspace-mcp-nginx-deploy.md](docs/workspace-mcp-nginx-deploy.md)**.

## MCP server deployment (Phase 1)

**Server source (Gateway org):** **[gateway-global-ai/aios_google_workspace_mcp](https://github.com/gateway-global-ai/aios_google_workspace_mcp)** — maintained fork of the Google Workspace MCP stack (includes `Dockerfile`, `docker-compose.yml`, Helm under `helm-chart/workspace-mcp`, and upstream-aligned docs for **`--transport streamable-http`**, OAuth 2.1, stateless mode, and **`WORKSPACE_EXTERNAL_URL`** behind a reverse proxy). Pin a release tag or commit in your deployment layer when upgrading.

**Target shape:** host that server as its **own service** on the **same machine** as the AI OS app (or same private network), not inside this frontend repo.

| Piece | Recommendation |
|--------|----------------|
| **Process** | Separate container or systemd unit; **independent** restart/deploy from `ai-os-voice-interface`. |
| **Listen** | **`127.0.0.1:<port>`** (or private interface only) until you intentionally expose it behind TLS. |
| **Port** | Any free port (e.g. **8787** or **8000**). Avoid colliding with other local services (an optional local documents server example may use **8100** in `README.md`). |
| **Transport** | **Streamable HTTP** where the upstream supports it; align **`VITE_WORKSPACE_MCP_JSONRPC_PATH`** with the server’s JSON-RPC POST path (default **`/mcp`** in this app). |
| **Auth model** | **OAuth 2.1 multi-user** and **stateless** mode per upstream docs — suitable for central hosting. Do **not** use **`--single-user`** for production central hosting (see SPEC-007). |

### Google OAuth scopes (MCP server)

The Google Cloud **OAuth consent screen** can list many APIs/scopes you approved for the project. The MCP host does **not** necessarily request every scope on each sign-in. In **[aios_google_workspace_mcp](https://github.com/gateway-global-ai/aios_google_workspace_mcp)**, **`get_scopes_for_tools()`** builds the requested set from:

- **`BASE_SCOPES`**, plus  
- scopes for **only the tools you enabled** (see **`TOOL_SCOPES_MAP`**), using either the full map or **`TOOL_READONLY_SCOPES_MAP`** when read-only mode is on.

If **granular permissions** mode is active, scope selection uses **`get_all_permission_scopes()`** instead (see the same module and **`auth/permissions.py`**).

So the Console configuration is the **universe** of scopes the MCP *may* use; the consent flow reflects the **subset** for your enabled tools plus base identity scopes, modulated by read-only vs full access, or granular permissions, as configured on the server.

#### Google Cloud Console — align scopes with the fork (`scopes.py`)

Canonical OAuth scope strings are defined in **[aios_google_workspace_mcp](https://github.com/gateway-global-ai/aios_google_workspace_mcp)** (e.g. **`scopes.py`**, **`TOOL_SCOPES_MAP`**, **`SCRIPT_SCOPES`**). Do **not** add scopes in Cloud Console just because the API picker lists them unless this server actually requests them. There is no **`https://mail.google.com/`**, no **`gmail.addons.*`**, no **`gmail.insert`**, no **`cloud-platform`**, and no extra Calendar rows (e.g. `calendar.app.created`, `calendar.acls*`, `calendar.calendarlist*`, `calendar.calendars`, `calendar.events.freebusy`, `calendar.events.public.readonly`) in that code path — only the **Calendar** scope strings the fork lists (typically three strings; broader `calendar` may subsume many narrower ones for Google’s verification UI, but **`get_scopes_for_tools()`** only asks for the strings in **`scopes.py`**).

| Often added by mistake | Notes |
|------------------------|--------|
| `.../auth/gmail.addons.current.*` | Gmail **add-on** scopes — not used by this MCP. |
| `.../auth/cloud-platform` | Entire GCP account — not required for Workspace APIs; remove unless another product needs it. |
| `https://mail.google.com/` | Full Gmail — MCP uses granular **`gmail.*`** from **`scopes.py`**, not this URL. |
| `.../auth/gmail.insert` | Not in **`scopes.py`**. |
| Extra Calendar scopes (see list above) | Not the strings in **`scopes.py`**; keep Calendar rows aligned with the fork only. |
| Extra Drive (`drive.metadata*`, `drive.meet.readonly`, `drive.activity*`, `drive.scripts`, …) | MCP Drive usage is **`drive` / `drive.readonly` / `drive.file`** only; Apps Script uses **`script.*`** via **`SCRIPT_SCOPES`**, not **`drive.scripts`**. |

**Practical recommendation:** Align the OAuth client with **`BASE_SCOPES` ∪ scopes from `get_scopes_for_tools()`** for your enabled tools (full vs **`TOOL_READONLY_SCOPES_MAP`**, or granular **`auth/permissions.py`**). Easiest check: run the server once and inspect the **auth URL** or logs, or print **`get_scopes_for_tools()`** for your **`tools_to_import`**. Remove unused rows to reduce verification burden and consent friction. Narrow **`--tools` / `--tool-tier` / `--read-only` / `--permissions`** in **`main.py`** (per upstream) and drop the matching API scopes from the client so consent stays minimal.

**Separate deployment repo (recommended):** keep **only** your ops layer next to a **clean clone, git submodule, or pinned fork** of **[aios_google_workspace_mcp](https://github.com/gateway-global-ai/aios_google_workspace_mcp)**, with the server checkout **pinned** by tag or commit:

- `docker-compose.yml` and/or **systemd** unit
- **`.env`** / secrets (never committed); document required variables
- **Reverse-proxy** notes (path prefix, TLS, upstream to `127.0.0.1:<port>`) for when you move to a public hostname
- **`README.md`**: how to run, upgrade upstream, rotate credentials

That gives **clean upgrades**, **separation** from this UI repo, and an **easier** later move to a public URL (change proxy + rebuild or reconfigure the app’s MCP base URL).

**This app’s wiring:** set **`VITE_WORKSPACE_MCP_URL`** to the base URL the **browser** can reach (e.g. `https://mcp.internal.example.com` behind the proxy, or `http://127.0.0.1:8787` for local dev). Values are **build-time** in Vite — set them in the environment used for `npm run build` (or dev server) for each deployment target.

**Phase 1 order of operations (deploy → QA → UX):** **[docs/workspace-mcp-phase1-checklist.md](docs/workspace-mcp-phase1-checklist.md)**.  
**Example — `mcp.gatewayglobal.ai` + path `/googleworkspace/`:** nginx, Certbot, systemd, paths under `/opt/gatewayglobal/…` — **[docs/workspace-mcp-nginx-deploy.md](docs/workspace-mcp-nginx-deploy.md)**.

## Legal pages — source of truth vs app rendering

**Canonical policy text** (Privacy Policy and Terms of Service) lives in **`governing_docs/legal/`**, not as authoritative copy inside app repos:

| ID | Document | Canonical file |
|----|----------|------------------|
| **LEGAL-001** | Privacy Policy | [`governing_docs/legal/LEGAL-001-Privacy-Policy.md`](governing_docs/legal/LEGAL-001-Privacy-Policy.md) |
| **LEGAL-002** | Terms of Service | [`governing_docs/legal/LEGAL-002-Terms-of-Service.md`](governing_docs/legal/LEGAL-002-Terms-of-Service.md) |

**Registry and workflow** (draft → review → counsel → ratify → mirror to app): **[`governing_docs/legal/README.md`](governing_docs/legal/README.md)**.

**App repo(s)** own routes and presentation only — e.g. Gateway web client: `PrivacyPolicy.tsx`, `TermsOfService.tsx`, `App.tsx` routes. **Mirror** approved text from the governed files; keep versions in sync. Placeholder or interim copy in the app is **provisional** until **`approved_for_publication`** (or equivalent) in front matter and an explicit sync.

These documents are public promises, compliance inputs, and OAuth verification inputs; follow the same governance discipline as other controlled artifacts.

## Google OAuth consent screen — Privacy & Terms URLs

Google Cloud **OAuth consent screen** (and similar forms) often require **Application home page**, **Privacy Policy**, and **Terms of Service** URLs. When the production site behind **gatewayglobal.ai** serves those routes:

| Page | Path | Canonical URL |
|------|------|-----------------|
| Privacy Policy | `/privacy` | `https://gatewayglobal.ai/privacy` |
| Terms of Service | `/terms` | `https://gatewayglobal.ai/terms` |

If you only deploy to a **dev** host first, use the same paths on that origin, e.g. `https://<dev-host>/privacy` and `https://<dev-host>/terms`.

**Implementation reference:** `aibizbot-dev.gatewayglobal.ai` — `client/src/pages/legal/`, routes in `client/src/App.tsx`. This voice app repo does not ship those pages; use the URLs above in Google Cloud when the Gateway app serves **gatewayglobal.ai**.

**Legal:** Do not treat any deployed page as **compliance-final** until counsel has reviewed the **governed** documents in **`governing_docs/legal/`** and the app reflects that approved revision.

## Pre–Workplace Phase 1 gate

Before calling Workplace integration **live** or **production-ready**, satisfy **[docs/pre-workplace-checklist.md](docs/pre-workplace-checklist.md)** (secret boundary, structured intent routing, no MCP bypasses).

## Phase 1 calendar read — QA

Manual QA for the first governed read path: **[docs/workspace-calendar-read-qa.md](docs/workspace-calendar-read-qa.md)**.

## Phase 1 Gmail read / search — slice spec & QA

Intent-level spec and test checklist (same architecture as calendar): **[docs/workspace-gmail-read-search-slice.md](docs/workspace-gmail-read-search-slice.md)**, **[docs/workspace-gmail-read-qa.md](docs/workspace-gmail-read-qa.md)**.

## Local and sovereign runtime lanes — Workspace Domain Pack v1

**AIOS-SPEC-007** covers **retrieval and execution** via MCP (Gmail search, message read, thread content, drafts). **Interpretation** of retrieved text **SHALL** use the **Local Interpretation Lane** by default (**AIOS-SPEC-009 §16**). **Sovereign voice** (speech-input and speech-output) **SHALL** follow **AIOS-SPEC-009 §17** when the product claims local-first voice.

**Normative runtime standards**

| Lane | Standard |
|------|----------|
| Interpretation (local LLM) | **[`OLLAMA_RUNTIME_STANDARD.md`](governing_docs/operations/OLLAMA_RUNTIME_STANDARD.md)** |
| Speech-input (STT) | **[`WHISPER_RUNTIME_STANDARD.md`](governing_docs/operations/WHISPER_RUNTIME_STANDARD.md)** |
| Speech-output (TTS) | **[`LOCAL_TTS_RUNTIME_STANDARD.md`](governing_docs/operations/LOCAL_TTS_RUNTIME_STANDARD.md)** |

**Canonical registry IDs (AMD-2026-008):** **AIOS-OPS-001** = Ollama standard, **AIOS-OPS-002** = Whisper STT standard, **AIOS-OPS-003** = local TTS standard (each file’s YAML lists `registry_id`).

### Capability registry (informative — align code with this table)

| `id` | `domain` | `plane` | `lane` | `runtime` | `fallbackPolicy` | Disclosure |
|------|------------|---------|--------|-----------|------------------|------------|
| `local.stt.transcribe` | `shell.voice`, `session` | `read` (input) | `local` | `whisper` / `faster-whisper` | `proposal` or `block` if remote disallowed | **SHALL** show STT readiness when §17 sovereign voice is active; **WHISPER_RUNTIME_STANDARD** |
| `local.tts.speak` | `shell.voice`, `session` | `read` (output) | `local` | `local_tts` (engine-specific) | same | **SHALL** show TTS readiness; **LOCAL_TTS_RUNTIME_STANDARD** |
| `local.llm.summarize` | `workspace.mail`, `workspace.calendar` | `read` | `local` | `ollama` | `proposal_required` or `block` if remote disallowed | Shell + operator; **OLLAMA_RUNTIME_STANDARD**. **Output:** `ThreadSummaryV1` + `summarySchema: "thread_summary_v1"`; `interpretation_invalid` on parse failure. |
| `local.llm.classify` | `workspace.mail` | `read` | `local` | `ollama` | same | As above. |
| `local.llm.extract_actions` | `workspace.mail` | `read` | `local` | `ollama` | same | As above. |
| `local.llm.propose_reply` | `workspace.mail` | `read` | `local` | `ollama` | same | Bullets or text for review; **Gmail draft** still MCP + **§15**. |

**`ui.primaryAllowed`:** `true` for interpretation outputs when local LLM readiness is `running_ready`; otherwise disclose **unavailable** per **OLLAMA_RUNTIME_STANDARD §5–6**. Same pattern for STT/TTS when wired (**§17**).

**Remote (cloud STT/TTS/Gemini):** only per **AIOS-SPEC-009 §16.4** and **§17.4** — explicit user choice, policy, or documented escalation — **never** silent substitution for sovereign / local-first lanes (**POL-LANE-VOICE-001**, **POL-MODEL-002**–**004**).

## Related documents

- **Privacy / Terms:** governed source — **[`governing_docs/legal/`](governing_docs/legal/)** (`LEGAL-001`, `LEGAL-002`); public URLs — § *Legal pages* / *Google OAuth consent screen* above.
- **Intent lifecycle / discovery / onboarding:** [`AIOS-SPEC-008`](governing_docs/specifications/IntentDiscoveryOnboardingFramework.md) — frames how Workspace-dependent intents evolve (dependency mapping, onboarding states, promotion path); extends [`AIOS-SPEC-007`](governing_docs/specifications/GoogleWorkspaceIntegrationGovernance.md) per the spec appendix.
- **Intent primitive (core execution object):** [`AIOS-SPEC-009`](governing_docs/specifications/IntentPrimitiveAndExecutionModel.md) — schema, lifecycle, UI contract, governance chain, **§16 local interpretation lane**; align with [`AMD-2026-007`](governing_docs/amendments/AMD-2026-007.md) for shell/policy scaffolding.
- **Local Ollama runtime (operations):** [`OLLAMA_RUNTIME_STANDARD`](governing_docs/operations/OLLAMA_RUNTIME_STANDARD.md) — readiness, fallback, disclosure (**POL-MODEL-001**–**004**).
- **Sovereign voice (operations):** [`WHISPER_RUNTIME_STANDARD`](governing_docs/operations/WHISPER_RUNTIME_STANDARD.md), [`LOCAL_TTS_RUNTIME_STANDARD`](governing_docs/operations/LOCAL_TTS_RUNTIME_STANDARD.md) — **AIOS-SPEC-009 §17**.
- **Amendment (sovereign voice lanes):** [`AMD-2026-008`](governing_docs/amendments/AMD-2026-008.md).
- **Pre-ratification conformance:** [`AIOS-SPEC-009-CONFORMANCE-TEST-V1`](governing_docs/specifications/AIOS-SPEC-009-CONFORMANCE-TEST-V1.md) — manual + P0/P1/P2 scorecard before SPEC-009 ratification.
- Amendment (Workspace plane): `governing_docs/amendments/AMD-2026-006.md`
- AIP workspace intents: `AIOS-SPEC-003` §11
- UI surfaces: `AIOS-SPEC-006` §13

```

---

## File: `src/workspace/intentRegistry.ts`

```
/**
 * Phase 1 — read plane only (AIOS-SPEC-007 §12). Extend later phases in separate commits.
 * @license SPDX-License-Identifier: Apache-2.0
 */

export const PHASE_1_WORKSPACE_INTENTS = [
  'workspace.hub',
  'workspace.calendar.list',
  /** List events in a time window (`get_events` without `event_id`). */
  'workspace.calendar.events.list',
  'workspace.calendar.get',
  'workspace.mail.search',
  'workspace.mail.read',
  /** Full thread text (extended MCP tool — get_gmail_thread_content). */
  'workspace.mail.thread.read',
  /** MCP thread read + local.llm.summarize (read plane; governed fallback). */
  'workspace.mail.thread.summarize',
  /** Create a Gmail draft reply (draft plane; proposal-gated). */
  'workspace.mail.draft_reply',
  /** Default Drive hub load — list/search files (empty query = recent / default list per MCP). */
  'workspace.drive.list',
  'workspace.drive.search',
  'workspace.drive.read',
  'workspace.docs.read',
  'workspace.docs.export',
  /** List connections (`list_contacts`) — use for hub default load. */
  'workspace.contacts.list',
  'workspace.contacts.search',
  'workspace.tasks.list',
  'workspace.tasks.get',
  /** Google Custom Search (PSE) — requires GOOGLE_PSE_* on MCP host. */
  'workspace.web.search',
] as const;

export type Phase1WorkspaceIntent = (typeof PHASE_1_WORKSPACE_INTENTS)[number];

export function isPhase1WorkspaceIntent(s: string): s is Phase1WorkspaceIntent {
  return (PHASE_1_WORKSPACE_INTENTS as readonly string[]).includes(s);
}

```

---

## File: `src/workspace/scopeClasses.ts`

```
/**
 * Layer 1 scope classes + mandatory one-to-one mapping from Layer 2 intents.
 * @license SPDX-License-Identifier: Apache-2.0
 */

import type { WorkspaceScopeClass } from './types';
import { PHASE_1_WORKSPACE_INTENTS, type Phase1WorkspaceIntent } from './intentRegistry';

/** Canonical Layer 1 values (for policy and UI). */
export const WORKSPACE_SCOPE_CLASSES: readonly WorkspaceScopeClass[] = [
  'workspace.google.read',
  'workspace.google.write',
  'workspace.google.send',
  'workspace.google.share',
  'workspace.google.automation',
  'workspace.google.identity',
  'workspace.google.search',
] as const;

/**
 * Single source of truth: each Phase 1 intent maps to exactly one scope class.
 * SPEC-007: one intent → one scope class — no multi-label intents.
 */
export const INTENT_TO_SCOPE_CLASS: Record<Phase1WorkspaceIntent, WorkspaceScopeClass> = {
  'workspace.hub': 'workspace.google.read',
  'workspace.calendar.list': 'workspace.google.read',
  'workspace.calendar.events.list': 'workspace.google.read',
  'workspace.calendar.get': 'workspace.google.read',
  'workspace.mail.search': 'workspace.google.read',
  'workspace.mail.read': 'workspace.google.read',
  'workspace.mail.thread.read': 'workspace.google.read',
  'workspace.mail.thread.summarize': 'workspace.google.read',
  'workspace.mail.draft_reply': 'workspace.google.write',
  'workspace.drive.list': 'workspace.google.read',
  'workspace.drive.search': 'workspace.google.read',
  'workspace.drive.read': 'workspace.google.read',
  'workspace.docs.read': 'workspace.google.read',
  'workspace.docs.export': 'workspace.google.read',
  'workspace.contacts.list': 'workspace.google.identity',
  'workspace.contacts.search': 'workspace.google.identity',
  'workspace.tasks.list': 'workspace.google.read',
  'workspace.tasks.get': 'workspace.google.read',
  'workspace.web.search': 'workspace.google.search',
};

function assertOneToOneMapping(): void {
  const seen = new Set<string>();
  for (const k of PHASE_1_WORKSPACE_INTENTS) {
    if (seen.has(k)) throw new Error(`Duplicate intent in registry: ${k}`);
    seen.add(k);
  }
  for (const intent of PHASE_1_WORKSPACE_INTENTS) {
    if (!INTENT_TO_SCOPE_CLASS[intent]) {
      throw new Error(`Missing scope class for intent: ${intent}`);
    }
  }
}

assertOneToOneMapping();

export function resolveScopeClass(intent: string): WorkspaceScopeClass | null {
  if (intent in INTENT_TO_SCOPE_CLASS) {
    return INTENT_TO_SCOPE_CLASS[intent as Phase1WorkspaceIntent];
  }
  return null;
}

```

---

## File: `src/workspace/mcpIntentToolMap.ts`

```
/**
 * Maps AIOS Phase 1 **intent** ids to **[gateway-global-ai/aios_google_workspace_mcp](https://github.com/gateway-global-ai/aios_google_workspace_mcp)** tool names
 * (`list_calendars`, `search_gmail_messages`, …). The MCP server does not register tools under `workspace.*` strings.
 *
 * **OAuth 2.1 / HTTP:** FastMCP exposes tools **without** `user_google_email` in JSON-RPC `arguments` — the account
 * comes from **`Authorization: Bearer`**. Passing `user_google_email` causes Pydantic **unexpected_keyword_argument**.
 *
 * **Legacy single-user** MCP: set **`VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL=true`** and **`VITE_AIOS_GOOGLE_USER_EMAIL`** so
 * `user_google_email` is sent (older servers that still require it in tool args).
 *
 * @license SPDX-License-Identifier: Apache-2.0
 */

import type { WorkspaceRoutingEnvelope } from './types';

/** Common copy-paste mistake: `.env` value set to the variable name instead of a real address. */
function isInvalidGoogleEmailPlaceholder(s: string): boolean {
  return s.trim().toLowerCase() === 'vite_workspace_google_user_email';
}

const GOOGLE_EMAIL_ENV_KEYS = ['VITE_AIOS_GOOGLE_USER_EMAIL', 'VITE_WORKSPACE_GOOGLE_USER_EMAIL'] as const;

export function getWorkspaceGoogleUserEmail(): string | null {
  const env = import.meta.env as Record<string, string | boolean | undefined>;
  for (const key of GOOGLE_EMAIL_ENV_KEYS) {
    const v = env[key];
    if (typeof v !== 'string' || !v.trim()) continue;
    const t = v.trim();
    if (isInvalidGoogleEmailPlaceholder(t)) continue;
    return t;
  }
  return null;
}

function includeUserGoogleEmailInMcpArgs(): boolean {
  const v = (import.meta.env as Record<string, string | undefined>).VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL;
  return typeof v === 'string' && v.trim().toLowerCase() === 'true';
}

export type ResolvedWorkspaceMcpCall =
  | { ok: true; tool: string; args: Record<string, unknown> }
  | { ok: false; message: string };

/**
 * Resolve governed intent → MCP `tools/call` name + arguments expected by the Python server.
 */
export function resolveWorkspaceMcpToolCall(envelope: WorkspaceRoutingEnvelope): ResolvedWorkspaceMcpCall {
  const passEmail = includeUserGoogleEmailInMcpArgs();
  const email = passEmail ? getWorkspaceGoogleUserEmail() : null;
  if (passEmail && !email) {
    return {
      ok: false,
      message:
        'VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL=true requires VITE_AIOS_GOOGLE_USER_EMAIL (or VITE_WORKSPACE_GOOGLE_USER_EMAIL) for legacy MCP tool args.',
    };
  }

  const userFields: Record<string, unknown> = passEmail && email ? { user_google_email: email } : {};
  const { intent } = envelope;

  switch (intent) {
    case 'workspace.calendar.list':
      return { ok: true, tool: 'list_calendars', args: { ...userFields } };

    case 'workspace.calendar.events.list': {
      const calId = envelope.resource_ref?.id?.trim() || envelope.resource_ref?.calendarId?.trim() || 'primary';
      const tr = envelope.calendar_time_range;
      if (!tr?.time_min?.trim() || !tr?.time_max?.trim()) {
        return {
          ok: false,
          message:
            'workspace.calendar.events.list requires calendar_time_range.time_min and time_max (RFC3339), and resource_ref.id (calendar id, or omit for primary).',
        };
      }
      return {
        ok: true,
        tool: 'get_events',
        args: {
          ...userFields,
          calendar_id: calId,
          time_min: tr.time_min.trim(),
          time_max: tr.time_max.trim(),
          max_results: 50,
        },
      };
    }

    case 'workspace.calendar.get': {
      const eventId = envelope.resource_ref?.id?.trim();
      if (!eventId) {
        return { ok: false, message: 'workspace.calendar.get requires resource_ref.id (calendar event id).' };
      }
      const calendarId = envelope.resource_ref?.calendarId?.trim() || 'primary';
      return {
        ok: true,
        tool: 'get_events',
        args: {
          ...userFields,
          calendar_id: calendarId,
          event_id: eventId,
        },
      };
    }

    case 'workspace.mail.search':
      return {
        ok: true,
        tool: 'search_gmail_messages',
        args: {
          ...userFields,
          query: envelope.query ?? '',
          page_size: 10,
        },
      };

    case 'workspace.mail.read': {
      const mid = envelope.resource_ref?.id?.trim();
      if (!mid) {
        return { ok: false, message: 'workspace.mail.read requires resource_ref.id (Gmail message id).' };
      }
      return {
        ok: true,
        tool: 'get_gmail_message_content',
        args: { ...userFields, message_id: mid },
      };
    }

    /** Extended tier on aios_google_workspace_mcp — align `args` with `gmail/gmail_tools.py` if the server errors. */
    case 'workspace.mail.thread.read': {
      const tid = envelope.resource_ref?.id?.trim();
      if (!tid) {
        return { ok: false, message: 'workspace.mail.thread.read requires resource_ref.id (Gmail thread id).' };
      }
      return {
        ok: true,
        tool: 'get_gmail_thread_content',
        args: { ...userFields, thread_id: tid },
      };
    }

    case 'workspace.mail.draft_reply': {
      const mid = envelope.resource_ref?.id?.trim();
      if (!mid) {
        return { ok: false, message: 'workspace.mail.draft_reply requires resource_ref.id (Gmail message id).' };
      }
      const body = (envelope.query ?? '').trim() || '(empty draft body)';
      const threadId = envelope.resource_ref?.threadId?.trim();
      const args: Record<string, unknown> = {
        ...userFields,
        reply_to_message_id: mid,
        body,
      };
      if (threadId) {
        args.thread_id = threadId;
      }
      return {
        ok: true,
        tool: 'draft_gmail_message',
        args,
      };
    }

    case 'workspace.drive.list':
    case 'workspace.drive.search':
      return {
        ok: true,
        tool: 'search_drive_files',
        args: {
          ...userFields,
          query: envelope.query ?? '',
          page_size: 10,
        },
      };

    case 'workspace.drive.read': {
      const fid = envelope.resource_ref?.id?.trim();
      if (!fid) {
        return { ok: false, message: 'workspace.drive.read requires resource_ref.id (Drive file id).' };
      }
      return { ok: true, tool: 'get_drive_file_content', args: { ...userFields, file_id: fid } };
    }

    case 'workspace.docs.read': {
      const docId = envelope.resource_ref?.id?.trim();
      if (!docId) {
        return { ok: false, message: 'workspace.docs.read requires resource_ref.id (Google Doc id).' };
      }
      return {
        ok: true,
        tool: 'get_doc_content',
        args: { ...userFields, document_id: docId },
      };
    }

    case 'workspace.docs.export': {
      const docId = envelope.resource_ref?.id?.trim();
      if (!docId) {
        return { ok: false, message: 'workspace.docs.export requires resource_ref.id (Google Doc id).' };
      }
      return {
        ok: true,
        tool: 'get_doc_as_markdown',
        args: { ...userFields, document_id: docId, include_comments: false },
      };
    }

    case 'workspace.contacts.list': {
      const pageToken = envelope.contacts_page_token?.trim();
      return {
        ok: true,
        tool: 'list_contacts',
        args: {
          ...userFields,
          page_size: 100,
          ...(pageToken ? { page_token: pageToken } : {}),
        },
      };
    }

    case 'workspace.contacts.search':
      return {
        ok: true,
        tool: 'search_contacts',
        args: {
          ...userFields,
          query: envelope.query ?? '',
          page_size: 30,
        },
      };

    case 'workspace.tasks.list': {
      const listId = envelope.resource_ref?.id?.trim();
      if (!listId) {
        return {
          ok: false,
          message:
            'workspace.tasks.list requires resource_ref.id (task list id from the Tasks API, e.g. after listing task lists).',
        };
      }
      return {
        ok: true,
        tool: 'list_tasks',
        args: { ...userFields, task_list_id: listId },
      };
    }

    case 'workspace.tasks.get': {
      const raw = envelope.resource_ref?.id?.trim() ?? '';
      const [taskListId, taskId] = raw.split(':').map((s) => s.trim());
      if (!taskListId || !taskId) {
        return {
          ok: false,
          message: 'workspace.tasks.get requires resource_ref.id as "taskListId:taskId".',
        };
      }
      return {
        ok: true,
        tool: 'get_task',
        args: { ...userFields, task_list_id: taskListId, task_id: taskId },
      };
    }

    case 'workspace.web.search': {
      const q = (envelope.query ?? '').trim() || '.';
      return {
        ok: true,
        tool: 'search_custom',
        args: {
          ...userFields,
          q,
          num: 10,
          start: 1,
        },
      };
    }

    default:
      return { ok: false, message: `No MCP tool mapping for intent: ${intent}` };
  }
}

```

---

## File: `src/workspace/workspaceIntentRouter.ts`

```
/**
 * Workspace Intent Router — validates Layer 2 shape and maps to canvas / scope class.
 * @license SPDX-License-Identifier: Apache-2.0
 */

import type { WorkspaceCanvasState } from '../shellCanvas/canvasTypes';
import { isPhase1WorkspaceIntent } from './intentRegistry';
import { resolveScopeClass } from './scopeClasses';

export type ParsedWorkspaceIntent = {
  intent: string;
  /** Optional hints for future MCP mapping */
  query?: string;
  resource_id?: string;
};

/**
 * Gmail **message** id for `loadWorkspacePayload` / `workspace.mail.read` only.
 * Do not use for `workspace.mail.thread.read` (thread id) or `workspace.mail.search` (uses `query`).
 */
export function workspaceMailReadMessageIdFromIntent(parsed: ParsedWorkspaceIntent): string | undefined {
  if (parsed.intent !== 'workspace.mail.read') return undefined;
  const t = parsed.resource_id?.trim();
  return t || undefined;
}

const WORKSPACE_INTENT_RE = /^workspace\.[a-z]+\.[a-z0-9_]+$/;

export function isValidWorkspaceIntentShape(intent: string): boolean {
  if (intent === 'workspace.hub') return true;
  return WORKSPACE_INTENT_RE.test(intent);
}

/**
 * Map intent → governed canvas surface (Phase 1).
 * Calendar / mail read-plane intents get dedicated hubs; others open the main workspace hub.
 */
export function workspaceIntentToCanvasView(parsed: ParsedWorkspaceIntent): WorkspaceCanvasState {
  const { intent } = parsed;
  if (!isPhase1WorkspaceIntent(intent)) {
    return { view: 'workspace_hub' };
  }
  if (intent === 'workspace.calendar.list' || intent === 'workspace.calendar.get') {
    return { view: 'workspace_calendar_hub' };
  }
  if (
    intent === 'workspace.mail.search' ||
    intent === 'workspace.mail.read' ||
    intent === 'workspace.mail.thread.read' ||
    intent === 'workspace.mail.thread.summarize' ||
    intent === 'workspace.mail.draft_reply'
  ) {
    return { view: 'workspace_mail_hub' };
  }
  if (
    intent === 'workspace.drive.list' ||
    intent === 'workspace.drive.search' ||
    intent === 'workspace.drive.read'
  ) {
    return { view: 'workspace_drive_hub' };
  }
  if (intent === 'workspace.contacts.list' || intent === 'workspace.contacts.search') {
    return { view: 'workspace_contacts_hub' };
  }
  if (intent === 'workspace.web.search') {
    return { view: 'workspace_search_hub' };
  }
  return { view: 'workspace_hub' };
}

export function routeWorkspaceIntent(parsed: ParsedWorkspaceIntent): {
  canvas: WorkspaceCanvasState;
  scopeClass: ReturnType<typeof resolveScopeClass>;
} {
  const scopeClass = resolveScopeClass(parsed.intent);
  return {
    canvas: workspaceIntentToCanvasView(parsed),
    scopeClass,
  };
}

```

---

## File: `src/workspace/integrationControlPlane.ts`

```
/**
 * Single governed entry for Workspace operations (AIOS-SPEC-007 §2 *Normative routing model*, item 1 — Intent Router → ICP → MCP Adapter).
 *
 * **Intent vs MCP tool:** Policy and audits use **`envelope.intent`** (`workspace.mail.search`, …).
 * **`resolveWorkspaceMcpToolCall`** maps to the server’s tool names (`search_gmail_messages`, …);
 * **`callWorkspaceMcpAdapter`** receives the mapped name only.
 *
 * **OAuth 2.1:** **`getSessionGoogleAccessToken()`** (GIS sign-in) or **`getWorkspaceMcpBearerTokenFromEnv()`** (**`VITE_WORKSPACE_MCP_BEARER_TOKEN`**, dev) → **`Authorization: Bearer`** on initialize + tools/call.
 *
 * **ICP boundary:** Policy + audit + `callWorkspaceMcpAdapter`. MCP **transport** session
 * (`initialize` / `Mcp-Session-Id`) is not the same as `envelope.session_id` (audit correlation).
 * FastMCP streamable HTTP needs the former; see **`mcpAdapter.ts`** header and **WORKSPACE.md**.
 *
 * @license SPDX-License-Identifier: Apache-2.0
 */

import type { WorkspaceRoutingEnvelope, WorkspaceControlPlaneResult } from './types';
import { resolveScopeClass } from './scopeClasses';
import { isPhase1WorkspaceIntent } from './intentRegistry';
import { canExecuteScopeClass } from './workspacePolicy';
import { callWorkspaceMcpAdapter, getWorkspaceMcpBearerTokenFromEnv } from './mcpAdapter';
import { getSessionGoogleAccessToken } from './workspaceSessionAuth';
import { resolveWorkspaceMcpToolCall } from './mcpIntentToolMap';
import { logWorkspaceAudit } from './workspaceAudit';
import { newWorkspaceAuditId } from './auditIds';
import { logScopeAllow, logScopeViolation } from '../scope/scopeAudit';
import { routingEnvelopeToScopeTarget } from '../scope/scopeRouting';
import { validateScopeOperation } from '../scope/validateScope';
import { getScopeMetricsSnapshot, recordScopeCheck } from '../scope/scopeMetrics';

function validateEnvelope(envelope: WorkspaceRoutingEnvelope): string | null {
  const scope = resolveScopeClass(envelope.intent);
  if (!scope) {
    return `Unknown or unregistered intent: ${envelope.intent}`;
  }
  if (scope !== envelope.policy_context.scope_class) {
    return `policy_context.scope_class (${envelope.policy_context.scope_class}) must match resolved scope (${scope}) for intent ${envelope.intent}`;
  }
  if (!isPhase1WorkspaceIntent(envelope.intent)) {
    return `Intent ${envelope.intent} is not in Phase 1 allowlist`;
  }
  return null;
}

/**
 * Execute a governed Workspace call: policy → adapter. UI shell may skip calling this until MCP is configured.
 */
export async function runWorkspaceControlPlane(
  envelope: WorkspaceRoutingEnvelope,
  options?: {
    surfaceMode?: 'public' | 'founder' | 'operator' | 'customer';
    signal?: AbortSignal;
  }
): Promise<WorkspaceControlPlaneResult> {
  const auditId = newWorkspaceAuditId();
  const err = validateEnvelope(envelope);
  if (err) {
    logWorkspaceAudit({
      intent: envelope.intent,
      scope_class: envelope.policy_context.scope_class,
      policy_decision: 'deny',
      failure_mode: 'invalid_envelope',
      detail: { message: err, auditId },
    });
    return { ok: false, code: 'invalid_intent', message: err, auditId };
  }

  const scope = resolveScopeClass(envelope.intent)!;
  const policy = canExecuteScopeClass(scope, options?.surfaceMode ?? 'founder');
  if (!policy.allowed) {
    logWorkspaceAudit({
      intent: envelope.intent,
      scope_class: scope,
      tenant_id: envelope.tenant_id,
      user_binding: envelope.user_binding,
      policy_decision: 'deny',
      detail: { reason: policy.reason, auditId },
    });
    return { ok: false, code: 'policy_denied', message: policy.reason ?? 'Policy denied', auditId };
  }

  logWorkspaceAudit({
    intent: envelope.intent,
    scope_class: scope,
    tenant_id: envelope.tenant_id,
    user_binding: envelope.user_binding,
    policy_decision: 'allow',
    execution_mode: envelope.execution_mode,
    proposed_vs_executed: envelope.execution_mode === 'execute' ? 'executed' : 'proposed',
    detail: { auditId },
  });

  const resolved = resolveWorkspaceMcpToolCall(envelope);
  if (resolved.ok === false) {
    const missingEmail =
      resolved.message.includes('VITE_AIOS_GOOGLE_USER_EMAIL') ||
      resolved.message.includes('VITE_WORKSPACE_GOOGLE_USER_EMAIL') ||
      resolved.message.includes('VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL');
    logWorkspaceAudit({
      intent: envelope.intent,
      scope_class: scope,
      policy_decision: 'allow',
      failure_mode: missingEmail ? 'not_configured' : 'invalid_envelope',
      detail: { message: resolved.message, auditId },
    });
    return {
      ok: false,
      code: missingEmail ? 'not_configured' : 'invalid_intent',
      message: resolved.message,
      auditId,
    };
  }

  if (envelope.execution_scope) {
    const target = routingEnvelopeToScopeTarget(envelope);
    if (target.ok === false) {
      logWorkspaceAudit({
        intent: envelope.intent,
        scope_class: scope,
        policy_decision: 'deny',
        failure_mode: 'scope_routing_invalid',
        detail: { message: target.message, auditId, scope_metrics: getScopeMetricsSnapshot() },
      });
      return {
        ok: false,
        code: 'scope_denied',
        message: target.message,
        auditId,
      };
    }
    const scopeCheck = validateScopeOperation({
      operation: target.operation,
      resourceKey: target.resourceKey,
      envelope: envelope.execution_scope,
    });
    if (!scopeCheck.allowed) {
      const reason = scopeCheck.reason ?? 'unknown';
      recordScopeCheck('denied');
      logScopeViolation({
        intent: envelope.intent,
        scope_class: scope,
        plan_id: envelope.execution_scope.plan_id,
        resourceKey: target.resourceKey,
        operation: target.operation,
        reason,
        envelope: envelope.execution_scope,
      });
      return {
        ok: false,
        code: 'scope_denied',
        message: `Execution scope denied: ${reason}`,
        auditId,
      };
    }
    recordScopeCheck('allowed');
    logScopeAllow({
      intent: envelope.intent,
      scope_class: scope,
      plan_id: envelope.execution_scope.plan_id,
      resourceKey: target.resourceKey,
      operation: target.operation,
    });
  }

  const bearerToken = getSessionGoogleAccessToken() ?? getWorkspaceMcpBearerTokenFromEnv();

  if (!bearerToken?.trim()) {
    logWorkspaceAudit({
      intent: envelope.intent,
      scope_class: scope,
      policy_decision: 'allow',
      failure_mode: 'auth_required',
      detail: {
        message: 'No Google access token for MCP OAuth 2.1 (Sign in with Google or env bearer).',
        auditId,
      },
    });
    return {
      ok: false,
      code: 'auth_required',
      message:
        'No Google access token for Workspace MCP. Click Sign in with Google at the top of this panel, complete the Google prompt, then open Calendar or Mail again. For dev without GIS, set VITE_WORKSPACE_MCP_BEARER_TOKEN in .env.local and restart the dev server.',
      auditId,
    };
  }

  const adapterResult = await callWorkspaceMcpAdapter({
    tool: resolved.tool,
    args: resolved.args,
    bearerToken,
    signal: options?.signal,
  });

  if (adapterResult.ok === false) {
    const { code, message } = adapterResult;
    logWorkspaceAudit({
      intent: envelope.intent,
      tool: resolved.tool,
      scope_class: scope,
      policy_decision: 'allow',
      failure_mode: code,
      detail: { message, auditId },
    });
    return {
      ok: false,
      code: code === 'not_configured' ? 'not_configured' : 'adapter_error',
      message,
      auditId,
      adapterCode: code,
    };
  }

  logWorkspaceAudit({
    intent: envelope.intent,
    tool: resolved.tool,
    scope_class: scope,
    tenant_id: envelope.tenant_id,
    user_binding: envelope.user_binding,
    policy_decision: 'allow',
    detail: { auditId, outcome: 'adapter_success' },
  });

  return { ok: true, data: adapterResult.data, auditId };
}

```

---

## File: `src/workspace/types.ts`

```
/**
 * Google Workspace integration — routing types (AIOS-SPEC-007).
 * Layer 2 intent → exactly one Layer 1 scope class (see scopeClasses.ts).
 * @license SPDX-License-Identifier: Apache-2.0
 */

import type { ExecutionScopeEnvelope } from '../scope/executionScopeTypes';

/** Layer 1 — canonical policy scope classes (risk / capability). */
export type WorkspaceScopeClass =
  | 'workspace.google.read'
  | 'workspace.google.write'
  | 'workspace.google.send'
  | 'workspace.google.share'
  | 'workspace.google.automation'
  | 'workspace.google.identity'
  | 'workspace.google.search';

export type WorkspaceExecutionMode = 'observe' | 'prepare' | 'execute' | 'automate';

export type WorkspaceActorType = string;

/**
 * For `workspace.mail.read`, use e.g. `{ type: 'message', id }` so the adapter forwards `id` in tool args.
 * For `workspace.mail.draft_reply`, include `threadId` when known so the MCP server can thread the draft.
 */
export type WorkspaceResourceRef = {
  type: string;
  id?: string;
  /** Gmail thread id (optional; used by draft/reply tools when distinct from `id`). */
  threadId?: string;
  /**
   * Google Calendar id (e.g. `primary` or `foo@group.calendar.google.com`) for `get_events` / event list.
   * Optional; defaults to `primary` in MCP mapping when omitted.
   */
  calendarId?: string;
};

export type WorkspacePolicyContext = {
  requires_confirmation?: boolean;
  /** MUST match the single scope class resolved from `intent`. */
  scope_class: WorkspaceScopeClass;
};

/**
 * Routing envelope — required shape before MCP adapter dispatch (SPEC-007 §6).
 */
export type WorkspaceRoutingEnvelope = {
  intent: string;
  actor_type: WorkspaceActorType;
  tenant_id: string;
  user_binding: string;
  execution_mode: WorkspaceExecutionMode;
  resource_ref?: WorkspaceResourceRef;
  policy_context: WorkspacePolicyContext;
  /** Correlation for audit. */
  session_id?: string;
  /**
   * For `workspace.mail.search` only: forwarded to MCP tool `arguments.query` (not `resource_ref`).
   * Omit for other intents. Empty string is valid if the MCP tool defines a default listing.
   */
  query?: string;
  /**
   * AIOS-SPEC-010: when set, `runWorkspaceControlPlane` validates the resolved MCP operation
   * against this envelope before calling the adapter.
   */
  execution_scope?: ExecutionScopeEnvelope;
  /**
   * `workspace.calendar.events.list` — RFC3339 window (inclusive start, exclusive end per API usage).
   * Required for that intent.
   */
  calendar_time_range?: { time_min: string; time_max: string };
  /**
   * `workspace.contacts.list` — People API `connections.list` pagination (`page_token` in MCP tool args).
   */
  contacts_page_token?: string;
};

export type WorkspaceControlPlaneResult<T = unknown> =
  | { ok: true; data: T; auditId: string }
  | {
      ok: false;
      code:
        | 'policy_denied'
        | 'invalid_intent'
        | 'adapter_error'
        | 'not_configured'
        | 'auth_required'
        | 'scope_denied';
      message: string;
      auditId: string;
      /** Set when code is `adapter_error` — original MCP adapter failure class. */
      adapterCode?: 'not_configured' | 'timeout' | 'aborted' | 'http_error' | 'auth_error';
    };

```

---

## File: `docs/implementation/AIOS-IMPLEMENTATION-CONTROL-PROGRAM.md`

```
# AI OS implementation control program

**Document ID:** AIOS-IMPL-CONTROL-001 (product-local; non-normative)  
**Repository:** `ai-os-voice-interface`  
**Execution status:** `pending_council` — **do not** treat this plan as **execution-approved** until **AIOS-COUNCIL-BRIEF-002** is **approved** and recorded in `aios-governing-docs` (see [Committee review and ratification](#committee-review-and-ratification)).  
**Normative law:** `aios-governing-docs` (see [Governing source inventory](#1-governing-source-inventory))  
**Companion pointer (governing repo):** `aios-governing-docs/reference/implementation/AIOS-IMPLEMENTATION-RUNWAY-POINTER.md` (**AIOS-REF-013**)  
**Master program (`draft` — council review before execution approval):** `aios-governing-docs/reference/implementation/AIOS-MASTER-IMPLEMENTATION-PROGRAM.md` (**AIOS-MASTER-IMPL-001**)  
**Ledger + ADR (governing repo):** `reference/implementation/AIOS-IMPLEMENTATION-LEDGER.md` (**AIOS-IMPL-LEDGER-001**, draft); `reference/implementation/ADR-001-core-shell-vs-interface-boundaries.md` (**AIOS-ADR-001**, proposed).  
**Council brief (master + ADR):** `reference/implementation/COUNCIL-REVIEW-BRIEF-AIOS-MASTER-IMPL-001.md` (**AIOS-COUNCIL-BRIEF-001**).  
**Council brief (this plan — interface spine):** `reference/implementation/COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md` (**AIOS-COUNCIL-BRIEF-002**, **`draft`** until voted).  
**Core pilot (this repo):** `src/core/shell/` — law-aligned modules; `src/shell/*` re-exports (proposed **ADR-001**).  
**Related memo:** [`docs/implementation-runway-memo.md`](../implementation-runway-memo.md) (product sequencing memo — **non-authoritative** vs master program)  
**Development triangulation (peer review, mirrored from governance):** [`docs/implementation/AIOS-DEVELOPMENT-TRIANGULATION-PROCESS.md`](AIOS-DEVELOPMENT-TRIANGULATION-PROCESS.md) (**AIOS-DEV-TRI-001**)  
**Governing process law (ratification target):** **`aios-governing-docs`** **AIOS-DEV-PROC-001** + **AIOS-COUNCIL-BRIEF-003** + `reviews/aios_dev_conformance_process/` (not a simulation).

---

## Committee review and ratification

This document is the **operational spine** for interface conformance (backlog, anti-drift, UI review agent, evidence). **If the process is not council-authorized, the program fails in governance** even when code ships.

| Step | Owner | Action |
|------|--------|--------|
| 1 | Council / committee | Review **AIOS-COUNCIL-BRIEF-002** in `aios-governing-docs` (`reference/implementation/COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md`). |
| 2 | Council | Vote per **Ratification motion** section in that brief (**Approve** / **Reject** / **Defer**). |
| 3 | Secretary / maintainer | Record decision: update brief **`status`**, **execution record** table, **CHANGELOG**; set **`execution_status: approved_for_execution`** in **this** file’s header when **Approve**. |
| 4 | Product | Continue implementation only against **ratified** law; this plan remains **child** to **AIOS-MASTER-IMPL-001** and **AIOS-COUNCIL-BRIEF-001**. |

**Related:** Amendment ratification (**AMD-2026-005**) applies to **normative text** in amendments/specs; **AIOS-COUNCIL-BRIEF-002** approves **this repo’s implementation process**, not a specification change.

---

## Purpose

**Child of** `aios-governing-docs/reference/implementation/AIOS-MASTER-IMPLEMENTATION-PROGRAM.md` (**AIOS-MASTER-IMPL-001**). Authoritative **cross-repo** sequencing, layer ownership (core shell/kernel/control-plane vs interface vs tenant), and master backlog live in that document — **not** here.

This file is the **repo-local interface workstream** plan for bringing **`ai-os-voice-interface`** into conformance with **ratified** governing documents. Execution may proceed from this file **without relying on chat history** for **this repository only**.

**Normative precedence:** If this document conflicts with ratified specs or amendments, **governing documents win**; update this file or the code.

### Binding intent and outcome: kernel, shell, and governed workspace

| | |
|--|--|
| **Intent** | **Bind** the **kernel** (control-plane law: session entry, §7 outcomes, policy predicates, disclosure inputs) and the **shell** (surface mode, voice/chat chrome, routing that applies shell state) to a **workspace of execution that follows governance** — i.e. behavior is traceable to **`aios-governing-docs`**, not ad hoc product invention. |
| **Outcome** | The **reference AI OS interface** is a **prebuilt shell** that **mirrors** the structural framework already in this repo (bootstrap, authority, surface modes, session classification, outcome derivation, identity/disclosure hooks) but **does not** ship **integrations, MCP, tenant skills, or domain agents** except those required to **control shell state** (e.g. shell navigation / `app.shell.*` class commands, diagnostics that only adjust shell mode). Everything else (Workspace, voice agents, third-party tools) is an **optional downstream layer**, explicitly subordinate to the shell (**AMD-2026-012**; **AIOS-ADR-001** when accepted). |
| **“Workspace” here** | Means the **governed integration and intent context** (**AIOS-SPEC-007** / SPEC-009), **subordinate** to the shell — not a parallel product surface loaded with unrelated capabilities. |

This separation is **normative for architecture reviews**: the minimal shippable AI OS surface is **shell-control-only**; adding non-shell integrations is a **labeled** program increment, not the default baseline.

### Hold / mainline (2026-04-07)

| Rule | Meaning |
|------|---------|
| **Child only** | Progress here is **interface-layer** and **does not** count as **master program** progress unless mapped to an **MBL-*** in **AIOS-MASTER-IMPL-001**. |
| **BL-004 not mainline** | **Do not** treat **BL-004** (or similar disclosure wiring) as the primary program track — **MBL-004** / **MBL-006** in the master program own **core** predicates first (**AIOS-ADR-001**). |
| **No default React shell law** | Do not keep hardening **shell semantics** only in React; **core** ownership is defined in **ADR-001**. |
| **No product redesign gate** | Do not reopen **product behavior design** until **core vs interface** enforcement in code follows **ADR-001** (**accepted** after **council**). |

---

## Anti-drift rules (mandatory)

| Rule | Enforcement |
|------|-------------|
| Every backlog item cites one or more **governing sources** (doc ID + section where possible). | Reviewer / CI checklist / PR template |
| No new product behavior from **local intuition** without a **labeled follow-on** backlog item tied to a future amendment or explicit non-binding experiment. | Reject in review |
| **Governance-manager** and dashboard-first **end-user** paths stay **out** of the primary runtime. | Code search + UX review |
| **Workspace** and tools remain **subordinate** to the Shell (no default entry that is Workspace-first). | Router + default view checks |
| No **“done”** without **concrete evidence** (tests, traces, conformance artifacts, or reproducible steps). | This document’s evidence column |
| **Cleanup-only** refactors that change behavior **must** map to a backlog ID or stay out of scope. | Diff review |
| **UI review agent** (`npm run dev-review:ollama`) runs on **material** shell / intent-flow changes; subjective UX-only PRs may skip. | PR label + checklist |
| **Development triangulation** (**AIOS-DEV-TRI-001**) on **material** implementation PRs: **DeepSeek + OpenAI + Gemini** + parallel **Ollama**; **full KB bundle** + **L1–L3 diagrams** per meta-prompt. | `docs/reviews/dev_triangulation/` + synthesis |

---

## UI review agent (Ollama + governed knowledge base)

**Problem frame — “agency without ability”:** A reviewer (human or model) cannot reliably grade **intent–outcome alignment**, shell subordination, or disclosure fitness without **grounding** in the same **law**, **design constraints**, and **interface reality** the implementation claims to follow. Giving an agent **agency** (a rubric and a grade) without **ability** (retrieval over governing docs, design guides, and the live interface contract) produces theater, not conformance.

**Role:** A **UI review agent** — implemented against the **Ollama** path already used for local interpretation (`/api/local-model/*`, see `src/api/localModelClient.ts`) — **analyzes** described or captured UI states and **intent-based workflows**, and **emits a structured grade** (pass / pass-with-findings / fail) with **cited** findings tied to checklist dimensions below. It is **advisory** unless council or program elevates it to a merge gate.

**Knowledge base (required contents):** **Primary** capability is **retrieval-augmented** review: an indexed corpus (or chunk + embed pipeline) over the sources below, passed into the Ollama chat path with **system + retrieved context**. Optional **Modelfile** / fine-tune on top of that is **not** a substitute for the KB; the core fix for **agency without ability** is **grounding**, not weights alone.

The agent must be run with **retrieval context** (RAG index, exported corpus, or equivalent) that minimally includes:

| Layer | Contents |
|--------|----------|
| **Law** | Ratified / in-scope drafts from **`aios-governing-docs`**: **AMD-2026-012**, **AIOS-SPEC-009** (§12 disclosure), **AIOS-SPEC-007** (routing / ICP), **AIOS-POLICY-INDEX**, relevant **amendments** and **AIOS-ADR-001** when ratified. |
| **Design / UX** | Product **design guides** and shell chrome conventions (this repo or linked design system docs). |
| **Interface contract** | **Dependencies** (`package.json`, key `src/` boundaries), **WORKSPACE.md** or equivalent orientation, **conformance artifacts** under `docs/conformance/`, and **reference descriptions** of current surfaces (`ShellIdentityBar`, `WorkspaceHubSurface`, intent routers). |

**Inputs to a review run:** Target **surface** (e.g. primary shell, workspace hub), **user journey** or **intent sequence** under test, optional **screenshot or DOM summary**, and **build / git ref** for reproducibility.

**Grading dimensions (non-exhaustive):** Shell-first entry; voice-first idle semantics; **new vs returning** scaffolding; **§7** outcome plausibility for the described state; **SPEC-009 §12.2** disclosure honesty (incl. local model when policy requires); Workspace **subordination** (no tool-first default); intent routing **traceability** to documented paths.

**Outputs:** Structured report: **grade**, **dimension scores** or findings list, **governing citations** (doc ID + section), **severity**, and **recommended fixes** mapped to backlog IDs when possible.

**Process integration:** **BL-007** automation: `npm run dev-review:ollama` — **`scripts/uiReviewAgent.ts`** (lexical RAG over **`scripts/uiReviewKb.manifest.json`**) + **Ollama** via `ollamaChatNonStreaming` / **`OLLAMA_BASE_URL`**. Optional **`AIOS_GOV_DOCS_ROOT`** for governing-repo excerpts. Use **`--dry-run`** without a live model. **Full** cloud triangulation (**DeepSeek + OpenAI + Gemini**) is in [**AIOS-DEV-TRI-001**](AIOS-DEVELOPMENT-TRIANGULATION-PROCESS.md). **BL-008:** `npm run check:dev-review`. Manual meta-prompt: [`docs/reviews/dev_triangulation/META_PROMPT_TEMPLATE.md`](../reviews/dev_triangulation/META_PROMPT_TEMPLATE.md).

---

## Development triangulation (mirrored governance reviews)

**AIOS-DEV-TRI-001** mirrors **`aios-governing-docs/reviews/`**: **Round 1** (three independent cloud models) → **revision** → **Round 2** → **development gate report**. **Ollama** runs as a **parallel UI lane** (like optional **kernel shadow** in governance — **not** a substitute for the three-way triangulation).

**Meta-prompt + KB:** Every agent receives the **same** knowledge bundle (law, program, interface paths, change scope); see **AIOS-DEV-TRI-001** and **`META_PROMPT_TEMPLATE.md`**.

**Diagrams:** Each review produces **L1** (user journey), **L2** (surface/state), **L3** (intent/router/policy logic) — **mermaid**, **at least three levels deep** in aggregate.

**Artifacts:** Under **`docs/reviews/dev_triangulation/{topic}/`** — `REVIEW_SYNTHESIS.md`, `DEV_REVIEW_GATE_REPORT.md`, etc.

**Backlog:** **BL-007** **done** (Ollama + RAG CLI); **BL-008** **done** (package check + CI on dev triangulation docs).

---

## Status summary

| Area | Snapshot (see [Gap assessment](#2-current-state-gap-assessment)) |
|------|-------------------------------------------------------------------|
| Shell single entry / surface mode | **Partial** — `shellBootstrap`, `shellAuthority`, `ShellStateContext` implement primary vs developer vs operator; interim elevation documented |
| Voice-first default | **Partial** — default mode voice; idle copy present; §8.4 numeric conformance not fully automated |
| New vs returning classification | **Was gap** — Sprint 1 addresses (**AMD-2026-012 §5**) |
| Shell outcome family (§7) | **Partial** — Sprint 1 introduces typed model + trace path |
| Session identity / fallback / transparency | **Partial** — §12.2 **predicates** in `src/core/compliance/spec009DisclosurePredicates.ts`; presentation in `spec009PrimaryDisclosure` + `ShellIdentityBar`; `resolvedIntentRequiresLocalModel` wired from `deriveWorkspaceIntentForDisclosure` + `localInterpretationRequired` (**BL-004** evidence) |
| Workspace subordination + ICP | **Partial** — `integrationControlPlane` + `callWorkspaceMcpAdapter` choke point; continued conformance per SPEC-007 routing model |
| Governance-manager in runtime | **Removed from `src/`** — archived under `archive/governance-manager/` |
| UI review agent (Ollama + KB) | **Implemented** — `npm run dev-review:ollama` (**BL-007**); set **`AIOS_GOV_DOCS_ROOT`** for law excerpts |
| Development triangulation (DeepSeek / OpenAI / Gemini + Ollama UI) | **Governing ratification pending** — **AIOS-DEV-PROC-001**; product **AIOS-DEV-TRI-001**; **BL-007**/**BL-008** **done** (CLI + `check:dev-review` + CI) |

**Blockers (law-level):** None identified at program open. **Note:** `AIOS-SPEC-007` YAML shows `draft` in-repo while **AMD-2026-012** normatively references Workspace integration; implementation follows ratified amendment + SPEC-009 spine until SPEC-007 status is reconciled in governing repo.

---

## 1. Governing source inventory

Normative definitions live in **`aios-governing-docs`**. Paths below are relative to that repository unless noted.

| Doc ID | Title | Ratified / draft (repo YAML) | Why it matters for runtime | Repos affected | Runtime domains | Significance (1–5) |
|--------|--------|-------------------------------|----------------------------|----------------|-----------------|---------------------|
| **AMD-2026-012** | Shell Authority and Voice-First Entry | **ratified** v1.0.0 | Single governed entry; voice-first; new/returning; §7 outcome family; subordinate tools; admin/runtime separation | `ai-os-voice-interface` | Shell, voice, session UX, outcomes, Workspace presentation | **5** |
| **AIOS-SPEC-009** | Intent Primitive and Execution Model (`specifications/IntentPrimitiveAndExecutionModel.md`) | **ratified** v0.5.5 | Intent lifecycle, shell vs domain, disclosure §12, PolicyRecord alignment | `ai-os-voice-interface`, `google-workspace-mcp` (adapter) | Intent, execution, transparency, audit | **5** |
| **AIOS-SPEC-007** | Google Workspace Integration Governance (`specifications/GoogleWorkspaceIntegrationGovernance.md`) | **draft** in YAML (see Blockers) | Intent router → ICP → MCP; no tool bypass | `ai-os-voice-interface`, `google-workspace-mcp` | Workspace, OAuth, MCP | **5** (treat as binding integration law via AMD-2026-012 / program scope) |
| **AMD-2026-007** | Intent Primitive, Shell Affordances, … | **draft** | POL-SHELL / POL-INTENT IDs; shell affordances; primary vs operator (cross-check with **AIOS-POLICY-INDEX**) | `ai-os-voice-interface` | Shell chrome, routing semantics | **4** (policies referenced by index; amendment draft) |
| **AIOS-POLICY-INDEX** | Policy Identifier Index (`reference/AIOS_POLICY_INDEX.md`) | **ratified** v1.2.0 | Registers **POL-*** IDs for AMD-2026-007 / AMD-2026-012 context | `ai-os-voice-interface` (traceability) | Policy IDs in code comments / tests | **3** |
| **AIOS-REF-013** | Implementation runway pointer | **draft** | Points to product memo; does not duplicate law | — | Traceability | **2** |
| **AMD-2026-010** | Kernel Engineer / shadow lane | **ratified** (per index) | Advisory / non-blocking for product spine | — | Process | **2** (until promoted) |

---

## 2. Current-state gap assessment

Evidence is **repository-based** (code, tests, docs). Status values: **implemented** | **partial** | **not implemented** | **violated** | **unclear**.

| Source | Topic | Status | Evidence |
|--------|--------|--------|----------|
| **AMD-2026-012** §4.1 Single point of entry | Default entry is Shell, not Workspace | **partial** | `App.tsx` centers voice + `ShellVoiceIdlePanel`; Workspace opens via menu/intent (`WorkspaceHubSurface`). No separate governance app in `src/`. |
| **AMD-2026-012** §5 New vs returning | First classification step | **not implemented** → **Sprint 1** | Prior grep: no `new`/`returning` classification in `src/`. |
| **AMD-2026-012** §7 Outcome family | Finite primary outcomes, not UI-only | **partial** → **Sprint 1** (types + mapping hook) | Canvas/workspace state exists; explicit §7 taxonomy not named in code. |
| **AMD-2026-012** §8 Voice-first + §8.4 interim numeric | Brief copy limits | **partial** | `ShellVoiceIdlePanel` short copy; automated §8.4 word budget optional test (Sprint 1 backlog). |
| **AIOS-SPEC-009** §12.2 Primary disclosure | PolicyRecord-style readiness | **partial** | `spec009PrimaryDisclosure.ts`, `ShellIdentityBar`, tests in `spec009PrimaryDisclosure.test.ts`. |
| **AIOS-SPEC-007** §2 Routing | ICP only | **partial** | `integrationControlPlane.ts`, `callWorkspaceMcpAdapterCallsite.test.ts`. |
| **Governance-manager** removal | Not end-user runtime | **implemented** | No `GovernanceCanvas` / `src/governance/` imports in `src/`; archive only. |

---

## 3. Phased backlog (dependency order)

| Phase | Name | Depends on | Objective |
|-------|------|------------|-------------|
| **P0** | Program control | — | This document + anti-drift rules |
| **P1** | Shell session semantics | P0 | New/returning, §7 outcomes, voice-first idle conformance |
| **P2** | Transparency + identity | P1 | SPEC-009 §12 completion, execution-policy wiring for local model / lane |
| **P3** | Workspace conformance | P1, P2 | SPEC-007 intent → scope → ICP → adapter; auth states |
| **P4** | Live conformance + dev triangulation + UI review agent + archive | P3 | Manual/live checks; **AIOS-DEV-TRI-001** reviews; **BL-007**/**BL-008** shipped; legacy quarantine |
| **P5** | Expansion (out of current mandate unless pulled) | P4 | AMD-2026-009 / SPEC-013 style gates per runway memo |

---

## 4. Itemized backlog

Status: `open` | `in_progress` | `done` | `blocked`

| ID | Title | Governing source(s) | Repo / area | Depends on | Objective | Acceptance criteria | Evidence | Risk if skipped | Status |
|----|-------|---------------------|-------------|------------|-----------|---------------------|----------|-----------------|--------|
| **BL-001** | Session entry classification (new vs returning) | AMD-2026-012 §5, §5.3 | `src/shell/sessionEntryClassification.ts`, `App.tsx`, `ShellVoiceIdlePanel.tsx` | — | Persist first-class **new** / **returning** for Shell journey; tools do not replace this | Classification readable on idle path; **returning** shows reduced scaffolding vs **new**; unit tests | `sessionEntryClassification.test.ts` | Shell violates entry law | **done** |
| **BL-002** | Shell primary outcome model (§7) | AMD-2026-012 §7; AIOS-SPEC-009 §12 cross-ref | `src/shell/shellPrimaryOutcome.ts` | BL-001 (soft) | Named outcome enum + derivation hook from shell + canvas | Types exported; `deriveShellPrimaryOutcome` covers idle + common canvas states; tests | `shellPrimaryOutcome.test.ts` | Drift to implicit UX states | **done** |
| **BL-003** | §8.4 idle copy word-budget check (optional hardening) | AMD-2026-012 §8.4.1 | `ShellVoiceIdlePanel` / tests | BL-001 | Automated guard for “minimal” opening copy | Test asserts visible copy under interim word ceiling for default opening | Test output | Cosmetic law drift | **open** |
| **BL-004** | Wire `resolvedIntentRequiresLocalModel` from execution policy | AIOS-SPEC-009 §12.2 | `App.tsx`, `ShellIdentityBar`, `deriveWorkspaceIntentForDisclosure`, `localInterpretationRequired` | BL-002 | No inference-only shell disclosure | When policy requires local model, bar shows capability line | Tests: `localInterpretationRequired.test.ts`, `deriveWorkspaceIntentForDisclosure.test.ts`; `App.tsx` passes prop | Misleading primary UI | **done** |
| **BL-005** | Workspace hub subordination review | AMD-2026-012 §9; AIOS-SPEC-007 §2 | `WorkspaceHubSurface`, menu routing | BL-001 | Hub opens only via Shell/menu/intent, not default entry | Manual + intent trace | Conformance note | Tool-first product | **open** |
| **BL-006** | Fallback outcome selection audit | AMD-2026-012 §4.4, §7 | Shell routing, agent pipeline | BL-002 | No silent persona/surface switch | Documented mapping when agent errors | Trace / test | Independent fallbacks | **open** |
| **BL-007** | UI review agent (Ollama + governed knowledge base) | AMD-2026-012; AIOS-SPEC-009 §12; AIOS-SPEC-007 §2 | `scripts/uiReviewAgent.ts`, `scripts/uiReviewRag.ts`, `scripts/uiReviewKb.manifest.json`; `npm run dev-review:ollama` | BL-002 (soft) | Graded **UI + intent-workflow** review grounded in **law + design + interface** corpus | RAG retrieval + Ollama report; `--dry-run` without LLM; optional **`AIOS_GOV_DOCS_ROOT`** | Stale review if KB not updated | **done** |
| **BL-008** | Dev triangulation tooling (package validator + optional CI) | AIOS-DEV-TRI-001; AIOS-DEV-PROC-001 (governing); AMD-2026-005 thresholds (alignment) | `scripts/dev_triangulation_check.py`; `npm run check:dev-review` | BL-007 (soft) | **Round 1** package validation (`--topic`); baseline files present | Script exits 0; CI may call `check:dev-review` | Inconsistent review packages | **done** |

---

## 5. Execution sprints

### Sprint 1 (current)

| Field | Content |
|-------|---------|
| **Objective** | Establish **session entry classification** and **§7 outcome typing** so later transparency and Workspace work trace to Shell state. |
| **Backlog items** | BL-001, BL-002 (BL-003 optional if time in same PR) |
| **Dependencies** | None blocking |
| **Acceptance target** | Tests green; idle UX differs **new** vs **returning**; outcome derivation returns stable values for idle and canvas |
| **Evidence target** | New unit tests; this table updated to **done** |
| **Done means** | BL-001/002 **done** with evidence; no regression in `npm test` |

### Sprint 2

| Field | Content |
|-------|---------|
| **Objective** | Deepen **SPEC-009** primary disclosure and execution-policy wiring; optional §8.4 idle guard. |
| **Backlog items** | BL-003 (BL-004 **done** — see progress log) |
| **Dependencies** | Sprint 1 complete |
| **Acceptance target** | Optional word-budget test for idle copy if pursued |
| **Evidence target** | Test output |
| **Done means** | BL-003 **done** or explicitly deferred |

### Sprint 3

| Field | Content |
|-------|---------|
| **Objective** | **Workspace** subordination and **fallback** audit paths. |
| **Backlog items** | BL-005, BL-006 |
| **Dependencies** | Sprint 2 complete (soft: can parallelize analysis) |
| **Acceptance target** | Documented hub entry + error fallback mapping |
| **Evidence target** | Conformance artifact update (`docs/conformance/`) |
| **Done means** | BL-005/006 **done** |

### Sprint 4 (optional; parallel when P3 stable)

| Field | Content |
|-------|---------|
| **Objective** | **BL-007** / **BL-008** — shipped; optional: attach sample report to conformance artifacts. |
| **Backlog items** | — (complete) |
| **Dependencies** | Soft: P2 transparency; can prototype on static exports before P3 complete |
| **Acceptance target** | `dev-review:ollama` + `check:dev-review` + CI on `docs/reviews/dev_triangulation/**` |
| **Evidence target** | `scripts/uiReviewAgent.ts`, `.github/workflows/dev-review-docs.yml` |
| **Done means** | **BL-007**/**BL-008** **done** |

---

## 6. Progress log (evidence-backed)

| Date | Item | Result | Evidence |
|------|------|--------|----------|
| 2026-04-07 | BL-001 | Implemented session entry classification + returning-scaffold copy | `src/shell/sessionEntryClassification.ts`, `sessionEntryClassification.test.ts`, `App.tsx`, `ShellVoiceIdlePanel.tsx` |
| 2026-04-07 | BL-002 | Implemented §7 outcome enum + derivation | `src/shell/shellPrimaryOutcome.ts`, `shellPrimaryOutcome.test.ts` |
| 2026-04-07 | BL-004 | Wired `resolvedIntentRequiresLocalModel` for primary disclosure | `App.tsx`, `src/core/policy/localInterpretationRequired.ts`, `src/shellCanvas/deriveWorkspaceIntentForDisclosure.ts`, tests |
| 2026-04-07 | BL-008 | Dev triangulation package check (`npm run check:dev-review`) | `scripts/dev_triangulation_check.py`, `package.json` |
| 2026-04-07 | BL-007 | UI review agent: RAG + Ollama CLI (`npm run dev-review:ollama`) | `scripts/uiReviewAgent.ts`, `scripts/uiReviewRag.ts`, `scripts/uiReviewKb.manifest.json` |
| 2026-04-07 | CI | `dev-review-docs` workflow on `docs/reviews/dev_triangulation/**` | `.github/workflows/dev-review-docs.yml` |
| 2026-04-07 | Governing | **AIOS-DEV-PROC-001** + **AIOS-COUNCIL-BRIEF-003** + peer packet `reviews/aios_dev_conformance_process/` | `aios-governing-docs` |

---

## 7. Blockers

| ID | Description | Owner |
|----|-------------|--------|
| B-001 | **AIOS-SPEC-007** shows `draft` in YAML while product references it as integration law | Governing repo / council reconciliation |

---

*End of implementation control program v1.5.*

```

---

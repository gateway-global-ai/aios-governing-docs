# Shell schema, route, and storage map

## Surface and route map

The current shell does not use a client URL router for primary surfaces. It uses in-memory app modes plus workspace canvas state.

### Shell app modes

| Route or surface state | Type | Meaning | Evidence |
|---|---|---|---|
| `voice` | `AppMode` | Default shell lane | `src/App.tsx` |
| `chat` | `AppMode` | Text fallback lane | `src/App.tsx` |
| `visual` | `AppMode` | Optional visual shell overlay | `src/App.tsx` |
| `menu` | `AppMode` | Menu/settings overlay | `src/App.tsx` |
| `voice_settings` | `AppMode` | TTS voice selector | `src/App.tsx` |
| `disc_settings` | `AppMode` | DISC profile overlay | `src/App.tsx` |
| `intent_settings` | `AppMode` | System configuration overlay | `src/App.tsx` |
| `api_health` | `AppMode` | Diagnostics overlay | `src/App.tsx` |

### Workspace canvas views

| Route or surface state | Type | Meaning | Evidence |
|---|---|---|---|
| `workspace_onboarding` | `CanvasView` | Workspace connection gate | `src/shellCanvas/canvasTypes.ts` |
| `workspace_hub` | `CanvasView` | Workspace root hub | `src/shellCanvas/canvasTypes.ts` |
| `workspace_calendar_hub` | `CanvasView` | Calendar read-plane view | `src/shellCanvas/canvasTypes.ts` |
| `workspace_mail_hub` | `CanvasView` | Mail read/search view | `src/shellCanvas/canvasTypes.ts` |
| `workspace_drive_hub` | `CanvasView` | Drive read/search view | `src/shellCanvas/canvasTypes.ts` |
| `workspace_contacts_hub` | `CanvasView` | Contacts read/search view | `src/shellCanvas/canvasTypes.ts` |
| `workspace_search_hub` | `CanvasView` | Search hub | `src/shellCanvas/canvasTypes.ts` |

## Schema and type map

| Schema or type | Role | Evidence |
|---|---|---|
| `CommandRailState` | Footer mode, primary action, status, optional intent | `src/components/shell/commandRailTypes.ts` |
| `ShellSurfaceMode` | `primary`, `developer`, `operator` shell authority plane | `src/shell/shellSurfaceMode.ts` |
| `ShellStateCommand` | Deterministic spoken or typed shell commands | `src/shell/shellStateCommands.ts` |
| `ShellNavigationAction` | Unified shell action model for deterministic commands and agent `INTENT_JSON` | `src/shell/shellIntentRouter.ts` |
| `ShellTargetMode` | Settings overlays addressable through app intents | `src/shell/shellIntentRouter.ts` |
| `WorkspaceState` | `not_configured`, `unknown`, `auth_required`, `connecting`, `connected`, `error` disclosure gate | `src/shell/workspaceState.ts` |
| `CanvasView` / `WorkspaceCanvasState` | In-memory Workspace surface routing | `src/shellCanvas/canvasTypes.ts` |
| `SessionEntryClassification` | New-vs-returning entry state | `src/core/shell/sessionEntryClassification.ts` |
| `Intent` | Governing intent shape for domain execution | `specifications/IntentPrimitiveAndExecutionModel.md` |

## Persistence and state ownership map

| Store | Key or owner | Purpose | Evidence |
|---|---|---|---|
| React local state | `mode`, `status`, `messages`, `chatInput`, `voice`, `discProfile`, `agentIntent`, `userIntent`, `desiredOutcome`, `agentName`, `agentCompany`, `agentRole` | Primary shell runtime state | `src/App.tsx` |
| Session storage | `aios.shell.surfaceMode` | Persist shell surface mode for current session | `src/shell/shellBootstrap.ts` |
| Local storage | `aios.workspace.connected` | User-local Workspace connect preference | `src/shell/workspaceState.ts` |
| Local storage / session storage | interim shell authority keys and legacy diagnostics hints | Local elevation/bootstrap signals | `src/shell/shellAuthority.ts`, `src/shell/shellBootstrap.ts` |
| Browser memory refs | speech recognition refs, transcript refs, audio context refs | PTT and TTS lifecycle control | `src/App.tsx` |
| Environment variables | Gemini API key, Workspace MCP URL, interim shell allowance | Runtime provider/configuration inputs | `src/App.tsx`, `src/shell/workspaceState.ts`, `src/shell/shellAuthority.ts` |
| Workspace control plane | integration control plane plus MCP adapter | Governed Workspace execution handoff | `src/workspace/integrationControlPlane.ts`, `src/workspace/mcpAdapter.ts` |

## Architecture observations

- Primary shell routing is currently state-machine based, not URL-route based.
- Shell-state control is already separated from domain intent execution, which is the correct boundary.
- Persistence is still browser-local for shell mode and Workspace preference; no governed account-backed session record exists yet in the interface repo.
- The baseline package therefore needs both a route map and a future state-ownership contract, not just a UI inventory.

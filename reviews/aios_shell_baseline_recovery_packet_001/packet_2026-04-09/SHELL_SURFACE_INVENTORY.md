# Shell surface inventory

## Core shell surface

| Surface | Current implementation | Key evidence |
|---|---|---|
| Shell root | Single React shell composed in one top-level app with shell providers and workspace canvas providers | `C:/Apps/ai-os-voice-interface/src/main.tsx`, `C:/Apps/ai-os-voice-interface/src/App.tsx` |
| Greeting | Initial agent message greets the user and frames the shell as voice-first | `src/App.tsx` |
| Voice idle orientation | Idle panel distinguishes new vs returning users and offers an `Open Menu` recovery action | `src/components/shell/ShellVoiceIdlePanel.tsx`, `src/shell/sessionEntryClassification.ts` |
| Shell identity bar | Top disclosure strip shows lane, workspace state, local model readiness, and optional diagnostics chrome | `src/components/shell/ShellIdentityBar.tsx` |
| Footer command rail | Persistent command rail provides voice/chat toggle, menu, PTT or chat input, and status | `src/components/shell/CommandRail.tsx` |

## Voice and chat interaction

| Surface | Current implementation | Key evidence |
|---|---|---|
| Voice-first entry | Default mode is `voice`; voice is primary and chat is fallback | `src/App.tsx` |
| PTT control | Hold-to-talk button uses browser speech recognition and status transitions | `src/components/ui/VoicePttButton.tsx`, `src/App.tsx` |
| Voice transcript | Active transcript is shown above the rail during listening | `src/App.tsx` |
| Transcript logging | Final voice transcription is appended to the message log; agent replies are also logged | `src/App.tsx` |
| Chat lane | Chat mode shows transcript history and a text input/send action | `src/App.tsx`, `src/components/shell/CommandRail.tsx` |
| TTS output | Agent replies are spoken through Gemini TTS with selectable voices | `src/App.tsx` |

## Menu and configuration overlays

| Surface | Current implementation | Key evidence |
|---|---|---|
| Menu overlay | Shell settings entry point with Visual, Workspace, Personalization, DISC Profile, System Configuration, and optional API health | `src/App.tsx` |
| Voice settings | Voice selection overlay with prebuilt voices | `src/App.tsx` |
| DISC settings | DISC profile sliders and radar view | `src/App.tsx` |
| System configuration | Inputs for agent identity, intent, and desired outcome | `src/App.tsx` |
| API health | Diagnostics overlay available only with operator chrome | `src/App.tsx`, `src/overlays/ApiHealthOverlay.tsx` |
| Visual mode | Optional visual overlay; explicitly framed as secondary to the voice shell | `src/App.tsx` |

## Shell state and authority

| Surface | Current implementation | Key evidence |
|---|---|---|
| Primary shell mode | Default end-user shell surface | `src/shell/ShellStateContext.tsx`, `src/shell/shellBootstrap.ts` |
| Developer shell mode | Enables developer HUD and shell diagnostics behaviors | `src/shell/ShellStateContext.tsx` |
| Operator shell mode | Enables operator diagnostics strip and extended shell chrome | `src/shell/ShellStateContext.tsx` |
| Deterministic shell commands | Voice/text commands can switch chat/voice and primary/developer/operator surfaces | `src/shell/shellStateCommands.ts` |
| Agent-driven shell actions | `INTENT_JSON` app intents can open settings, workspace, and shell-state changes | `src/shell/shellIntentRouter.ts`, `src/shell/shellNavigationApply.ts` |
| Interim authority clamp | Elevated shell modes are currently controlled by browser-local authority signals, not full RBAC | `src/shell/shellBootstrap.ts`, `src/shell/shellAuthority.ts` |

## Workspace plane

| Surface | Current implementation | Key evidence |
|---|---|---|
| Workspace onboarding | Separate onboarding surface for connect vs continue without | `src/overlays/WorkspaceOnboardingSurface.tsx` |
| Workspace hub | Hub entry for calendar, mail, drive, contacts, and search | `src/overlays/WorkspaceHubSurface.tsx` |
| Workspace canvas views | In-memory canvas states for hub and individual Workspace read-plane hubs | `src/shellCanvas/canvasTypes.ts`, `src/shellCanvas/WorkspaceCanvasContext.tsx` |
| Subordinate routing | Workspace opens from shell intent or menu and remains subordinate to shell entry | `src/App.tsx`, `src/workspace/integrationControlPlane.ts` |

## Notable absent or incomplete surfaces

- No governed account creation flow.
- No OTP verification surface.
- No user profile display surface with name, phone, and email.
- No user profile edit surface.
- No document create/edit/save/rename shell flow.
- No explicit shell control for Gemini vs Whisper/Ollama voice lanes.
- No structured shell document/artifact output surface beyond chat text and overlays.
- No explicit single-option vs multi-option governed flow primitives in the runtime UI.

## Inventory verdict

The current shell is real and reviewable. It already contains a coherent voice-first shell, fallback chat lane, command rail, menu system, and a bounded shell-state plane.

The baseline failure is not the absence of a shell. The failure is that the current shell has not yet been reduced into a governed baseline artifact set with explicit coverage for accounts, document flows, dual voice lanes, and approved shell control contracts.

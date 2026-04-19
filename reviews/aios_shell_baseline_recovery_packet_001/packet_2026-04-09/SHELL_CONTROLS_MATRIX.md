# Shell controls matrix

| Control | Purpose | State owner | Doctrine reference | Audience |
|---|---|---|---|---|
| PTT button | Primary voice entry and intent capture | `App.tsx` local state plus browser speech API session | `AMD-2026-012`, `AMD-2026-007` | Primary user |
| Voice/chat toggle | Switch between voice-first and text fallback | `App.tsx` mode state via `tryApplyShellNavigationAction()` | `AMD-2026-007`, `AIOS-SPEC-009` §2.1 | Primary user |
| Menu button | Open shell settings and optional tools | `App.tsx` mode state | `AMD-2026-007` | Primary user |
| Chat input + send | Text fallback for shell interaction | `App.tsx` message state, `CommandRail.tsx` form | `AMD-2026-007`, `AMD-2026-012` | Primary user |
| Voice settings | Select shell TTS voice | `App.tsx` `voice` state | `AMD-2026-012`, draft `AMD-2026-008-ADD-002` | Primary user |
| DISC profile sliders | Adjust behavioral profile values used in prompt shaping | `App.tsx` `discProfile` state | `AMD-2026-008-ADD-003` role/intent/outcome support, implementation-only today | Primary user |
| System configuration fields | Set agent name, role, company, agent intent, user intent, desired outcome | `App.tsx` local state | `AMD-2026-008-ADD-003` contract spirit; implementation-only today | Primary user / operator |
| Visual mode | Secondary visualization overlay | `App.tsx` mode state | `AMD-2026-012` low-noise shell rule; current visual mode is optional only | Primary user |
| Workspace menu entry | Open subordinate Workspace plane | Workspace canvas state and integration control plane | `AMD-2026-012`, `AMD-2026-007`, `AIOS-SPEC-007` | Primary user |
| API health | View provider status diagnostics | `App.tsx` mode state | `AMD-2026-007` primary vs operator split | Operator |
| Enter developer mode | Enable developer shell surface and HUD | `ShellStateContext`, session storage, interim authority | `AMD-2026-007` `POL-SHELL-004` to `006` | Operator / developer |
| Exit developer mode | Return to primary shell surface | `ShellStateContext`, session storage | `AMD-2026-007` `POL-SHELL-004` to `006` | Operator / developer |
| Enter operator mode | Enable operator diagnostics shell chrome | `ShellStateContext`, session storage, interim authority | `AMD-2026-007`, `AMD-2026-012` | Operator |
| Exit operator mode | Return from operator to primary shell surface | `ShellStateContext`, session storage | `AMD-2026-007`, `AMD-2026-012` | Operator |
| Agent `app.open.*` intents | Open voice settings, DISC, system config, workspace | `routeShellAgentText()` plus shell apply handlers | `AIOS-SPEC-009` shell/domain separation, `AMD-2026-007` | Primary user |
| Agent `app.shell.*` intents | Controlled shell-state transitions through intent JSON | `routeShellAgentText()` plus shell apply handlers | `AIOS-SPEC-009` §2.1, `AMD-2026-007` §11.9 | Operator / developer / primary as allowed |

## Current control-plane observations

- Primary-user shell controls are real and persistent.
- Operator and developer controls exist, but are still governed by interim device-local authority instead of full identity-bound admin policy.
- Shell controls are already separated from Workspace domain execution, which is aligned with `AIOS-SPEC-009` §2.1.
- The missing control surfaces are account management, document authoring/storage, and dual voice-lane switching.

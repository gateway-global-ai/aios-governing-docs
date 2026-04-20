# Shell baseline gap map

## Status legend

- `present` — implemented in a materially recognizable way now
- `partial` — some baseline behavior exists, but not enough to approve the requirement as complete
- `missing` — no credible baseline implementation exists in the current shell

## Required capability map

| # | Required capability | Status | Current evidence | Gap to baseline |
|---|---|---|---|---|
| 1 | Greets the user | `present` | Initial shell greeting plus voice idle orientation | Greeting exists, but not yet formalized as an approved shell baseline artifact |
| 2 | Determines intent (`new` vs `returning`) | `partial` | Session classification distinguishes new vs returning | Classification exists, but deeper intent intake and restoration logic are still thin |
| 3 | Creates new account and verifies identity with OTP | `missing` | No account or OTP surface in current shell | Needs account model, identity flow, verification surface, and governance rules |
| 4 | Communicates as voice first | `present` | Default shell mode is voice with PTT and spoken responses | Needs baseline approval and explicit doctrine-to-runtime conformance record |
| 5 | Logs all voice communication in chat | `present` | Final voice transcript and agent replies are appended to message history | Needs explicit validation that voice-session logging is complete and retained correctly |
| 6 | Clear control over AI OS state and behavior with admin/user separation | `partial` | `primary`, `developer`, `operator` shell modes plus shell authority gate | Separation exists, but it is still device-local/interim rather than identity-bound admin policy |
| 7 | Displays user account info with user name, phone, and email | `missing` | No user account display surface | Needs a governed user profile surface and data ownership rules |
| 8 | Lets user edit account info | `missing` | No account edit surface | Needs edit flow, validation rules, and persistence design |
| 9 | Creates, edits, saves, and renames documents/folders | `missing` | No baseline document/file management shell flow | Needs composition-to-storage baseline and approval path |
| 10 | Converses through Gemini and Whisper TTS using Ollama with shell switching | `partial` | Gemini chat + Gemini TTS exist; local model readiness is disclosed | Missing explicit dual-lane voice/TTS switch and Whisper/Ollama shell control |
| 11 | Controls agent behavior including DISC, ARCH, Agent Voice, and system prompt from shell | `partial` | DISC, voice choice, identity, intent, and desired outcome fields exist | ARCH controls and a governed system-prompt/control contract are not yet explicit |
| 12 | Produces full range of output from start button to structured document | `partial` | Voice shell, chat, settings overlays, and text responses exist | Structured artifact output path is not yet governed as a baseline shell capability |
| 13 | Exercises control over shell state, separation of power, skill/action/outcome | `partial` | Shell-state commands, shell intent routing, subordinate Workspace lane | Skill/action/outcome model is incomplete and not yet tied to approved shell artifacts |
| 14 | Demonstrates single-option flow and multi-option flow | `partial` | Menu, chat input, settings forms, and shell overlays imply flow types | Explicit governed navigation primitives are still draft and not materialized as first-class shell runtime states |

## Aggregate baseline view

| Status | Count |
|---|---:|
| `present` | 3 |
| `partial` | 7 |
| `missing` | 4 |

## Interpretation

The current shell is strong enough to serve as a truthful extraction target, but not strong enough to serve as the approved AI OS baseline without review and follow-on work.

The most important gap is not cosmetic. It is structural:

- the shell exists
- the shell control plane exists
- but the account, document, dual-lane voice, and explicit flow-baseline contracts are not yet complete

## Recommended artifact follow-ups

- Keep this packet as the approval gate.
- Use review findings to decide whether the missing pieces are implementation-only gaps or doctrine gaps.
- Open a narrow shell-baseline addendum only if the review proves current doctrine is insufficient for the missing baseline capabilities.

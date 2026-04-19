---
document_id: AIOS-VOICE-TTS-ARCHITECTURE-STANDARD-001
version: 0.4.0
status: draft
category: reference
title: AI OS Voice TTS Architecture Standard
author: Gateway Global AIOS
created: 2026-04-16
last_updated: 2026-04-19
cross_references:
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes
  - doc_id: AMD-2026-008-ADD-001
    title: Base Shell Navigation Primitives and Start-Here Control
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output and Output Packaging
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model (§17 Sovereign Voice)
  - doc_id: AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001
    title: AI OS Shell UI Layout and Component Standard
---

# AI OS Voice TTS Architecture Standard

`AIOS-VOICE-TTS-ARCHITECTURE-STANDARD-001` — Draft v0.4.0

---

## 1. Purpose

This document establishes the canonical architecture for Text-to-Speech (TTS) routing in the AI OS voice shell runtime. It defines the governed `VoiceRouteId` enum, the `IVoiceEngine` interface contract, the single-dispatch rule, the shell-level cue controller, and the configuration authority. It exists to prevent ad-hoc TTS implementations from bypassing the governed routing layer or turning audio into an invisible side effect.

---

## 2. Scope

This standard applies to all TTS-related code in the `ai-os-voice-interface` repository:
- `src/config/voiceRoutePreference.ts`
- `src/core/io/VoiceEngine.ts` and all engine implementations
- The `speakText()` / stop dispatch functions in `src/App.tsx`
- Shell audio cue state in `src/App.tsx`
- `src/api/geminiGateway.ts`
- `server/geminiServe.ts`
- `src/components/shell/ShellIdentityBar.tsx`
- `src/components/shell/ShellSystemControls.tsx`
- `src/components/shell/LoyaltyIntroSequence.tsx`
- Any component or hook that triggers spoken output

---

## 3. VoiceRouteId — Governed Values

The `VoiceRouteId` type is the sole enumeration of permitted TTS output routes. It is defined in `src/config/voiceRoutePreference.ts`.

```typescript
export type VoiceRouteId = 'voicebox' | 'browser' | 'gemini';
```

| Value | Description | Runtime requirement |
|-------|-------------|---------------------|
| `voicebox` | Local Voicebox TTS — runs on operator hardware | Voicebox server running locally |
| `browser` | Web Speech API / browser built-in synthesis | Browser `SpeechSynthesis` API |
| `gemini` | Gemini voice routed through the same-origin host gateway using Gemini native-audio or TTS models | `GEMINI_API_KEY` configured on the app host |

**Default route:** `'gemini'`. When no preference is stored in localStorage, `getVoiceRoute()` returns `'gemini'`.

No additional `VoiceRouteId` values may be added without:
1. Updating this standard document
2. Adding a corresponding `IVoiceEngine` implementation
3. Adding a dispatch case in `App.tsx speak()`
4. Adding a UI tile in `VoiceControlPanel` Model section

---

## 4. Configuration Authority

`src/config/voiceRoutePreference.ts` is the **sole** file authorized to read and write the `aios_voice_route` localStorage key.

```typescript
const LS_KEY = 'aios_voice_route';

export function getVoiceRoute(): VoiceRouteId {
  // Returns stored value or 'gemini' as default
}

export function setVoiceRoute(route: VoiceRouteId): void {
  // Writes to localStorage
}
```

No other file may read or write `aios_voice_route` directly.

---

## 5. IVoiceEngine Interface Contract

All TTS engine implementations MUST implement `IVoiceEngine` from `src/core/io/VoiceEngine.ts`:

```typescript
export interface IVoiceEngine {
  /** Begin capturing audio (PTT down). */
  startListening(): Promise<void>;

  /** Stop capturing audio (PTT up). Triggers LLM pipeline. */
  stopListening(): Promise<void>;

  /** Submit text directly (chat input or transcription). */
  submitText(text: string): Promise<void>;

  /** Synthesize and play spoken response. */
  speak(text: string, overrideVoice?: string): Promise<void>;

  /** Callbacks set by App.tsx before use */
  onStatusChange?: (status: SystemStatus, detail?: string) => void;
  onTranscription?: (text: string, isFinal: boolean) => void;
  onAgentResponse?: (text: string) => void;
}
```

Implementations MUST NOT add public methods outside this interface. Side effects are communicated exclusively through the callback properties.

---

## 6. Single-Dispatch Rule

All TTS routing MUST flow through the `speakText()` function defined in `src/App.tsx`. No component or utility outside of `App.tsx` may instantiate a voice engine or call `engine.speak()` directly.

```typescript
// App.tsx — the ONLY authorized dispatch point
const speakText = async (text: string, overrideVoice?: string) => {
  const route = getVoiceRoute();
  if (route === 'gemini') {
    await geminiEngine.current?.speak(text, overrideVoice);
  } else if (route === 'voicebox') {
    await sovereignEngine.current?.speak(text, overrideVoice);
  } else {
    await browserEngine.current?.speak(text, overrideVoice);
  }
};
```

The `speakTextRef` is passed into child components that need to trigger speech. Components call `speakTextRef.current(text)` and MUST NOT resolve the route themselves.

### 6.1 Shell cue controller

The shell MUST maintain a user-visible audio controller above raw route dispatch. That controller lives in `App.tsx` and governs:

- the current cue,
- pending queued cues,
- speaker enabled / disabled state,
- microphone enabled / disabled state, and
- replay / interruption authority surfaced through `ShellIdentityBar`.

When speaker output is disabled, the shell MAY queue spoken events instead of playing them immediately. That queued state MUST remain inspectable to the operator rather than disappearing into internal state.

### 6.2 Stop authority

The stop path for active shell speech is also governed by `App.tsx`. Route-specific interruption hooks MAY exist behind that boundary, but components MUST use the shell stop function rather than calling engine-specific stop behavior themselves.

---

## 7. Governed Engine Implementations

| Engine file | Route | Status |
|-------------|-------|--------|
| `src/core/io/BrowserVoiceEngine.ts` | `browser` | Implemented |
| `src/core/io/SovereignVoiceEngine.ts` | `voicebox` | Implemented |
| `src/core/io/GeminiVoiceEngine.ts` | `gemini` | Required per this standard |

`GeminiVoiceEngine` uses the governed same-origin Gemini gateway rather than reading provider keys in the browser bundle.

### 7.1 Gemini gateway rule

The Gemini route SHALL terminate provider credentials on the app host.

The canonical runtime split is:

- `server/geminiServe.ts` owns the host-side Gemini connection,
- `src/api/geminiGateway.ts` is the only browser-facing Gemini transport wrapper,
- `src/core/io/GeminiVoiceEngine.ts` owns playback queueing and fallback behavior.

No browser component, hook, or overlay may instantiate `GoogleGenAI` directly for the governed voice route.

### 7.2 Streamed audio queue rule

When the Gemini route is active, the shell SHALL prefer streamed audio delivery over a fully buffered audio response whenever the host runtime supports it.

The browser playback queue SHALL:

- decode base64 PCM or other returned inline audio chunks,
- convert 16-bit PCM to `Float32` channel data when needed,
- schedule chunks against a persistent `AudioContext` timeline using a tracked next-start time, and
- preserve stop and replay authority behind the shell cue controller rather than handing scheduling to ad hoc component-local code.

If streaming fails, the route MAY fall back to a host-side one-shot TTS response, but that fallback SHALL remain behind the same host credential boundary.

---

## 8. Voice Control Surfaces

The operator-facing route selection UI is `VoiceControlPanel.tsx`. It MUST:
- operate as a governed Level 1 / Level 2 routing surface rather than a feature-dense destination page,
- expose route selection as a focused Level 2 pane,
- hand off deeper Voice Box profile work into the governed Voice Box intent surface,
- call `setVoiceRoute()` on selection, and
- never bypass the `voiceRoutePreference.ts` configuration authority.

The operator-facing playback / cue surface is `ShellIdentityBar.tsx`. It MUST:

- expose the current cue and any queued cues,
- surface play or stop authority for shell-controlled spoken output,
- expose microphone and speaker enabled state,
- allow the operator to inspect queued audio before replay, and
- remain a shell disclosure surface, not a hidden implementation detail.

The cue drawer inside `ShellIdentityBar.tsx` MUST remain cue-only. It SHALL NOT duplicate route switching or deeper settings actions that belong to `VoiceControlPanel.tsx` or the governed header menu.

The top-right system handoff surface is `ShellSystemControls.tsx`. It MUST:

- expose the currently active governed voice route label,
- show current voice runtime status handed off from the shell cue controller,
- preserve bounded handoff only and avoid becoming a second primary system-navigation surface,
- avoid becoming a second independent voice dispatcher or queue owner.

The deeper local profile surface is `VoiceBoxPanel.tsx`. It MUST:

- open as an intent-first menu with `View Profiles`, `Create Profile`, `Record Voice`, and `Upload Profile` as explicit Level 1 entries,
- route each of those entries into a focused Level 2 pane,
- preserve archive import, profile activation, and sample recording behind those panes, and
- keep local personalization subordinate to the governed route-selection model rather than inventing a parallel shell authority surface.

---

## 9. Conformance

Agents and developers making changes to TTS-related code SHALL:

1. Read this document and `AMD-2026-008` before modifying voice routing
2. Only add `VoiceRouteId` values that have a corresponding `IVoiceEngine` implementation
3. Route all speech through `App.tsx speakText()` — never directly from components
4. Use `getVoiceRoute()` / `setVoiceRoute()` from `voiceRoutePreference.ts` only
5. Keep the shell cue controller in `App.tsx` authoritative for replay, queue visibility, speaker mute, and stop behavior
6. Keep Gemini provider keys on the app host and out of the browser bundle
7. Route Gemini browser calls only through `src/api/geminiGateway.ts`
8. Update this document when adding new engine implementations or changing shell audio authority

Violations of §6 (single-dispatch rule) constitute voice system architecture failures incompatible with the sovereign voice requirements of AMD-2026-008 §3.

---

*Document status: draft. Enters peer review → ratification pipeline per AMD-2026-005.*

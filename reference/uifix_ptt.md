Phase 0 — Design System Foundation (4 items)

Added ICON_SIZES, TOUCH_TARGETS, FOOTER_ZONE constants to client/src/config/brand.ts — these are now the canonical source of truth for all layout dimensions
Added "Hard Design Constants" section to ui-design-governance/SKILL.md with prohibited pattern enforcement
Added design dependency block to shadcn-ui-agent/SKILL.md so all UI generation agents must follow design governance
Created .cursor/rules/canvas-intent-views.mdc — governance rule enforcing full-canvas (100% W x 100% H) intent views and prohibiting duplicate control surfaces
Phase 1 — AIOS Logo + Purple Blob Fix (3 items)

Created AIOSLogoSVG.tsx — inline SVG component (green AI OS mark) for the visualizer center
Wired the AIOS logo as an HTML overlay centered inside the DynamicVisualizer ring
Eliminated the purple blob: changed DEFAULT_VISUALIZER_CONFIG.secondaryColor from #6366f1 (indigo) to #10b981 (emerald), updated all 3 engine fallbacks, and changed the PTT button's recording/processing state from bg-indigo-500 to bg-emerald-600
Phase 2 — Live Transcript Strip (1 item)

Added liveTranscript state, captured partial transcription text from the voice pipeline, and rendered a frosted-glass transcript strip with "Thinking..." bounce animation positioned at the bottom of the canvas area
Phase 3 — Footer Redesign (2 items)

Left slot: Replaced Mute with Chat toggle (MessageSquare/MessageSquareOff) + Visualizer toggle (Eye/EyeOff), both with text labels
Right slot: Replaced MoreVertical/User with hamburger Menu icon with "Menu" label
All buttons use governed ICON_SIZES.footerControl (20px) and TOUCH_TARGETS.footerButton (44px min height)
Footer logo upgraded from h-5 to FOOTER_ZONE.logoHeight (28px) with boosted opacity
Phase 4 — Canvas Overlay Governance (1 item)

Removed both duplicate <details> "Canvas appearance" accordion cards from the idle canvas
Phase 5 — System Menu Categories (1 item)

Added 3 new L1 categories to useSystemMenuAuthority: AI Tools (Transcription, Generate Document, Voice Selector, Task Queue), Developer (Terminal, API Tester — owner only), Files (Upload, Browse — authenticated only)
Phase 6 — Shadcn AI Blocks (2 items)

Created 4 Sovereign wrapper components in client/src/components/ai-blocks/: SovereignTranscription, SovereignPromptInput, SovereignVoiceSelector, SovereignTaskQueue
Registered all 4 blocks in registry-yaml/gateway-sdk-manifest.yaml with proper SDK references, allowed props, and prohibited patterns
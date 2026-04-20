$ErrorActionPreference = "Stop"

$docsRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$interfaceRoot = "C:\Apps\ai-os-voice-interface"
$outputZip = Join-Path $PSScriptRoot "shell_baseline_packet__AIOS-SHELL-BASELINE-RECOVERY-PACKET-001__2026-04-09.zip"
$stageRoot = Join-Path $env:TEMP "aios-shell-baseline-packet-20260409"

$files = @(
  @{ Root = $docsRoot; Rel = "reference\implementation\AIOS-SHELL-BASELINE-RECOVERY-PACKET-001.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\README.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\README.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\DEEP_RESEARCH_META_PROMPT.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\PROJECT_SCOPE_INTENT_AND_DESIRED_OUTCOME.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\SHELL_SURFACE_INVENTORY.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\SHELL_CONTROLS_MATRIX.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\SHELL_SCHEMA_ROUTE_STORAGE_MAP.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\SHELL_BASELINE_GAP_MAP.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\SHELL_BASELINE_SCOPE.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\packet_2026-04-09\FILE_MANIFEST.md" }
  @{ Root = $docsRoot; Rel = "reviews\aios_shell_baseline_recovery_packet_001\build_shell_baseline_packet.ps1" }
  @{ Root = $docsRoot; Rel = "core\technical_manifesto.md" }
  @{ Root = $docsRoot; Rel = "amendments\AMD-2026-007.md" }
  @{ Root = $docsRoot; Rel = "amendments\AMD-2026-008.md" }
  @{ Root = $docsRoot; Rel = "amendments\AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md" }
  @{ Root = $docsRoot; Rel = "amendments\AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md" }
  @{ Root = $docsRoot; Rel = "amendments\AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md" }
  @{ Root = $docsRoot; Rel = "amendments\AMD-2026-012.md" }
  @{ Root = $docsRoot; Rel = "specifications\IntentPrimitiveAndExecutionModel.md" }
  @{ Root = $docsRoot; Rel = "specifications\UIComponentRegistryStandard.md" }
  @{ Root = $docsRoot; Rel = "specifications\WorkspaceDomainPackV1.md" }
  @{ Root = $interfaceRoot; Rel = "package.json" }
  @{ Root = $interfaceRoot; Rel = "src\App.tsx" }
  @{ Root = $interfaceRoot; Rel = "src\components\shell\CommandRail.tsx" }
  @{ Root = $interfaceRoot; Rel = "src\components\shell\ShellIdentityBar.tsx" }
  @{ Root = $interfaceRoot; Rel = "src\components\shell\ShellVoiceIdlePanel.tsx" }
  @{ Root = $interfaceRoot; Rel = "src\components\ui\VoicePttButton.tsx" }
  @{ Root = $interfaceRoot; Rel = "src\core\shell\sessionEntryClassification.ts" }
  @{ Root = $interfaceRoot; Rel = "src\core\shell\shellPrimaryOutcome.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\ShellStateContext.tsx" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellBootstrap.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellIntentRouter.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellNavigationApply.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellStateCommands.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\workspaceState.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shellCanvas\canvasTypes.ts" }
  @{ Root = $interfaceRoot; Rel = "src\workspace\integrationControlPlane.ts" }
  @{ Root = $interfaceRoot; Rel = "src\workspace\mcpAdapter.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellStateCommands.test.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellIntentRouter.test.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellBootstrap.test.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\shellNavigationApply.test.ts" }
  @{ Root = $interfaceRoot; Rel = "src\shell\workspaceState.test.ts" }
  @{ Root = $interfaceRoot; Rel = "src\core\shell\sessionEntryClassification.test.ts" }
)

if (Test-Path $stageRoot) {
  Remove-Item -Recurse -Force $stageRoot
}

New-Item -ItemType Directory -Path $stageRoot | Out-Null

foreach ($file in $files) {
  $source = Join-Path $file.Root $file.Rel
  if (-not (Test-Path $source)) {
    throw "Missing source file: $source"
  }

  $repoName = if ($file.Root -eq $docsRoot) { "aios-governing-docs" } else { "ai-os-voice-interface" }
  $destination = Join-Path $stageRoot (Join-Path $repoName $file.Rel)
  $destinationDir = Split-Path -Parent $destination
  if (-not (Test-Path $destinationDir)) {
    New-Item -ItemType Directory -Force -Path $destinationDir | Out-Null
  }
  Copy-Item -Path $source -Destination $destination -Force
}

if (Test-Path $outputZip) {
  Remove-Item -Force $outputZip
}

Compress-Archive -Path (Join-Path $stageRoot "*") -DestinationPath $outputZip -CompressionLevel Optimal
Write-Host "Created $outputZip"

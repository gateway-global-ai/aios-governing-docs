$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$zipName = "peer_review_export__AMD-2026-015-ADD-006__2026-04-09.zip"
$zipPath = Join-Path (Join-Path $repoRoot "reviews") $zipName

$files = @(
    "amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md",
    "reference/implementation/CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001.md",
    "reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md",
    "CHANGELOG.md",
    "DOCUMENT_REGISTRY.md",
    "DOCUMENT_REGISTRY.json",
    "reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/README.md",
    "reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/AUDIT_AND_CHANGE_HISTORY.md",
    "reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/FILE_MANIFEST.md",
    "reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/REVIEWER_CHECKLIST.md",
    "reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/build_peer_review_export.ps1"
)

if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($relativePath in $files) {
        $sourcePath = Join-Path $repoRoot $relativePath
        if (-not (Test-Path $sourcePath)) {
            throw "Missing required export file: $relativePath"
        }
        $entryName = $relativePath -replace "\\", "/"
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $sourcePath, $entryName) | Out-Null
    }
}
finally {
    $zip.Dispose()
}

Write-Host "Built $zipPath"

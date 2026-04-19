$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$zipName = "peer_review_export__AMD-2026-015-ADD-005__2026-04-09.zip"
$zipPath = Join-Path (Join-Path $repoRoot "reviews") $zipName

$files = @(
    "amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md",
    "amendments/AMD-2026-015-ADD-001-governed-knowledge-artifact-registry-and-declared-input-bridge.md",
    "amendments/AMD-2026-015-ADD-002-cani-observation-schema-and-recommendation-routing-bridge.md",
    "amendments/AMD-2026-015-ADD-003-cani-persisted-artifact-taxonomy-and-routing-storage-bridge.md",
    "amendments/AMD-2026-015-ADD-004-cani-telemetry-ingestion-envelope-and-normalization-bridge.md",
    "amendments/AMD-2026-015-ADD-005-cani-validator-and-tooling-bridge.md",
    "reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md",
    "reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md",
    "reference/implementation/CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.md",
    "reference/implementation/CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001.md",
    "reference/implementation/CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001.md",
    "reference/implementation/CANI-VALIDATOR-AND-TOOLING-CONTRACT-001.md",
    "reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md",
    "reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md",
    "reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md",
    "reference/implementation/AIOS-PEER-REVIEW-EXPORT-STANDARD-001.md",
    "CHANGELOG.md",
    "DOCUMENT_REGISTRY.md",
    "DOCUMENT_REGISTRY.json",
    "reviews/amd_2026_015_add_005_cani_validator_and_tooling_bridge/README.md",
    "reviews/amd_2026_015_add_005_cani_validator_and_tooling_bridge/AUDIT_AND_CHANGE_HISTORY.md",
    "reviews/amd_2026_015_add_005_cani_validator_and_tooling_bridge/FILE_MANIFEST.md",
    "reviews/amd_2026_015_add_005_cani_validator_and_tooling_bridge/REVIEWER_CHECKLIST.md",
    "reviews/amd_2026_015_add_005_cani_validator_and_tooling_bridge/build_peer_review_export.ps1"
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

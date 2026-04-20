# Builds a self-contained governed peer-review export for AMD-2026-015-ADD-003.
# Run with Windows PowerShell or PowerShell 7:
#   powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\build_peer_review_export.ps1
#
# Standard contract:
# - archive name: <artifact_class>__<document_id>__<date>.zip
# - artifact class: peer_review_export
# - repo-relative tree at archive root
# - normalized zip entry separators: /

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$Here = $PSScriptRoot
$RepoRoot = (Resolve-Path (Join-Path $Here "..\..")).Path
$ExportName = "peer_review_export__AMD-2026-015-ADD-003__2026-04-09.zip"
$ZipOut = Join-Path $RepoRoot "reviews\$ExportName"

$Files = @(
    "amendments/AMD-2026-015-ADD-003-cani-persisted-artifact-taxonomy-and-routing-storage-bridge.md",
    "amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md",
    "amendments/AMD-2026-015-ADD-001-governed-knowledge-artifact-registry-and-declared-input-bridge.md",
    "amendments/AMD-2026-015-ADD-002-cani-observation-schema-and-recommendation-routing-bridge.md",
    "reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md",
    "reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md",
    "reference/implementation/CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.md",
    "reference/implementation/CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001.md",
    "reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md",
    "reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md",
    "reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md",
    "reference/implementation/AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md",
    "reference/implementation/AIOS-PEER-REVIEW-EXPORT-STANDARD-001.md",
    "reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md",
    "CHANGELOG.md",
    "DOCUMENT_REGISTRY.md",
    "DOCUMENT_REGISTRY.json",
    "reviews/amd_2026_015_add_003_cani_persisted_artifact_taxonomy_and_routing_storage_bridge/build_peer_review_export.ps1",
    "reviews/amd_2026_015_add_003_cani_persisted_artifact_taxonomy_and_routing_storage_bridge/README.md",
    "reviews/amd_2026_015_add_003_cani_persisted_artifact_taxonomy_and_routing_storage_bridge/AUDIT_AND_CHANGE_HISTORY.md",
    "reviews/amd_2026_015_add_003_cani_persisted_artifact_taxonomy_and_routing_storage_bridge/FILE_MANIFEST.md",
    "reviews/amd_2026_015_add_003_cani_persisted_artifact_taxonomy_and_routing_storage_bridge/REVIEWER_CHECKLIST.md"
)

foreach ($rel in $Files) {
    $src = Join-Path $RepoRoot $rel
    if (-not (Test-Path $src -PathType Leaf)) {
        throw "Missing file: $rel"
    }
}

if (Test-Path $ZipOut) {
    Remove-Item $ZipOut -Force
}

$zip = [System.IO.Compression.ZipFile]::Open($ZipOut, [System.IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($rel in $Files) {
        $src = Join-Path $RepoRoot $rel
        $entryName = ($rel -replace "\\", "/")
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
            $zip,
            $src,
            $entryName,
            [System.IO.Compression.CompressionLevel]::Optimal
        ) | Out-Null
    }
}
finally {
    $zip.Dispose()
}

Get-Item $ZipOut | Format-List FullName, Length, LastWriteTime
Write-Host "Done: $ZipOut"

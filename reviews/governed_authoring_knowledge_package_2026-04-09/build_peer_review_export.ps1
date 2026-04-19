# Builds a self-contained governed peer-review export for AMD-2026-014.
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
$ExportName = "peer_review_export__AMD-2026-014__2026-04-09.zip"
$ZipOut = Join-Path $RepoRoot "reviews\$ExportName"

$Files = @(
    "amendments/AMD-2026-014-governed-authoring-knowledge-inputs-and-bounded-author-like-drafting.md",
    "reference/implementation/AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md",
    "reference/implementation/AIOS-PEER-REVIEW-EXPORT-STANDARD-001.md",
    "reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md",
    "reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md",
    "reference/knowledge_base/agents/README.md",
    "reference/knowledge_base/agents/agent_kb_manifest.yaml",
    "reference/knowledge_base/agents/style/JT_EDITORIAL_STYLE_CARD.md",
    "reference/knowledge_base/agents/style/JT_NARRATION_STYLE_CARD.md",
    "reference/knowledge_base/agents/style/JT_AUTHORING_MODE_BOUNDARIES.md",
    "reference/knowledge_base/agents/style/JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml",
    "reference/knowledge_base/agents/style/JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml",
    "scripts/ollama_authoring_agent.py",
    "modelfiles/jt_authoring_agent.Modelfile",
    "DEVELOPER.md",
    "CHANGELOG.md",
    "reviews/governed_authoring_knowledge_package_2026-04-09/build_peer_review_export.ps1",
    "reviews/governed_authoring_knowledge_package_2026-04-09/README.md",
    "reviews/governed_authoring_knowledge_package_2026-04-09/AUDIT_AND_CHANGE_HISTORY.md",
    "reviews/governed_authoring_knowledge_package_2026-04-09/FILE_MANIFEST.md",
    "reviews/governed_authoring_knowledge_package_2026-04-09/REVIEWER_CHECKLIST.md"
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

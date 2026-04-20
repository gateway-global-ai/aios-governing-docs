# Builds a self-contained zip: taxonomy doc + scripts + DEVELOPER.md + full ADD-004 packet tree.
# Run from anywhere with Windows PowerShell or PowerShell 7:
#   powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\build_standalone_zip.ps1
# Default repo root: three levels above this script (peer_review_package -> amd_* -> reviews -> repo root).

$ErrorActionPreference = "Stop"
$Here = $PSScriptRoot
$RepoRoot = (Resolve-Path (Join-Path $Here "..\..\..")).Path
# Naming contract: <artifact_class>__<document_id>__<date>.zip (see AIOS-REVIEW-PACKET-TAXONOMY-001)
$ExportName = "peer_review_export__AMD-2026-008-ADD-004__2026-04-08"
$Staging = Join-Path $env:TEMP $ExportName
$ZipOut = Join-Path $RepoRoot "reviews\$ExportName.zip"

if (Test-Path $Staging) { Remove-Item $Staging -Recurse -Force }
New-Item -ItemType Directory -Path $Staging -Force | Out-Null

# Mirror repo paths under staging. The zip root is the repo-relative tree itself,
# not an extra wrapper directory, so unzip-root validation matches the README.
$refDir = Join-Path $Staging "reference\implementation"
New-Item -ItemType Directory -Path $refDir -Force | Out-Null
Copy-Item (Join-Path $RepoRoot "reference\implementation\AIOS-REVIEW-PACKET-TAXONOMY-001.md") $refDir

$scriptsDir = Join-Path $Staging "scripts"
New-Item -ItemType Directory -Path $scriptsDir -Force | Out-Null
foreach ($f in @("peer_review.py", "review_packet_taxonomy.py", "validate_review_packet.py")) {
    Copy-Item (Join-Path $RepoRoot "scripts\$f") $scriptsDir
}

Copy-Item (Join-Path $RepoRoot "DEVELOPER.md") $Staging

# Evidence paths in PACKET_EVENTS reference this amendment; include so validate_review_packet passes at unzip root.
$amdDir = Join-Path $Staging "amendments"
New-Item -ItemType Directory -Path $amdDir -Force | Out-Null
Copy-Item (Join-Path $RepoRoot "amendments\AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md") $amdDir

$packetSrc = Join-Path $RepoRoot "reviews\amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate"
$reviewsDir = Join-Path $Staging "reviews"
New-Item -ItemType Directory -Path $reviewsDir -Force | Out-Null
Copy-Item $packetSrc (Join-Path $reviewsDir "amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate") -Recurse

Copy-Item (Join-Path $Here "README_STANDALONE.md") (Join-Path $Staging "README_STANDALONE.md")

if (Test-Path $ZipOut) { Remove-Item $ZipOut -Force }
Compress-Archive -Path (Join-Path $Staging "*") -DestinationPath $ZipOut -CompressionLevel Optimal
Remove-Item $Staging -Recurse -Force

Get-Item $ZipOut | Format-List FullName, Length, LastWriteTime
Write-Host "Done: $ZipOut"

# Zips this peer_review_package_* folder only (naming contract: peer_review_package__<document_id>__<date>.zip).
# Run with Windows PowerShell or PowerShell 7:
#   powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\build_peer_review_package_zip.ps1

$ErrorActionPreference = "Stop"
$Here = $PSScriptRoot
$RepoRoot = (Resolve-Path (Join-Path $Here "..\..\..")).Path
$ZipName = "peer_review_package__AMD-2026-008-ADD-004__2026-04-08.zip"
$ZipOut = Join-Path $RepoRoot "reviews\$ZipName"

if (Test-Path $ZipOut) { Remove-Item $ZipOut -Force }
Compress-Archive -Path (Join-Path $Here "*") -DestinationPath $ZipOut -CompressionLevel Optimal
Get-Item $ZipOut | Format-List FullName, Length, LastWriteTime
Write-Host "Done: $ZipOut"

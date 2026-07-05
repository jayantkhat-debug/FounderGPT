$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$archiveDir = Join-Path $repoRoot "archive/legacy-streamlit"
New-Item -ItemType Directory -Path $archiveDir -Force | Out-Null

$legacyFiles = @(
  "app.py",
  "dashboard.py",
  "boardroom.py",
  "founder_dna.py",
  "multiverse.py",
  "startup_engine.py",
  "styles.py"
)

foreach ($file in $legacyFiles) {
  $src = Join-Path $repoRoot $file
  if (Test-Path $src) {
    Move-Item -Path $src -Destination (Join-Path $archiveDir $file) -Force
  }
}

$rootRequirements = Join-Path $repoRoot "requirements.txt"
if (Test-Path $rootRequirements) {
  Remove-Item $rootRequirements -Force
}

$rootAssets = Join-Path $repoRoot "assets"
if (Test-Path $rootAssets) {
  $items = Get-ChildItem $rootAssets -Force
  if ($items.Count -eq 0 -or ($items | Where-Object { $_.Name -notmatch 'README|placeholder|\.gitkeep' }).Count -eq 0) {
    Move-Item -Path $rootAssets -Destination (Join-Path $archiveDir "assets") -Force
  }
}

@"
# Archived legacy Streamlit files

These files were moved here as part of the repository cleanup for the new production architecture.
"@ | Set-Content -Path (Join-Path $archiveDir "README.md")

$gitignorePath = Join-Path $repoRoot ".gitignore"
@"
.venv/
venv/
env/
ENV/
.conda/
.next/
__pycache__/
**/__pycache__/
node_modules/
build/
dist/
*.pyc
*.pyo
*.pdb
*.egg-info/
.coverage
.pytest_cache/
.mypy_cache/
"@ | Set-Content -Path $gitignorePath

$readmePath = Join-Path $repoRoot "README.md"
@"
# FounderGPT X

This repository is organized as a production-ready monorepo for FounderGPT X.

## Structure
- `backend/` – FastAPI backend services and application logic
- `frontend/` – Next.js frontend application
- `docs/` – product, architecture, and deployment documentation
- `database/` – database migrations and schemas
- `agents/` – agent implementations and orchestration
- `prompts/` – reusable prompt templates

## Legacy cleanup
Legacy Streamlit files have been archived under `archive/legacy-streamlit/` and are no longer part of the active production architecture.
"@ | Set-Content -Path $readmePath

if (Test-Path (Join-Path $repoRoot "backend")) {
  python -m compileall backend
}

if (Test-Path (Join-Path $repoRoot "frontend/package.json")) {
  $packageJson = Join-Path $repoRoot "frontend/package.json"
  $pkg = Get-Content $packageJson -Raw | ConvertFrom-Json

  if ($pkg.scripts.PSObject.Properties.Name -contains "typecheck") {
    npm --prefix frontend run typecheck
  }

  if ($pkg.scripts.PSObject.Properties.Name -contains "build") {
    npm --prefix frontend run build
  }
}

git add .
git commit -m "refactor: clean repository for production deployment"
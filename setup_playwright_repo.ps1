<#
.SYNOPSIS
  One-click Playwright Python MCP repo scaffolding and environment setup.

.DESCRIPTION
  Creates folder structure, writes files safely, initializes venv, installs dependencies,
  and runs a sample test.

.USAGE
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
  .\setup_playwright_repo.ps1
#>

$ErrorActionPreference = "Stop"
Write-Host "=== Initializing Playwright Python MCP Repository ===" -ForegroundColor Cyan

# === Directory Setup ===
$dirs = @(".github/workflows", "docs", "playwright_mcp", "tests")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "Created directory: $dir"
    }
    else {
        Write-Host "Exists: $dir"
    }
}

# === Helper Function ===
function Write-IfNotExists {
    param([string]$Path, [string]$Content)
    if (-not (Test-Path $Path)) {
        $dir = Split-Path $Path -Parent
        if ($dir -and -not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
        $Content | Out-File -FilePath $Path -Encoding UTF8
        Write-Host "Created file: $Path"
    }
    else {
        Write-Host "Skipped (exists): $Path"
    }
}

# === Files ===

# .gitignore
$gitignore = @'
venv/
__pycache__/
*.pyc
.playwright/
test-results/
.DS_Store
Thumbs.db
'@
Write-IfNotExists ".gitignore" $gitignore

# requirements.txt
$requirements = @'
playwright
pytest
pytest-html
'@
Write-IfNotExists "requirements.txt" $requirements

# README.md
$readme = @'
# Playwright Python MCP Framework
Python Playwright test framework with MCP integration.

Quick Start (Windows PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
pytest -v
```
'@
Write-IfNotExists "README.md" $readme

# docs/setup.md
$setupDoc = @'
# Setup Guide

## Prerequisites

- Python 3.9+
- Git
- PowerShell

## Run locally

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
pytest -v
```
'@
Write-IfNotExists "docs/setup.md" $setupDoc

# playwright_mcp/__init__.py
Write-IfNotExists "playwright_mcp/__init__.py" "# Playwright MCP package"

# playwright_mcp/browser.py
$browserPy = @'
from playwright.sync_api import sync_playwright

def launch_and_get_title(url: str = "https://example.com") -> str:
    """Launch Chromium headless, navigate to URL, return title."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        browser.close()
        return title

if __name__ == "__main__":
    print("Title:", launch_and_get_title())
'@
Write-IfNotExists "playwright_mcp/browser.py" $browserPy

# tests/test_example.py
$testPy = @'
from playwright_mcp.browser import launch_and_get_title

def test_example_title():
    title = launch_and_get_title("https://example.com")
    assert "Example Domain" in title
'@
Write-IfNotExists "tests/test_example.py" $testPy

# .github/workflows/ci.yml
$ciYaml = @'
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate || .\venv\Scripts\Activate.ps1
          pip install --upgrade pip
          pip install -r requirements.txt
          playwright install

      - name: Run tests
        run: |
          source venv/bin/activate || .\venv\Scripts\Activate.ps1
          pytest -v
'@
Write-IfNotExists ".github/workflows/ci.yml" $ciYaml

# === Virtual Environment Setup ===
Write-Host "Creating virtual environment..." -ForegroundColor Cyan
if (-not (Test-Path "venv")) {
    python -m venv venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "venv created successfully" -ForegroundColor Green
    }
    else {
        Write-Error "Failed to create venv"
        exit 1
    }
}
else {
    Write-Host "venv exists - skipping" -ForegroundColor Yellow
}

# === Install dependencies ===
$venvPython = ".\venv\Scripts\python.exe"
Write-Host "Installing dependencies..." -ForegroundColor Cyan
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r requirements.txt

# === Install Playwright browsers ===
Write-Host "Installing Playwright browsers..." -ForegroundColor Cyan
& $venvPython -m playwright install

# === Verification test ===
Write-Host "Running sample test..." -ForegroundColor Cyan
& $venvPython -m pytest -v tests/test_example.py

# === Completion Message ===
Write-Host ""
Write-Host "Setup completed successfully!" -ForegroundColor Green
Write-Host "Activate environment: .\venv\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "Run tests: pytest -v" -ForegroundColor Yellow
Write-Host "All done" -ForegroundColor Cyan
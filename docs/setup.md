# Setup Guide

## Prerequisites

- Python 3.9+
- Node.js 20+
- Git
- PowerShell (Windows)

## Install

python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
npm install -g @playwright/mcp@latest
npx -y @playwright/mcp@latest install-browser --with-deps chrome-for-testing

## Run tests

python -m pytest -v

## Run the live MCP stdio smoke

$env:RUN_PLAYWRIGHT_MCP_INTEGRATION = "1"
python -m pytest -v tests/test_mcp_integration.py
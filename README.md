# Playwright Python MCP

This repository demonstrates a Python test client driving browser automation through the official Playwright MCP server over stdio.

```text
GitHub Actions -> Python MCP Client --stdio--> Playwright MCP server (@playwright/mcp) -> Browser automation

```

## What Runs

- `playwright_mcp/mcp_client.py` starts `@playwright/mcp` with `npx` and keeps the stdio session alive.
- `playwright_mcp/mcp_adapter.py` performs a smoke flow against Playwright's public TodoMVC demo, then evaluates `document.title`.
- `tests/test_example.py` verifies the Python client is wired to the Playwright MCP stdio command and tool names.
- `tests/test_mcp_integration.py` is an opt-in live smoke test that launches the real MCP server and browser.
- `.github/workflows/ci.yml` installs Python dependencies, Node 20, `@playwright/mcp`, Chromium, then runs the full test suite.

## Local Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
npm install -g @playwright/mcp@latest
npx -y @playwright/mcp@latest install-browser chrome-for-testing
```

Run unit tests only:

```powershell
python -m pytest -v
```

Run the live MCP smoke locally:

```powershell
$env:RUN_PLAYWRIGHT_MCP_INTEGRATION = "1"
python -m pytest -v tests/test_mcp_integration.py
```

Run the manual flow:

```powershell
python main.py
```

## Configuration

The client defaults to the official stdio command:

```text
npx -y @playwright/mcp@latest --headless --browser chrome --isolated
```

You can override the executable with:

```powershell
$env:PLAYWRIGHT_MCP_COMMAND = "npx"
```

You can override the public smoke-test URL with:

```powershell
$env:PLAYWRIGHT_MCP_SMOKE_URL = "https://playwright.dev/"
$env:PLAYWRIGHT_MCP_SMOKE_TITLE_TEXT = "Playwright"
```

The previous `MCP_SERVER_URL` WebSocket flow is no longer required for this repo. Browser automation now happens through the local stdio MCP server process.

`@playwright/mcp@latest` currently requires Node.js 20+ for the live smoke. The unit tests still run without launching the MCP server.

The default smoke URL is `https://demo.playwright.dev/todomvc/`, a free public demo app maintained for Playwright automation examples.

## GitHub Actions

The CI workflow:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs `requirements.txt`.
4. Sets up Node 20.
5. Installs `@playwright/mcp@latest`.
6. Installs Chromium for Playwright.
7. Runs pytest and uploads `report.html`.

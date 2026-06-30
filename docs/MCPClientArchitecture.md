# MCPClient Architecture

This repository implements a Python MCP client that launches `@playwright/mcp` as a local process and communicates with it over stdio.

- `playwright_mcp/mcp_client.py`: starts the MCP process using `npx` and opens a stdio session.
- `playwright_mcp/mcp_adapter.py`: sends browser navigation commands and evaluates the smoke-test page.
- `tests/test_example.py`: verifies the MCP stdio defaults and tool invocation.
- `tests/test_mcp_integration.py`: runs an opt-in live browser smoke test.
- `.github/workflows/ci.yml`: installs Python, Node 20, `@playwright/mcp`, browser dependencies, and executes pytest.

GitHub Actions
   ↓
Python MCP Client
   ↓ (stdio)
Playwright MCP server (@playwright/mcp)
   ↓
Browser automation
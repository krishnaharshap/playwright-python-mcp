# Project Directory Structure

This repository demonstrates a Python MCP client driving browser automation through the official Playwright MCP server over stdio.

```plaintext
playwright-python-mcp/
│
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions CI workflow
│
├── docs/
│   ├── PROJECT_STRUCTURE.md          # This architecture/reference doc
│   └── setup.md                      # Local setup and usage guide
│
├── playwright_mcp/                   # Python MCP client implementation
│   ├── __init__.py
│   ├── browser.py                    # Playwright browser helper utilities
│   ├── config.py                     # Default smoke-test URL/text and config
│   ├── mcp_adapter.py                # MCP smoke flow and evaluation logic
│   └── mcp_client.py                 # Starts @playwright/mcp over stdio
│
├── tests/                            # Pytest test cases
│   ├── test_example.py               # Unit/test wiring for MCP stdio client
│   └── test_mcp_integration.py       # Opt-in live Playwright MCP smoke test
│
├── requirements.txt                  # Python dependency manifest
├── pytest.ini                        # Pytest configuration and default options
├── README.md                         # Project overview and CI usage
├── setup_playwright_repo.ps1         # Local Windows setup helper script
├── commands.txt                      # Useful local development commands
├── main.py                           # Optional manual runner/demo entry point
└── report.html                       # Generated HTML test report artifact
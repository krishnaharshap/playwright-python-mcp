import os


DEFAULT_SMOKE_URL = os.getenv(
    "PLAYWRIGHT_MCP_SMOKE_URL",
    "https://demo.playwright.dev/todomvc/",
)
DEFAULT_SMOKE_TITLE_TEXT = os.getenv("PLAYWRIGHT_MCP_SMOKE_TITLE_TEXT", "TodoMVC")

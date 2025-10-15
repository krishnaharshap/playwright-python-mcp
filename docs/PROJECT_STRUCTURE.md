## 📁 Project Directory Structure

```plaintext
playwright-python-mcp/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml        # GitHub Actions CI workflow
│
├── tests/                       # All test cases (Pytest format)
│   ├── test_sample.py           # Example test file
│   └── conftest.py              # Common pytest fixtures/hooks
│
├── pages/                       # ⚙️ TODO: Add Page Object Model (POM) classes
│   ├── base_page.py               # TODO: Create shared page methods
│   ├── login_page.py              # TODO: Define login locators/actions
│   └── dashboard_page.py          # TODO: Implement dashboard interactions
│
├── utils/                         # ⚙️ TODO: Add reusable helper utilities
│   ├── config_reader.py           # TODO: For reading test configs
│   ├── logger.py                  # TODO: Centralized logging setup
│   └── playwright_helpers.py      # TODO: Shared Playwright operations
│
├── requirements.txt              # Project dependencies
├── pytest.ini                    # Pytest configuration
├── README.md                     # Project overview and usage guide
├── report.html                   # Generated test report (artifact)
├── venv/ or .venv/               # Local virtual environment (ignored in CI)
└── main.py                       # Optional entry point for manual run

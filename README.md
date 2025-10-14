## 🔗 Playwright + MCP Integration

This repository demonstrates how to connect **Playwright-based Python UI tests** to **MCP (Model Context Protocol)** for intelligent testing flows.

### Features
- ✅ Browser automation with Playwright
- 🤖 AI-aware testing using MCP SDK
- 🧩 Configurable YAML for connecting to custom MCP servers
- 💡 Extendable design for adaptive and self-healing test logic

*NOTE: pom.xml is for local-use only*

#### Legacy Java Artifacts (pom.xml)
This project is primarily a **Python / Playwright / MCP** framework. The file `pom.xml` was retained for local reference/legacy compatibility, but **is not committed** to this repository.  
To keep it locally without committing:
1. Add `pom.xml` to `.gitignore` (already included).  
2. If `pom.xml` was previously tracked, run:
   ```bash
   git rm --cached pom.xml
   git commit -m "Remove pom.xml from Git and ignore it"

Run locally:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v

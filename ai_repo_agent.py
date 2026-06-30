# notepad ai_repo_agent.py

import os
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:7b"

REPO_PATH = "."

def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def fix_file(path):
    code = read_file(path)

    prompt = f"""
You are a senior QA automation engineer.

Fix ALL issues in this code for:
- CI failures
- Playwright issues
- MCP integration issues
- Python best practices

Return ONLY corrected code.

FILE:
{code}
"""

    print(f"[AI] Fixing {path}")
    fixed = ask_llm(prompt)
    write_file(path, fixed)

def run_repo_scan():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                fix_file(os.path.join(root, file))

if __name__ == "__main__":
    run_repo_scan()
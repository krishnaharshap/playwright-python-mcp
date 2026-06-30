# ollama_agent.py

import requests
import os

def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5-coder:7b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def fix_file(path):
    code = load_file(path)

    prompt = f"""
You are a senior QA automation engineer.

Fix this Python code for CI failures, MCP integration issues, and Playwright reliability.

Return ONLY corrected code.

FILE:
{code}
"""

    result = ask_ollama(prompt)

    with open(path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Fixed: {path}")


# Example usage
fix_file("playwright_mcp/mcp_client.py")
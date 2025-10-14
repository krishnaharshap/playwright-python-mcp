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

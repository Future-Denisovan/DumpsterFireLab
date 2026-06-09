# 🔥 DumpsterFireLab

A Flask web app that answers the eternal question: **"Is this a dumpster fire?"**

Roll a virtual dice (1–6). Odd = 🔥 dumpster fire. Even = ✅ safe.

## Quick Start

```bash
pip install -r requirements.txt
python app/main.py
```

Visit `http://localhost:5000` and roll the dice.

## Deployment

This app deploys automatically to Azure Web Apps via GitHub Actions on push to `main`.

## Stack

- Python 3.11
- Flask
- Deployed via Azure Web Apps (OIDC / secretless auth)

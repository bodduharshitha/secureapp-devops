# SecureApp DevOps Platform

A small Python Flask application used as the application layer for an end-to-end DevOps learning project.

## Current Status

Phase 1: Python application and automated tests

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Application information |
| `/health` | Health check |
| `/info` | Application version and environment |

## Technology

- Python
- Flask
- pytest
- Git
- GitHub

## Local Setup

```bash
cd app

python -m venv .venv

source .venv/Scripts/activate

python -m pip install -r requirements.txt

python app.py
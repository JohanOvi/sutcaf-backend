# FastAPI Electronic Invoicing Backend

Backend service for electronic invoicing built with FastAPI, using Factus API for electronic invoicing, following Clean Architecture and DDD principles.

## Tech Stack
- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite (development)
- Pyenv + Virtualenv

## Project Structure
- app/api: HTTP layer
- app/domain: business rules
- app/application: use cases
- app/infrastructure: persistence and external services

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
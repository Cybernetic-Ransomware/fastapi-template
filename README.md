# Template
This repository contains a template for FastAPI-based projects.

## Overview
The goal of this project is to provide a clean and extensible starting point for building FastAPI applications.

## Features
- Clean and modular project structure,
- Docker deployment support,
- Pre-commit hooks for linting and formatting,
- Dev environment without docker instance.


## Requirements
- Python >=3.13.3 with [UV](https://github.com/astral-sh/uv) package manager
- Docker Desktop / Docker + Compose

## Getting Started (Windows)
### Deploy
1. Clone the repository:
      ```powershell
      git clone https://github.com/Cybernetic-Ransomware/fastapi-template.git
      ```
2. Set .env file based on the template.
3. Run using Docker:
      ```powershell
      docker-compose -f .\docker\docker-compose.yml up --build -d
      ```
### Dev-instance
1. Clone the repository:
      ```powershell
      git clone https://github.com/Cybernetic-Ransomware/fastapi-template.git
      ```
2. Set .env file based on the template.
3. Install UV:
      ```powershell
   pip install uv
      ```
4. Install dependencies:
      ```powershell
   uv sync
      ```
5. Configure interpreter in correct way for your IDE,
6. Install pre-commit hooks:
      ```powershell
      uv run pre-commit install
      uv run pre-commit autoupdate
      uv run pre-commit run --all-files
      ```
7. Run the application locally:
      ```powershell
      uv run uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload
      ```

## Testing
#### Postman
- The repository will include a Postman collection with ready-to-import webhook mockers

#### Pytest
```powershell
uv sync --extra dev
uv run pytest
```

#### Ruff
```powershell
uv sync --extra dev
uv run ruff check
```
or as a standalone tool:
```powershell
uvx ruff check
```

#### Mypy
```powershell
uv sync --extra dev
uv run mypy .\src\
```
or as a standalone tool:
```powershell
uvx mypy .\src\
```

#### Database Access:
To describe

## Useful links and documentation
- Description: [site_name](https://placeholder.com/)

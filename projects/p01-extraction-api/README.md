# p01-extraction-api

Extraction API: a Python 3.12 package (`extraction_api`) with a src layout. It is currently a
skeleton that exposes `__version__`; the extraction logic is not implemented yet.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (it installs Python 3.12 if needed)
- Docker, only for the container steps below

## Setup

```bash
cd projects/p01-extraction-api
uv sync
```

## Run checks

Same commands as CI:

```bash
uv run ruff check
uv run ruff format --check
uv run mypy
uv run pytest
```

## Run with Docker

```bash
docker build -t extraction-api .
docker run --rm extraction-api   # prints the package version, e.g. 0.1.0
```

The image is multi-stage, runs as a non-root user, and contains only the virtualenv and `src`.

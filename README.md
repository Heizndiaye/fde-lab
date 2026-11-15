# fde-lab

A monorepo of eight independent Python projects under `projects/`, each with its own `pyproject.toml`, lockfile and tests, sharing one root lint config (`ruff.toml`) and one set of pre-commit hooks (ruff, ruff-format, gitleaks). Python 3.12 and [uv](https://docs.astral.sh/uv/) are used throughout.

## Run checks

Root hooks (lint, format, secret scan), after a one-time `uv tool install pre-commit && pre-commit install`:

```bash
pre-commit run --all-files
```

Per project (example: `p01-extraction-api`):

```bash
cd projects/p01-extraction-api
uv sync
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```

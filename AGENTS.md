# AGENTS.md

## workflow

-write the failing test first, then the code.
-One small change per commit
-Run lint, type-check and tests before saying "done"

## Limits

-Never commit secrets or .env files.
-No Co-Authored-by or "Generated with" lines
-Ask before adding dependency.
-Do not edit tests to make them pass.

## Stack

- Python 3.12, uv, pytest, ruff, mypy.

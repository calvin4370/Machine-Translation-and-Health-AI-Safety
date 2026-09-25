.PHONY: install test

# Sets up .venv from uv.lock so every machine gets identical package versions
install:
	uv sync

test:
	uv run pytest

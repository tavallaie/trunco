.PHONY: help sync install test lint format format-check check docs serve pre-commit-install

UV ?= uv

help:
	@echo "Trunco development targets:"
	@echo "  make sync          Install/sync dev dependencies (uv)"
	@echo "  make install       sync + editable install"
	@echo "  make test          Run pytest"
	@echo "  make lint          Run ruff linter"
	@echo "  make format        Auto-fix lint issues and format with ruff"
	@echo "  make format-check  Check formatting without writing"
	@echo "  make check         lint + test"
	@echo "  make pre-commit-install  Install pre-push hook (ruff)"
	@echo "  make docs          Build docs site → docs/_site/"
	@echo "  make serve         Preview docs at http://127.0.0.1:8000"

sync:
	$(UV) sync

install: sync
	$(UV) pip install -e .

test:
	$(UV) run pytest

lint:
	$(UV) run ruff check .

format:
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

format-check:
	$(UV) run ruff format --check .

check: lint test

docs:
	$(UV) run python docs/build.py

serve:
	$(UV) run python docs/serve.py

pre-commit-install: sync
	$(UV) run pre-commit install --hook-type pre-push
.PHONY: run test lint

run:
	uvicorn app.main:app --reload --port 8000

test:
	python -m pytest

lint:
	ruff check --fix

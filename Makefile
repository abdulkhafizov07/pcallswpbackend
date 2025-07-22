
VENV := env
PIP := $(VENV)/bin/pip
BLACK := $(VENV)/bin/black
ISORT := $(VENV)/bin/isort
FLAKE8 := $(VENV)/bin/flake8
PYTEST := $(VENV)/bin/pytest
UVICORN := $(VENV)/bin/uvicorn
ALEMBIC := $(VENV)/bin/alembic

.PHONY: build dev install install-dev format lint test clean ci

build-db:
	$(ALEMBIC) upgrade head

build:
	docker build -t pcallswp-backend .

dev:
	$(UVICORN) main:app --reload

install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements.txt -r requirements-dev.txt

format:
	$(BLACK) .
	$(ISORT) .

lint:
	$(FLAKE8) . --count

test:
	$(PYTEST)

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache .mypy_cache dist htmlcov

ci: install-dev format lint test

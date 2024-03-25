pycache:
	@echo "Running Clean Pycache..."
	@find . \( -name *.py[co] -o -name __pycache__ \) -delete

setup-dev:
	@poetry run pre-commit install

run:
	@poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	@poetry run pytest

test-matching:
	@poetry run pytest ./tests -vv -k $(K)

unit-tests:
	@poetry run pytest ./tests -m "not integration"

integration-tests:
	@poetry run pytest ./tests -m integration

coverage:
	@poetry run pytest --cov=app --cov-report=term-missing --cov-report=xml ./tests/

lint:
	@poetry run ruff check .

lint-fix:
	@poetry run ruff check . --fix

.PHONY: run test generate-coverage lint-check lint-fix

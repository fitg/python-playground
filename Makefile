unit-test:
	poetry run pytest tests/unit_tests

lint:
	poetry run flake8

black:
	poetry run black -v .

mypy:
	poetry run mypy src
	poetry run mypy tests

start:
	./scripts/run_local.sh

smoke:
	./scripts/test_service.sh

destroy:
	docker rm -f python-playground

all: unit-test black mypy lint start smoke destroy

run: unit-test black mypy lint start smoke

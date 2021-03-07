unit-test:
	poetry run pytest tests/unit_tests

lint:
	poetry run flake8

black:
	poetry run black .

start:
	./scripts/run_local.sh

smoke:
	./scripts/test_service.sh

destroy:
	docker rm -f python-playground

all: unit-test black lint start smoke destroy

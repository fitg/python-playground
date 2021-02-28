unit-test:
	poetry run pytest tests/unit_tests

lint:
	poetry run flake8

black:
	poetry run black .

run:
	poetry run run_local

all: unit-test black lint run
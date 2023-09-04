install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

plain:
	poetry run gendiff --format plain ./tests/fixtures/file1.json ./tests/fixtures/file2.json

stylish:
	poetry run gendiff --format stylish ./tests/fixtures/file1.json ./tests/fixtures/file2.json
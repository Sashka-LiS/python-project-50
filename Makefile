install:
	poetry install

build: check
	poetry build

test:
	poetry run pytest -vv

lint:
	poetry run flake8 --extend-ignore E501,C901 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

plain_flat_json:
	poetry run gendiff --format plain tests/fixtures/json/file1.json tests/fixtures/json/file2.json

stylish_flat_json:
	poetry run gendiff --format stylish tests/fixtures/json/file1.json tests/fixtures/json/file2.json

plain_flat_yaml:
	poetry run gendiff --format plain tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

stylish_flat_yaml:
	poetry run gendiff --format stylish tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

json_flat_json:
	poetry run gendiff --format json tests/fixtures/json/file1.json tests/fixtures/json/file2.json

json_flat_yaml:
	poetry run gendiff --format json tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

plain_tree_json:
	poetry run gendiff --format plain tests/fixtures/json/file1_tree.json tests/fixtures/json/file2_tree.json

stylish_tree_json:
	poetry run gendiff --format stylish tests/fixtures/json/file1_tree.json tests/fixtures/json/file2_tree.json

plain_tree_yaml:
	poetry run gendiff --format plain tests/fixtures/yaml/file1_tree.yaml tests/fixtures/yaml/file2_tree.yaml

stylish_tree_yaml:
	poetry run gendiff --format stylish tests/fixtures/yaml/file1_tree.yaml tests/fixtures/yaml/file2_tree.yaml

json_tree_json:
	poetry run gendiff --format json tests/fixtures/json/file1_tree.json tests/fixtures/json/file2_tree.json

json_tree_yaml:
	poetry run gendiff --format json tests/fixtures/yaml/file1_tree.yaml tests/fixtures/yaml/file2_tree.yaml
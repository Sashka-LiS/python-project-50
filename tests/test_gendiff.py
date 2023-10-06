import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def links():

    files = {
        "file1_flat_json": "tests/fixtures/json/file1.json",
        "file1_tree_json": "tests/fixtures/json/file1_tree.json",
        "file2_flat_json": "tests/fixtures/json/file2.json",
        "file2_tree_json": "tests/fixtures/json/file2_tree.json",

        "file1_flat_yaml": "tests/fixtures/yaml/file1.yaml",
        "file1_tree_yaml": "tests/fixtures/yaml/file1_tree.yaml",
        "file2_flat_yaml": "tests/fixtures/yaml/file2.yaml",
        "file2_tree_yaml": "tests/fixtures/yaml/file2_tree.yaml",

        "result_flat_plain": "tests/fixtures/result/result_flat_plain.txt",
        "result_tree_plain": "tests/fixtures/result/result_tree_plain.txt",
        "result_flat_stylish": "tests/fixtures/result/result_flat_stylish.txt",
        "result_tree_stylish": "tests/fixtures/result/result_tree_stylish.txt",
        "result_flat_json": "tests/fixtures/result/result_flat_json.txt",
        "result_tree_json": "tests/fixtures/result/result_tree_json.txt"
}

    return files


def test_flat_plain(links):

    with open(links["result_flat_plain"]) as result_file:
        expected = result_file.read()
        assert generate_diff(links["file1_flat_json"], links["file2_flat_json"], "plain") == expected
        assert generate_diff(links["file1_flat_yaml"], links["file2_flat_yaml"], "plain") == expected


def test_tree_plain(links):

    with open(links["result_tree_plain"]) as result_file:
        expected = result_file.read()
        assert generate_diff(links["file1_tree_json"], links["file2_tree_json"], "plain") == expected
        assert generate_diff(links["file1_tree_yaml"], links["file2_tree_yaml"], "plain") == expected


def test_flat_stylish(links):

    with open(links["result_flat_stylish"]) as result_file:
        expected = result_file.read()
        assert generate_diff(links["file1_flat_json"], links["file2_flat_json"], "stylish") == expected
        assert generate_diff(links["file1_flat_yaml"], links["file2_flat_yaml"], "stylish") == expected


def test_tree_stylish(links):

    with open(links["result_tree_stylish"]) as result_file:
        expected = result_file.read()
        assert generate_diff(links["file1_tree_json"], links["file2_tree_json"], "stylish") == expected
        assert generate_diff(links["file1_tree_yaml"], links["file2_tree_yaml"], "stylish") == expected


def test_flat_json(links):

    with open(links["result_flat_json"]) as result_file:
        expected = result_file.read()
        assert generate_diff(links["file1_flat_json"], links["file2_flat_json"], "json") == expected
        assert generate_diff(links["file1_flat_yaml"], links["file2_flat_yaml"], "json") == expected


def test_tree_json(links):

    with open(links["result_tree_json"]) as result_file:
        expected = result_file.read()
        assert generate_diff(links["file1_tree_json"], links["file2_tree_json"], "json") == expected
        assert generate_diff(links["file1_tree_yaml"], links["file2_tree_yaml"], "json") == expected

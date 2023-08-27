from gendiff.gendiff import generate_difference


def test_generate_difference():
    """тест функции с .json файлами"""

    with open("tests/fixtures/expected_json.txt", "r") as f:
        expected_result = f.read()
        assert generate_difference("tests/fixtures/file1.json", "tests/fixtures/file2.json") == expected_result


def test_generate_difference():
    """тест функции с .yaml файлами"""

    with open("tests/fixtures/expected_yaml.txt", "r") as f:
        expected_result = f.read()
        assert generate_difference("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml") == expected_result
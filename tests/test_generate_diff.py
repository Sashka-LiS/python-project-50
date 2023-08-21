from gendiff.output_diff import generate_diff
from gendiff.find_diff import find_difference


def test_generate_diff():
    path_file1 = "tests/fixtures/file1.json"
    path_file2 = "tests/fixtures/file2.json"
    diff = find_difference(path_file1, path_file2)
    with open("tests/fixtures/answer.txt") as answer_file:
        result = "".join(answer_file.readlines())
        assert generate_diff(diff) == result

from gendiff.output_diff import generate_diff
from gendiff.find_diff import find_difference


path_file1 = "tests/fixtures/file1.json"
path_file2 = "tests/fixtures/file2.json"
diff = find_difference(path_file1, path_file2)
reference = "{\n"+"  - follow: False"+"\n    host: hexlet.io"+"\n  - proxy: 123.234.53.22"+"\n  - timeout: 50"+"\n  + timeout: 20"+"\n  + verbose: True"+"\n}" # noqa


def test_generate_diff():
    assert generate_diff(diff) == reference

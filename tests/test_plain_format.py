from gendiff.formatters.plain import plain


def test_plain_format():
    with open("tests/fixtures/expected_plain.txt") as f:
        result = f.read()
        assert plain("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result
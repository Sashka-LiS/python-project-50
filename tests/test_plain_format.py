from gendiff.formatters.render_plain import plain_view


def test_plain_format():
    
    with open("tests/fixtures/expected_plain.txt") as f:
        result = f.read()
        assert plain_view("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result
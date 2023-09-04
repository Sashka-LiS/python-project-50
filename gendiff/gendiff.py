from gendiff.parser import get_file_extension, parse
from gendiff.find_diff import find_diff
from gendiff.formatters.render import render


def generate_diff(first_file: str, second_file: str, format: str) -> str:
    data1 = parse(first_file, file_extension=get_file_extension(first_file))
    data2 = parse(second_file, file_extension=get_file_extension(second_file))
    diff = find_diff(data1, data2)
    print(render(diff, format))

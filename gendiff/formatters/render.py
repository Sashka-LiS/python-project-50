from gendiff.formatters.render_plain import render_plain
from gendiff.formatters.render_stylish import render_stylish
from gendiff.formatters.render_json import render_json
from gendiff.constants import PLAIN, STYLISH, JSON


def render(diff: list, format: str) -> str:

    if format == PLAIN:
        result = render_plain(diff)
    elif format == JSON:
        result = render_json(diff)
    elif format == STYLISH:
        result = render_stylish(diff)

    return result

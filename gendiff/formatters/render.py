from gendiff.formatters.render_plain import plain_view
from gendiff.formatters.render_stylish import stylish_view
from gendiff.constants import PLAIN, STYLISH


def render(diff: list, format: str) -> str:

    if format == PLAIN:
        result = plain_view(diff)
    elif format == STYLISH:
        result = stylish_view(diff)

    return result

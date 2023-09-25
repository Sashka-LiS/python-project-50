from gendiff.constants import ADDED, REMOVED, UNCHANGED, UPDATED, NESTED, TEMPLATE_STYLISH, TEMPLATE_NESTED
from itertools import chain


def render_stylish(diff: list) -> str:
    '''Отображает различие в формате stylish'''

    result = iter_diff(diff)

    return result


def iter_diff(diff: any, depth: int = 0) -> str:
    """Итерирует список узлов внутреннего представления разницы и возвращает строку разницы"""

    lines = []
    indent = "    " * depth

    for node in diff:

        if node["status"] == ADDED:
            lines.append(create_line(node["key"], node["add_value"], "+", depth))
        elif node["status"] == REMOVED:
            lines.append(create_line(node["key"], node["del_value"], "-", depth))
        elif node["status"] == UNCHANGED:
            lines.append(create_line(node["key"], node["add_value"], " ", depth))
        elif node["status"] == UPDATED:
            lines.append(create_line(node["key"], node["del_value"], "-", depth))
            lines.append(create_line(node["key"], node["add_value"], "+", depth))
        elif node["status"] == NESTED:
            diff = node["children"]
            lines.append(TEMPLATE_NESTED.format(indent, node["key"], iter_diff(diff, depth + 1)))

    strings = chain("{", lines, [indent + "}"])
    result = "\n".join(strings)

    return result


def create_line(key: any, value: any, sign: str, depth: int) -> str:
    """Создает одну строку для окончательного рендеринга"""

    line = []
    indent = "    " * depth

    if isinstance(value, dict):
        line.append(TEMPLATE_STYLISH.format(indent, sign, key, render_dict(value, depth + 1)))
    else:
        line.append(TEMPLATE_STYLISH.format(indent, sign, key, convert(value)))

    result = "\n".join(line)

    return result


def render_dict(_dict: dict, depth: int) -> str:
    """Представление словаря"""

    lines = []
    indent = "    " * depth

    for key, value in _dict.items():
        lines.append(create_line(key, value, " ", depth))

    strings = chain("{", lines, [indent + "}"])
    result = "\n".join(strings)

    return result


def convert(value: any) -> str:
    """Конвертирует значение в тип str для унификации"""

    if isinstance(value, bool):
        result = str(value).lower()
    elif isinstance(value, int):
        result = str(value)
    elif isinstance(value, dict):
        result = "[complex value]"
    elif value is None:
        result = "null"
    else:
        result = str(value)

    return result

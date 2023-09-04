from gendiff.constants import ADDED, REMOVED, UNCHANGED, UPDATED, TEMPLATE_STYLISH
from itertools import chain


def stylish_view(diff: list) -> str:
    '''Отображает различие в формате stylish'''

    result = _iter(diff)

    return result


def _iter(diff: any, depth: int = 0) -> str:
    """Итерирует список узлов внутреннего представления разницы и возвращает строку разницы"""

    lines = []
    indent = "    " * depth

    for node in diff:

        key = node["key"]
        status = node["status"]
        add_value = node["add_value"]
        del_value = node["del_value"]
        sign_add = "+"
        sign_del = "-"
        sign_unchanged = " "
        
        if status == ADDED:
            lines.append(create_line(key, add_value, sign_add, depth))
        elif status == REMOVED:
            lines.append(create_line(key, del_value, sign_del, depth))
        elif status == UNCHANGED:
            lines.append(create_line(key, add_value, sign_unchanged, depth))
        elif status == UPDATED:
            lines.append(create_line(key, del_value, sign_del, depth))
            lines.append(create_line(key, add_value, sign_add, depth))

    strings = chain("{", lines, indent + "}")
    result = "\n".join(strings)

    return result


def create_line(key: any, value: any, sign: str, depth: int) -> str:
    """Создает одну строку для окончательного рендеринга"""

    line = []
    indent = "    " * depth
    
    line.append(TEMPLATE_STYLISH.format(indent, sign, key, convert(value)))

    result = "\n".join(line)

    return result



def convert(value: any) -> str:
    """Конвертирует значение в тип str для унификации"""

    if isinstance(value, bool):
        result = str(value).lower()
    else:
        result = str(value)

    return result
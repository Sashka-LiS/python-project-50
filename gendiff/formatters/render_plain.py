from gendiff.constants import ADDED, REMOVED, UNCHANGED, UPDATED, TEMPLATE_PLAIN, TEMPLATE_UPDATED_PLAIN


def plain_view(diff: list) -> str:
    lines = []

    for node in diff:

        key = node["key"]
        status = node["status"]
        add_value = node["add_value"]
        del_value = node["del_value"]

        if node["status"] == ADDED:
            lines.append(TEMPLATE_PLAIN.format(key, status, convert(add_value)))
        elif node["status"] == REMOVED:
            lines.append(TEMPLATE_PLAIN.format(key, status, convert(del_value)))
        elif node["status"] == UNCHANGED:
            lines.append(TEMPLATE_PLAIN.format(key, status, convert(add_value)))
        elif node["status"] == UPDATED:
            lines.append(TEMPLATE_UPDATED_PLAIN.format(key, status, convert(del_value), convert(add_value)))

    result = "\n".join(lines)

    return result


def convert(value: any) -> str:
    """Конвертирует значение в тип str для унификации"""

    if isinstance(value, bool):
        result = str(value).lower()
    else:
        result = str(value)

    return result

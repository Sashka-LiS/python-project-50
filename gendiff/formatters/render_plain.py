from gendiff.constants import (ADDED,
                               REMOVED,
                               UPDATED,
                               NESTED,

                               TEMPLATE_PLAIN_PATH,
                               TEMPLATE_PLAIN_ADDED,
                               TEMPLATE_PLAIN_REMOVED,
                               TEMPLATE_PLAIN_UPDATED)


def render_plain(diff: list, source: str = "") -> str:

    lines = []

    for node in diff:

        if source:
            path = TEMPLATE_PLAIN_PATH.format(source, node["key"])
        else:
            path = node["key"]

        if node["status"] == ADDED:
            lines.append(TEMPLATE_PLAIN_ADDED.format(path, convert(node["add_value"])))
        elif node["status"] == REMOVED:
            lines.append(TEMPLATE_PLAIN_REMOVED.format(path))
        elif node["status"] == UPDATED:
            lines.append(TEMPLATE_PLAIN_UPDATED.format(path, convert(node["del_value"]), convert(node["add_value"])))
        elif node["status"] == NESTED:
            diff = node["children"]
            lines.append(render_plain(diff, path))

    result = "\n".join(lines)

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
        result = f"'{str(value)}'"

    return result

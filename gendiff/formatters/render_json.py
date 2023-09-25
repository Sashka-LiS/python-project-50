import json
from gendiff.constants import ADDED, REMOVED, UPDATED, UNCHANGED, NESTED


def render_json(diff: list):

    result = json.dumps(iter_diff(diff), indent=4)

    return result


def iter_diff(diff: list) -> dict:
    """итерирует внутреннее представление разницы для дальнейшего рендеринга"""

    diff_dict = {}

    for node in diff:
        if node["status"] == ADDED:
            diff_dict[node["key"]] = {"status": ADDED,
                                      "added value": node["add_value"]}
        elif node["status"] == REMOVED:
            diff_dict[node["key"]] = {"status": REMOVED,
                                      "deleted value": node["del_value"]}
        elif node["status"] == UPDATED:
            diff_dict[node["key"]] = {"status": UPDATED,
                                      "old value": node["del_value"],
                                      "new value": node["add_value"]}
        elif node["status"] == UNCHANGED:
            diff_dict[node["key"]] = {"status": UNCHANGED,
                                      "value": node["add_value"]}
        elif node["status"] == NESTED:
            diff_dict[node["key"]] = {"status": NESTED,
                                      "value": iter_diff(node["children"])}

    return diff_dict

from gendiff.constants import ADDED, REMOVED, UNCHANGED, UPDATED


def find_diff(data1: dict, data2: dict) -> list:

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    nodes = []

    for key in all_keys:
        if key in data1 and key not in data2:
            node = create_node(key, REMOVED, del_value=data1[key])
        elif key not in data1 and key in data2:
            node = create_node(key, ADDED, add_value=data2[key])
        elif data1[key] == data2[key]:
            node = create_node(key, UNCHANGED, add_value=data2[key])
        elif data1[key] != data2[key]:
            node = create_node(key, UPDATED, del_value=data1[key], add_value=data2[key])
        nodes.append(node)

    return nodes


def create_node(key, status, del_value=None, add_value=None, children=None) -> dict:

    node = {"key": key,
            "status": status,
            "del_value": del_value,
            "add_value": add_value,
            "children": children}

    return node

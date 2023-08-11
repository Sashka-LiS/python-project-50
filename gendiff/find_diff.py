from gendiff.get_data import get_data


def find_difference(path_file1: str, path_file2: str) -> dict:
    data1 = get_data(path_file1)
    data2 = get_data(path_file2)
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    diff = {}
    for key in all_keys:
        if key not in data1:
            diff.setdefault(f"added {key}", data2[key])
        elif key not in data2:
            diff.setdefault(f"deleted {key}", data1[key])
        elif data1[key] == data2[key]:
            diff.setdefault(f"{key}", data2[key])
        else:
            diff.setdefault(f"deleted {key}", data1[key])
            diff.setdefault(f"added {key}", data2[key])
    return diff

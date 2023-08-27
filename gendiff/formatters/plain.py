from gendiff.parser import get_file_extension, parse


def create_str(key, status, del_value = None, add_value = None):
    if status == "removed":
        result_str = f"key: {key} / status: {status} / value: {del_value}\n"
    elif status == "added":
        result_str = f"key: {key} / status: {status} / value: {add_value}\n"
    elif status == "unchanged":
        result_str = f"key: {key} / status: {status} / value: {add_value}\n"
    elif status == "changed":
        result_str = f"key: {key} / status: {status} / value: {del_value} -> {add_value}\n"
    return result_str.lower()


def plain(file1_path: str, file2_path: str) -> str:
    extension1 = get_file_extension(file1_path)
    data1 = parse(file1_path, extension1)
    extension2 = get_file_extension(file2_path)
    data2 = parse(file2_path, extension2)
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))
    result_str = ""
    for key in all_keys:
        if key in data1 and key not in data2:
            status = "removed"
            result_str += create_str(key, status, del_value = data1[key])
        elif key not in data1 and key in data2:
            status = "added"
            result_str += create_str(key, status, add_value = data2[key])
        elif data1[key] == data2[key]:
            status = "unchanged"
            result_str += create_str(key, status, add_value = data2[key])
        elif data1[key] != data2[key]:
            status = "changed"
            result_str += create_str(key, status, del_value = data1[key], add_value = data2[key])
    return result_str.rstrip()
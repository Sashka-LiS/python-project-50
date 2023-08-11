def format_key(key: str) -> str:
    if key.startswith("added"):
        key = key.replace("added ", "  + ")
        return key
    elif key.startswith("deleted"):
        key = key.replace("deleted ", "  - ")
        return key
    else:
        key = f"    {key}"
        return key


def generate_diff(diff: dict) -> str:
    strings = []
    for key, value in diff.items():
        key = format_key(key)
        strings.append(f"{key}: {value}")
    return "{\n" + "\n".join(strings) + "\n}"

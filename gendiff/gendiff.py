from gendiff.parser import get_file_extension, parse


def generate_difference(first_file: str, second_file: str) -> str:
    file1 = parse(first_file, file_extension=get_file_extension(first_file))
    file2 = parse(second_file, file_extension=get_file_extension(second_file))
    dict1 = {value: key for key, value in file1.items()}
    dict2 = {value: key for key, value in file2.items()}
    temporary_dict = dict()
    temporary_dict.update(dict1)
    temporary_dict.update(dict2)
    sorted_temporary_dict = sorted(temporary_dict, key=temporary_dict.get)
    result_dict = dict()
    for key in sorted_temporary_dict:
        result_dict[key] = temporary_dict[key]
    result_str = "{\n"
    for key, value in result_dict.items():
        result_str += "  "
        if dict1.get(key) and not dict2.get(key):
            result_str += "- "
        elif not dict1.get(key) and dict2.get(key):
            result_str += "+ "
        elif dict1.get(key) and dict2.get(key):
            result_str += "  "
        result_str += f"{value}: {key}\n"
    result_str += "}"
    result_str = result_str.lower()
    return result_str

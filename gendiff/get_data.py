import json


def get_data(path_to_file: str)-> dict:
    data = json.load(open(path_to_file))
    return data

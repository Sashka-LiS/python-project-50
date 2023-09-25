import json
import yaml
import os
import argparse
from gendiff.constants import STYLISH, PLAIN, JSON


def get_file_extension(file_path: str) -> str:
    """возвращает расширение файла"""

    _, file_extension = os.path.splitext(file_path)

    return file_extension


def parse(file_path: str, file_extension: str):

    if file_extension == ".json":
        result = json.load(open(file_path, "r"))
        return result

    if file_extension == ".yml" or ".yaml":
        result = yaml.safe_load(open(file_path))
        return result


def parse_arguments():

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", type=str, choices=[STYLISH, PLAIN, JSON], default=STYLISH, help="set format of output")
    args = parser.parse_args()

    return args

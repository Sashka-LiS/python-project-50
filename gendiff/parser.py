import json
import yaml
import os


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

import json
import os


def read_file(file_path="data.json"):
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_file(content, file_path="data.json"):
    with open(file_path, "w") as file:
        json.dump(content, file, indent=4)


def initialize_file(file_path="data.json"):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)

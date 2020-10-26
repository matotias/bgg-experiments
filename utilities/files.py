from pathlib import Path
from typing import Dict
import json


def read_json_files(path: str) -> Dict[str, Dict[str, str]]:
    """
    This function returns a dict with all the json files in all folders and
    subfolders of the given path
    :param path: path where the json files will be searched in
    :return: dictionary with all the json files
    """
    json_files = Path(path).rglob('*.json')
    return {
        file.stem: json.loads(open(str(file), 'r').read())
        for file in json_files
    }


def read_json_file(path: str) -> Dict[str, str]:
    return json.loads(open(str(Path(path)), 'r').read())

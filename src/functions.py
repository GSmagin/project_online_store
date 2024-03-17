import json
from confing import dir_json


def products_json_file(dir_path=dir_json):
    with open(dir_path,  encoding='utf-8') as f:
        products_json = json.load(f)
        return products_json

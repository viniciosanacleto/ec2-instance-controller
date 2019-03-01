import json


def read_instances_json(file_name='instances'):
    with open(file_name + '.json') as f:
        data = json.load(f)
        if data:
            return data
        else:
            return None

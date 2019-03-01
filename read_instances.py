import json


def readInstancesJson(file_name='instances'):
    with open(file_name + '.json') as f:
        data = json.load(f)
        if data:
            return data
        else:
            return None

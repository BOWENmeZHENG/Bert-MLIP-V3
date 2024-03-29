import json

def load_json(file):
    with open(file, "r") as f:
        data = json.loads(f.read())
    return data

def read_data(json_file):
    data_list = []
    with open(json_file) as f:
        for jsonObj in f:
            record = json.loads(jsonObj)
            data_list.append(record)
    return data_list

# Extract an entry from training data
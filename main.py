import json
import os.path
path = "./api/all.json"

if os.path.isfile(path):
    print("found file: " + path)

with open(path) as json_file:
    json_data = json.load(json_file)
    print(json_data)
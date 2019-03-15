import json
import os.path
import psycopg2


path = "./api/all.json"
endpoint = "bigdatalabstoresource.cbjor7hidfop.eu-west-1.rds.amazonaws.com"
port = 5432



with open("./credentials/postgres") as credentials:
    content = credentials.readlines()
content = [x.strip() for x in content]
conn = psycopg2.connect(host=content[0], port=port, database=content[1], user=content[2], password=content[3])

print(conn)


if os.path.isfile(path):
    print("found file: " + path)

with open(path) as json_file:
    json_data = json.load(json_file)
    for id in json_data:
        print(id)
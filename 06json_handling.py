import json

data = {
    "id": 0,
    "name": "Mau",
    "age": 24,
    "position": "Web Developer"
}

data_as_json = json.dumps(data)
print(type(data_as_json))

with open('06data.json', 'w') as json_file:
    json.dump(data, json_file)


with open('06data.json', 'r') as json_file:
    pythonic_json = json.load(json_file)

print(pythonic_json)

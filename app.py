import json

data = {"Name": "Benjamin", "Age" : 24, "Nationality": "Kenyan"}
json_string = json.dumps(data)
print(json_string)
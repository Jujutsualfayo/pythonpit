import json

data = {"Name": "Mitchel Maina", "School": "Mary Hill", "Age": 24}
with open("data.json" "w") as f:
    json.dump(data, f)


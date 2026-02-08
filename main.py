import json

with open("data.json", "r") as file:
    data = json.load(file)
    data.append({
        "name": "Aleksandar I",
        "age": 38,
        "height": 193,
        "gender": "male"
    })

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
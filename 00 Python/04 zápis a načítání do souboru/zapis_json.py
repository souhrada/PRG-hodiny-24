import json

path = "data.json"

animal = {
    "Name": "Hugo",
    "Type": "elephant",
    "height": "tall"
}

# pozor, při práci s json píšeme mode="w", nestačí samostatné "w"
with open(path, mode="w") as file:
    json.dump(animal, file, indent=2)

# pozor, při práci s json píšeme mode="r", nestačí samostatné "r"
with open(path, mode="r") as file:
    data = json.load(file)

print(data)
example = {
    "student": "Alice",
    "teacher": "Bob",
    "janitor": "Charlie"
}


# print(example["janitor"])


cat = {
    "name": "Mycash",
    "age": 7,
    "color": "purpleblack",
    "fav_food": "lasagna",
    "alive": True,
    "friends": ["Dragon", "Jerry"]
}




print(cat["friends"][1])

print(cat)

for key in cat:
    print(key)

for key in cat:
    print(cat[key]) #1. kolo cat["name"] 2. kolo cat["age"]

# alternativní výpis hodnot (values)

for value in cat.values():
    print(value)

# alternativní způsob 2

for key, value in cat.items():
    print(f"Tohle je key {key}, tohle je value {value}")


for friend in cat["friends"]:
    print(friend)


cat["fav_food"] = "mouse"

print(cat)


if "fav_food" in cat:
    print(cat["fav_food"])

cat["number_of_legs"] = 4

print(cat)
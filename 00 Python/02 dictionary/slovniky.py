# dictionary (slovník) soubor zpárovaných klíčů a hodnot (key - value)
# levá strana = key, pravá strana = value

example = {
    "student": "Alice",
    "teacher": "Bob",
    "janitor": "Charlie",
}

# pro vypsání jedné hodnoty používáme název_slovníku[key]
print(example["janitor"])


cat = {
    "name": "Mycash",
    "age": 7,
    "color": "purpleblack",
    "fav_food": "lasagna",
    "alive": True,
    "friends": ["Dragon", "Jerry"],
}

# vypsání druhé položky ze slovníkové hodnoty, která je seznamem
print(cat["friends"][1])

# vypsání slovníku, jako celého objektu
print(cat)


# pomocí jednoduchého for můžeme vypsat všechny key (levá strana)
for key in cat:
    print(key)


# pokud chceme vypsat value (hodnoty, pravá strana), můžeme použít několik způsobů:
for key in cat:
    print(cat[key])  # 1. kolo cyklu je cat["name"] 2. kolo cat["age"] atd...

# alternativní výpis hodnot (values)
for value in cat.values():
    print(value)

# alternativní způsob II

for key, value in cat.items():
    print(f"Tohle je key {key}, tohle je value {value}")

# vypsání všech položek seznamu friends
for friend in cat["friends"]:
    print(friend)

# přepsání hodnoty fav_food
cat["fav_food"] = "mouse"

print(cat)

# kontrola, jestli existuje hodnota "fav_food"
if "fav_food" in cat:
    print(cat["fav_food"])

# přidání nového párů key-value
cat["number_of_legs"] = 4

print(cat)


# otázky z hodiny:
# jak vypsat všechny values (hodnoty), včetně listu (seznamu) bez hranatých závorek


for key, value in cat.items():
    if isinstance(value, list):
        for friend in cat[key]:
            print(friend, end=" ")
        print()
    else:
        print(value)

    # is instance kontroluje, jestli daná věc je určitého typu
    # isinstance(co_kontrolujeme, datový_typ_který_ověřujeme)
    # alternativně by šla použít i funkce type() --> if type(value) == list


# nebo hezčí zápis


for key, value in cat.items():
    if isinstance(value, list):
        print(", ".join(value))
        # funkce .join spojuje položky z seznamu --> čím_oddělit.join(seznam)
    else:
        print(value)

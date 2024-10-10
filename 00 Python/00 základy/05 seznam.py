names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Hannah",
    "Isaac",
    "Jack",
    "Kathy",
    "Leo",
    "Mia",
    "Nina",
    "Oscar",
    "Paul",
    "Quinn",
    "Rita",
    "Sam",
    "Tina",
]

# jednotlivou položku vypisujeme stejně jako v Javascriptu název_seznamu[index]
print(names[3])

# celý seznam vypisujeme pomocí cyklu for
for name in names:
    print(name)

# když chceme i index, použijeme funkci enumerate
# v printu používáme tzv. f-string (viz látka 01)
for i, name in enumerate(names):
    print(f"{i+1}. {name}")

names = [
    "Alice", "Bob", "Charlie", "David", "Eve", 
    "Frank", "Grace", "Hannah", "Isaac", "Jack", 
    "Kathy", "Leo", "Mia", "Nina", "Oscar", 
    "Paul", "Quinn", "Rita", "Sam", "Tina"
]


print(names[3])

# celý seznam vypisujeme pomocí cyklu for
for name in names:
    print(name)

# když chceme i index, použijeme funkci enumerate
for i, name in enumerate(names):
    print(f"{i+1}. {name}")
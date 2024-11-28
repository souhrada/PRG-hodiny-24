import csv

path = "data.csv"

seznam = ["Anděla", "Josefína", "Jarmil"]

# with open(path, "w", encoding="utf-8") as file:
#     writer = csv.writer(file, delimiter=";")
#     writer.writerow(seznam)


# with open(path, "r", encoding="utf-8") as file:
#     reader = csv.reader(file, delimiter=";")
#     for row in reader:
#         print(row)


students = [
    {"Name": "Anděla", "School": "Třebešín", "fav_color": "blue"},
    {"Name": "Jarmil", "School": "Oxford", "fav_color": "green"}
]

with open(path, "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file,fieldnames=["Name", "School", "fav_color"], delimiter=";")

    writer.writeheader()

    writer.writerows(students)

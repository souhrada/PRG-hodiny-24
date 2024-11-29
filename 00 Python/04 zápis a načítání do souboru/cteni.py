# proměnná, pod kterou ukládáme cestu - není nutné, ale je vhodné pro přehlednější kód
path = "data.txt"

# "w" -> write, "a" -> append, "r" -> read
# with open otevře a na konci zavře soubor
with open(path, "r") as file: # otevři soubor z dané cesty pod proměnnou file
    content = file.read() # pod proměnnou content ulož, co jsi přečetl ze souboru
    print(content)
# proměnná, pod kterou ukládáme cestu - není nutné, ale je vhodné pro přehlednější kód
path = "data.txt"

# "w" -> write, "a" -> append, "r" -> read
with open(path, "w") as file: # otevři soubor z dané cesty pod proměnnou file
    file.write("hi") # do souboru zapiš "hi"



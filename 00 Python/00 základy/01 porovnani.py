# nepoužíváme let nebo const pro proměnné
krestni_jmeno = "Hugo"
cislo = 5
pravda = True

seznam_studentu = ["Emil", "Emilie", "Jarmila", "Jarmil", "Hvězdoň"]

# místo console.log používáme print
print(krestni_jmeno)

# funkce vytváříme pomocí slova def
def nahodna_funkce():
    print("funguje")

nahodna_funkce()

# !!! důležité odsazovat
# nepoužíváme složené závorky, odsazování určuje
# do jakého bloku patří kód
if cislo > 0:
    print("číslo je kladné")
elif cislo < 0:
    print("číslo je záporné")
else:
    print("číslo je 0")

pocitadlo = 1


# v javascriptu pro porovnávání používáme 3x rovnítko
# === v pythonu používáme 2x rovnítko ==
while pocitadlo < 11:
    print(pocitadlo)
    # python neumí pocitadlo++, musíme používat +=
    pocitadlo+=1

# range(od kolika, do kolika, po kolika)
# v tomto případě lze zkrátit na range(11)
for x in range(0, 11, 1):
    print(x)

for n in range(20, 0, -1):
    print(n)


for student in seznam_studentu:
    print(student)
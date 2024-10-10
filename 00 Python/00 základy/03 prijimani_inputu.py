jmeno = input("Zadej jméno: ")

print("Tvé jméno je", jmeno)


# pozor, input je vždy string, pokud chceme matematicky porovnávat,
# musíme převést na číslo, např. integer --> můžeme použít funkci int()

cislo = int(input("Zadej číslo:"))

if cislo > 0:
    print("Zadané číslo je kladné")

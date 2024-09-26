def pocitani(n):
    for cislo in range(1, n+1):
        if cislo == 13:
            continue
        print(cislo)

# nebo

def pocitani2(n):
    for cislo in range(1, n+1):
        if cislo != 13:
            print(cislo)

pocitani(15)
pocitani2(20)
pin = int(input("Zadej pin: "))
pokus = 0

while pin != 1234 or pokus < 2:
    pin = int(input("Zadej pin: "))
    pokus += 1



# nebo takhle

while True:
    pin = int(input("Zadej pin: "))
    if pin == 1234:
        print("Správný pin")
        break
    elif pokus > 2:
        print("moc pokusů")
        break
    print("zadal jsi špatný pin")
    pokus += 1

   

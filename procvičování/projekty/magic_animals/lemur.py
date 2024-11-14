import sys
import datetime as dt


# vytvoření dictionary, ve kterém jsou vypsané vlastnosti našeho zvířátka
lemur = {
    'name': "Mortimer",
    'color': "purpleblack",
    'health': 100,
    'hunger': 50,
    'thirst': 0,
    'cleanliness': 100,
    'energy': 90,
    'happiness': True,
    'alive': True,
    'gambler': False,
}

original_time = dt.datetime.now()


# Zde jsou různé funkce našeho programu, od krmení, přes čištění, spánek atd.        

def feeding():
    lemur['hunger'] -= 30
    if lemur['hunger'] < 0:
        lemur['alive'] = False
    

def pet_play():
    print(f"You've played fetch with {lemur['name']}. {lemur['name']} looks happy.")
    lemur['energy'] -= 10
    lemur['hunger'] += 10
    if lemur['happiness'] == False:
        lemur['happiness'] = True

def bathing():
   print(f"{lemur['name']} loves baths. {lemur['name']} is clean now.")
   lemur['cleanliness'] = 100

def sleeping():
    print(f"Your lullaby was very effective. {lemur['name']} slept for 12 hours.")
    lemur['energy'] = 100
    lemur['happiness'] = True

# tato funkce je pro uživatele, pokud chce znát aktuální hodnoty lemura
def display_status():
   print(f"Hunger: {lemur['hunger']} \n Energy: {lemur['energy']} \n Health: {lemur['health']} \n Thirst: {lemur['thirst']}")

# tato funkce nám umožní vypsat jednu samostatnou vlastnost
def display_attribute(attribute):
    if attribute not in lemur:
        print(f"Lemur doesn't have {attribute}")
    else:
        print(f"Current {attribute} is: {lemur[attribute]}")

# tuto funkci spouštíme na začátku kódu a kontroluje, jeslti je lemur na živu a celkově vytváří logiku hry
# mění štěstí, pokud je lemur hladový atp.
def check_lemur_status():
    if lemur['hunger'] > 100:
        lemur['alive'] == False
    elif lemur['hunger'] > 75:
        lemur['happiness'] == False

    if lemur['alive'] == False:
        print("Lemur died. :(")
        sys.exit()

def check_time():
    current_time = dt.datetime.now()
    if current_time > original_time + dt.timedelta(minutes=30):
        lemur['hunger'] += 10
        print(f"{lemur['name']} is getting hungry...")
        original_time = current_time
    


# zde vytváříme hlavní funkci našeho programu
def main():


    while True:
        
        
        check_time()
        # kontrola stavu lemura, která se spouští pokaždé před zadáním instrukce
        check_lemur_status()

        # instrukce pro uživatele, trojité uvozovky nám umožňují psát v kódu na více řádků
        print("""
              Instructions: For feeding press F, press S for status, press X for exit,
              press P for play, press l to put lemur to sleep, press b to bathe lemur
              """)
        
        # input uživatele, co chce dělat
        user_action = input("What do you want to do?")
        

        # alternative k podmínkám if elif else, která může být v určitých případech čitelnější
        # na základě zadaného písmenka spustíme požadovanou funkci
        match user_action.lower():
            case "f":
                feeding()
                print(f"Lemur has been fed. Current hunger: {lemur['hunger']}. Is lemur alive: {lemur['alive']}")
            case "x":
                print("Exiting...")
                sys.exit()
            case "s":
                display_status()
            case "p":
                pet_play()
            case "l":
                sleeping()
            case "b":
                bathing()
            case _:
                print("Wrong input")

    
# zde spouštíme hlavní funkci našeho programu, bývá vždy úplně na konci
main()
    





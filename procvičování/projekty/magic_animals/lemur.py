import sys

lemur = {
    "name": "Mortimer",
    "color": "purpleblack",
    "health": 100,
    "hunger": 50,
    "thirst": 0,
    "cleanliness": 100,
    "energy": 90,
    "happiness": True,
    "alive": True,
    "gambler": False,
}

def main():


    # TODO: finish instructions
    while True:
        check_lemur_status()
        print("""
              Instructions: For feeding press F, press S for status, press X for exit,
              press P for play, press l to put lemur to sleep, press b to bathe lemur
              """)
        
        user_action = input("What do you want to do?")
        
        match user_action.lower():
            case "f":
                feeding()
                print(f"Lemur has been fed. Current hunger: {lemur["hunger"]}. Is lemur alive: {lemur["alive"]}")
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

        

def feeding():
    lemur["hunger"] -= 30
    if lemur["hunger"] < 0:
        lemur["alive"] = False
    

def display_status():
   print(f"Hunger: {lemur["hunger"]} \n Energy: {lemur["energy"]} \n Health: {lemur["health"]} \n Thirst: {lemur["thirst"]}")


def display_attribute(attribute):
    if attribute not in lemur:
        print(f"Lemur doesn't have {attribute}")
    else:
        print(f"Current {attribute} is: {lemur[attribute]}")

def pet_play():
    print(f"You've played fetch with {lemur["name"]}. {lemur["name"]} looks happy.")
    lemur["energy"] -= 10
    lemur["hunger"] += 10
    if lemur["happiness"] == False:
        lemur["happiness"] = True

def bathing():
   print(f"{lemur["name"]} loves baths. {lemur["name"]} is clean now.")
   lemur["cleanliness"] = 100

def sleeping():
    print(f"Your lullaby was very effective. {lemur["name"]} slept for 12 hours.")
    lemur["energy"] = 100
    lemur["happiness"] = True

def check_lemur_status():
    if lemur["hunger"] > 100:
        lemur["alive"] == False
    elif lemur["hunger"] > 75:
        lemur["happiness"] == False

    if lemur["alive"] == False:
        print("Lemur died. :(")
        sys.exit()
    
    

main()
    





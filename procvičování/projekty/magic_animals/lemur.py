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

        print("Instructions: For feeding press F, press S for status, press X for exit")

        user_action = input("What do you want to do?")

        if user_action.lower() == "f":
            feeding()
            print(f"Lemur has been fed. Current hunger: {lemur["hunger"]}. Is lemur alive: {lemur["alive"]}")
        elif user_action.lower() == "x":
            print("Exiting...")
            sys.exit()
        elif user_action.lower() == "s":
            display_status()
        else:
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
    print("You've played fetch with Mortimer. Mortimer looks happy.")
    lemur["energy"] -= 10
    if lemur["happiness"] == False:
        lemur["happiness"] = True



main()
    





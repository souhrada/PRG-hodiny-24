lemur = {
    "name": "Mortimer",
    "color": "purpleblack",
    "health": 100,
    "hunger": 5,
    "thirst": 0,
    "cleanliness": 100,
    "energy": 90,
    "happiness": True,
    "alive": True,
}

def main():

    # TODO: finish instructions
    print("Instructions: For feeding press F")

    user_action = input("What do you want to do?")

    if user_action.lower() == "f":
        feeding()
        print(f"Lemur has been fed. Current hunger: {lemur["hunger"]}. Is lemur alive: {lemur["alive"]}")


def feeding():
    lemur["hunger"] -= 30
    if lemur["hunger"] < 0:
        lemur["alive"] = False




main()
    





import sys, json
import tkinter as tk

# vytvoření dictionary, ve kterém jsou vypsané vlastnosti našeho zvířátka
lemur = {}

root = None
text_label = None
stats_label = None

path = "save_data.json"

# Zde jsou různé funkce našeho programu, od krmení, přes čištění, spánek atd.        

# TODO: přidat tlačítko pro save hry
def save_game():
    global lemur
    global path
    with open(path, mode="w") as file:
        json.dump(lemur, file, indent=2)


def load_game():
    global lemur
    global path
    load_data = {}
    with open(path, mode="r") as file:
        load_data = json.load(file)

    
    if len(load_data) > 0:
        lemur = load_data
        print("loading")
    else:
        print("default")
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

def getting_hungry():
    global root
    lemur['hunger'] += 10
    update_stats()
    root.after(10000, getting_hungry)


def update_stats():
    global stats_label
    stats_label.config(text=f"""
                            Name: {lemur['name']}  
                            Health: {lemur['health']}
                            Hunger: {lemur['hunger']}
                            Thirst: {lemur['thirst']}
                            Energy: {lemur['energy']}
                            Happiness: {lemur['happiness']}
                                """)


def feeding():
    global text_label
    text_label.config(text=f"{lemur['name']} has been fed.")
    update_stats()
    lemur['hunger'] -= 30
    if lemur['hunger'] < 0:
        lemur['alive'] = False
    

# TODO: upravit zbylé funkce pro TKinter, podobně jako funguje feeding()

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



# TODO: implementovat s funkcí .after() pro TKinter
def check_lemur_status():
    if lemur['hunger'] > 100:
        lemur['alive'] == False
    elif lemur['hunger'] > 75:
        lemur['happiness'] == False

    if lemur['alive'] == False:
        print("Lemur died. :(")
        sys.exit()


# zde vytváříme hlavní funkci našeho programu
def main():
    global root, text_label, stats_label

    load_game()

    root = tk.Tk()
    
    root.title(f"{lemur['name']}")
    root.geometry("800x600")

    lemur_image = tk.PhotoImage(file="lemur.png")

    for x in range(3):
        root.grid_rowconfigure(x, weight=1)
        root.grid_columnconfigure(x, weight=1)


    image_label = tk.Label(root, image=lemur_image)
    image_label.grid(row=0, column=0)

    text_label = tk.Label(root, text=f"Welcome.\n What would you like to do?")
    text_label.grid(row=0, column=1)

    stats_label = tk.Label(root, text=f"""
                                    Name: {lemur['name']}  
                                    Health: {lemur['health']}
                                    Hunger: {lemur['hunger']}
                                    Thirst: {lemur['thirst']}
                                    Energy: {lemur['energy']}
                                    Happiness: {lemur['happiness']}
                                        """)
    stats_label.grid(row=0, column=2)
    

    feed_button = tk.Button(root, text=f"Feed {lemur['name']}", command=feeding)
    feed_button.grid(row=1, column=0)
    
    getting_hungry()
    root.mainloop()
    


    
# zde spouštíme hlavní funkci našeho programu, bývá vždy úplně na konci
if __name__ == "__main__":
    main()
    





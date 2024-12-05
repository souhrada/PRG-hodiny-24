# importuji knihovnu tkinter pod kratší přezdívkou tk
import tkinter as tk

def say_hello():
    print("Hello!!!")
    label_example.config(text="Hello!")

# root nám vytvoří naše GUI
root = tk.Tk()

# přidání nadpisu
root.title("Hello?")

# změna rozlišení
root.geometry("800x600")

# vytvořtení labelu (štítek s textem) pod proměnnou label_example
# root a text v závorce jsou povinné, font je nepovinný
label_example = tk.Label(root, text="Toto je náhodný text", font=("Consolas", 20))
# pakc nám úmístní náš label jednoduše do GUI
label_example.pack()

btn_example = tk.Button(root, text="Click me", command=say_hello)
btn_example.pack()

# toto spustí naše GUI
root.mainloop()
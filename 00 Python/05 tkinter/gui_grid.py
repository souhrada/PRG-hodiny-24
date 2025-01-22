import tkinter as tk


root = tk.Tk()

# pokud pracujeme s grid je dobré si předpřipravit mřížku, ať můžeme prvky
# vložit kamkoliv chceme - např. |_|_|_|
#                                |_|_|_|
#                                |_|_|x| <--- prvek můžeme vyložit přímo vpravo dolu

# příprava mřížky (weight 1 u všech řad nám říká, že všechny budou zabírat stejně místa)
# řady
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)

# sloupce
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)

# efektivnější je využít cyklus, který nám vytvoří např. 3x3 mřížku
for x in range(3):
    root.grid_rowconfigure(x, weight=1)
    root.grid_columnconfigure(x, weight=1)


label = tk.Label(root, text="Down right", bg="green")
label.grid(row=2, column=2)

root.mainloop()

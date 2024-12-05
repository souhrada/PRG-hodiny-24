import tkinter as tk

# label je jen parametr, takový placeholder, za který dosadíme opravdovou hodnotu
# až zavoláme funkci
def say_hello(label):
    print("Hello!!!")
    label.config(text="Hello!")

def main():
    root = tk.Tk()

    root.title("Hello?")
    root.geometry("800x600")

    label_example = tk.Label(root, text="Toto je náhodný text", font=("Consolas", 20))
    # grid nám umožňuje urovnat prvky na grid (mřížku)
    label_example.grid(row=0, column=1)

    # lambda je tzv. anonymní funkce, v našem případě lambda zavolá funkci say_hello
    # přes lambdbu můžeme do command= přidat funkci s parametrem (s informací/hodnout v závorce, kterou pošleme funkci, aby s ní mohla pracovat)
    btn_example = tk.Button(root, text="Click me", command=lambda: say_hello(label_example))
    btn_example.grid(row=1, column=1)

    btn_example2 = tk.Button(root, text="Click me", command=lambda: say_hello(label_example))
    btn_example2.grid(row=1, column=2)

    root.mainloop()
main()
import tkinter as tk


root = tk.Tk()


# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)

# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)

for x in range(3):
    root.grid_rowconfigure(x, weight=1)
    root.grid_columnconfigure(x, weight=1)


label = tk.Label(root, text="Down right", bg="green")
label.grid(row=2, column=2)

root.mainloop()
import sqlite3


# vytvoř spojení s databází
connection = sqlite3.connect("game.db")

# vytvoření kurzoru, který nám umožňuje navigaci po databázi
cursor = connection.cursor()


user_input = input("Přidej postavičku do databáze: ")

# zápis do db
cursor.execute("INSERT INTO characters (name) VALUES (?)", (user_input,))

# potvrzení vložení dat do db
connection.commit()

connection.close()
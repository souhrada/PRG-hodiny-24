import sqlite3


# vytvoř spojení s databází
connection = sqlite3.connect("game.db")

# vytvoření kurzoru, který nám umožňuje navigaci po databázi
cursor = connection.cursor()


user_input = input("Přidej postavičku do databáze: ")
user_input2 = input("Přidej classu do databáze: ")

# zápis do db
# cursor.execute("INSERT INTO characters (name, class) VALUES (?, ?)", (user_input, user_input2))

# potvrzení vložení dat do db
connection.commit()

cursor.execute("SELECT * FROM characters")

# fetchall() data získá a umožní nám je uložit pod proměnnou
# data se vrací jako list jednotlivých rows (řad) z databáze, kde data v řadě jsou v tuple 
# [(data za řady 1, další data z řady 1), (data z řady 2, další data z řady 2)]
rows = cursor.fetchall() 
for row in rows:
    print(row)

connection.close()
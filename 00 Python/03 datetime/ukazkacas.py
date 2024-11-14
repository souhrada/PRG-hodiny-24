# datetime je příliš dlouhý název, proto jej importujeme pod zkratkou dt
import datetime as dt

# vytváříme proměnnou now, pod kterou uložíme momentální čas
now = dt.datetime.now()

# Různé způsoby přístupu k současnému času

# celý čas
print(now)
# pouze měsíc
print(now.month)
print(now.day)
print(now.year)
print(now.second)

# delta time používáme pro odečítání, přičítání nebo porovnávání času
delta = dt.timedelta()

print("teď je ", now)
# nová proměnná minus 10 je současný čas - 10 minut (k odečtení času použijeme delta time)
minus10 = now - dt.timedelta(minutes=10)
print(minus10)

# pomocí funkce dattetime můžeme vytvořit nový, vlastní čas ve formátu roky, měsíce, dny, hodiny, minuty, sekundy, milisekundy
new_time = dt.datetime(2024,11,14,14,15,0,0)

# časy můžeme od sebe odečítat
how_long_till_break = new_time - now
print("Do přestávky zbývá", how_long_till_break)

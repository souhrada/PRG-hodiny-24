import datetime as dt


now = dt.datetime.now()

# print(now.month)
# print(now.day)
# print(now.year)
# print(now.second)

# delta = dt.timedelta()

print("teď je ", now)
minus10 = now - dt.timedelta(minutes=10)
print(minus10)

new_time = dt.datetime(2024,11,14,14,15,0,0)
how_long_till_break = new_time - now
print("Do přestávky zbývá", how_long_till_break)

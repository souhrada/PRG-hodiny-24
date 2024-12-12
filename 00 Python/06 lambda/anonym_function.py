def hello():
    print("Hello")

def plus10(x):
    print(x+10)


a = lambda x : x + 10
b = lambda: print("Hello")

print(a(0))

b()
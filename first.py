name = "My name is imran khan"
print(name.split())
print(type(name.splitlines()))
print(name)
x = "ZZZZZyZZZZyZZZyZZZZZyZZZZyZZZZZyZZZZZyZZZZZ"
y = 2323232.323
print(x.casefold())
print(x.encode())
print(x.find("y"))
print(x.count("y"))
print(x.index("y"))
print(x.isalnum())
print(x.isalpha())
print(x.isdecimal())
print(x.isdigit())
print("")

if x.isdigit():
    print(True)
else: 
    print(False)

if x.isdecimal():
    print(True)
else: 
    print(False)

if x.isalnum():
    print(True)
else:
    print(False)

me = "cdrive\tinput\tpass\tclient\tmegha"
print(me.encode(encoding="ascii",errors="backslashreplace"))
print(me.encode(encoding="ascii",errors="ignore"))
print(me.encode(encoding="ascii",errors="namereplace"))

print(me.expandtabs(2))

ex = "The price is: {price:.2f}".format(price=25)
print(ex)
value = 500
pr = f"The price is {value:.2f}"
print(pr)

dic = {"name": "imran", "age":23}
txt = "Hello dear {name} your are now {age} years old!"
print(txt.format_map(dic))

des = "fdfkdfjsdfksdf"
if des.islower():
    print(True)
else:
    print(False)

ss = "322323"
if ss.isnumeric():
    print(True)
else:
    print(False)

dd = "2j3k4h5k6"
if dd.isalnum():
    print(True)
else:
    print(False)

class Car:
    brand = "Mercedez"
    model = 2025
    def __init__(self, color, custom):
        self.color = color
        self.custom = custom
    def show(self):
        print(f"The color is: {self.color}, and the custom is: {self.custom}")

car1 = Car("red", 122)
car1.show()
print(car1.brand)
print(car1.model)
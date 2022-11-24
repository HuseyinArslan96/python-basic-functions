global scope
x = "global x"
def function():
    #local scope
    x = "local x"
    print(x)
function()
print(x)

name = "Çınar"
def changeName(new_name):
    name = new_name
    print(name)
changeName("Ada")
print(name)

name = "global string"
def greeting():
    # name = "Ada"
    def hello():
        # name = "Çınar"
        print("Hello " + name)
    hello()
greeting()

x = 50
def test(x):
    print(f"x: {x}")
    x = 100
    print(f"x changed to {x}")
test(x)
print(x)

'''Global scope'u fonksiyon aracılığıyla güncelleme'''
x = 50
def test():
    global x
    print(f"x: {x}")
    x = 100
    print(f"x changed to {x}")
test()
print(x)

name = "Hasan"
def changeName():
    global name
    print(f"name: {name}")
    name = "Hüseyin"
    print(f"name changed to {name}")
changeName()
print(name)

name = "Hasan"
def changeName(new_name):
    global name
    print(f"name: {name}")
    name = new_name
    print(f"name changed to {name}")
changeName("Hüseyin")
print(name)
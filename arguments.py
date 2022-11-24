def changeName(n):
    n = "Hasan"
name = "Hüseyin"
changeName(name)
print(name)

def change(n):
    n[0] = "İstanbul"
sehirler = ["Ankara", "İzmir"]
n = sehirler[:] # slicing
n[1] = "İzmit"
change(sehirler[:])
change(n)
print(sehirler)
print(n)

def add(a, b, c = 0):  # "c = 0" koduyla c elemanını girsek de girmesek de fonksiyon çalışır.
    return sum((a, b, c))
print(add(10, 20))

def add(*params): # "(*params)" koduyla fonksiyona istediğimiz kadar parametre ekleyebiliriz. Tuple listesi için tek yıldız koyulur.
    print(params) # params içindeki elemanları listeler.  
    print(params[2]) # params içindeki elemanların üçüncüsünü listeler.
    return sum((params))

def add(*params):
    print(params)
    sum = 0
    for n in params:
        sum = sum + n    
    return sum
print(add(25, 35, 45))
print(add(10, 20, 40, 70, 100))

def displayUser(**args): # Dictionary tipinde liste için çift yıldız koyulur.
    for key, value in args.items():
        print("{} is {}".format(key, value))
displayUser(name = "Yaren", age = 16, city = "Ankara")
displayUser(name = "Hasan", age = 18, city = "Antalya", phone = 12345)
displayUser(name = "Hüseyin", age = 25, city = "Amasya", phone = 12345, mail = "abc@gmail.com")

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(10, 20, 30, 40, 50, key1 = "value1", key2 = "value2")
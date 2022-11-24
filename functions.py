def sayHello(name = "user"):
    return "Hello " + name
msg = sayHello("Hüseyin")
print(msg)

def total (num1, num2):
    return num1 + num2
result = total(10, 20)
print(result)

def yasHesapla(dogumYili):
    return 2021 - dogumYili
ageHasan = yasHesapla(2003)
ageYaren = yasHesapla(2005)
ageHüseyin = yasHesapla(1996)
print(f"Hasan'ın yaşı: {ageHasan}, Yaren'in yaşı: {ageYaren}, Hüseyin'in yaşı: {ageHüseyin}")

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yilina gore emeklilige kac yil kaldigini hesaplayan fonksiyon
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f"{isim}, emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emekli oldunuz.")
EmekliligeKacYilKaldi(1996, "Hüseyin")
EmekliligeKacYilKaldi(1971, "Bünyamin")
print(help(EmekliligeKacYilKaldi))
list = [1, 2, 3]
print(help(list.append))


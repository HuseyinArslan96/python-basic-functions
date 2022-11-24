def square(num):
    return num ** 2
numbers = [1, 3, 5, 9]
result = list(map(square, numbers))
print(result)
for item in map(square, numbers):
    print(item)
'''Listelenen sayı ya da sayıların karesini bulmak için alternatif kod'''
numbers = [1, 3, 5, 9]
result = list(map(lambda num: num ** 2, numbers)) # lambda fonksiyonuyla yalnızca tek bir satırda kullanılacak fonksiyon yazılabilir.
print(result)
'''Listelenen sayı ya da sayıların karesini bulmak için alternatif kod'''
square = lambda num: num ** 2
numbers = [1, 3, 5, 9]
result = list(map(square, numbers))
print(result)
'''Fonksiyonu düz çalıştırma'''
square = lambda num: num ** 2
print(square(3))
'''Liste içindeki çift sayıları bulma'''
numbers = [1, 3, 5, 9, 10, 24]
def checkEven(num): return num % 2 == 0
result = list(filter(checkEven, numbers))
result = list(filter(lambda num: num % 2 == 0, numbers))
print(result)
checkEven = lambda num: num % 2 == 0
result = checkEven(numbers[2]) # Numbers listesindeki üçüncü elemanın çift sayı olup olmadığını kontrol etme
print(result)
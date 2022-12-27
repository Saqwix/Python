#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
#in
#88
#out
#1011000

def ConvertToBinary (number):
    list = []
    while number != 1:
        list.insert(0, number % 2)
        number //=  2
    if number <= 1: list.insert(0, number)
    print(*list)

x = int(input('введите число: '))

ConvertToBinary(x)
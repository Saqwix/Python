# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = input ('Введите число: ')
sum = 0
for x in number:
    if x.isdigit():
        sum += int(x)

print(f"Cyмма {number} равна: ", sum)

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input("Введите день недели (от 1 до 7): "))

if number < 1 or number > 7:
    print('Такого дня недели не существует')
elif number > 5:
    print('Выходной день!')
else:
    print('Рабочий день(((')
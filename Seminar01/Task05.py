# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример: 
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

x1 = int(input('Введите координату х1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату х2: '))
y2 = int(input('Введите координату y2: '))
# Функция sqrt () — квадратный корень числа
import math
sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
print(f'Расстояние: (A - ({x1}, {y1}) между B - ({x2}, {y2}) = {sqrt}')
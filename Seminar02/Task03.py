# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = int(input('Введите число: ')) 
def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
print(sequence(n))
print(round(sum(sequence(n))))
# 1.Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#in
#5
#out
#[10, 2, 3, 8, 9]
#22

from random import sample

def list_random_numbers(count: int) -> list:
    if count < 0:
        print("Negative value of the number of numbers")
        return []

    list_nums = sample(range(1, count *2), count)
    return list_nums

def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums

all_list = list_random_numbers(int(input("Number of numbers: ")))
print(all_list)
print(sum_odd_pos(all_list))

#x = [2, 3, 6, 10, 12, 16, 5]
#print(x)
#summ = 0
#for i in range(1, len(x), 2):
    #if i % 2 == 1:
#        summ += x[i]       
#print(f"{x} -> сумма элементов на нечётных позициях: {summ}")



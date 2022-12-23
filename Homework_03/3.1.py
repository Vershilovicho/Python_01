# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
from random import sample

def sum_of_odd (amount):
    new_list = sample(range(2, (amount+1)*2), k=amount)
    print(new_list)
    l_list = len(new_list)
    sumel = 0
    for i in range(0, l_list, 2):
        sumel += new_list[i]
    return sumel

sum_el = sum_of_odd(int(input('Введите количество элементов списка: ')))
print(sum_el)
# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def product_of_pairs (amount):
    list = sample(range(1, (amount+1)*2), k=amount)
    print(list)            
    n = len(list)//2
    res_list = []
    for i in range(n):
        m = list[i]*list[len(list)-i-1]
        res_list.append(m)        
    if len(list)%2 != 0:
        res_list.append(n)
    return res_list

list1 = product_of_pairs(int(input('Введите количество элементов списка: ')))
print(list1)
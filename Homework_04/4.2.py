# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]


num = int(input("Enter number N: "))


def multipliers(n):
    p=2
    my_list = []
    while p <= n:
        if n % p == 0:
            my_list.append(p)
            n //= p
            # p = 2
        else:
            p += 1
    return my_list

my_list1 = multipliers(num)
print(my_list1)
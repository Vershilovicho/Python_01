# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# 1, -3, 9, -27, 81
# -3 в степени i

# for i in range(5): еще вариант

# print((-3) ** i, end=" ")
# n = int(input())


n = int(input())
seq_n = 1

for i in range(n):
    print(seq_n, end=' ')
    seq_n*=-3

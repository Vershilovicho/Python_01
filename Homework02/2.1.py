# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

n = float(input("Введите вещественное число: "))

while n != int(n):
    n *= 10
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(int(sum))


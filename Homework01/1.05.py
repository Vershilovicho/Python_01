# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

xa = int(input("Введите координату X точки А: "))
ya = int(input("Введите координату Y точки А: "))
xb = int(input("Введите координату X точки B: "))
yb = int(input("Введите координату Y точки B: "))
distance = ((xb-xa)**2 + (yb-ya)**2)**0.5
print(round(distance, 3))
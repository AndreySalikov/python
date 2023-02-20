# Напишите программу, которая принимает на вход 
# координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

x1 = float(input('Input X 1: '))
y1 = float(input('Input Y 1: '))
x2 = float(input('Input X 2: '))
y2 = float(input('Input Y 2: '))

print(int(((x1-x2)**2 +(y1-y2)**2)**0.5))
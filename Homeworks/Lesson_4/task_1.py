# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите кол-во элементов первого множества: ")) 
m = int(input("Введите кол-во элементов второго множества: ")) 

a = set([int(input()) for i in range(n)]) 
b = set([int(input()) for i in range(m)]) 

c = list(a&b) # пересечение двух множеств 
c.sort() # сортировка элементов в порядке возрастания 

print(*c) # вывод элементов пересечения без повторений


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

import random

n = int(input("Введите общее количество кустов -> "))
a = list()
for i in range(n):
# Допустим, урожайность куста от 10 до 20 ягод:
    a.append(random.randint(10, 20))
print("Количество ягод на каждом кусту -> ", a)
# Т.к. кусты замкнуты по кругу, необходимо учесть первые два куста при подсчете урожая с двумя послденими
a.extend((a[0],a[1]))
max = 0
for i in range(1, n+1): # У нас стало n+2 элементов в списке
    if (a[i]+a[i-1]+a[i+1]) > max:
        max = a[i]+a[i-1]+a[i+1]
print("Максимальное количество ягод, котое может собрать модуль за один заход -> ", max)
# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)

# N = int(input("Введите N - количество элементов в первом массиве: "))
# array1 = [int(i) for i in input("Введите элементы массива через пробел: ").split()]
# M = int(input("Введите M - количество элементов во втором массиве: "))
# array2 = [int(i) for i in input("Введите элементы массива через пробел: ").split()]

# for i in array1:
#     if i not in array2: 
#         print(i)

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5
# 1 2 3 4 5 
# Ввод:
# 5
# 1 5 1 5 1
# Вывод: 
# 0
# Вывод:
# 2
# (каждое число вводится с новой строки)

# num_elements = int(input("Введите количество элементов массива: "))
# array = [int(i) for i in input("Введите элементы массива через пробел: ").split()]
# print(array)
# count = 0
# for i in range(1, num_elements - 1):
#     if array[i] > array[i - 1] and array[i] > array[i + 1]:  
#         count += 1
 
# print("Количество элементов, у которых два соседних и, при этом, оба они соседних элемента меньше этого элемента: ", count)

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 

# Вывод:
# 2

# array_1 = [int(i) for i in input("Введите элементы массива через пробел: ").split()]
# count_1 = 0
# for i in range(0, len(array_1)): 
#     for j in range(i + 1, len(array_1)): 
#         if array_1[i] == array_1[j]: 
#             count_1 += 1 
# print('Количество пар равных элементов:', count_1)

# Вариант 2

# import random

# n = int(input('Enter count elements array: '))
# list_n = [random.randint(-100,100) for x in range(n)]
# print(list_n)

# counter = 0

# while (n>0):
#     for k in range(1, len(list_n)):
#         if list_n[0] == list_n[k]:
#             counter+=1
#             list_n.pop(k)
#             n-=1
#             break
#     n -= 1
#     list_n.pop(0)

# print(counter)

# Вариант 3

# def _res(arr: list) -> int:
#     counter = 0 
#     for item in arr:
#         counter += (arr.count(item)//2)
#     return counter //2 

# def random_list(N: int, min=-100, max=100) -> int:
#     import random
#     arr =[]
#     for i in range(N):
#         arr.append(random.randint(min, max))
#     return arr

# if __name__ == "__main__":
#     count = int(input("Введите длинну списка: "))
#     arr = random_list(count, 0, 10)
#     print(arr)
#     print(_res(arr))

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10 в5
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 
# 300
# Вывод:
# 220 284

# maxVal = 300
# for i in range(1, maxVal+1):
#   sum1 = 0 # Init sum of divisors
#   sum2 = 0 # Init sum of divisors
 
#   # Get divisors of number i
#   for j in range(1,i):
#     if(i % j == 0):
#       sum1 += j
  
#   for j in range(1,maxVal+1):
#     if(j % i == 0):
#       sum2 += j
  
#   # Check pair friens
#   if((sum1 == j) & (sum2 == i)):
#     print(i, j)

# Вариант 2
# N = int(input("Enter number N:"))
# listN = [x + 1 for x in range(N)]
# # print(listN)

# def calc_sum(N):
#     cnt = 0
#     for i in range(1, N):
#         if N % i == 0:
#             cnt+=1
#     return cnt

# for i in range(N):
#     if calc_sum(i) in listN and calc_sum(i) < i:
#         print(i, end= " ")
#         print(calc_sum(i))

# Вариант 3
# """
# Функция для подсчета суммы делителей числа n
# """
# def sum_of_divisors(n):
#     divisors_sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             divisors_sum += i
#     return divisors_sum

# k = int(input())

# for n in range(1, k):
#     m = sum_of_divisors(n)
#     if n < m <= k and sum_of_divisors(m) == n:
#         print(n, m)

# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе 
# одномерный список из значений элементов списка d. 
# Функция должна возвращать новый созданный одномерный список.

def get_line_list(d,a=[]):
    res = []
    for i in d:
        if type(i) == list:
            res += get_line_list(i,res)
        else:
            res.append(i)
    return res


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
print(get_line_list(d))

a = ['car', 'top', 'lot']
a.append('row')
print(a)
# ['car', 'top', 'lot', 'row']
b = ['moon', 'sun']
a.append(b)
print(a)
# ['car', 'top', 'lot', 'row', ['moon', 'sun']]
b = ['dog', 'cat']
a.extend(b)

print(a)
# ['car', 'top', 'lot', 'dog', 'cat']

c = ('like', 'mode')
a.extend(c)

print(a)
# ['car', 'top', 'lot', 'dog', 'cat', 'like', 'mode']

d = 'man'
a.extend(d)
print(a)
# ['car', 'top', 'lot', 'dog', 'cat', 'like', 'mode', 'm', 'a', 'n']

a = [2, 3]
b = [1, 4]
a += b

print(a)
# [2, 3, 1, 4]

a = [2, 3]
b = [1, 4]
a[len(a):] = b

print(a)
# [2, 3, 1, 4]

a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]
print(a.__sizeof__())
# 36
print(b.__sizeof__())
# 44

a = tuple('hello, world!')
print(a)
# ('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')
a = list('список')
print(a)
# ['с', 'п', 'и', 'с', 'о', 'к']

s = []  # Пустой список
l = ['s', 'p', ['isok'], 2]
print(s)
print(l)
# ['s', 'p', ['isok'], 2]

# генераторы списков
c = [c * 3 for c in 'list']
print(c)
b = [b*5 for b in 'Python']
print(b)
c = [c * 3 for c in 'list' if c != 'i']
print(c)
c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
print(c)
c.insert(5, 'Andrey')
print(c)
print(c.count('lm'))
c.reverse()
print(c)
c.clear()
print(c)
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
# [66.25, 333, -1, 333, 1, 1234.5, 333]
print(a.index(333))
# 1
a.remove(333)
print(a)
# [66.25, -1, 333, 1, 1234.5, 333]
a.reverse()
print(a)
# [333, 1234.5, 1, 333, -1, 66.25]
a.sort()
print(a)
# [-1, 1, 66.25, 333, 333, 1234.5]




c = '''это очень большая
... строка, многострочный
... блок текста'''
print(c)
c = 'это очень большая\nстрока, многострочный\nблок текста'
print(c)
# это очень большая
# строка, многострочный
# блок текста
S = r'\n\n\\'[:-1]
S = r'\n\n' + '\\'
S = '\\n\\n'
print(S)

# while for
i = 5
while i < 25:
    print(i)
    i = i + 2

for i in 'hello world':
    print(i * 2, end='')

print()
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')

print()
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')

print()
for i in 'hello world':
    if i == 'a':
        break
else:
    print('Буквы а в строке нет')


# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


# coins = [1, 0, 1, 1, 0]

# count = 0
# for i in range(len(coins)):
#     if coins[i] == 0:
#         coins[i] = 1
#         count += 1

# print(count)

n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

# s = int(input('Введите сумму: '))
# p = int(input('Введите произведение: '))

# # Используем дискриминант для вычисления x и y - значений
# d = (s ** 2) - (4 * p)

# # Проверяем, существуют ли корни уравнения
# if d < 0:
#     print('Нет решений.')
# elif d == 0:
#     x = (4 + (d / 2)) / 2
#     y = s - x
#     print(f'Одно решение: x = {int(x)}, y= {int(y)}.')
# else:
#     x1 = (s + (d ** 0.5)) / 2 #извлекаем квадратный корень и делим на 2
#     x2 = (s - (d ** 0.5)) / 2
#     y1 = s - x1
#     y2 = s - x2
#     print((f'Два решения: x1 = {int(x1)}, y1 = {int(y1)}, x2 = {int(x2)}, y2 = {int(y2)}.'))


# : Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1

# # Задаем значение N
# N = 10

# # Инициализируем переменную k
# k = 0

# # Используем цикл, пока k не будет больше, чем N
# while 2 ** k <= N:
#     print(2 ** k, end = " ")   # Выводим значение 2 в степени k
#     k = k + 1     # Увеличиваем k на 1

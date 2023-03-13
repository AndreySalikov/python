# 1.Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.


# пример - 8 11 0 -23 140 1 => 11 -23

numbers = [8, 11, 0, -23, 140]

number_new = list(filter(lambda x: 0.09 < x/100 <
                  1 or -0.09 > x/100 > -1, numbers))
number_new_1 = list(filter(lambda x: 9 < x < 100 or -9 > x > -100, numbers))

print(number_new)
print(number_new_1)
print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))


# Вводится натуральное число N.
# С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы.
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
# Результат вывести в виде таблицы чисел как показано в примере ниже.


# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

def get_matrix(n):
    return[[int(i==j) for i in range(n)] for j in range(n)]

if __name__ == "__main__":
    print(*get_matrix(4), sep='\n')


N = int(input())
lst = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for r in lst:

    print(*r)

# 3. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор

# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]



# и потом вернуть в исходное состояние

# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

if __name__ == "__main__":
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    ids = [4, 5, 9, 14, 7]
    salary = [111, 222, 333]
    print(list(zip(users, ids, salary)))
    print(list(zip(*zip(users, ids, salary))))

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a,b,c = map(list,zip(users, ids, salary))
print(a,b,c, sep="\n")
a,b,c= map(list,zip(a,b,c))

print(a,b,c, sep="\n")


# Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:

# (символ, порядковый индекс)

# Первый индекс имеет значение 0. 
# Строка может быть короче 10 символов, а может быть и длиннее. 
# То есть, число пар может быть 10 и менее. 
# Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.


# Sample Input:
# Python дай мне силы пройти этот курс до конца!
# Sample Output:
# True

def _res(text):
    return list(zip(text, range(0, 11)))

if __name__ == "__main__":
    lst = _res("afgga dafd")
    print(lst)
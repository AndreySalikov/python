# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

print(max(int(input()), int(input()), int(input()), int(input()), int(input())))

a = int(input())
max = a
for i in range(4):
    a = int(input())
    if a > max:
        max = a
print(max)


a = [2, 3, 4, 5]
print(len(a))
for i in range(0, len(a)):
    print(i, a[i])
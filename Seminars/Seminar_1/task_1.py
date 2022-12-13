# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
if a * a == b: #or b * b == a:
    print('Yes')
elif b * b == a:
    print('Yes')
else:
    print('No')
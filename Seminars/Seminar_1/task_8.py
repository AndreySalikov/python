# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 0,34 -> 3

num = float(input())
print(f'{int(num*10) % 10}')
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# number = int(input("Enter a three-digit number:")) 

# digit1 = number % 10
# digit2 = (number // 10) % 10
# digit3 = number // 100

# sum = digit1 + digit2 + digit3

# print("The sum of the digits is:", int(sum))

# решение 2 

# n = input("Введите трехзначное число: ")
# n = int(n)

# a = n % 10
# b = n % 100 // 10
# c = n // 100

# print("Сумма цифр числа:", a + b + c)

# решение 3

# a = int(input())
# x = (a//100)+(a%10)+((a//10)%10)
# print(x)

# решение 4

a = str (input('Enter number: '))
summa = int(a[0]) + int(a[1]) + int(a[2])
print(summa)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# s = int(input("Input count: "))

# katya = s // 3 * 2
# sergey_and_petya = (s - katya) // 2


# print("Petya made", sergey_and_petya, "paper cranes")
# print("Katya made", katya, "paper cranes")
# print("Sergey made", sergey_and_petya, "paper cranes")

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# num = input("Enter the number of the ticket to check: ")

# if len(num) == 6 and int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
#     print("Yes, this is a lucky ticket")
# else:
#     print("No, this is not a lucky ticket")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# Пример кода:

# n = int(input("Enter length of the chocolate bar: "))
# m = int(input("Enter width of the chocolate bar: "))
# k = int(input("Enter the number of pieces you want to get: "))

# if ((n * m) % k != 0):
#     print("Yes, it is possible to get", k, "pieces")
# else:
#     print("No, it is not possible to get", k, "pieces")


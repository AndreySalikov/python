

value = None
print(type(value))
a = 123
b = 1.23
print(a)
print(b)
value = 12334
print(value)
print(type(a))
print(type(b))
print(type(value))
s = '"Hello \n \'world'
print(s)
print(a, b, s)
print(a, '-',b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1','2','3']
# col = ['hello', 1, 2, 3.14, True]
# print(list)
# print(col)

# print() – отвечает за вывод данных
# input() – отвечает за ввод данных

print('Enter a')
a = int(input())
print('Enter b')
b = float(input())
print(a,' + ', b, ' = ', a + b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))5
# c = a + b
# print('{} + {} = {}'.format(a, b, c))



# Сокращённые операции и операции присваивания
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# range(*(1,5,2))

# Логические операции

# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 > 2
# b = 1 == 2
# c = 1 != 2
# print( a, b, c)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2

# print(func<T>(x))

# f = 1 > 2 or 4 < 6 # Дизъюнкция двух высказываний называется высказывание тогда и только тогда, когда олдно из высказованийистино
# print (f)

# f = [1, 2, 3, 4]
# is_odd = not f[0] % 2
# print(is_odd)







# Управляющая конструкция 
# for

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)



# Знакомьтесь – range
r = range(5) # range(0, 5)
r = range(2, 5) # range(2, 5)
r = range(-5, 0) # range(-5, 0)
r = range(1, 10, 2) # range(1, 10, 2)
r = range(100, 0, -20) # range(100, 0, -20)

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
 print(i)
# 100 80 60 40 20
for i in range(5):
 print(i)
# 0 1 2 3 4

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

r = range(10)
for i in r:
    print(i)

for i in range(10):
    print(i)

for i in range(5,15,5):
    print(i)

for i in 'qwe - rty':
    print(i)    


# Немного о строках

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)


text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[6:22]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
print(text)

# Списки: введение

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

print(sum_numbers(5))

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', '1'))
print(sum_str('q', 'e', '1', '5', 'w'))
# print(sum_str(1, 8, 9))

def max1(a, b):
    if a > b:
        return a
    return b


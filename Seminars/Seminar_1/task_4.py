# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

n = float(input('Enter n:'))
print(int(n*10 % 10))

print('\n')

b = input('Enter B: ')
a = b.split(".")
print(a[1][0])

print('\n')


def t4(float_t4):
    if round(float_t4, 0) == float_t4:
        return 0
    return int(float_t4*10) % 10


10


def main():

    print(t4.__name__)
    print(t4(0))
    print(t4(0.0002))
    print(t4(9.75))


main()

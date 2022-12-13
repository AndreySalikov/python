# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
N = int(input('Enter N: '))
for i in range(-N,N+1):
    print(i, end= " ")
print('\n')


def t3(int_i:int) -> list:
    output = []
    int_m = -int_i
    while int_m <= int_i:
        output.append(int_m)
        int_m += 1
    print(output)
    return output


def main():

    t3(int(input("Enter number: ")))


main()

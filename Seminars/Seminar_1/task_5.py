# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.



nums = int(input('Enter N: '))
if (nums%5==0 and nums%10==0 or nums%15==0) and nums%30 !=0:
    print('Yes')
else:
    print('No')


print('\n')

def t5(int_asked: int, base0=5, base1=10, base2=15, base3=30) -> bool:
    return True if (int_asked % base0 == False and\
                    (int_asked % base1 != False or int_asked % base2 != False) and\
                    int_asked % base3 > 0) else False



def main():

    print(t5.__name__)
    print(t5(20))
    print(t5(30))
    print(t5(60))

main()

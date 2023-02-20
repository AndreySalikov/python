def Fibonacci(n: int) ->int:
    f1 = 0
    f2 = 1
    fib = 0
    for i in range(n-1):
        fib = f1 + f2
        f1, f2 = f2, fib #Python позволяет менять местами несколько элементов
    return fib    
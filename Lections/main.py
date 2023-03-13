# def calkk1(a):
#     return a + a

# def calkk2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# calkk3 = lambda a: a + a
# math(calkk2, 5)
# math(calkk3, 5)


# data= [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

def select(f, col):  # функция map
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)

list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

data = '5 26 48 2 57 9 33 489 55'
print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)

data_1 = [5, 26, 48, 2, 57, 9, 33, 489, 55]
res_1 = list(filter(lambda x: x % 10 == 5, data_1))
print(res_1)

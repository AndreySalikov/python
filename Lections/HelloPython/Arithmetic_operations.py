# Арифметические операции
# +, -, * , /, %, //,**
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

a = 8.123
b = 3 
c = round(a + b, 5)
print(c)
print(a ** b)
print(a % b)
print(round(a // b))
exp1 = 2**3 - 10 % 5 + 2*3
exp2 = 2**3 - 10 / 5 + 2*3
print(exp1) # 14.0 или 14
print(exp2) # 12.0 или 12
exp1 = 2**3 - 10 % 5 + 2*3
exp2 = (2**3) - (10 / 5) + (2*3)
print(exp1) # 14.0 или 14
print(exp2) # 12.0 или 12
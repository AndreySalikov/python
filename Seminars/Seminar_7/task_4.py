# Написать функцию, которая принимает список строк и возвращает список строк, 
# содержащих только одно слово, с использованием лямбда-функции:

strings = ["Hello, world!", "This is a sentence.", "Another sentence", "world"]

strings_1 = list(filter(lambda x:len(x.split()) == 1, strings))
print(strings_1)

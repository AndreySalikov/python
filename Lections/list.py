Метод	    Что делает
list.append(x)	Добавляет элемент в конец списка
list.extend(L)	Расширяет список list, добавляя в конец все элементы списка L
list.insert(i, x)	Вставляет на i-ый элемент значение x
list.remove(x)	Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
list.pop([i])	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
list.index(x, [start [, end]])	Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
list.count(x)	Возвращает количество элементов со значением x
list.sort([key=функция])	Сортирует список на основе функции
list.reverse()	Разворачивает список
list.copy()	Поверхностная копия списка
list.clear()	Очищает список

Модуль array. Массивы в python
Код типа	Тип в C	            Тип в python	Минимальный размер в байтах
'b'	        signed char	        int	                        1
'B'	        unsigned char	    int	                        1
'h'	        signed short	    int	                        2
'H'	        unsigned short	    int	                        2
'i'	        signed int	        int	                        2
'I'	        unsigned int	    int	                        2
'l'	        signed long	        int	                        4
'L'	        unsigned long	    int	                        4
'q'	        signed long long	int	                        8
'Q'	        unsigned long long	int	                        8
'f'	        float	            float	                    4
'd'	        double	            float	                    8


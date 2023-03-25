# Задача №49. Решение в группах Создать телефонный справочник с
# возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def show_menu() -> list:
    print("\nМеню:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти обонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу\n")
    choice = int(input('Введите номер пункта меню: '))
    return choice

def print_result(data) -> list:
    print(*data, sep='\n')

def write_csv(filename: str, data) -> str:
    file = open(filename, 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')

def write_txt(filename: str, data) -> str:
    file = open(filename + ".txt", 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')

def get_file_name() -> str:
    name_of_the_file = input(
        'Ввведите название файла который вы хотите сохранить: ')
    return name_of_the_file

def get_search_name() -> str:
    name = input('Ввведите фамилию абонента: ')
    return name

def find_by_name(data, surname) -> str:
    for key in data:
        if key['Фамилия'].upper() == surname.upper():
            return key.values()
    return ('Такого абонента нет')

def get_search_number():
    number = input('Ввведите номер абонента: ')
    return number

def find_by_number(data, number):
    for key in data:
        if key['Телефон'] == number:
            return key.values()
    return ('Такого абонента нет')

def get_new_user():
    surname = input('Введите фамилию абонента: ')
    name = input('Введите имя абонента: ')
    number = input('Введите номер абонента: ')
    description = input('Введите описание: ')
    return dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'],
        [surname, name, number, description]))

def add_user(data, user):
    data.append(dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'],
        [user['Фамилия'], user['Имя'], user['Телефон'], user['Описание']])))
    
def get_delete_user():
    surname = input('Введите фамилию абонента: ')
    return surname

def delete_user(data: list, last_name: str) -> str:
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            del data[i]
            return f"Абонент {last_name} успешно удален"
    return "Такой абонент отсутствует в списке"

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('Seminars\Seminar_8\phonebook.csv')
    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
            break
        elif choice == 2:
            name = get_search_name()
            print(*find_by_name(phone_book, name), end='')
            break
        elif choice == 3:
            number = get_search_number()
            print(*find_by_number(phone_book, number), end='')
            break
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('Seminars\Seminar_8\phonebook.csv', phone_book)
            break
        elif choice == 5:
            user_data = input('Введите фамилию: ')
            delete_user(phone_book, user_data)
            write_csv('Seminars\Seminar_8\phonebook.csv', phone_book)
            break        
        elif choice == 6:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
            choice = show_menu()

work_with_phonebook()
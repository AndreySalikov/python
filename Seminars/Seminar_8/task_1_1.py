def import_data(txt_file): # функция импорта данных из текстового файла
    file = open(txt_file, 'r') # открываем файл
    # читаем файл построчно
    lines = file.readlines()
    data = []
    # парсим файл
    for line in lines:
        line_data = line.split(',')
        data.append(line_data)
    # закрываем файл
    file.close()
    # возвращаем результат
    return data

def export_data(txt_file, data): # функция для экспорта данных в .txt файл
    file = open(txt_file, 'w') # открываем файл для записи
    for row in data:
        # пишем данные в файл через запятую
        line = ','.join(row)
        file.write(line)
    file.close() # закрываем файл

def create_directory(data): # функция для создания телефонного справочника
  directory = {}
  # наполняем справочник
  for row in data:
    name = row[0].strip()
    number = row[1].strip()
    directory[name] = number
  # возвращаем результат
  return directory

def search_directory(directory, query): # функция для поиска в справочнике
    result = {}
    for name, number in directory.items():
        # проверяем содержимое строки поиска в справочнике
        if query.lower() in name.lower():
            # добавляем найденные значения в результат
            result[name] = number
    return result

def print_directory(directory, title): # функция для печати справочника
    # выводим заголовок
    print(title)
    # выводим содержимое справочника
    for name, number in directory.items():
     print(f'{name:>30}:{number}')

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

# главная функция
def main():
    # имя текстового файла
    txt_file = 'data.txt'
    # импорт данных из файла
    data = import_data(txt_file)
    # создание телефонного справочника
    directory = create_directory(data)
    # поиск данных по запросу
    result = search_directory(directory, 'Ivan')
    # печать результатов
    print_directory(result, 'Search results:')
    # экспорт данных в файл
    export_data(txt_file, data)
# запуск программы
if __name__ == "__main__":
    main()
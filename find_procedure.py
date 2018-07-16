# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

# 1. получить адрес директории мигрейшнс
# 2. сделать цикл перебора всех файлов в фигрейшс
# 3. создать список адресов файлов sql
# 4. проходим по спику дресов, каждый файл открываем проверяем, есть ли в нём нужная ситрока
# 5. если да, заносим имя файла в новый список

import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def database_init(dir_name, file_type=".sql"):
    files_total = os.listdir(os.path.join(current_dir, dir_name))
    files_type_total = [x for x in os.listdir(os.path.join(current_dir, dir_name)) if x.endswith(file_type)]
    return files_type_total

def searching_text_in_files(file_list, text):
    result = []
    for file in file_list:
        with open(os.path.join(current_dir, migrations, file)) as f:
            raw = f.read()
            if text.lower() in raw.lower():
                result.append(file)
    pp.pprint(result)
    print("Всего: {}".format(len(result)))
    return(result)

if __name__ == '__main__':
    files = (database_init(migrations, ".sql"))
    search = input("Введите строку поиска\n")
    new_list = searching_text_in_files(files, search)
    while True:
        new_list = searching_text_in_files(new_list, input("Введите строку поиска\n\n"))
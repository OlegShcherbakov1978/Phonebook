from const import FILE_PATH
# from const import FILE_PATH1

import data_worker
import csv
import os


def del_person():
    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        all_names_info = name_data.readlines()

    del_name = input('Введите данные для поиска: ')

    result = [line for line in all_names_info if del_name not in line]

    with open(FILE_PATH, 'w', encoding='utf8') as name_data:
        for line in result:
            name_data.write(line)


def add_person():
    name1 = input('Введите фамилию: ')
    name2 = input('Введите имя: ')
    name3 = input('Введите отчество: ')
    tel = input('Введите номер телефона: ')
    with open(FILE_PATH, 'a', encoding='utf8') as name_data:
        name_data.write(f'\n{name1},{name2},{name3}, {tel}')


def edit_person():

    data_dict = {}

    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        for line in name_data:
            row = line.strip().split(',')
            last_name, first_name, middle_name, phone_number = row
            data_dict[phone_number] = {
                'Фамилия': last_name, 'Имя': first_name, 'Отчество': middle_name}

    search_query = input('Введите данные для поиска и редактирования: ')

    results = {}
    for phone_number, person_info in data_dict.items():
        if search_query.lower() in person_info['Фамилия'].lower() or \
                search_query.lower() in person_info['Имя'].lower() or \
                search_query.lower() in person_info['Отчество'].lower() or \
                search_query.lower() in phone_number:
            results[phone_number] = person_info
    print()

    count = 1
    for key, value in results.items():
        print(f'{count}).')
        print(f'Номер телефона: {key}')
        for inner_key, inner_value in value.items():
            print(inner_key + ': ' + inner_value)
        count += 1
        print()

    option = int(input("Ведите номер записи для редактирования: "))
    items = list(results.items())
    key, value = items[option-1]
    value_for_edit = (key, value)
    phone_number = value_for_edit[0].strip()
    del data_dict[phone_number]

    phone_number = input("Введите номер телефона: ")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")

    new_entry = {'Фамилия': last_name,
                 'Имя': first_name, 'Отчество': middle_name}

    data_dict[phone_number] = new_entry

    with open('phonebook.csv', 'w', encoding='utf8', newline='') as file:

        writer = csv.writer(file, delimiter=',')

        writer.writerow(['Номер телефона ', 'Фамилия ', 'Имя ', 'Отчество '])

        for phone, data in data_dict.items():
            row = [phone] + list(data.values())
            writer.writerow(row)


def csv2txt():
        
    csv_file = 'phonebook.csv'
    txt_file = os.path.join('src', 'data', 'phonebook.txt')

    with open(csv_file, 'r') as f_csv, open(txt_file, 'w') as f_txt:
        csv_reader = csv.reader(f_csv)
        for row in csv_reader:
            f_txt.write(','.join(row) + '\n')

    print(f'Файл {csv_file} успешно сконвертирован в {txt_file}')


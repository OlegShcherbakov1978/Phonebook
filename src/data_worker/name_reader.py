from const import FILE_PATH


def get_names_info():

    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        for line in name_data:
            print(line.strip())


def search_name1():
    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        name_info = input('Введите фамилию для поиска: ')
        for line in name_data:
            if name_info in line:
                print(line.strip())


def search_name2():
    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        name_info = input('Введите имя для поиска: ')
        for line in name_data:
            if name_info in line:
                print(line.strip())


def search_name3():
    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        name_info = input('Введите отчество для поиска: ')
        for line in name_data:
            if name_info in line:
                print(line.strip())


def search_tel():
    with open(FILE_PATH, 'r', encoding='utf8') as name_data:
        tel_info = input('Введите номер телефона для поиска: ')
        for line in name_data:
            if tel_info in line:
                print(line.strip())

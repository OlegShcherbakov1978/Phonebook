import data_worker


def start_menu():
    while True:
        change = int(input('\n1. Показать все контакты'
                           '\n2. Поиск по фамилии'
                           '\n3. Поиск по имени'
                           '\n4. Поиск по отчеству'
                           '\n5. Поиск по номеру телефона'
                           '\n6. Удалить контакт'
                           '\n7. Изменить контакт'
                           '\n8. Добавить контакт'
                           '\n9. Сохранить изменения в txt'
                           '\n10. Сохранить изменения в csv'
                           '\n0. exit'
                           '\n ---> '))
        if change == 1:
            data_worker.get_names_info()
        elif change == 2:
            data_worker.search_name1()
        elif change == 3:
            data_worker.search_name2()
        elif change == 4:
            data_worker.search_name3()
        elif change == 5:
            data_worker.search_tel()
        elif change == 6:
            data_worker.del_person()
        elif change == 7:
            data_worker.edit_person()
        elif change == 8:
            data_worker.add_person()
        elif change == 9:
            data_worker.csv2txt()
        elif change == 10:
            break
        else:
            break

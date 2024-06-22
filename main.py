from db import DB

db = DB()


def view_table():
    answer = 1
    while answer:
        table_name = input("Название таблицы >>> ")
        if table_name == 'groups':
            print(db.view_groups())
        elif table_name == 'student':
            print(db.view_student())
        else:
            print("У нас нет группы с таким названием ")
        answer = int(input("Будете ли вы продолжать? Да ( 1 ),  Нет ( 0 ) >>> "))


def add_to_table():
    answer = 1
    while answer:
        table_name = input('Название таблицы >>> ')
        if table_name == 'groups':
            group_name = input('Название группы >>> ')
            db.add_group(group_name)
        elif table_name == "student":
            name = input("Имя >>> ")
            last_name = input("Фамиля >>> ")
            phone_number = input("Телифон номер >>> ")
            email = input('email >>> ')
            group_id = int(input("group id >>> "))
            db.add_student(name, last_name, phone_number, email, group_id)

        answer = int(input("Будете ли вы продолжать? Да ( 1 ),  Нет ( 0 ) >>> "))


def edit_table():
    answer = 1
    while answer:
        table_name = input('Название таблицы >>> ')
        column_name = input("Имя столбца >>> ")
        new_value = input("Новое значение >>> ")
        id_ = int(input("id >>> "))
        db.edit_tables(table_name, column_name, new_value, id_)
        answer = int(input("Будете ли вы продолжать? Да ( 1 ),  Нет ( 0 ) >>> "))


def delete_table():
    answer = 1
    while answer:
        table_name = input('Название таблицы >>> ')
        id_ = int(input("id >>> "))
        db.delete_tables(table_name, id_)
        answer = int(input("Будете ли вы продолжать? Да ( 1 ),  Нет ( 0 ) >>> "))


def result():
    answer = 1
    while answer:
        x = int(input("Посмотреть таблицу: ( 1 ), Добавлять ( 2 ), Изменять ( 3 ), Удалить ( 4 ), Прекратить ( 0 )"))
        if x == 1:
            view_table()
        elif x == 2:
            add_to_table()
        elif x == 3:
            edit_table()
        elif x == 4:
            delete_table()
        elif x == 0:
            answer = x

    return "Спасибо, что попробовали приложение"


print(result())






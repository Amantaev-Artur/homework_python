import sqlite3

menu_level = 1
connection = None
cursor = None
while True:
    if menu_level == 1:
        answer = int(input('1. Выбор БД\n2. Ред. БД\n3. Выход\n'))
        if answer == 1:
            if connection:
                    connection.close()
            if cursor:
                    cursor.close()
            connection = sqlite3.connect("new_db.sqlite")
            cursor = connection.cursor()
        elif answer == 2:
            menu_level = 2
        else:
            break
    else:
        answer = int(input('1. SELECT\n2. INSERT\n3. DELETE\n4. UPDATE\n0. Выход\n'))
        if answer == 1:
            sel = input('SELECT:')
            fr = input('FROM:')
            where = input('WHERE:')
            if cursor:
                if where=='':
                    cursor.execute("SELECT "+sel+" FROM " + fr + ";")
                else:
                    cursor.execute("SELECT "+sel+" FROM " + fr + " WHERE "+where+";")
                print(cursor.fetchall())
        elif answer == 2:
            table = input('TABLE:')
            id = input('ID:')
            name = input('NAME:')
            if cursor:
                cursor.execute("INSERT INTO "+table+" VALUES (\""+id+"\", \""+name+"\");")
                print(cursor.fetchall())
                connection.commit()
        elif answer == 3:
            table = input('TABLE:')
            condition = input('CONDITION:')
            if cursor:
                cursor.execute("DELETE FROM "+table+" WHERE "+condition+";")
                print(cursor.fetchall())
                connection.commit()
        elif answer == 4:
            table = input('TABLE:')
            set_ = input('SET:')
            condition = input('CONDITION:')
            if cursor:
                cursor.execute("UPDATE "+table+" SET \""+set_+"\" WHERE "+condition+";")
                print(cursor.fetchall())
                connection.commit()
        else:
            menu_level = 1
import sqlite3


async def register(user_id):
    '''Регистрация пользователя'''
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()

    sql_query = 'SELECT * FROM users WHERE id = ?'
    adr_query = (str(user_id),)
    cursor.execute(sql_query, adr_query)

    my_result = cursor.fetchall()

    if my_result is None or my_result == [] or my_result == ():
        cursor = connect.cursor()
        sql_query = "INSERT INTO users (id, famos_lang, choose_lang) VALUES (?, ?, ?)"
        val_query = (str(user_id), 'ru, en, nl, it', 'en')
        cursor.execute(sql_query, val_query)
        connect.commit()
        cursor.close()
        connect.close()
        return True
    else:
        cursor.close()
        connect.close()
        return False



async def show_lang(user_id):
    '''Отправка данных о избранный языках пользователя'''
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    sql_query = 'SELECT famos_lang FROM users WHERE id = ?'
    adr = (str(user_id),)
    cursor.execute(sql_query, adr)
    data = cursor.fetchall()
    return data


async def show_choose(user_id):
    '''Отправка данных о выбранном языке'''
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    sql_query = 'SELECT choose_lang FROM users WHERE id = ?'
    adr = (str(user_id), )
    cursor.execute(sql_query, adr)
    data = cursor.fetchall()
    return data


async def switch_choose(user_id, new_choose):
    '''Сменя основного языка'''
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    sql_query = 'UPDATE users SET choose_lang = ? WHERE id = ?'
    sql_value = (new_choose, str(user_id))
    cursor.execute(sql_query, sql_value)
    connect.commit()
    # return new_choose


async def change_famous(user_id, new_lang, old_lang):
    '''Поменять избранное'''
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    sql_query = 'SELECT famos_lang FROM users WHERE id = ?'
    sql_value = (str(user_id), )
    cursor.execute(sql_query, sql_value)
    data_famous: list = cursor.fetchall()[0][0].split(', ')
    data_famous[data_famous.index(old_lang)] = new_lang
    text = ', '.join(data_famous)
    # for i_lang in data_famous:
    #     text += str(i_lang) + ', '
    sql_query = 'UPDATE users SET famos_lang = ? WHERE id = ?'
    sql_val = (text, user_id)
    cursor.execute(sql_query, sql_val)
    connect.commit()

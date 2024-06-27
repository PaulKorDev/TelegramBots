import sqlite3 as sq
from json import loads, dumps

def sql_start():
    global base, cur
    base = sq.connect('anonimBot.db')
    cur = base.cursor()
    if base:
        print("Data base connected")
    base.execute('CREATE TABLE IF NOT EXISTS anonimBot (userID TEXT PRIMARY KEY, name TEXT, description TEXT, unread_messages INT, notification BOOLEAN, friends TEXT, interlocutor INTEGER, messages_of_users TEXT)')
    base.commit()

async def sql_check_user (id_user):
    return cur.execute('SELECT * FROM anonimBot WHERE userID=?', (id_user, )).fetchone()

async def sql_return_friends (id_user):
    returned_friend_list = cur.execute('SELECT friends FROM anonimBot WHERE userID == ?', (id_user, )).fetchone()[0]
    if (returned_friend_list is not None) and (',' in returned_friend_list):
        return returned_friend_list.split(',')
    else:
        return returned_friend_list
    

async def sql_check_friend (id_of_friend, id_user):
    return cur.execute(f'SELECT friends FROM anonimBot WHERE friends like \'%{id_of_friend}%\' and userID = ?', (id_user,)).fetchone()

async def sql_add_userID (id_user):
    cur.execute('INSERT OR IGNORE INTO anonimBot (userID, unread_messages, notification, description, interlocutor) VALUES (?, ?, ?, ?, ?)', (id_user, 0, True, "Неизветно", 0))
    base.commit()

async def sql_nickname (name, id_user):
    cur.execute('UPDATE anonimBot SET name = ? WHERE userID = ?', (name, id_user))
    base.commit()

async def sql_description (description, id_user):
    cur.execute('UPDATE anonimBot SET description = ? WHERE userID = ?', (description, id_user))
    base.commit()

async def sql_increment_unread_messages (id_user):
    cur.execute('UPDATE anonimBot SET unread_messages = (unread_messages + 1) WHERE userID = ?', (id_user,))
    base.commit()

async def sql_decrease_unread_messages (id_user):
    cur.execute('UPDATE anonimBot SET unread_messages = (unread_messages - 1) WHERE userID = ?', (id_user,))
    base.commit()

async def sql_notification (bool, id_user):
    cur.execute('UPDATE anonimBot SET notification = ? WHERE userID = ?', (bool, id_user))
    base.commit()

async def sql_interlocutor (interlocutor, id_user):
    cur.execute('UPDATE anonimBot SET interlocutor = ? WHERE userID = ?', (interlocutor, id_user))
    base.commit()

async def sql_friends (interlocutor, id_user):
    if await sql_return_friends(id_user):
        cur.execute('UPDATE anonimBot SET friends = friends || \',\' || ? WHERE userID = ?', (interlocutor, id_user))
    else:
        cur.execute('UPDATE anonimBot SET friends = ? WHERE userID = ?', (interlocutor, id_user))
    base.commit()

async def sql_delete_friends (interlocutor, id_user):
    friends = await sql_return_friends(id_user)
    if type(friends) is str:
        cur.execute('UPDATE anonimBot SET friends = null WHERE userID = ?', (id_user,))
    elif type(friends) is list:
        friends.remove(str(interlocutor))
        friends = ",".join(friends)
        cur.execute('UPDATE anonimBot SET friends = ? WHERE userID = ?', (friends, id_user))
    base.commit()

async def sql_dict_mes (dict_mes, id_user):
    dict_to_str = dumps(dict_mes)
    cur.execute('UPDATE anonimBot SET messages_of_users = ? WHERE userID = ?', (dict_to_str, id_user))
    base.commit()

async def sql_return_interlocutor (id_user):
    return cur.execute('SELECT interlocutor FROM anonimBot WHERE userID == ?', (id_user,)).fetchone()[0]

async def sql_return_name (id_user):
    return cur.execute('SELECT name FROM anonimBot WHERE userID == ?', (id_user,)).fetchone()[0]

async def sql_return_unread_messages (id_user):
    return cur.execute('SELECT unread_messages FROM anonimBot WHERE userID == ?', (id_user,)).fetchone()[0]

async def sql_return_notification (id_user):
    return cur.execute('SELECT notification FROM anonimBot WHERE userID == ?', (id_user,)).fetchone()[0]

async def sql_return_description (id_user):
    return cur.execute('SELECT description FROM anonimBot WHERE userID == ?', (id_user,)).fetchone()[0]

async def sql_return_dict_mes (id_user):
    dict_mes = cur.execute('SELECT messages_of_users FROM anonimBot WHERE userID == ?', (id_user,)).fetchone()[0]
    if dict_mes is not None:
        dict_mes = loads(dict_mes)
    return dict_mes


async def sql_search_person (name_user):
    try:
        return cur.execute('SELECT userID FROM anonimBot WHERE name=?', (name_user,)).fetchone()[0]
    except:
        return None

"""
async def sql_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO anonimBot VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM anonimBot').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_justread():
    return cur.execute('SELECT * FROM anonimBot').fetchall()

async def sql_delete(data):
    cur.execute('DELETE FROM anonimBot WHERE name == ?', (data, ))
    base.commit()
"""
    
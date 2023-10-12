import sqlite3 as sql

def sql_start():
    global base, cur
    base = sql.connect('pattern.db')
    cur = base.cursor()
    if base:
        print("Data base connected")
    base.execute('CREATE TABLE IF NOT EXISTS PatternDB (patternID INT PRIMARY KEY, name TEXT)')
    base.commit()

"""
-    Вставка несколько значений в таблицу в sql
async def sql_insert_values_into_table (id, name):
    cur.execute('INSERT OR IGNORE INTO PatternDB (patternID, name) VALUES (?, ?)', (id, name))
    base.commit()

-    Обновление-установка значения в sql
async def sql_set_value (name, id):
    cur.execute('UPDATE PatternDB SET name = ? WHERE patternID = ?', (name, id))
    base.commit()

-    Возврат значения из sql
async def sql_return_value (id):
    return cur.execute('SELECT column-name FROM PatternDB WHERE patternID == ?', (id,)).fetchone()[0]

-    Конкатенация строк в sql
friends = friends || \',\' || ?

-    Выгрузка значений из стейта в sql
async def sql_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO anonimBot VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

-    Поочередная выгрузка значений из sql
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM anonimBot').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

-    Удаление из базы данных
async def sql_delete(data):
    cur.execute('DELETE FROM anonimBot WHERE name == ?', (data, ))
    base.commit()
"""
    
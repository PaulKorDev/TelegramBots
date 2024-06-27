import sqlite3


def sql_start():
    global base, cur
    base = sqlite3.connect('followers.db')
    cur = base.cursor()
    if base:
        print("Data base connected")
    base.execute('CREATE TABLE IF NOT EXISTS followers (username TEXT PRIMARY KEY, part INTEGER, donat INTEGER, mark TEXT)')
    base.commit()


async def sql_add_username(username):
        cur.execute('INSERT OR IGNORE INTO followers (username) VALUES (?)', (username,))
        base.commit()

async def sql_add_mark(mark, username):#, username):
        cur.execute('UPDATE followers SET mark = ? WHERE username = ?', (mark, username))
        base.commit()

async def sql_add_donat(donat, username):#, username):
        cur.execute('UPDATE followers SET donat = ? WHERE username = ?', (donat, username))#('INSERT INTO followers (donat) VALUES (?)', donat)
        base.commit()

async def sql_add_part(part, username):#, username):
        cur.execute('UPDATE followers SET part = ? WHERE username = ?', (part, username))#INSERT OR REPLACE INTO followers (part) VALUES (?)
        base.commit()

async def sql_return_donat(username):
    return cur.execute('SELECT donat FROM followers WHERE username == ?', (username,)).fetchone()[0]

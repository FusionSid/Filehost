import random
import string
import aiosqlite


async def create_db():
    async with aiosqlite.connect("utils/database/files.db") as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            file_type TEXT,
            file BLOB
            )""")
        await db.commit()


async def get_db():
    async with aiosqlite.connect("utils/database/files.db") as db:
        cur = await db.execute("""SELECT * FROM files""")
        data = await cur.fetchall()
    return data


async def create_code():
    choices = string.ascii_lowercase + string.ascii_uppercase + string.digits

    while True:
        code = "".join(random.sample(choices, 8))

        async with aiosqlite.connect("utils/database/files.db") as db:
            cur = await db.execute(f"""SELECT * FROM files WHERE code='{code}'""")
            data = await cur.fetchall()
        
        if len(data) == 0:
            break
        
    return code


async def insert_file(file_bytes : bytes, file_type : str):

    code = await create_code()

    async with aiosqlite.connect("utils/database/files.db") as db:
        if file_type is None:
            await db.execute(f"""INSERT INTO files (code, file) VALUES (?, ?)""", (code, file_bytes))

        else:
            await db.execute("""INSERT INTO files (code, file_type, file) VALUES (?, ?, ?)""", (code, file_type, file_bytes))
        
        await db.commit()
    return code


async def get_file(code):
    async with aiosqlite.connect("utils/database/files.db") as db:
        cur = await db.execute(f"""SELECT * FROM files WHERE code='{code}'""")
        data = await cur.fetchall()
    try:
        return data[0]
    except IndexError:
        return False
import random
import string
import aiosqlite


async def create_db():
    async with aiosqlite.connect("utils/database/images.db") as db:
        await db.execute("""CREATE TABLE Images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            author TEXT,
            image BLOB
            )""")
        await db.commit()


async def get_db():
    async with aiosqlite.connect("utils/database/images.db") as db:
        cur = await db.execute("""SELECT * FROM Images""")
        data = await cur.fetchall()
    return data


async def create_code():
    choices = string.ascii_lowercase + string.ascii_uppercase + string.digits

    while True:
        code = "".join(random.sample(choices, 8))

        async with aiosqlite.connect("utils/database/images.db") as db:
            cur = await db.execute(f"""SELECT * FROM Images WHERE code='{code}'""")
            data = await cur.fetchall()
        
        if len(data) == 0:
            break
        
    return code


async def insert_image(image_bytes : bytes, author : str = None):

    code = await create_code()

    async with aiosqlite.connect("utils/database/images.db") as db:
        if author is None:
            await db.execute(f"""INSERT INTO Images (code, image) VALUES (?, ?)""", (code, image_bytes))

        else:
            await db.execute("""INSERT INTO Images (code, author, image) VALUES (?, ?, ?)""", (code, author, image_bytes))
        
        await db.commit()
    print(code)
    return code


async def get_image(code):
    async with aiosqlite.connect("utils/database/images.db") as db:
        cur = await db.execute(f"""SELECT * FROM Images WHERE code='{code}'""")
        data = await cur.fetchall()
    try:
        return data[0]
    except IndexError:
        return False
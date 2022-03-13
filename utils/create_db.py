import asyncio
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

loop = asyncio.new_event_loop()
loop.run_until_complete(create_db())
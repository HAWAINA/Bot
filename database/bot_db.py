import sqlite3


def sgl_create():
    global db, cursor
    db = sqlite3.connect("bot.sglite3")
    cursor = db.cursor()
    if db:
        print("database connected successfully")
    db.execute(
        "CREATE TABLE IF NOT EXISTS anime "
        "(photo TEXT, title TEXT PRIMARI KEY,descriptions TEXT)"
    )
    db.commit()


async def sgl_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anime VALUES(?, ?. ?)", tuple(data.values()))
        db.commit()

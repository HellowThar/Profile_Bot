import sqlite3
from sqlite3 import Error
import aiosqlite

def initialize(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS profile (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL UNIQUE,
                                        profile text
                                        );""")
    c.close()

async def create(profile):
    async with aiosqlite.connect("profile.sqlite") as db:
        await db.execute("""INSERT INTO profile(username,profile)
                        VALUES(?,?)""", profile)
        await db.commit()

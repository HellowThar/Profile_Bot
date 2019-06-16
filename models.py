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

async def create(full_profile):
    async with aiosqlite.connect("profile.sqlite") as db:
        await db.execute("""INSERT INTO profile(username,profile)
                        VALUES(?,?)""", full_profile)
        await db.commit()

async def edit(full_profile):
    async with aiosqlite.connect("profile.sqlite") as db:
        await db.execute("""UPDATE profile SET profile=? WHERE username=?""", full_profile)
        await db.commit()

async def delete(user):
    async with aiosqlite.connect("profile.sqlite") as db:
        await db.execute("""DELETE FROM profile WHERE username=?""", profile)
        await db.commit()

async def show(user):
    async with aiosqlite.connect("profile.sqlite") as db:
        async with db.execute("""SELECT * FROM profile WHERE username=?""", user) as cursor:
            async for profile in cursor:
                await profile

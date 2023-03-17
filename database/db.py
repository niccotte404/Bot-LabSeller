import sqlite3

async def connection():
    
    connect = sqlite3.connect("studentorder.db")
    curr = connect.cursor()
    
    curr.execute("""CREATE TABLE IF NOT EXISTS administration(
        user_id TEXT PRIMARY KEY,
        username TEXT,
        status TEXT
        )""")
    
    curr.execute("""CREATE TABLE IF NOT EXISTS orders(
        user_id TEXT PRIMARY KEY,
        username TEXT,
        description TEXT,
        photo_id TEXT
        price INT
        )""")
    
    curr.execute("""CREATE TABLE IF NOT EXISTS executors(
        user_id TEXT PRIMARY KEY,
        username TEXT,
        descriprion TEXT,
        photo_id TEXT,
        price INT
        )""")
    
    connect.commit()
    print("db connection ok")
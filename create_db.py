import sqlite3
from variables import SQLBD

con = sqlite3.connect(SQLBD)
cur = con.cursor()
with open('create_db.sql', 'r') as f:
    text = f.read()
cur.executescript(text)
cur.close()
con.close()

import sqlite3

db = sqlite3.connect('shoes.db')
curs = db.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS users(
    code TEXT,
    name TEXT, 
    photo TEXT, 
    price TEXT, 
    quantity TEXT, 
    Размер TEXT   
)''')

db.commit()



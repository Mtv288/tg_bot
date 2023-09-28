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

curs.execute('SELECT code FROM users')
if curs.fetchone() is None:
    curs.execute(f'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', ('2334', 'gfhfhg', '545gjgj54', 'fg', '3', 'поолп'))
    db.commit()



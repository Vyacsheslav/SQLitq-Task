import sqlite3
connection=sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER))
               ''')
connection.commit()
connection.close()
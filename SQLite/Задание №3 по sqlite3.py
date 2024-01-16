import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('CREATE INDEX idx_email ON Users (email)')
cursor.execute('INSERT INTO User (username, email, age) VALUES (?,?,?)', ('newuser', 'newuser@example.com', 26))

connection.commit()
connection.close()
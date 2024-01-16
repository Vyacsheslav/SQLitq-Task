import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM Users')
first_user = cursor.fetchone()
print(first_user)

cursor.execute('SELECT * FROM Users')
first_five_users = cursor.fetchmany(5)
print(first_five_users)

cursor.execute('SELECT * FROM Users')
all_users = cursor.fetchall()
print(all_users)

connection.close()
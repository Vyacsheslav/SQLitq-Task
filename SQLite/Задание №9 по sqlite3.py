import sqlite3
conncetion=sqlite3.connect('my_database.db')
cursor=conncetion.cursor()
cursor.execute('SELECT username,aga FROM Users ORDER BY age DESC')
results=cursor.fetchall()
for row in results:
    print(row)
conncetion.close()
import sqlite3
conncetion=sqlite3.connect('my_database.db')
cursor=conncetion.cursor()
cursor.execute('SELECT AVG(age) FROM Users')
average_age=cursor.fetchone()[0]
print('Средний возраст пользователей:',average_age)
conncetion.close()
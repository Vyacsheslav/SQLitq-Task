import sqlite3
conncetion = sqlite3.connect('my_database.db')
cursor = conncetion.cursor()
cursor.execute ('DELETE FROM User WHERE username =&',('newuser',))
conncetion.commit()
conncetion.close()
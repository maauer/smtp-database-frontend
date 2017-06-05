import sqlite3


database_name = 'greeleysmtp.db'

database = sqlite3.connect(database_name)

database.close()

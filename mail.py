#http://pythoncentral.io/introduction-to-sqlite-in-python/?ref=EmailThis.me

import sqlite3


database_name = 'greeleysmtp.db'

database = sqlite3.connect(database_name)

cursor = db.cursor()


database.close()

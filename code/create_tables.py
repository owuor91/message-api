import sqlite3

connection = sqlite3.connect('message.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, author text, title text, body text)"
cursor.execute(create_table)

connection.commit()
connection.close()

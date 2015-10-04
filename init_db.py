import sqlite3
conn = sqlite3.connect('Comments.db')

c = conn.cursor()

c.execute("CREATE TABLE Comments (Name, datetime, comment)")

c.execute("INSERT INTO Comments VALUES ('bob', '100', 'Hello world!')")

c.execute("SELECT * FROM Comments")
print(c.fetchall())

conn.commit()
conn.close()

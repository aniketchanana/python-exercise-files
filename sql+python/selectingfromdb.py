import sqlite3

conn = sqlite3.connect("my_friends.db")

c = conn.cursor()

query = "SELECT * from friends where closeness>3 ORDER BY closeness"

c.execute(query)

# for result in c :
#     print(result)

print(c.fetchall())

conn.commit()

conn.close()
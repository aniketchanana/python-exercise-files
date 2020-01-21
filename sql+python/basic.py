import sqlite3

conn = sqlite3.connect("my_friends.db")

# create cursor object
c = conn.cursor()
#execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT,last_name TEXT,closeness INTEGER);")
# insert_query = "INSERT INTO friends VALUES('aniket','chanana',7)"
# c.execute(insert_query)
#commit changes





# bad way
# first = "dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{first}')"
# c.execute(query)


# first = "jatin"
# query = f"INSERT INTO friends (first_name) values (?)"
# c.execute(query,(first,))

data = ("steve","irwin",9)
query = f"INSERT INTO friends VALUES (?,?,?)"
c.execute(query,data)

conn.commit()
conn.close()
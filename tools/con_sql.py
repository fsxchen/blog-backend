import sqlite3


conn = sqlite3.connect("./db.sqlite3")

cur1 = conn.execute("SELECT * FROM poem_poet;") 
cur2 = conn.execute("SELECT * FROM poem_poem;") 

# 同步poet
for row in cur1:
    print(row)
for row in cur2:
    print(row)

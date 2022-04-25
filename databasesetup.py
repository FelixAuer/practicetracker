import sqlite3

con = sqlite3.connect('practicetracker.db')
cur = con.cursor()

cur.execute('''CREATE TABLE practice
               (started text, stopped text, seconds real)''')
con.commit()
con.close()

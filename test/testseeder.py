import datetime
import random
import sqlite3

con = sqlite3.connect('demo.db')
cur = con.cursor()

end = datetime.datetime.now()

for i in range(500):
    playing = random.randint(3*60, 60*60)
    resting = random.randint(10*60, 5*60*60)
    start = end - datetime.timedelta(seconds=playing)
    cur.execute("INSERT INTO practice (started, stopped, seconds) VALUES (?, ?, ?)",
                (start.strftime("%Y-%m-%d %H:%M:%S"),
                 end.strftime("%Y-%m-%d %H:%M:%S"),
                 playing))
    end = start - datetime.timedelta(seconds=resting)

con.commit()
con.close()

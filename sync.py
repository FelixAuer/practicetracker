import sqlite3
import os
import requests

con = sqlite3.connect('practicetracker.db')
cur = con.cursor()

cur.execute(
    "SELECT DATE(started) AS date, cast(sum(seconds) as int) AS time_in_seconds FROM practice GROUP BY DATE(started)")
days = [{'date': x[0], 'time_in_seconds': x[1]} for x in cur.fetchall()]
data = {'days': days, 'auth_token': os.getenv('FRYDERYK_AUTH_TOKEN')}
print(data)

url = os.getenv('FRYDERYK_WEB_URL') + '/days'

x = requests.post(url, json=data)

# print(x.text)

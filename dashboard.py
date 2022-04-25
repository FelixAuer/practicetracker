import sqlite3

import pandas as pd
from flask import Flask
from flask import render_template

app = Flask(__name__)


def minutes_to_hours(time):
    if time is None:
        time = 0
    hours = time / 60
    minutes = time % 60

    return "%d:%02d" % (hours, minutes)


@app.route("/")
def hello_world():
    con = sqlite3.connect('practicetracker.db')
    cur = con.cursor()

    cur.execute(
        "SELECT round(sum(seconds)/60) FROM practice WHERE DATE(started) = date('now','localtime','start of day')")
    today = cur.fetchone()[0]

    cur.execute(
        "SELECT round((sum(seconds))/60) FROM practice WHERE DATE(started) >= date('now','localtime','-8 days') AND DATE(started) < date('now','localtime','start of day')")
    sum_7 = cur.fetchone()[0]

    cur.execute(
        "SELECT round((sum(seconds)/7)/60) FROM practice WHERE DATE(started) >= date('now','localtime','-7 days') AND DATE(started) < date('now','localtime','start of day')")
    average = cur.fetchone()[0]

    cur.execute(
        "SELECT count(distinct(date(started))) FROM practice WHERE DATE(started) >= date('now','localtime','-7 days') AND DATE(started) < date('now','localtime','start of day')")
    days_played = cur.fetchone()[0]

    cur.execute(
        "select * from (select date(started) as day, round(sum(seconds) / 60) as minutes from practice group by date(started) order by day desc limit 30) order by day")
    days = cur.fetchall()
    df = pd.DataFrame(days, columns=['day', 'minutes'])
    df['day'] = pd.to_datetime(df['day'])

    df.set_index('day', inplace=True)

    idx = pd.date_range(df.index.min(), df.index.max())
    df = df.reindex(idx, fill_value=0)
    df.reset_index(inplace=True)

    con.close()

    return render_template(
        'dashboard.html',
        today=minutes_to_hours(today),
        sum_7=minutes_to_hours(sum_7),
        average=minutes_to_hours(average),
        days_played=days_played,
        days_x=[d.strftime('%Y-%m-%d') for d in df['index'].tolist()],
        days_y=df['minutes'].tolist(),
    )

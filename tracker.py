import datetime
import sqlite3
import time
import os

import pygame.midi


def output(message):
    #print(message)
    pass


def load_input():
    time.sleep(1)
    output("trying to load")
    pygame.init()
    output("pygame.initalized")
    pygame.midi.init()
    output("pygame.midi.initalized")
    piano_input = pygame.midi.Input(int(os.getenv('PIANO_PORT')))
    output("piano_input loaded " + str(piano_input))

    return piano_input


def log_playtime(started):
    playtime = str(time.time() - started)
    con = sqlite3.connect('practicetracker.db')
    cur = con.cursor()

    cur.execute("INSERT INTO practice (started, stopped, seconds) VALUES (?, ?, ?)",
                (datetime.datetime.fromtimestamp(started).strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 playtime))
    con.commit()
    con.close()
    output(playtime)


if __name__ == '__main__':
    output("HELLO MOTO")
    pygame.init()
    i = None
    last_note_played = None
    started = None
    no_input_counter = 0

    while True:
        if i is not None:
            if i.poll():
                no_input_counter = 0
                midi_events = i.read(1000)
                output(midi_events)
                for midi in midi_events:
                    midi_value = midi[0][1]
                    # Movement to the left
                    if midi_value > 0:
                        output("note played: " + str(midi_value))
                        last_note_played = time.time()
                        if started is None:
                            started = time.time()
            else:
                no_input_counter += 1
                if no_input_counter == 200:
                    output("NO INPUT")
                    no_input_counter = 0
                    i = None
            if last_note_played is not None and started is not None and time.time() - last_note_played > 20:
                log_playtime(started)
                started = None
            time.sleep(0.1)
        else:
            # noinspection PyBroadException
            try:
                i = load_input()
            except Exception as e:
                output(str(e))
                if last_note_played is not None and started is not None:
                    log_playtime(started)
                    started = None

                pygame.midi.quit()
                time.sleep(0.1)

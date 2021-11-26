import pygame.midi
import time

def load_input():
    pygame.init()
    pygame.midi.init()
    return pygame.midi.Input(3)

def log_playtime(playtime):
    playtime = str(playtime)
    with open("tracking.log", "a") as trackingfile:
        trackingfile.write(playtime + "\n")
    print(playtime)

if __name__ == '__main__':
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
                for midi in midi_events:
                    midi_value = midi[0][1]
                    # Movement to the left
                    if midi_value > 0:
                        last_note_played = time.time()
                        if started is None:
                            started = time.time()
            else:
                no_input_counter += 1
                if no_input_counter == 5:
                    i = None
            if last_note_played is not None and started is not None and time.time() - last_note_played > 20:
                played_for = time.time() - started
                log_playtime(played_for)
                started = None
            time.sleep(0.1)
        else:
            # noinspection PyBroadException
            try:
                i = load_input()
            except Exception as e:
                if last_note_played is not None and started is not None:
                    played_for = time.time() - started
                    log_playtime(played_for)
                    started = None

                pygame.midi.quit()
                time.sleep(1)

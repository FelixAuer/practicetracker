import sys
import os
import time
import pygame
import pygame.midi

pygame.init()
pygame.midi.init()
i = pygame.midi.Input(3)
last_note_played = None
started = None

while True:
  if i.poll():
    midi_events = i.read(1000)
    for midi in midi_events:
      midi_value = midi[0][1]
      #Movement to the left
      if midi_value > 0:
        print("midi_value")
        last_note_played = time.time()
        if started is None:
          started = time.time()
  else:
    print("turned off")
  if last_note_played is not None and started is not None and time.time() - last_note_played > 5:
    played_for = time.time() - started
    print("Played for {} seconds".format(played_for))
    started = None
  time.sleep(0.1)
 

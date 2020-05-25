#!/bin/python
from gpiozero import Button
from signal import pause
from subprocess import Popen

def increase_volume():
    change_volume('+')
#    print("volume up")

def decrease_volume():
    change_volume('-')
#    print("volume down")

def change_volume(ch_sign):
#    Popen(['amixer', 'sset', 'PCM', 'unmute'])
    Popen(['amixer', 'set', 'PCM', '2%{}'.format(ch_sign)])
#    print("unmuted!")

def mute_volume():
    Popen(['amixer', 'set', 'PCM', '0%'])
#    print("muted!")

while True:
    button_up = Button(2)
    button_up.when_pressed = increase_volume
    button_down = Button(15)
    button_down.when_pressed = decrease_volume
    button_mute = Button(14)
    button_mute.when_pressed = mute_volume
    pause()

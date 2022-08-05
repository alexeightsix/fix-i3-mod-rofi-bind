#!/usr/bin/env python3
import os
import time
from pynput import keyboard

def now():
    return round(time.time() * 1000)

mod_key = "Key.cmd"
command_to_execute = "rofi -show run"

last_key_pressed = None
time_last_pressed = now()
max_wait_time = 1000

def is_mod(key):
    return str(key) == mod_key

def on_press(key):
    global last_key_pressed
    global time_last_pressed
    last_key_pressed = str(key)
    time_last_pressed = now()

def on_release(key):
    global last_key_pressed
    if is_mod(key) and is_mod(last_key_pressed):
        if (now() - time_last_pressed) <= max_wait_time: 
            os.system(command_to_execute)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: listener.join()

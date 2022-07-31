#!/usr/bin/env python3
import time
import os
from pynput import keyboard

def now():
    return round(time.time() * 1000)

command_to_execute = "sudo -u alex rofi -show run"
time_last_pressed = 0
last_key_pressed = ""

mod_key = "Key.cmd"

def open_rofi():
    os.system(command_to_execute)

def is_mod(key):
    key = str(key)
    return key == mod_key

def set_last_key(key):
    global last_key_pressed
    last_key_pressed = str(key)

def on_press(key):
    set_last_key(key)
    if is_mod(key):
        global time_last_pressed
        time_last_pressed = now()

def on_release(key):
    if is_mod(key) and now() - time_last_pressed:
        global last_key_pressed
        if is_mod(last_key_pressed):
            open_rofi()


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: listener.join()


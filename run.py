#!/usr/bin/env python3
import os
from pynput import keyboard

mod_key = "Key.cmd"
command_to_execute = "rofi -show run"

last_key_pressed = None


def is_mod(key):
    return str(key) == mod_key

def on_press(key):
    global last_key_pressed
    last_key_pressed = str(key)

def on_release(key):
    global last_key_pressed
    if is_mod(key) and is_mod(last_key_pressed):
        os.system(command_to_execute)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: listener.join()


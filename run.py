import keyboard
import time
import os

def current_milli_time():
    return round(time.time() * 1000)

last_pressed = current_milli_time()
halt_keys = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "r"}
mod_key = "windows"
command_to_execute = "sudo -u alex rofi -show run"

while True:
    try:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN and event.name in halt_keys:
            time.sleep(0.500)
    
        if event.event_type == keyboard.KEY_UP and event.name == mod_key:
    
            if current_milli_time() - last_pressed < 400:
                os.system(command_to_execute)

        if event.event_type == keyboard.KEY_DOWN and event.name == mod_key:
            last_pressed = current_milli_time()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit(0)

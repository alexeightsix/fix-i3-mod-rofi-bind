# Problem
Switching between workstations will also bring up the Rofi menu unintentionally if you have the $mod key also binded to bring up the Rofi menu. I tried various utilities to be able to create a custom keybinding that nothing worked.

# Solution
I ended up writing my own simple script in Python with the help of the "keyboard" module to create my own custom keybind.
# System Requirements
- GIT
- Python
- Rofi
- i3
# Installation
`git clone https://github.com/alexeightsix/fix-i3-mod-rofi-bind.git` 

`sudo pip install -r fix-i3-mod-rofi-bind.git/requirements.txt`

# Configuration
Currently all the configuration values are hard-coded in the script. To change the command that runs and the user it runs as 
you will need to open up `run.py` and edit the variables accordingly. 
# Run
`python3 fix-i3-mod-rofi-bind.git/run.py`

# i3config
Add the following line to have the script startup once i3 starts

`exec --no-startup-id sudo python3 fix-i3-rofi-bind/run.py`

# Notes
The keyboard module requires the script to run as sudo.


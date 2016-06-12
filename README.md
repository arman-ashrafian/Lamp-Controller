# Lamp-Controller
This is the script I use to control the lamp in my room with my raspberry pi. My lamp is connected to a relay which is controlled by the gpio pins of the Rpi

I connect to my Rpi with SSH and am able to control my lamp from anyhwere in my house.

The autoLamp.py script is on my laptop to automate connecting to my Rpi
It uses the PyAutoGUI to open up PuTTy (SSH application), log into my Rpi, and type the command to run relay1.py

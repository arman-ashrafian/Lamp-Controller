
# Relay Controller 1
# Will take in on/off input

# Arman Ashrafian

import sys, time, os
import RPi.GPIO as gpio

def lampOn():
    print()
    print("                                 ||||||||||||||||||")
    print("                                |||              ||")
    print("                              |||||||            ||")
    print("                            |||||||||||          ||")
    print("                          |||||||||||||||        ||")
    print("                         /       |       \       ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                         ||||||||||||||||||")
    print()

def lampOff():
    print()
    print("                                 ||||||||||||||||||")
    print("                                |||              ||")
    print("                              |||||||            ||")
    print("                            |||||||||||          ||")
    print("                          |||||||||||||||        ||")
    print("                                OFF              ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                                 ||")
    print("                                         ||||||||||||||||||")
    print()



# Some pretty things
for x in range(8):
        print()
os.system("apt-get moo")
print("\n")
lampOff()


gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.cleanup()

pin1 = 11
on = False
off = True
program = True

# Pin set up
gpio.setup(pin1, gpio.OUT)
gpio.output(pin1, off)

try:
        while(program == True):

                switch = input("Command:\n ")

                if(switch == "on" or switch == "On"):
                        gpio.output(pin1, on)
                        lampOn()

                elif(switch == "off" or switch == "Off"):
                        gpio.output(pin1, off)
                        lampOff()

                elif(switch == "rave"):
                        for x in range(10):
                                gpio.output(pin1, on)
                                time.sleep(.2)
                                gpio.output(pin1, off)
                                time.sleep(.2)

                else:
                        print("Enter on or off")


except KeyboardInterrupt:
        lampOff()
        gpio.output(pin1, off)
        gpio.cleanup()
        print("\nSCRIPT ENDED")



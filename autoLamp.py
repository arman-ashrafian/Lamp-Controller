# Open PuTTy
# Click on RPi
# Type "pi", press enter, type "raspberry"
# Type "sudo python3 relay1.py", press enter

import pyautogui as pag
import time as t
import sys

pag.PAUSE = 0.5
pag.FAILSAFE = True

puttyX = 5
puttyY = 125
RPiX = 697
RPiY = 527
openX = 834
openY = 688

pag.moveTo(puttyX, puttyY)
pag.doubleClick()
pag.moveTo(RPiX, RPiY)
pag.click()
pag.moveTo(openX, openY)
pag.click()
t.sleep(3)

pag.typewrite("pi", pause=True)
pag.press("enter")
t.sleep(.5)
pag.typewrite("raspberry", pause=True)
pag.press("enter")
t.sleep(2)
pag.typewrite("sudo python3 relay1.py")
pag.press("enter")



print("done.")

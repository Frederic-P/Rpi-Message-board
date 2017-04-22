#!/usr/bin/env python

#Creates a shortcut that launches PiLib
import sys
import os
import time

absdir = os.path.dirname(sys.argv[0])
absdir = absdir[0:len(absdir)-6]
fnm = "/Pi-Lib Server.dekstop"
fpt = str(absdir)+fnm


shortcut = open(fpt, "w+")

shortcut.write("[Desktop Entry]\n")
shortcut.write("Name=Pi-Lib-Server\n")
shortcut.write("Comment=I launch Pi-Lib server\n")
shortcut.write("Icon=lxterminal\n")
shortcut.write("#If the terminal is too big for your screen, modify the geometry option on the line below (--geometry='width'x'height')\n")
shortcut.write("Exec= lxterminal --geometry=238x65 -e python %s/server.py\n" %(absdir))
shortcut.write("Type=Application\n")
shortcut.write("Terminal=true\n")
shortcut.write("StartupNotify=false\n")


shortcut.close()


print "shortcut generated\n"

print "verify if the shortcut works as expected by opening it, the terminal is configured for full HD screens."
print "The size of the terminal can be adjusted to fit your screen, for this open the desktop file with a text editor"
print "and look for the line that starts with 'Exec =', modify the numbers in the geoometry option.\n"

time.sleep(1)
print "Don't add spaces, and leave the 'x' between the two numbers."
time.sleep(1)
print "Verify if the new settings work; if yes, continue following the manual."
time.sleep(1)


closes = raw_input("Press enter to close this window")

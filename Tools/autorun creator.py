#!/usr/bin/env python

#Creates an instance in /home/pi/.config/lxsession/LXDE-pi/autostart which will autolaunch the server on the pi user account.
import time

print "Copy the path of the shortcut file by right clicking it and clicking 'copy path(s)'."
print "Paste the path when prompted by right clicking in the terminal and clicking 'paste'."


dspath = raw_input("Paste the full path to the server shortcut: ")
atspath = "/home/pi/.config/lxsession/LXDE-pi/autostart"


desktopentry = open(dspath, "r")

desktopcnt = desktopentry.readlines()
desktopentry.close()
workingline = "failsafe"

for line in desktopcnt:
    if line[0:4] == "Exec":
        workingline = line


if workingline == "failsafe":
    print "no Exec line was found in the file you specified."
    print "The program will terminate"
    time.sleep(5)
    exit()
workingline = workingline.strip()
workingline = workingline[6:len(workingline)]
autostartline = "@"+workingline+"\n"



readcurrent = open(atspath, "r")
readcnt = readcurrent.readlines()
readcurrent.close()


memory = []

for line in readcnt:
    if len(line) > 2:
        memory.append(line)

memory.insert(0, autostartline)

print memory

overwritecurrent = open(atspath, "w")
lenmem = len(memory)
for x in range(lenmem):
    overwritecurrent.write("%s" %(memory[x]))

overwritecurrent.close()


print "Autostart entry created."
print "Program will terminate"
time.sleep(5)
exit()

VERSION: 1.1

###########################################################################
###########################################################################
###############          INSTALLATION INSTRUCTIONS          ###############
###########################################################################

1) Follow the configuration advice in the manual.
2) Place the server folder in the location you want, this can be your Desktop or Documents folder
3) Go to the 'Tools' folder and create a shortcut with the program 'shortcut generator.py' by double clicking it.
	* If you get prompted click 'cancel' and set the permission of the .py files so that they can be executed by 'nobody'.
4) Test the shortcut file by double-clicking it.
	* You can move the shortcut to your desktop.
	* The shortcut launches the terminal with a geometry that works for full-HD screens.
	* If the terminal is too big, right click the shortcut and edit it with a 'Text Editor'.
	* Modify the line that starts with 'Exec' and look for '--geometry=238x65'.
		. Lower the numbers if the terminal is too big.
		. Increase the numbers if the terminal is too small.
		. Please note that there are no spaces in '--geometry=238x65'.
		. Save the shortcut file, and try with the new settings.
		. Remodify if needed.
5) Now run the 'autorun creator.py' program.
	* When prompted by the terminal, point it to the shortcut file.
		. Do this by right-clicking the shortcut file and click 'copy path(s)'
		. Paste this path in the terminal by right clicking in it and clicking paste.
	* Press enter.
	* If you pointed the program to the correct file, it will create an autostart entry.
6) Autostart might not work if the file permissions aren't set properly.
	* Right click the 'server.py' file and verify that the file permissions are:
		View content: Anyone
		Change content: Only owner
		Execute: Nobody
7) Reboot the Raspberry Pi.

###########################################################################
###########################################################################
###############                   CHANGELOG                 ###############
###########################################################################

From V1.0 to V1.1
- Added script that generated the .desktop file.
- Added script that made an autostart entry.
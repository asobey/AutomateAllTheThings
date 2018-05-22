#!/usr/bin/python3

#Call program from SSH with: 'python /home/pi/Desktop/IR_TV_Basic.py'
#resource: http://www.piddlerintheroot.com/ir-blaster-lirc/
# https://www.youtube.com/watch?v=7vmzQ8bWwmo
# Rpi3 Model B Pinouts: https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry-pi-circuit-note.html

import os, time

#Turn On TV and change input source
os.system('irsend SEND_ONCE /home/pi/lircd_toshiba.conf KEY_POWER')
time.sleep(12)
os.system('irsend SEND_ONCE /home/pi/lircd_toshiba.conf KEY_I')
time.sleep(1)
os.system('irsend SEND_ONCE /home/pi/lircd_toshiba.conf KEY_5')
time.sleep(1)
os.system('irsend SEND_ONCE /home/pi/lircd_toshiba.conf KEY_ENTER')

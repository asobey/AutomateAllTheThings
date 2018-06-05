#! Python3
#SpeedTest.py

#Programmer: alex.sobey@gmail.com
#Heavy use of this script: https://gist.github.com/jgamblin/3428a164e561baee829c339ac1982e5c

import os
import time

#from twilio.rest import Client
# run test
speed_test = os.popen('speedtest-cli --simple').read()
# split output from 3 lines into speed
lines = speed_test.split('\n')
# get current time for record keeping
now = time.strftime('%Y-%m-%d_%H%M%S')
# if speedtest could not connect set the speeds to 0
if "Cannot" in speed_test:
	p = 0
	d = 0
	u = 0
# extract the values for ping, down and up values
else:
    d = lines[1][10:23]
    u = lines[2][8:19]
#print for debug
    p = lines[0][6:18]
print(now,p, d, u)

msg = f'Time:{now} Ping:{p} D:{d} U:{u}'

print(msg)
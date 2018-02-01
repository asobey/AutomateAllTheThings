#! Python3
#TwilioTest.py

#Programmer: alex.sobey@gmail.com
#Notes: Test for use of SMS with twilio

import os

from twilio.rest import Client

speed_test = os.system('speedtest-cli --simple')

print(speed_test)

accountSID = 'AC046802bc1bcd9de48e4a997d35888ee9'
authToken = ''

client = Client(accountSID, authToken)

myTwilioNumber = '+15129569204'
myCellPhone = '+1'

client.messages.create(body=speed_test, from_=myTwilioNumber, to=myCellPhone)

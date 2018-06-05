#! python3
# RestartTheInterent.py - Xfininity new modem signal, Restart Router

import requests, webbrowser, bs4, time, yaml
from selenium import webdriver

with open('RestartTheInternet.yaml', 'r') as private:
    try:
        privateData = yaml.load(private)
        globals().update(privateData)
    except yaml.YAMLError as exc:
        print(exc)
print(globals())
'''
#webbrowser.open('https://customer.xfinity.com/#/services/modem-restart')
browser = webdriver.Firefox()
#browser.get('https://customer.xfinity.com/#/services/modem-restart')
browser.get('https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3D%2523%252Fservices%252Fmodem-restart%26response%3D1&forceAuthn=1&client_id=my-account-web&reqId=4de868f6-4297-41f7-9a6a-89cc73e6dc1f')

### Modem Reboot
browser2 = webdriver.Firefox()
browser2.get('http://192.168.0.1/AMSOHJDAMKGLGPNC/userRpm/Index.htm')

time.sleep(2)
userName = browser.find_element_by_id('userName')
userName.send_keys(routerUserName)

pcPassword = browser.find_element_by_id('pcPassword')
pcPassword.send_keys(routerPassword)

time.sleep(2)

username = browser.find_element_by_id('user')
username.send_keys(comcastUserName)

passwd = browser.find_element_by_id('passwd')
passwd.send_keys(comcastPassword)

passwd.submit()

time.sleep(10)

browser.get('https://customer.xfinity.com/#/services/modem-restart')


### Modem Reboot
#browser2 = webdriver.Firefox()
#browser2.get('http://192.168.0.1/AMSOHJDAMKGLGPNC/userRpm/Index.htm')



pcPassword.submit

'''
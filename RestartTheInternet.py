#! python3
# RestartTheInterent.py - Xfininity new modem signal, Restart Router

import requests, webbrowser, bs4, time, yaml
from selenium import webdriver

def comcastNewSignal(comcastUserName, comcastPassword):
    #webbrowser.open('https://customer.xfinity.com/#/services/modem-restart')
    browser = webdriver.Firefox()
    #browser.get('https://customer.xfinity.com/#/services/modem-restart')
    browser.get('https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3D%2523%252Fservices%252Fmodem-restart%26response%3D1&forceAuthn=1&client_id=my-account-web&reqId=4de868f6-4297-41f7-9a6a-89cc73e6dc1f')

    username = browser.find_element_by_id('user')
    username.send_keys(comcastUserName)

    passwd = browser.find_element_by_id('passwd')
    passwd.send_keys(comcastPassword)

    passwd.submit()
    time.sleep(10)

    browser.get('https://customer.xfinity.com/#/services/modem-restart')
    time.sleep(5)
    restart = browser.find_element_by_css_selector('button.button')
    restart.click()
    print('Comcast is sending a new signal!')

def modemReboot(routerUserName, routerPassword):
    browser = webdriver.Firefox()
    browser.get('http://192.168.0.1/AMSOHJDAMKGLGPNC/userRpm/Index.htm')

    time.sleep(2)
    userName = browser.find_element_by_id('userName')
    userName.send_keys(routerUserName)

    pcPassword = browser.find_element_by_id('pcPassword')
    pcPassword.send_keys(routerPassword)

    #pcPassword.submit()
    LoginButton = browser.find_element_by_css_selector('#loginBtn')
    LoginButton.click()
    time.sleep(2)
    #browser.get('http://192.168.0.1/PKVJKTJAMEWSGJKA/userRpm/DateTimeCfgRpm.htm')
    #browser.get('http://192.168.0.1/YCPPGYJBESAAVRYB/userRpm/Index.htm')


if __name__ == '__main__':
    with open('RestartTheInternet.yaml', 'r') as private:
        try:
            privateData = yaml.load(private)
        except yaml.YAMLError as exc:
            print(exc)

    #comcastNewSignal(privateData['comcastUserName'], privateData['comcastPassword'])

    modemReboot(privateData['routerUserName'], privateData['routerPassword'])






#! Python3
#ResetModem.py
#Programmer: alex.sobey@gmail.com
#Heavily used: https://automatetheboringstuff.com/chapter11/    Web Scrapping Chapter

import time
import requests
import bs4
from selenium import webdriver

import pyperclip
import pyautogui

browser = webdriver.Firefox()
type(browser)

browser.get('https://speedof.me/')

#Press button to start the speed test
try:
    startBtn = browser.find_element_by_id('startBtn')
    startBtn.click()
except:
    print('Was not able to find start button')

#Wait so test can be performed
time.sleep(60)
'''
try:
    highcharts = browser.find_element_by_class_name('highcharts-subtitle')
    print(f'highcharts is {highcharts}')
except:
    print('Was not able to find highcharts (chart data on first page)')
'''
try:
    btnShare = browser.find_element_by_id('btnShare')
    btnShare.click()
except:
    print('Was not able to find share button')

time.sleep(5)

try:
    txtShareUrl = browser.find_element_by_id('txtShareUrl')
    txtShareUrl.click()

except:
    print('Was not able to find txtShareUrl')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

url = pyperclip.paste()

print(f'The URL is: {url}')

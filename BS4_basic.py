from bs4 import BeautifulSoup

import requests

#url = input("Enter a website to extract the URL's from: ")
url = 'http://www.pythonforbeginners.com'

#r = requests.get('http://'+ url)
r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

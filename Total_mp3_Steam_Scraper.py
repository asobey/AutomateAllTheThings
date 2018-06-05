#!python3
#Total_mp3_Stream_Scraper.py

#Author: A. Sobey
#Repository: https://github.com/asobey/AutomateAllTheThings/Total_mp3_Steam_Scraper.py
#Description: Asks for a URL and scrapes/downloads all .mp3's located at or under that URL.

import os, requests, re
from bs4 import BeautifulSoup as bs
import urllib.request

#url = input("Enter a website to extract .mp3's from (please include http...): ")
url = 'http://podbay.fm/show/201598403'

# make target folder if it does not exist
target_folder = 'C:\\Users\\alexs\\PycharmProjects\\AutomateAllTheThings\\mp3_downloads'
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
print('mp3\'s will be placed into: ' + target_folder)
print('Scraping for mp3\'s...')

top_r = requests.get(url)
top_soup = bs(top_r.text)

links = []
for link in top_soup.find_all('a'):
    link_href = link.get('href')
    if 'show' in link_href and link_href not in links:
        print(link_href)
        links.append(link_href)

        link_r = requests.get(link_href)
        link_soup = bs(link_r.text)

        for sub_link in link_soup.find_all('a'):
            if 'Download' in sub_link:
                download_link = sub_link.get('href')
                print('---------> ' + download_link)
                if 'Episode' or 'Lesson' in download_link:
                    if 'Episode' in download_link:
                        episode = re.search('Episode-([0-9]*)', download_link).group(1)
                    elif 'Lesson' in download_link:
                        episode = re.search('Lesson-([0-9]*)', download_link).group(1)
                    else:
                        episode = 'none'
                    season = 'none'
                    try:
                        season = re.search('Season-([0-9]*)', download_link).group(1)
                    except:
                        season = 'none'
                    file_name = 'Coffee_Break_Spanish_S' + season + '_E' + episode
                    print('Downloading===================>' + file_name)
                    target_path = os.path.join(target_folder, file_name)
                    try:
                        urllib.request.urlretrieve(download_link, target_path)
                    except:
                        print('could not download :' + download_link)
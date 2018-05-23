#!python3
#Total_mp3_Stream_Scraper.py

#Author: A. Sobey
#Repository: github.com/asobey/
#Description: Asks for a URL and scrapes/downloads all .mp3's located at or under that URL.

import os, requests, re
from bs4 import BeautifulSoup as bs
import urllib.request

#url = input("Enter a website to extract .mp3's from (please include http...): ")
url = 'http://podbay.fm/show/201598403'

# make target folder if it does not exist
target_folder = 'C:\\Users\\asobey\\PycharmProjects\\AutomateAllTheThings\\mp3_downloads'
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
                if 'Episode' in download_link:
                    episode = re.search('Episode-([0-9]*)', download_link).group(1)
                    season = re.search('Season-([0-9]*)', download_link).group(1)

                    file_name = 'Coffee_Break_Spanish_S' + season + '_E' + episode
                    print('Downloading===================>' + file_name)
                    target_path = os.path.join(target_folder, file_name)
                    urllib.request.urlretrieve(download_link, target_path)




'''
#stream_url = 'https://audio-cdn.acast.com/encoded/985e7c00-8945-4e0d-a4da-b93049180ce1/853cc505-64c9-40d3-b628-c22de74574e2/encoded-9ee7fbfb0918de2d635262ef3fdb1f3b-128.mp3?response-content-disposition=filename%3D%22Coffee-Break-Spanish-Episode-25-Season-4-Coffee-Br.mp3%22&ci=f91fcfb2-dd98-4378-91f0-1d35741d3d1f&chid=985e7c00-8945-4e0d-a4da-b93049180ce1&aid=853cc505-64c9-40d3-b628-c22de74574e2&Expires=1527348736&Signature=bJoDXVsu58aTUPcscJs5Ofv%7EnVdgJeODNYQ6CXXMzxfyz%7E-wJj6lFaXFEQzD6PpmdqM03oh87JOqT0jx-4HZejwbF1rC1UrN2DIzQ4zQY-KCr90GiQnJKZxjoWOD-qfpIhXBq6bKC1Sg-iVqHn-atDFb%7ELyz7VVAb7dzaidHrgrr38sf6cMt12alvVB6KDa%7Eolf3gFatzCAWY5kwuKRYralF-BwNIY1h4zJO6XLvsT3N6dcGp8SPalvALOBUxIvoacx3TWTDNS2rgt8v2WgtkYKfV24MefM8u-w2tK60Mkx3KdBdJ-ycGXTPnU%7EkEDnb4IbufLLR%7EIrzh0HP8FfFNg__&Key-Pair-Id=APKAJXAFARUOTJQ3BLOQ'
#target_path = 'mp3s/mp3.mp3'
#urllib.request.urlretrieve(stream_url, target_path)


#file_name = 'cb.mp3'
#target_path = os.path.join(target_folder, file_name)
#print(target_path)



#urllib.request.urlretrieve(stream_url, target_path)
    '''
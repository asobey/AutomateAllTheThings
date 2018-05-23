#Currently working

import urllib.request
import os

stream_url = 'https://audio-cdn.acast.com/encoded/985e7c00-8945-4e0d-a4da-b93049180ce1/853cc505-64c9-40d3-b628-c22de74574e2/encoded-9ee7fbfb0918de2d635262ef3fdb1f3b-128.mp3?response-content-disposition=filename%3D%22Coffee-Break-Spanish-Episode-25-Season-4-Coffee-Br.mp3%22&ci=f91fcfb2-dd98-4378-91f0-1d35741d3d1f&chid=985e7c00-8945-4e0d-a4da-b93049180ce1&aid=853cc505-64c9-40d3-b628-c22de74574e2&Expires=1527348736&Signature=bJoDXVsu58aTUPcscJs5Ofv%7EnVdgJeODNYQ6CXXMzxfyz%7E-wJj6lFaXFEQzD6PpmdqM03oh87JOqT0jx-4HZejwbF1rC1UrN2DIzQ4zQY-KCr90GiQnJKZxjoWOD-qfpIhXBq6bKC1Sg-iVqHn-atDFb%7ELyz7VVAb7dzaidHrgrr38sf6cMt12alvVB6KDa%7Eolf3gFatzCAWY5kwuKRYralF-BwNIY1h4zJO6XLvsT3N6dcGp8SPalvALOBUxIvoacx3TWTDNS2rgt8v2WgtkYKfV24MefM8u-w2tK60Mkx3KdBdJ-ycGXTPnU%7EkEDnb4IbufLLR%7EIrzh0HP8FfFNg__&Key-Pair-Id=APKAJXAFARUOTJQ3BLOQ'
target_folder = 'C:\\Users\\asobey\\PycharmProjects\\AutomateAllTheThings\\mp3_downloads'
file_name = 'cb.mp3'
target_path = os.path.join(target_folder, file_name)
print(target_path)
#make target folder if it does not exist
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

urllib.request.urlretrieve(stream_url, target_path)

#r  = requests.get(stream_url)
#print(r.text)

#target = open(target_path, "wb")
#conn = urllib.urlopen(stream_url)
#while True:
#    target.write(conn.read(buf_size))

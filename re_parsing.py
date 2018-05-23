import re

text = 'https://audio-cdn.acast.com/encoded/985e7c00-8945-4e0d-a4da-b93049180ce1/3241f831-ef01-454e-82e8-0f3d1e922585/encoded-aaef7b07b4f129b694abfc6aa2f2e8d7-128.mp3?response-content-disposition=filename%3D%22Coffee-Break-Spanish-Episode-40-Season-4-Coffee-Br.mp3%22&ci'

episode = re.search('Episode-([0-9]*)', text).group(1)
season = re.search('Season-([0-9]*)', text).group(1)

file_name = 'Coffee_Break_Spanish_S' + season + '_E' + episode

print(file_name)
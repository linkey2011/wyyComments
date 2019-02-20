import json
import sys, io
from urllib.request import urlopen


playlistId = 979458599


# urladd = "http://music.163.com/api/playlist/detail?id=979458599"
#     # Your code where you can use urlopen
# with urlopen(urladd) as url:
#     response = url.read().decode('utf-8')

txt = open('1.txt','r', encoding='UTF-8')
response = txt.read()
data = json.loads(response)


playlistName = data["result"]["name"]
tracks = data['result']['tracks']
i = 0
for track in tracks:
    i += 1
    print(i)
    trackName = track["name"]
    artist = track["artists"][0]["name"]
    output = trackName + ' - ' + artist + '\n'
    with open(playlistName+'.txt', 'a',encoding='utf-8') as file:
        file.write(output)




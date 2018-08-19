# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/17 19:52
@Author  : linkey
@Email   : i@hello.faith
@File    : getsong_util.py

"""
from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
from model.entity import song

#返回某个歌单的html
def getUserhtml(url, headers={}):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    code = response.status
    if code != 200:
        print("请求歌单页面出错：",response.status_code)
    content = response.read().decode('utf-8')
    response.close()
    return content

def DownloadSongList(user_palylist_id,listenerid):  #传入某个歌单id

    user_palylist_url = 'https://music.163.com/playlist?id='+user_palylist_id  #拼接歌单的url
    user_palylist_html = getUserhtml(user_palylist_url, headers={
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'music.163.com'
    })
    bsObj = BeautifulSoup(user_palylist_html,"html.parser")   #美化
    #查找符合要求的song文本
    songlist = bsObj.findAll("a",{"href":re.compile("\/song\?id=\d")})
    #逐条插入
    mysongList =[]

    for songGot in  songlist:
        Song  = song.Song()
        songname = songGot.get_text()
        songid   = songGot['href']
        songid = re.sub("\D", "", songid)#截取数字
        Song.setsongid(songid)
        Song.setsongname(songname)
        Song.setlistenerid(listenerid)
        mysongList.append(Song)

    return mysongList
        #将单个歌单的歌曲封装，并返回










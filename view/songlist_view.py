# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/17 17:14
@Author  : linkey
@Email   : i@hello.faith
@File    : songlist_view.py

"""
from  action import songaction
from  util import bar_util
from util import getsong_util


import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "/..")))

# 功能尚未是实现，暂时手动填写
def GetAllSonglistIdOfSomeone(listenerid):
    SonglistId = ['979458599']
    return SonglistId

# actionname = '更新听众所有歌单'
def DownLoadSongList():
    print('你想爬谁的歌单？输入她的id：',end='')
    listenerid = input();
    second = 5
    print("原则上此时应该根据输入的听众id -->获取其所有歌单id，由于此功能暂未完成，手台已经手动填写完毕，休息",second,"秒")
    bar_util.bar(second)
    AllSonglistId = GetAllSonglistIdOfSomeone(listenerid)
    action = songaction.SongAction()
    for SingleSongListId in AllSonglistId:
        #获取单个歌单里的所有歌，封装成类对象Song, 返回songlist
        songList    =  getsong_util.DownloadSongList(SingleSongListId,listenerid)
        for SingSong in songList:

            ans = action.addSingleSong(SingSong)
            if ans == 0:
                return ans


    return 1


#展示库中某位听众的全部歌曲
def ShowAllSong():
    print("输入你要查找的的听众的id")
    action = songaction.SongAction()
    listenerID = input()
    ans, songList =   action.ShowAllSong(listenerID)
    if ans == 1:
        for single in songList:
            songid = single[0]
            songname = single[1]
            songid = '%-20s' % songid
            print("歌曲id：",songid, "歌名：",songname)

    return 1


def main(command):
    if command == "2":
        return DownLoadSongList()

    if command == "4":
        return ShowAllSong()




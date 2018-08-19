# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/17 17:43
@Author  : linkey
@Email   : i@hello.faith
@File    : songaction.py

"""
from model.dao import song_dao
class SongAction:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def addSingleSong(self,song):
        dao = song_dao.SongDao()
        return dao.addSong(song)


    def ShowAllSong(self,listenerID):
        dao = song_dao.SongDao()
        ans ,songList = dao.ShowAllSong(listenerID)
        return  ans, songList


    def GetOk(self,songid):
        dao  = song_dao.SongDao()
        result = dao.GetOk(songid)
        return result

    def UpdateOk(self,songid):
        dao  = song_dao.SongDao()
        result = dao.GetOk(songid)
        return result

    def GetFinish(self,songid):
        dao  = song_dao.SongDao()
        result = dao.GetFinish(songid)
        return result

    def UpdateFinish(self,songid):
        dao  = song_dao.SongDao()
        result = dao.UpdateFinish(songid)
        return result

    def GetLastPage(self,songid):
        dao  = song_dao.SongDao()
        result = dao.GetlastPage(songid)
        return result

    def UpdateLastPage(self,songid,lastpage):
        dao  = song_dao.SongDao()
        result = dao.UpdateLastPage(songid,lastpage)
        return result

# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/17 15:25
@Author  : linkey
@Email   : i@hello.faith
@File    : song.py

"""
class Song:
    def __init__(self):
        pass
    def __init__(self,songid = "默认值",lastage = "默认值",finish = "默认值",ok = "默认值",listenerid = "默认值",num = "默认值",songname = "默认值"):
        self.songid     = songid
        self.lastpage   = lastage
        self.finsh      = finish
        self.ok         = ok
        self.listenerid =listenerid
        self.num        = num
        self.songname   = songname


    def getsongname(self):
        return self.songname

    def setsongname(self, songname):
        self.songname = songname

    def getsongid(self):
        return self.songid

    def setsongid(self, songid):
        self.songid = songid

    def getlastage(self):
        return self.lastage

    def setlastage(self, lastage):
        self.lastage = lastage

    def getfinish(self):
        return self.finish

    def setfinish(self, finish):
        self.finish = finish

    def getok(self):
        return self.ok

    def setok(self, ok):
        self.ok = ok

    def getlistenerid(self):
        return self.listenerid

    def setlistenerid(self, listenerid):
        self.listenerid = listenerid

    def getnum(self):
        return self.num

    def setnum(self, num):
        self.num = num





















# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/18 20:48
@Author  : linkey
@Email   : i@hello.faith
@File    : comment.py

"""
class Comment:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __init__(self,time = "默认值",content= "默认值",username= "默认值",userid= "默认值",zan= "默认值",onpage= "默认值",id = '默认值'):
        self.time = time
        self.content = content
        self.username = username
        self.userid = userid
        self.zan = zan
        self.onpage = onpage
        self.id = id

    def gettime(self):
        return self.time

    def settime(self, time):
        self.time = time


    def getcontent(self):
        return self.content

    def setcontent(self, content):
        self.content = content

    def getusername(self):
        return self.username

    def setusername(self, username):
        self.username = username

    def getuserid(self):
        return self.userid

    def setuserid(self, userid):
        self.userid = userid

    def getzan(self):
        return self.zan

    def setzan(self, zan):
        self.zan= zan

    def getonpage(self):
        return self.onpage

    def setonpage(self, onpage):
        self.onpage= onpage



    def getid(self):
            return self.id

    def setid(self, id):
        self.id = id
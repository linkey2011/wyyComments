# coding=utf-8
from model.dao import listener_dao
class ListenerAction:
    def __init__(self):
        pass

    def addListener(self,Listener):
        dao = listener_dao.ListenDao()
        return  dao.addListener(Listener)

    def SelectAllListener(self,):
        dao = listener_dao.ListenDao()
        ans , ListenerList = dao.SelectAllListenerId()
        return  ans , ListenerList

# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/18 22:31
@Author  : linkey
@Email   : i@hello.faith
@File    : commentaction.py

"""
from model.dao import comment_dao
class CommentAction:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def InsertComment(self,commentNew,songid):
        dao = comment_dao.CommentDao()
        return dao.InsertComment(commentNew,songid)



    def CreatTable(self,songid):
        dao = comment_dao.CommentDao()
        return dao.CreatSongCommentTable(songid)
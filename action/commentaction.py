# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/18 22:31
@Author  : linkey
@Email   : i@hello.faith
@File    : commentaction.py

"""
from model.dao import comment_dao
from model.entity import comment
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


    def GetMaxID(self,songid):
        dao = comment_dao.CommentDao()
        return dao.GetMaxID(songid)

    def GetCommentbyID(self,songid,id):
        dao = comment_dao.CommentDao()
        Comment = comment.Comment()
        res =  dao.GetCommentbyID(songid,id)
        Comment.id = res[0]
        Comment.content = res[1]
        Comment.username = res[2]
        Comment.userid = res[3]
        Comment.zan = res[4]
        Comment.onpage = res[5]
        Comment.time = res[6]

        return Comment
# ge = CommentAction();
# res = ge.GetCommentbyID(28854182,10058)
#
# print(res.content)

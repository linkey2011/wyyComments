# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/18 20:54
@Author  : linkey
@Email   : i@hello.faith
@File    : comment_dao.py

"""
from util import db_util
from model.entity import comment
class CommentDao:

    def __init__(self):
        pass

    #建立对应的song评论表
    def CreatSongCommentTable(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql_creatTable="""create table  if not exists  songid_%s  
        (
          id       bigint not null auto_increment,
          content  varchar(500), 
          username varchar(255), 
          userid   varchar(255), 
          zan      varchar(255), 
          onpage   varchar(255), 
          time     varchar(255),
          primary  key (id)
        ) DEFAULT CHARSET=utf8mb4 """ % songid
        try:
            cursor.execute(sql_creatTable)
            connect.commit()
        except Exception as e:
            print("建表出错",'错误是:', e)
            return 0
        else:
            return 1
        finally:
            cursor.close()
            cursor.close()

    #插入评论
    def InsertComment(self,comment,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()

        content = comment.content
        username = comment.username
        userid = comment.userid
        zan = comment.zan
        onpage = comment.onpage
        time   = comment.time

        content = content.replace("'","\\\'")
        content = content.replace('"','\\\"')  #防止因为含有【"】【'】导致sql语句执行出错
        username = username.replace("'","\\\'")
        username = username.replace('"','\\\"')  #防止因为含有【"】【'】导致sql语句执行出错
        sql  = "INSERT INTO songid_%s (content,username,userid,zan,onpage,time)VALUE ('%s','%s','%s', '%s','%s','%s')"
        data = (songid,content,username,userid,zan,onpage,time)
        try:
            cursor.execute(sql % data)
            connect.commit()
        except Exception as  e:
            print("插入评论出错",'错误是:', e)
            return 0
        else:
            return 1
        finally:
            cursor.close()
            connect.close()

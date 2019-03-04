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


            return  1
        finally:
            cursor.close()
            connect.close()

    #根据歌曲id, 用户id，评论内容和时间四个方面唯一标志一个评论，并获取此评论的id
    def GetCommentID(self,songid,userid,content,time):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        #SELECT id FROM songid_28854182 WHERE username = '许家的小可爱' AND content = '唱不了啊[大哭]' AND time = '2018-07-29 18:53:46'
        sql  = "SELECT id from songid_%s WHERE userid = '%s' AND content = '%s' AND time = '%s'"
        data = (songid,userid,content,time)
        try:

            cursor.execute(sql % data)
            connect.commit()
        except Exception as  e:
            print("获取最新评论主键id出错",'错误是:', e)
            return 0
        else:
            result = cursor.fetchall()
            length = len(result)

            return result[length - 1][0]
        finally:
            cursor.close()
            connect.close()

    #获取当前最新插入的评论的id值
    def GetMaxID(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()

        sql  = "select max(id) from songid_%s"
        data = (songid)
        try:
            cursor.execute(sql % data)
            connect.commit()
        except Exception as  e:
            print("获取max id出错",'错误是:', e)
            return 0
        else:
            return cursor.fetchone()[0]
        finally:
            cursor.close()
            connect.close()


    #根据id获取评论
    def GetCommentbyID(self,songid,id):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        #SELECT * FROM `songid_28854182` WHERE id = 10058
        sql  = "SELECT * FROM songid_%s WHERE id = '%s'"
        data = (songid,id)
        try:
          #  print(sql % data)
            cursor.execute(sql % data)
            connect.commit()
        except Exception as  e:
            print("根据id获取评论出错",'错误是:', e)
            return 0
        else:
            return cursor.fetchone()
        finally:
            cursor.close()
            connect.close()


# b = CommentDao()
# res = b.GetCommentbyID(28854182,10058)
# print(res)
# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/17 16:38
@Author  : linkey
@Email   : i@hello.faith
@File    : song_dao.py

"""
from util import db_util
class SongDao:
    def __init__(self):
        pass

    #验证歌曲是否在库中， 为用户id和歌曲id双验证
    def verify(self,songid,listenerid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql = "select count(*)  from songtotal WHERE songid = '%s' AND listenerid = '%s'"
        data = (songid,listenerid)
        try:
            cursor.execute(sql % data)
            connect.commit()
        except Exception as  e:
            print("查重出错, id: ",listenerid,"已在库中歌曲总数出错",'错误是:', e)
        else:
            result = cursor.fetchone()[0]
            return  result    #返回这首歌在库中查到的次数
        finally:
            cursor.close()
            connect.close()

    # 插入新歌
    def addSong(self,song):

        songid     = song.getsongid()
        listenerid = song.getlistenerid()
        MyVerify = self.verify(songid,listenerid)

        if  MyVerify > 0:
            return 1
        elif MyVerify == 0:
            connectObj = db_util.ConnectToMysql()
            connect    = connectObj.getConnect()
            cursor  = connect.cursor()

            lastage    = 1
            finish     = 0
            ok         = 0
            songname   = song.getsongname()
            num        = self.GetNum(song.listenerid)

            songname=songname.replace("'","\\\'")
            songname=songname.replace('"','\\\"')  #防止因为含有【"】【'】导致sql语句执行出错
            sql  = "INSERT INTO songtotal (songid,lastpage,finish,ok,listenerid,num,songname)VALUES ('%s','%s','%s','%s','%s','%s','%s');"
            data = (songid,lastage,finish,ok,listenerid,num,songname)
            try:
                cursor.execute(sql % data)
                connect.commit()
                songid = '%-20s' % songid
                listenerid = '%-20s' % listenerid
                print("成功插入歌曲，       id ：",songid, " 听众id：",listenerid,"歌名：",songname)
            except Exception as  e:
                print("插入song出错",'错误是:', e)
                return 0
            else:
                return 1
            finally:
                cursor.close()
                connect.close()

    #展示某人所有歌曲
    def ShowAllSong(self,listenerid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql = "select songid , songname from songtotal WHERE  listenerid = '%s'" % listenerid
        try:
            cursor.execute(sql)
            connect.commit()
        except Exception as  e:
            print("展示某人所有歌曲",'错误是:', e)
            return  0,0
        else:
            return 1,cursor.fetchall()
        finally:
            cursor.close()
            connect.close()

    #获取lastpage
    def GetlastPage(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "select lastpage from songtotal WHERE songid = '%s'" %songid
        try:
            cursor.execute(sql)
            connect.commit()
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print("获取lastpage出错","歌曲id",songid,'错误是:', e)
        finally:
            cursor.close()
            connect.close()

    #更新lastpage
    def UpdateLastPage(self,songid,lastpage):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "UPDATE songtotal SET lastpage = %s WHERE songid ='%s';"
        data = (lastpage,songid)
        try:
            cursor.execute(sql % data)
            connect.commit()
        except Exception as e:
            print("更新lastpage出错",'错误是:', e)
            return 0
        else:
            return 1
        finally:
            cursor.close()
            connect.close()

    #获取ok
    def GetOk(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "select ok from songtotal WHERE songid = '%s'" %songid
        try:
            cursor.execute(sql)
            connect.commit()
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print("获取ok出错",'错误是:', e)
        finally:
            cursor.close()
            connect.close()

    #ok  置 1
    def UpdateOk(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "UPDATE songtotal SET ok = 1 WHERE songid ='%s';" % songid
        try:
            cursor.execute(sql)
            connect.commit()
        except Exception as e:
            print("更新ok出错",'错误是:', e)
            return 0
        else:
            return 1
        finally:
            cursor.close()
            connect.close()

    #获取finish
    def GetFinish(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "select finish from songtotal WHERE songid = '%s'" %songid
        try:
            cursor.execute(sql)
            connect.commit()
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print("获取finish出错",'错误是:', e)
        finally:
            cursor.close()
            connect.close()

    #finish   置 1
    def UpdateFinish(self,songid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "UPDATE songtotal SET finish = 1 WHERE songid ='%s';" % songid
        try:
            cursor.execute(sql)
            connect.commit()
        except Exception as e:
            print("更新finsih出错",'错误是:', e)
            return 0
        else:
            return 1
        finally:
            cursor.close()
            connect.close()

    #某个歌曲的排名
    def GetNum(self,listenerid):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql = "select count(*) as value from songtotal WHERE listenerid = '%s'" % listenerid
        try:
            cursor.execute(sql)
            connect.commit()
        except Exception as  e:
            print("查询",listenerid,"已在库中歌曲总数出错",'错误是:', e)
        else:
            result = cursor.fetchone()[0]
            return  result
        finally:
            cursor.close()
            connect.close()



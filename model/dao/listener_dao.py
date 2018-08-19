from util import db_util
import re
class ListenDao:

    def __init__(self):
        pass

    #添加听众
    def addListener(self,newListener):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql  = "insert into listener (listenerid)VALUE ('%s');"
        data = (newListener.getid())
        try:
            cursor.execute(sql % data)
            connect.commit()
        except Exception as  e:
            print("插入newListener出错",'错误是:', e)
            return 0
        else:
            return 1
        finally:
            cursor.close()
            connect.close()


    #展示所有听众
    def SelectAllListenerId(self):
        connectObj = db_util.ConnectToMysql()
        connect    = connectObj.getConnect()
        cursor  = connect.cursor()
        sql = "select listenerid from listener"
        try:
            cursor.execute(sql)
            connect.commit()
        except Exception as  e:
            print("查看库中已有全部听众id出错",'错误是:', e)
            return  0,0
        else:
            return 1, cursor.fetchall()

        finally:
            cursor.close()
            connect.close()

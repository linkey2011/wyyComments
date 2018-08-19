import pymysql


class ConnectToMysql:
    def __init__(self):
        pass

    def  getConnect(self):
        try:
            connect = pymysql.Connect(
                host    = '127.0.0.1',
                port    = 3306,
                user    = 'root',
                passwd  = 'root',
                db      = 'wyy',
                charset = 'utf8mb4'
            )
            return connect
        except Exception as e:
            print("连接数据库失败",'错误是:', e)



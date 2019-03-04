# coding=utf-8
"""
@project : wyyComments
@Time    : 2019/2/23 16:46
@Author  : linkey
@Email   : i@hello.faith
@File    : bark.py

"""
from urllib import request
from urllib.parse import quote
import string
import configparser
import os

class Bark:
    #读取bark默认的端口和主机
    def __init__(self):
        cf = configparser.ConfigParser()


        pwd = os.path.dirname(os.path.abspath(__file__))
        cf.read(pwd+"/bark.conf")
        # secs = cf.sections()
        # opts = cf.options("bark")
        # kvs = cf.items("bark")

        self.host = cf.get("bark","bark_host")
        self.port = cf.get("bark","bark_port")
        self.key  = cf.get("bark","bark_key")
    # 消息提醒
    def Notice(self,msg,command,title = ''):
        url = self.GetURL(msg,command,title)
        link = quote(url,safe=string.printable)
        # print(link)
        request.urlopen(link)

    #  0 代表不用跳转, 1 代表链接跳转
    def GetURL(self,msg,command,title):
        # /:key/:category/:title/:body


        url = "http://"+ self.host + ':' + self.port +  '/' + self.key + '/'
        title = title + '/'
        if command == 0:
            url = url + title + msg

        elif command == 1: # 这个功能暂时好像用不到，想到了再来填坑
            url = url + title + msg

        return url



#
#
# k = Bark()
# k.Notice('出错12000000000000000000003了',0,'标111111题')
#


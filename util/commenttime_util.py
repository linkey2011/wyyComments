# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/20 12:28
@Author  : linkey
@Email   : i@hello.faith
@File    : commenttime_util.py

"""
import  time
def CommentTime(sjc):
    length =len(str(sjc))
    if length >= 11:      #防止13位时间戳
        sjc = float(sjc/1000)


    st = time.localtime(sjc)  #时间戳结构化

    mytime = time.strftime('%Y-%m-%d %H:%M:%S', st)
    return  mytime
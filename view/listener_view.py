# coding=utf-8
from  action import listeneraction
from  model.entity import listener
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "/..")))

#查看库中已有全部听众id
def ShowAllListenerId():
    action =  listeneraction.ListenerAction()
    ans , ListenerList = action.SelectAllListener()
    p = 0
    if ans == 1:
        for single in  ListenerList:
            single = single.__str__()  #查询返回结果为元组，转化为字符串
            single = re.sub("\D", "", single)#截取数字
            p += 1
            q = '%-4d' % p
            print("听众",q,'id：',single)
    return ans

#添加听众id
def AddLidtener():
    print('输入要添加的听众的id：',end='')
    id = input()
    sb     =  listener.Listener()
    sb.setid(id)
    action =  listeneraction.ListenerAction()
    feedback = action.addListener(sb)

    return  feedback
def main(command):
    if command == "1":
       return AddLidtener()
    elif command == "3":
     return ShowAllListenerId()
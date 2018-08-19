# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/18 13:16
@Author  : linkey
@Email   : i@hello.faith
@File    : feedback_util.py

"""
def MyFeedback(actionname,feedback):
    if feedback == 1:
        print(actionname,"成功",'继续输入指令进行下一步操作')
    elif feedback == 0:
        print(actionname,"失败",'继续输入指令进行下一步操作')

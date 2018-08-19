# coding=utf-8
# 模块名 类名 函数名 构造函数两个就够
from view import listener_view
from view import songlist_view
from util import feedback_util
from view import comment_view
import time
CONTEXT = "[*]:主菜单\n" \
          "[1]:添加听众\n" \
          "[2]:更新某位听众的歌单\n" \
          "[3]:获取库中已有的听众id\n" \
          "[4]:展示库中某位听众的全部歌曲\n" \
          "[5]:爬取某位听众歌单里所有歌曲的评论,支持 断点续爬 😄，输入她的id\n" \
          "[0]:退出当前功能，返回主菜单" \
          "[#]:退出程序\n"

def Start():
    print(CONTEXT)
    while True:
        myCommand = input()

        if myCommand == "1":
            actionname = '添加听众id'
            result = listener_view.main(myCommand)
            feedback_util.MyFeedback(actionname,result)
        if myCommand == "2":
            start_time = time.time()           # 记录代码开始时间

            actionname = '更新听众所有歌单'
            result = songlist_view.main(myCommand)
            feedback_util.MyFeedback(actionname,result)

            end_time = time.time()             # 记录代码结束时间
            run_time = end_time - start_time   # 计算运行时间
            print('run_time: ', run_time)
        if myCommand == "3":
            actionname = '查看库中已有全部听众id'
            result = listener_view.main(myCommand)
            feedback_util.MyFeedback(actionname,result)
        if myCommand == "4":
            actionname = '展示库中某位听众的全部歌曲'
            result = songlist_view.main(myCommand)
            feedback_util.MyFeedback(actionname,result)
        if myCommand == "5":
            actionname = '爬取某位听众歌单里所有歌曲的评论'
            result = comment_view.main(myCommand)
            feedback_util.MyFeedback(actionname,result)
        elif myCommand == "0":
            pass
        elif myCommand == "#":
            print("程序结束")
            break





if __name__ == '__main__':
    Start()

# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/17 19:36
@Author  : linkey
@Email   : i@hello.faith
@File    : bar_util.py

"""
from time import sleep
from tqdm import tqdm# 这里同样的，tqdm就是这个进度条最常用的一个方法# 里面存一个可迭代对象

def bar(second):
    for i in tqdm(range(0, 1000)): # 模拟你的任务
        sleep(second/1000)
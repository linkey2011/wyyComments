# coding=utf-8
"""
@project : wyyComments
@Time    : 2018/8/19 0:10
@Author  : linkey
@Email   : i@hello.faith
@File    : getsinglesongallcomment_util.py

"""
# coding = utf-8
from Crypto.Cipher import AES
import base64
import requests
import json
import time
from  fake_useragent import UserAgent
from action import songaction, commentaction
from action.commentaction import CommentAction
from action.songaction import SongAction
from model.entity import  comment

uaObj = UserAgent()

proxies = {
    'http':'127.0.0.1:1080',
}

headers = {
    'Host': 'music.163.com',
    'User-Agent': uaObj.random,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',



    "Cookie":'JSESSIONID-WYYY=S02voAW%2FlsB73k%5CI8hJ7r2DyAbEjt4OBrmqyoPERHFEDbCogcXu2RT8WkrRdnJ6uWa443wh%2FuJa1TwblHUAE3f2hGQ%5C9HKW5HUh5jnUgyIwVUZxB0%2FXw%5CSzxx8tKdFoGkn71lQzPTVT7dOcYaKkeZpQKT8dQT3%2BJTm4OhgaXyjGVHBJc%3A1534693422094; _iuqxldmzr_=32; _ntes_nnid=85486da3b45afb0b02d5e8e84986fd3c,1534691622120; _ntes_nuid=85486da3b45afb0b02d5e8e84986fd3c; __utma=94650624.1393191032.1534691622.1534691622.1534691622.1; __utmc=94650624; __utmz=94650624.1534691622.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=uqWIsQ0oCz1NwkarNHZWAgdNxT8UEf6BNcjDeaCaLjllSOVkCQZZPe4pzG%2BZ56hJrjQyeYV89ohoAxCiScS6eqOZUOFS3sN3f%2FnR6RvBq%2B19EApqb%2B%2F5FbnTh8as4y8YWHA%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d95b96bcbdaad87df5f597aeb33f8beca689c8409ab09c95f321b1b0bea3f62af0fea7c3b92ab7af99aaf25bf4b18d9bb446b5b5af93cd449a898f88e746bc8cf8b6c86ef69e8284e950a7bf8d82cf62b0b49db0d561818f96bbd36ff8b0b6a8aa52f7eaa8abf16293a7abbad534fbb1a890c47481b79d84d23ea7af81bbd845868dfd94cd39a6f1a2b3b55ab69ebfccb433879fc092e121edeb8a83ed60ace8af94b773fc8799a9c437e2a3; WM_TID=z7vbcBuk6qCbl2hzioBPRYC19eh11PBe; __utmb=94650624.3.10.1534691622'
}

#获取params
def get_params(first_param, forth_param):
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key.encode(), iv.encode())
    h_encText = AES_encrypt(h_encText.decode(), second_key.encode(), iv.encode())
    return h_encText.decode()

# 获取encSecKey
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey

# 解AES秘
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text.encode())
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

# 获取json数据
def get_json(url, data):
    # response = requests.post(url, headers=headers, data=data, proxies=proxies)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        print("获取json出错","请求状态码：",response.status_code)

    return response.content

# 传入post数据
def crypt_api(id, offset):
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=" % id
    if offset == 0:
        first_param = "{rid:\"\", offset:\"%s\", total:\"true\", limit:\"20\", csrf_token:\"\"}" % offset
    if offset != 0:
        first_param = "{rid:\"\", offset:\"%s\", total:\"false\", limit:\"20\", csrf_token:\"\"}" % offset
    forth_param = "0CoJUm6Qyw8W8jud"
    params = get_params(first_param, forth_param)
    encSecKey = get_encSecKey()
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    return url, data


# 获取评论
def get_comment(songid,step):
    SongAction = songaction.SongAction()
    CommentAction = commentaction.CommentAction()
    commentNew = comment.Comment()

    #获取歌曲的lastpage
    lastPage  = SongAction.GetLastPage(songid)

    #第一次请求 offset = 0  -- 目的为了获得该歌曲一共有多少页面评论
    try:
        offset = 0
        url, data = crypt_api(songid, offset)
        json_text = get_json(url, data)
        json_dict = json.loads(json_text.decode("utf-8"))
        comments_sum = json_dict['total']
        if comments_sum % 20 == 0:
            totalPage = int(comments_sum/20)
        else:
            totalPage = int(comments_sum/20) + 1
    except Exception as e:
        print('进程',step,"获取评论总页面出错，错误为：",e,'神秘代码',json_text)
        time.sleep(5)
        return 0
    else:
        # 逐页面获取评论，并插入
        for page in range(lastPage, totalPage + 1):   #起始页面为lastpage
            if page % 11 == 0:
                print('休息周期')
                time.sleep(11.11)

            #获取当前页面所有评论的json数据
            offset = (page - 1) * 20
            try:
                url, data    = crypt_api(songid, offset)
                json_text    = get_json(url, data)
                json_dict    = json.loads(json_text.decode("utf-8"))
                json_comments = json_dict['comments']   #一次json返回一页面评论
                print('进程',step,'已经获取一页json,歇会')
                time.sleep(2)
            except Exception as e:
                print('进程',step,"获取第",page,"页json数据出错，错误是：",e,'神秘代码',json_text)
                time.sleep(10)
                return 0
            else:
                p       =  0   #当前页面的的评论排名
                nowPage = page  #当前爬取的评论所在页面
                # 一个个 的插入评论
                SongAction.UpdateLastPage(songid,nowPage)    #更新当前最新的lastpage
                for json_comment in json_comments:

                    p += 1
                    #封装数据
                    commentNew.username = str(json_comment['user']['nickname'])  #用户名
                    commentNew.content  = str(json_comment['content'] )          #评论内容
                    commentNew.onpage   = nowPage                                #评论所在页面
                    commentNew.zan      = json_comment['likedCount']             #点赞数
                    commentNew.userid   = str(json_comment['user']['userId'])    #用户的id标志

                    ans = CommentAction.InsertComment(commentNew,songid)
                    if ans != 1:
                        print('进程',step,"插入评论出错")
                        time.sleep(10)
                    else:
                        show = '%s%s%s%s%s%s%s' % (songid,": " ,commentNew.username, "写道: " ,commentNew.content,"   点赞数：",commentNew.zan)
                        num  ="%-2s" % p
                        printPage = "%-4s" % nowPage
                        print('进程',step,' ',printPage, '页 第',num,'个',' ',show)
        print('进程',step,songid,"评论爬取完成")
        return 1      #只有爬完了才能返回1
    finally:
        SongAction.__del__()
        CommentAction.__del__()
        commentNew.__del__()


def main(songid,step):
   ans =  get_comment(songid,step)
   return ans
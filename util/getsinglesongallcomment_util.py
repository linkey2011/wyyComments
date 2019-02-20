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
from model.entity import  comment
from util import commenttime_util
uaObj = UserAgent()



#
# f = open(os.path.abspath('..')+'\\resource\\cookie.txt')
# myCookie = str(f.read())
# print(myCookie)
# f.close()
#
#


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
    "Cookie":'_iuqxldmzr_=32; _ntes_nnid=b1e5bb4939794b0b1537627220a25585,1534698463481; _ntes_nuid=b1e5bb4939794b0b1537627220a25585; __utmc=94650624; WM_TID=7dETf%2BqkrscMK8uT4klP4LVcmzbW0DZy; hb_MA-BFF5-63705950A31C_source=www.baidu.com; __f_=1534737106682; __utmz=94650624.1534737104.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; playerid=21595483; JSESSIONID-WYYY=NRho9KD9MpUhatXWWaXWYd%2BYfZYDf0ql7eoXS2pRKQOiDF%5C%2B71b4yRsmo6Rcz%5CapUIDsRTM97%2FJ6cpSY8FlUSWikziovmreBjiHJhD993cvsqQilakFq8XdOiwxn%5CDyD%2BSp8YT%5CP1abCGpsn0fXcv5eXTNoiga7cb6Cw2G%5C013OZc%5C7m%3A1534752658208; __utma=94650624.1104846434.1534698464.1534737104.1534750858.3; WM_NI=iP9ldZ4wndxishqmokv%2Fi9aJgXBTsCxs7xS4Xc0oX%2BedPNhRaaGaXjrPBomwQUvY9FNvP41RpempAQdB%2FZUQFWEZSk%2FnhMod%2BAQ0IidhkKARYdQJImoGyazPAyI5Rpf9ZXQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8fb1648dbebe8dc821838a96a3c5408be8acafce39b3f1beaadc59ab98f8b6d62af0fea7c3b92aab90f78de752f8a9a285fb63b1b8bf8eee61b6f1a7dae442a5888eb5f249bcadf999d2409cbd0090db21a7bca0afeb5aa3bf8982db62b2908e90f07d938bbababc4e8eaaa0d5b45ab4bba391c45ba89ee1bbd85b86898bbbd261edb2a8aeee70e99f9fd1cc63a8b8a5acc45a9bbc9fabcc67ad99b782f95c83a787d6d17ca6e796b9d437e2a3; __utmb=94650624.4.10.15347508582'
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
    RestCycleTime = 300
    ErrorRestTime = 5
    RoutineRestTime = 1
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
        time.sleep(ErrorRestTime)
        return 0
    else:
        # 逐页面获取评论，并插入
        for page in range(lastPage, totalPage + 1):   #起始页面为lastpage
            if page % 11 == 0:
                print('休息周期')
                time.sleep(RestCycleTime)

            #获取当前页面所有评论的json数据
            offset = (page - 1) * 20
            try:
                url, data    = crypt_api(songid, offset)
                json_text    = get_json(url, data)
                json_dict    = json.loads(json_text.decode("utf-8"))
                json_comments = json_dict['comments']   #一次json返回一页面评论
                print('进程',step,'已经获取一页json,歇会')
                time.sleep(RoutineRestTime)
            except Exception as e:
                print('进程',step,"获取第",page,"页json数据出错，错误是：",e,'神秘代码',json_text)
                time.sleep(ErrorRestTime)
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
                    sjc                 = json_comment['time']
                    commentNew.time     = commenttime_util.CommentTime(sjc)
                    commentNew.onpage   = nowPage                                #评论所在页面
                    commentNew.zan      = json_comment['likedCount']             #点赞数
                    commentNew.userid   = str(json_comment['user']['userId'])    #用户的id标志

                    ans = CommentAction.InsertComment(commentNew,songid)
                    if ans != 1:
                        print('进程',step,"插入评论出错")
                        time.sleep(ErrorRestTime)
                    else:
                        num  ="%-2s" % p
                        printPage = "%-4s" % nowPage
                        print('进程',step,printPage, '页 第',num,'个',commentNew.time,songid,commentNew.username,"写道: " ,commentNew.content,"   点赞数：",commentNew.zan)
        print('进程',step,songid,"评论爬取完成")
        return 1      #只有爬完了才能返回1
    finally:
        SongAction.__del__()
        CommentAction.__del__()
        commentNew.__del__()


def main(songid,step):
   ans =  get_comment(songid,step)
   return ans
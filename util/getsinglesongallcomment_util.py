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



    "Cookie":'_ntes_nnid=b54843e4662d37f48cf33be4813606f1,1534497592747; _ntes_nuid=b54843e4662d37f48cf33be4813606f1; _iuqxldmzr_=32; WM_TID=4fi1fG%2FOS5ERW%2FFPqzFBl53BB1hixtvf; hb_MA-BFF5-63705950A31C_source=www.baidu.com; __utmz=94650624.1534594592.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __f_=1534594592655; __remember_me=true; _ga=GA1.2.2054658316.1534646886; _gid=GA1.2.1478541200.1534646886; hb_MA-8EA5-1B4E54656795_source=www.baidu.com; __root_domain_v=.163.com; _qddaz=QD.ee1uik.ezbm5p.jl094sjd; __utmc=94650624; playerid=31938229; WM_NI=YOj45eW06SO%2BHcMXJ7xltK7Bn1GeLPKGGbabRNQiq5LvlNsUHVdXNq6gS%2Bp9pgefWw2f%2Fh7I8GHLnuxn1PMrpEiAiJ%2Bh4lxrX%2Fj%2FkxzSsEP%2Fj7OtaVRZ4droy%2BK%2BJJQLTTg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee82e76296bbfd8ec24aa1959eb2aa54f5a8a9d2c8509a97a593e13ffba900a3b42af0fea7c3b92a9b91a6d5b86f95f0fab4ce218cbd83b9c93dbcb4bcacb64aaeef8986cf5c89998983e46a92929f8af43f90aaa4aff25f8c8aacb9cd7bf6b99dccf333b4b9ab87d67df2bae189b643fc9988aded7fbcb2ffb1d07ab49ba7a2ec42e9b8fc8dfb7a9cf1a6d0ea74ba8dbda6d325aae98195e45e9286fc85f165bbf585ccc94293949cb5e637e2a3; JSESSIONID-WYYY=3JRuAIFf%2FjhjFWwwKgq22Gi4Wzv8r6xj8RhsNdGDuM%2BFASyEFAYCtaxlx2%2BAYU3hObZSER6fkHzbUy8uo4xQNHJ7xqbiY43yru7B7M%5C%5CjiiIuAcJAie5CQx6HkmcTaC3qRcyu9iFfy%5Cu1lXj45TP4wqPYZKiy%2BHw26avlJgR%2B%5CGKmhPN%3A1534692022357; __utma=94650624.239093928.1534509264.1534682731.1534690425.11; MUSIC_U=b69389b0ac7fff0238198edfa56c16504ac5902dbf6f5b3d59382c8a0db313a7cbe6d5c0d97cd3bf450e6711710193c1bdacb52a57efbf6e964b527f29d7d8288ab9ad06a6e73154bf122d59fa1ed6a2; __csrf=3146cb7261a86fc331a019db794db95d; __utmb=94650624.29.10.1534690425'
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
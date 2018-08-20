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
    "Cookie":'JSESSIONID-WYYY=no6Z%2B3mtgpzNgJ0P0lJ0enE%2BDtEOjir8tQ7mZ%5CyhmQoNgYNKta9zje%2B46UiHKWK%5C80ulivMteTb%5Cfx9wNGNyZk556I%2BQ1%2Fs%5CcxlMQNBJ4md%2BFiI%2BV1rFBl8VMag1N4hipVZ%5Cml85ERo27xEsDciPhABZlWik7eFS85AVUqjaFfBOQOCc%3A1534700104425; _iuqxldmzr_=32; _ntes_nnid=d3e814a9e3f82c6655fa0bc766cd198c,1534698304445; _ntes_nuid=d3e814a9e3f82c6655fa0bc766cd198c; __utma=94650624.1943392121.1534698305.1534698305.1534698305.1; __utmc=94650624; __utmz=94650624.1534698305.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=hrH%2Bu%2B3vtOlVQnbMgo0wzL6YFlefXAYjSgVEboL4h8zsChJc%2Fahztwo5Q6qsV1bigbF41V8A9K%2BDmwmKrCJNXPR5V3C9MYOSbMJhf37V2ieuFDvQ9ge4Zlo36XCdpUOXaDk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee86c7468fbabfadea33edebe190f146ae928c85c7709b8caa9aeb418cbf86afe12af0fea7c3b92aacae88ccf821f1aabcb0ef5e93b2aeaee665f4a9b6adb55386b4ab87db4b9bb69d88d54fa2b184d5eb34baad8d89c969edbfa89bf77dadeb9fd7f47996efae8ae66a86ecffb7bb4bfb95e5a5f07daf95bea4c9469c909ed6d53981e783bace59a2938689e539f58afe8ae87f869cbab2bc6da7ec968dee39f6888d85f35f8d88afa5ea37e2a3; WM_TID=CCZ1rYrUZQYNe21sCulMzaFN%2BnKMfB2B; __utmb=94650624.3.10.1534698305'
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
                time.sleep(5)
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
                    sjc                 = json_comment['time']
                    commentNew.time     = commenttime_util.CommentTime(sjc)
                    commentNew.onpage   = nowPage                                #评论所在页面
                    commentNew.zan      = json_comment['likedCount']             #点赞数
                    commentNew.userid   = str(json_comment['user']['userId'])    #用户的id标志

                    ans = CommentAction.InsertComment(commentNew,songid)
                    if ans != 1:
                        print('进程',step,"插入评论出错")
                        time.sleep(10)
                    else:
                        show = '%s%s%s%s%s%s%s%s' % (songid,": " ,commentNew.username, "在", commentNew.time,"写道: " ,commentNew.content,"   点赞数：",commentNew.zan)
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
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



    "Cookie":'_ntes_nnid=933e5f4680466b8ed60d10177e9b0fa9,1532952113420; _ntes_nuid=933e5f4680466b8ed60d10177e9b0fa9; __f_=1533230102311; _iuqxldmzr_=32; WM_TID=BHgUuwIV1f%2BPOWKM7F9ODYqyKq4%2BL90%2B; vjuids=4e4e18181.16531ca0c29.0.ff7fc3cd7e886; vinfo_n_f_l_n3=9debe14f0d7bb8e1.1.0.1534138649849.0.1534138853063; __remember_me=true; __utmc=94650624; vjlast=1534138650.1534333889.13; __utmz=94650624.1534383389.23.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; playerid=29914519; JSESSIONID-WYYY=ocpqge7VTE%5C1QOrmW9amZ3j0qxRGBelH%2FcTGbxy5%2Fr90OgE3PNKZ5l9ITsyF%2F6%5CxfO%5CJt6VVUigokf%2FHECf4b8wKRtUx7f7KFA2dxJdMdszrWz2p2JZyw8MTeQzZwyhn22pSUteJ689c%2BT0UEc9e%2BkXQo2H2sBKqcRtvpJjcm1V2zmJU%3A1534409561526; __utma=94650624.1684817944.1533695170.1534399048.1534407762.25; WM_NI=5AukCLo4o6zhgan8iP5XIPhhh8%2B2VpCAJ1PwcbGgPWO4OPaOEu4hIDeOeth8Nxj%2BXWC3ot9xkY6LQbzLfCOf1PZE6v0j19JZzAUzM%2BVR1kBBCzldqUZksg92wZunsPn9dEI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9af55d93bea093d725af869fb1c8748a9e8799c4649a8996a8bb4e96be8889f82af0fea7c3b92af79fbb8cc248adeca1d7f964a5bfa2d9ec5cf78887b1eb64ace8e5d3d57c819f86d2d37da1be8988d35d8dec81b1e44587abfc89cc50a791ab95eb348ea8a6ccdb5d81eda195bc74a987faadd46aba94aaa4ce6ef39096a6b57ef4b6ffdac952ba9f9b9bd021968eff8cc14a81a6a485f45f9ab5bd88bc3ab586bb8ff25caee7aca6cc37e2a3; MUSIC_U=b69389b0ac7fff0238198edfa56c16504ac5902dbf6f5b3d59382c8a0db313a75e762eee8c053d37e10f8b3a03f16d42b5803f685b54568f85d8d9e1642db219418c90241b392a29bf122d59fa1ed6a2; __csrf=26867521e46cf5cb83e66da54939ec0c; __utmb=94650624.8.10.1534407762'

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
        print('进程',step,"获取评论总页面出错，错误为：",e)
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
                print('已经获取一页json,歇会')
                time.sleep(2)
            except Exception as e:
                print('进程',step,"获取第",page,"页json数据出错，错误是：",e)
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
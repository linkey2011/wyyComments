import requests

headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
   # "Cookie":'afb0b02d5e8e84986fd3c,1534691622120; _ntes_nuid=85486da3b45afb0b02d5e8e84986fd3c; __utma=94650624.1393191032.1534691622.1534691622.1534691622.1; __utmc=94650624; __utmz=94650624.1534691622.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=uqWIsQ0oCz1NwkarNHZWAgdNxT8UEf6BNcjDeaCaLjllSOVkCQZZPe4pzG%2BZ56hJrjQyeYV89ohoAxCiScS6eqOZUOFS3sN3f%2FnR6RvBq%2B19EApqb%2B%2F5FbnTh8as4y8YWHA%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d95b96bcbdaad87df5f597aeb33f8beca689c8409ab09c95f321b1b0bea3f62af0fea7c3b92ab7af99aaf25bf4b18d9bb446b5b5af93cd449a898f88e746bc8cf8b6c86ef69e8284e950a7bf8d82cf62b0b49db0d561818f96bbd36ff8b0b6a8aa52f7eaa8abf16293a7abbad534fbb1a890c47481b79d84d23ea7af81bbd845868dfd94cd39a6f1a2b3b55ab69ebfccb433879fc092e121edeb8a83ed60ace8af94b773fc8799a9c437e2a3; WM_TID=z7vbcBuk6qCbl2hzioBPRYC19eh11PBe; __utmb=94650624.4.10.1534691622; JSESSIONID-WYYY=d5PrqQmy9oUDvOdWQyebC8jEl2yt2z84jPt5Qlee47DqI5PZEh%2BW4A%2F%5C7%2BmllYmFkxbAvqkyF4pKyyqsmrsdpxTq9rN1zhGQ7R3TNmYeDqDmZISkljvXTi6pKnpIugkwYiVQNvCH4%5CpUDR1C1pc%2BtZAtDzM4TkvWiTVY22FOVXN4fav2%3A1534693763007'
}

s=requests.Session()  #创建会话，可以保持cookie
s.headers.update(headers)  #默认headers参数
pic_url = 'https://music.163.com/#/song?id=86357'


for i in range(0,10):
    response = requests.get(pic_url,headers = headers)
    c  = response.cookies.get_dict()
    s.cookies.update(response.cookies)
    print(c)

import requests
url = "https://fanyi.baidu.com"
res = requests.get(url)
print( res.cookies)
print( type(res.cookies))
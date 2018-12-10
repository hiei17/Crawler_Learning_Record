# coding=utf-8

import urllib.request
from http import cookiejar  # mark 用来保存cookie的 代替我手动复制
from urllib import parse



#  登录post的数据是这么找的: 清network记录,点登录, 看第一个post就是登录post  它的form data 就是以下这个
login_form_data = {

    # 用户名密码 是我填的
    "username": "xiaomaoera12",
    "pwd": "lina081012",

    # 这2个是隐藏域里面的带的
    "formhash": "CE3ADF28C5",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"

}

# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


def getOpenerWithCookie():

    cook_jar = cookiejar.CookieJar()
    # mark cookie 功能的 hanlder
    cook_hanlder = urllib.request.HTTPCookieProcessor(cook_jar)
    opener_with_cookie = urllib.request.build_opener(cook_hanlder)

    # encode是因为 mark post请求的 data要求是bytes
    login_str = parse.urlencode(login_form_data).encode('utf-8')
    # 带着参数 发送post请求
    login_request = urllib.request.Request('https://www.yaozh.com/login', headers=headers, data=login_str)

    # 发起请求  : 如果登录成功, cookjar自动保存cookie
    opener_with_cookie.open(login_request)

    return opener_with_cookie


def visitWithCookie( opener):

    center_url = 'https://www.yaozh.com/member/'
    center_request = urllib.request.Request(center_url, headers=headers)
    response = opener.open(center_request)

    # mark  utf-8
    data = response.read().decode("utf-8")
    with open('02cook.html', 'w', encoding="utf-8") as f:
        f.write(data)


# mark 1. 代码模拟登录 得到保存了cookie的 opener
opener = getOpenerWithCookie()


# mark 2. 用保存着cooke的opener 能进入需要登录才能进的个人中心
visitWithCookie(opener)


# 一个用户 在不同的地点(IP(福建,上海, 杭州, 河南)) 不同浏览器 上面 不停的登录 mark 非人为操作 封你的账号
#
# mark 解决: N 个 账号(不用和ip那么多 几十个就够了)

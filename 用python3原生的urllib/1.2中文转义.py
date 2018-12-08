# coding=utf-8
import urllib.request
import urllib.parse
import string


def get_method_params():

    url = "http://www.baidu.com/s?wd="

    name = "美女"
    final_url = url+name

    # UnicodeEncodeError: 'ascii' codec can't encode
    # characters in position 10-11: ordinal not in range(128)
    # python:是解释性语言;解析器只支持 ascii 0 - 127
    # 不支持中文

    # mark url的query转义
    # 网址里面包含了汉字;ascii是没有汉字的;url转译
    # 将包含汉字的网址进行转译 safe是跳过不转的
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)

    # 转义前url: http: // www.baidu.com / s?wd = 美女
    # 转义后url: http: // www.baidu.com / s?wd = % E7 % BE % 8 E % E5 % A5 % B3

    # 使用代码发送网络请求
    response = urllib.request.urlopen(encode_new_url)

    # 读取内容
    data = response.read().decode()
    print(data)

    # 保存到本地
    with open("02-encode.html","w",encoding="utf-8")as f:
        f.write(data)


get_method_params()
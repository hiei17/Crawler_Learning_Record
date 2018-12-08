# coding=utf-8
import urllib.request


def load_data():

    url = "http://www.baidu.com/"

    # response:http相应的对象 mark urllib.request 是 python3 自带了 是一切的基础
    response = urllib.request.urlopen(url)  # http请求 get的请求
    print(response)
    # 读取内容 bytes类型
    data = response.read()

    # 将字符串类型转换成bytes
    # str_name = "baidu"
    # bytes_name = str_name.encode("utf-8")
    # print(bytes_name)

    # python爬取的类型:str bytes
    # 如果爬取回来的是bytes类型:但是你写入的时候需要字符串 decode("utf-8")
    # 如果爬取过来的是str类型:但你要写入的是bytes类型 encode(""utf-8")

    # mark 百度返回的二进制(bytes) 需要转成字符串
    str_data = data.decode("utf-8")
    print(str_data)

    # mark 将数据写入文件
    # w stands for writing permission for the opened file
    with open("baidu.html", "w", encoding="utf-8")as f:

        f.write(str_data)



load_data()


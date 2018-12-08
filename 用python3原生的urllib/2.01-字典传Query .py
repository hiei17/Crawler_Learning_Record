import urllib.request
import urllib.parse
import string


def get_params():

    url = "http://www.baidu.com/s?"


    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san"

    }
    # mark  字典传参 字典自动转参数对
    str_params = urllib.parse.urlencode(params)
    print(str_params)   # wd=%E4%B8%AD%E6%96%87&key=zhang&value=san

    final_url = url + str_params
    end_url = urllib.parse.quote(final_url, safe=string.printable)  # 中文转义
    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")  # 二进制转字符串
   # print(data)


get_params()



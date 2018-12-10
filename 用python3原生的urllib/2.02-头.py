
import urllib.request


def load_baidu():

    url= "https://www.baidu.com"

    # 批量  mark 设置请求头
    header = {
        #浏览器的版本
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        # 随便什么头
         "haha":"hehe"
    }
    request = urllib.request.Request(url, headers=header)

    # 也可以这样只设一个
    # request = urllib.request.Request(url)
    # request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")

    # mark 请求网络数据 urllib.request.urlopen 就不传url了 传request
    response = urllib.request.urlopen(request)
    # 之前写的这个
    # response = urllib.request.urlopen(url)

    # print(response)

    # 响应头
    print(response.headers)

    # 请求头
    print(request.headers)

    # 完整的url
    print(request.get_full_url())

    # 指定头
    print(request.get_header("User-agent"))


load_baidu()
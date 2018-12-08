import urllib.request

def proxy_user():

    proxy_list = [



        {"https":""},
        # 免费的写法 来自http://www.xicidaili.com/ 西刺免费代理
        # {"https":"http://106.75.226.36:808"},
        # {"https":"106.75.226.36:808"},# http:// 可省略
        # {"https":"61.135.217.7:80"},
        # {"https":"125.70.13.77:8080"},
        # {"https":"118.190.95.35:9001"},
        # 付费的代理
        # "http":"xiaoming":123@115.
    ]
    for proxy in proxy_list:

        print(proxy)

        # 利用遍历出来的ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)

        # 创建opener
        opener = urllib.request.build_opener(proxy_handler)

        try:
            data = opener.open("http://www.baidu.com", timeout=1)

            haha = data.read().decode("utf-8")
            print(haha)
        except Exception as e:
            print(e)


proxy_user()

# mark  为什么不用 urlopen
# urlopen并没有添加代理的功能
# urllib.request.urlopen() # 点进去观察
# urlopen可以请求数据是因为里面的 handler处理器
# 用handler 的创造opener 才是 urlopen 最终返回的对象






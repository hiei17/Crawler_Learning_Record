import requests
from lxml import etree
import json


class BtcSpider(object):
    def __init__(self):
        self.base_url = 'http://8btc.com/forum-61-'
        self.headers = {
           "Cookie": "eCM1_5408_saltkey=rh53aKPV; eCM1_5408_lastvisit=1542615216; eCM1_5408_smile=2D1; UM_distinctid=1672b3ef6744a-064cc079dc7509-47e1039-144000-1672b3ef67516b; eCM1_5408_visitedfid=61D2D42D147D186D41D187; yd_cookie=cb4d61fc-df80-42f1a88b088312ae639a249701db97914f44; _ydclearance=348067b0f373f61ca38face9-5cad-429a-8449-7c4778ecee5f-1544892512; eCM1_5408_atarget=1; PHPSESSID=d6arrqnharnm6n1m7ipc2r3cr1; CNZZDATA5934912=cnzz_eid%3D1642669416-1542616124-http%253A%252F%252F8btc.com%252F%26ntime%3D1544883164; eCM1_5408_sid=eO5466; eCM1_5408_forum_lastvisit=D_61_1544886342; eCM1_5408_sendmail=1; _fmdata=tm5J8v6x5IsfhLn%2FJX0eqRLZvUsbF885abDrpjp7Xs5hzHOWR3SOwvVcf8c7ZjKz0w19NZMmzhe54w8%2BX2LALy%2FjZhH%2BTPn0IrDIsCIcCRg%3D; eCM1_5408_lastact=1544886374%09forum.php%09ajax; QINGCLOUDELB=357aa5de761afb88fff0143d75a28ce9df8df81e67e223b1ddcf15080c9f3df6|XBUYa|XBUWL",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

        self.data_list = []

    # 1.发请求
    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        # 网页的 编码到底 是 gbk 还是 urf-8  head--meta-charset=""
        # <meta http-equiv="Content-Type" content="text/html; charset=gb2312">
        data = response.content.decode('gbk')
       # data = response.content

        # with open('05btc.html', 'w') as f:
        #     f.write(data)
        return data

    # 2.解析数据
    def parse_data(self, data):
        # 使用xpath 解析当前页面 所有的 新闻title 和url 保存
        # 1.转类型
        x_data = etree.HTML(data)

        # 2.根据xpath路径解析
        # 路径 mark 观察发现 有个独特的class
        #title_list = x_data.xpath('//a[@class="s xst"]/text()')
        title_list = x_data.xpath('/html[1]/body[1]/div[6]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/form[1]/div/div[2]/div[1]/a[2]/text()')
        #title_list = x_data.xpath('//div[contain(@id,"normalthread_")]/div[2]/div/a[1]/text()')

        # title_list = x_data.xpath('//form[@id="moderate"]/div/div[2]/div/a[@class="s xst"]/text()')
        url_list = x_data.xpath('//a[@class="s xst"]/@href')

        # mark 处理数据格式
        for index, title in enumerate(title_list):
            news = {}
            # print(index)
            # print(title)
            news['name'] = title
            news['url'] = url_list[index]
            self.data_list.append(news)

    # 3.保存数据
    def save_data(self):

        # 将 list---str
        data_str = json.dumps(self.data_list)
        # 这样出来看到\u5f88 这样是正常的 去https://www.bejson.com/ 校验 就能看到中文了
        with open('05btc.json', 'w',encoding='gbk') as f:
            f.write(data_str)

    # 4.启动
    def run(self):

        for i in range(1, 5):
            # 1.拼接 完整url
            url = self.base_url + str(i) + '.html'
            print(url)
            # 2.发请求
            data = self.get_response(url)

            # 3.做解析
            self.parse_data(data)
        # 4.保存
        self.save_data()


BtcSpider().run()

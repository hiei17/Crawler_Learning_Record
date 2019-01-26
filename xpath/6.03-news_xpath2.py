import re
import requests

# 安装支持 解析html和XML的解析库 lxml
# pip install lxml
from lxml import etree

url = 'http://news.baidu.com/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

data = requests.get(url, headers=headers).content.decode()


# 1.转解析类型
xpath_data = etree.HTML(data)


# xpath 语法 1. 节点 /
#            2. 跨节点不从根找: //
#            3. 精确的标签: //a[@属性="属性值"]   尽量用id
#            4. 标签包裹的内容 text()
#            5. 属性:@href
#              xpath--s数据类型---list
# 2调用 xpath的方法


'''
<html>
    <head>
        <title>百度新闻——全球最大的中文新闻平台</title>'''

# result = xpath_data.xpath('/html/head/title//text()')


# result = xpath_data.xpath('//a/text()')

# @ 按属相选择
# result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/text()')
# result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/@href')  # 返回网址

# 所有 <li>包<a>的里面内容
# result = xpath_data.xpath('//li/a/text()')
# result = xpath_data.xpath('//li[3]/a/text()')

result = xpath_data.xpath('//li/text()') # ['\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n 这样取到的是直接文字

print(result)  # 数组

# with open('02news.html', 'w') as f:
#     f.write(data)

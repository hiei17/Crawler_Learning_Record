
# 1.记得安装 第三方 模块 requests
# pip install requests

import requests

url = 'http://www.baidu.com'
response = requests.get(url)

# content属性 返回的类型 是bytes
data = response.content.decode('utf-8')

# mark text 属性 返回的类型 是文本str 编码方式靠拆
data2 = response.text

print(type(data))
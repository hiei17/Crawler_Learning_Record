# https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3&rsv_spt=1&rsv_iqid=0xefb8b43600013949&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E5%25A4%25B4%25E6%259D%25A1&rsv_t=6e3aSjYtw0WgEg7MAIuUlOc3D5lwFBJUVw3KsdkhkWYhZWcNMn9kLBO12GflHlOeUHxx&inputT=506&rsv_pq=81d8f9470001b348&rsv_sug3=19&rsv_sug1=16&rsv_sug7=100&bs=%E5%A4%B4%E6%9D%A1

import requests


# 这个 网址 返回的内容不是html 而是标准的json
url = 'https://api.github.com/user'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


response = requests.get(url, headers=headers)

# 不用自己这样转json了
# str
# data = response.content.decode()
# # str-- dict
# data_dict = json.loads(data)


# json() mark 自动将json字符串 转换成字典或者列表
data = response.json()

print(data['message'])

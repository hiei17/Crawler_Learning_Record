import requests
from lxml import etree
# 请求数据url
member_url = 'https://www.yaozh.com/member/'

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
#  cookies 的字符串
cookies = '_ga=GA1.2.572074981.1548035826; GCID=e1600c5-55ea002-9d5f5e2-4341937; _gid=GA1.2.890858080.1548512312; GCESS=BAwBAQsCBAAJAQEGBJSGwIQEBIBRAQACBFdsTFwHBMJ31acBBDO1EAADBFdsTFwKBAAAAAAFBAAAAAAIAQM-; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1548036113,1548039490,1548041776,1548512356; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1548512356; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1548512500|1548512355'


def cookie_str2dict(cookies):


    # 字典推导式
    cook_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split('; ')}

    # 和上面那句 一个意思
    # cookies_list = cookies.split('; ')
    # for cookie in cookies_list:
    #     cook_dict[cookie.split('=')[0]] = cookie.split('=')[1]

    return cook_dict


# 可以点进去看 cookies 需要字典
response = requests.get(member_url, headers=headers, cookies=cookie_str2dict(cookies))

data = response.content.decode()
xpath_data = etree.HTML(data)
result = xpath_data.xpath('//li/text()')
with open('05-cookie.html','w') as f:
    f.write(data)


    #https://time.geekbang.org/column/article/79026
    #https://time.geekbang.org/column/article/78658

    # / html[1] / body[1] / div[2] / div[1] / div[2] / div[3] / div[1] / div[*] / div[1] / div[2] / a[1]
    # < a
    # href = "/column/article/78658"
    #
    #
    # class ="article-item-more-text" data-gk-spider-link="/column/article/78658" style="" xpath="2" > 阅读全文 < / a >
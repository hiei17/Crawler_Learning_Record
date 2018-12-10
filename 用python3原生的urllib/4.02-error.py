
# urlib.request  提示错误 HTTPError UrlError

"""
     raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
    
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found

"""

import urllib.request

# 2, HTTPError 404
url = 'https://blog.csdn.net/zjsxxzh/article/details/110'

# 1. 根本没这个域名 URLError
# url = 'https://affdsfsfsdfd.cn'

try:
    response = urllib.request.urlopen(url)

except urllib.request.HTTPError as error:
    print(error.code)
    if "404" == error.code:
        print("找不到网页")


except urllib.request.URLError as error:
    print(error)



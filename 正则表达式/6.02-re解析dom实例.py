import re


data=r'<a href="http://baijiahao.baidu.com/s?id=1619718634123862050" title="张小龙的孤独，张一鸣的寂寞" target="_blank" mon="&amp;a=12" class="img" style="background-image:url(http://hiphotos.baidu.com/news/crop%3D53%2C0%2C551%2C370%3Bq%3D80%3B/sign=c27b979d7ef0820239ddcb7f76cec8c1/71cf3bc79f3df8dcbe30fc2fc011728b4710287a.jpg)"></a>'


# 正则解析 数据
#  每个新闻的titile, url



# *? 不贪婪 有个匹配就返回了
pattern = re.compile('<a href="(.*?)" target="_blank" mon="(.*?)">(.*?)</a>',re.S)
# re.S 让. 可以匹配换行

result = pattern.findall(data)

print(result[0])



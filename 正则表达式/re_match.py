import re

# mark 必须匹配最开始 比如匹配com 或者没有这里结果都是none
m = re.match('www', 'www.santostang.com')
print("匹配的结果:  ", m)
# 结果如果是none 下面会报错
print("匹配的起始与终点:  ", m.span())
print("匹配的起始位置:  ", m.start())
print("匹配的终点位置:  ", m.end())

#

# line = "Fat cats are smarter than dogs, is it right?"
# m = re.match( r'(.*) are (.*?) dogs', line)
# print ('匹配的整句话', m.group(0))
# print ('匹配的第一个结果', m.group(1))
# print ('匹配的第二个结果', m.group(2))
# print ('匹配的结果列表', m.groups())


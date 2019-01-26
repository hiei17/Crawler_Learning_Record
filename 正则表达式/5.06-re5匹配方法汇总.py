import re

one = 'abc 123'
patter = re.compile('\d+')
# match 从头匹配 匹配一次
result = patter.match(one)

# search 从任意位置 , 匹配一次
result = patter.search(one)

# mark  常用! findall  查找  符合正则的 内容 -- list
result = patter.findall(one)

# mark  常用! sub  替换  字符串
result = patter.sub('#',one)

# mark  常用! split  拆分
patter = re.compile(' ')
result = patter.split(one)





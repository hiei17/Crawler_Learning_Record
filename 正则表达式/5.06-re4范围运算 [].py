import re


# 被匹配字符串
one = '7893452'

# 匹配模式
pattern = re.compile('[1-9]')

# 找出所有匹配的 组成数组
result = pattern.findall(one)

# ['7', '8', '9', '3', '4', '5', '2']

print(result)

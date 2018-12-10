import re


# 范围运算 [123] [1-9]
one = '7893452'

pattern = re.compile('[1-9]')

result = pattern.findall(one)

# ['7', '8', '9', '3', '4', '5', '2']

print(result)

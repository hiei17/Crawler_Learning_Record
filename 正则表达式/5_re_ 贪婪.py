import re
one = 'mdfsdsfffdsn12345656n'

# mark . 是任意(除换行符)字符
# # pattern = re.compile('m(.)n') # [] 没有 m某字母n  这样三连一起的
# # pattern = re.compile('m(.)f')  # ['d']

# mark * 代表匹配前面那个0到多次
# pattern = re.compile('m(.*)n') # ['dfsdsfffdsn12345656']mark 默认贪婪 取后面那个n

# mark ? 表示 最多一次
# + 代表至少一次
# mark () 是分组
pattern = re.compile('m(.*?)n') # ['dfsdsfffds'] mark *? 不贪婪 有个匹配就返回了


result = pattern.findall(one) # findall 是返回列表
print(result)
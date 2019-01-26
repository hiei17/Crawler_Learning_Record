import re

one = '234'

# 匹配一个数字
#pattern = re.compile('\d')  # 2

# 纯数字的正则 \d 0-9之间的一个数 mark +  是至少一个
pattern = re.compile('^\d+$') # 234 mark 数字开头 数字结尾 至少一个数字

# 匹配判断的方法
# match 方法 是否匹配成功 从头开始 匹配一次
result = pattern.match(one)


print(result.group()) #  .group 拿出结果


import re


one = """
    msfdsdffdsdfsn
    1234567778888nN
"""

pattern = re.compile('m(.*)n') #  mark . 除了 换行符号\n 之外的 匹配
# ['sfdsdffdsdfs']


#  mark  re.S: make . match 换行符号\n
# pattern = re.compile('m(.*)n', re.S)
# ['sfdsdffdsdfsn\n    1234567778888']

# mark  re.I:忽略大小写   默认贪婪 会尽量长
# pattern = re.compile('m(.*)n', re.S | re.I)
# ['sfdsdffdsdfsn\n    1234567778888n']

result = pattern.findall(one)
print(result)

import re

# 匹配中文
two = '<a href="https://www.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/s?ie=utf-8&amp;fr=bks0000&amp;wd=">网页是最新版本的,适配移动端</a>'

# mark  python中 匹配中问 [a-z] unicode的范围
#  *  任意次
#  +  最少一次
#  ? 最多1次
# 这里是意思是 匹配连续的中文
pattern = re.compile('[\u4e00-\u9fa5]+')


result = pattern.findall(two)
print(result)
# ['网页是最新版本的', '适配移动端']
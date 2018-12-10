# 爬维基相关词 深搜 单线程
import requests
import re
import time

time1 = time.time()
exist_url = []  # 记录已经爬过的
g_write_count = 0


def scrappy(current_word, depth=1):

    # 全局变量要写 必须这样global
    global g_write_count

    print(current_word)

    try:
        headers = \
            {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
            }

        r = requests.get("https://en.wikipedia.org/wiki/" + current_word, headers=headers)
        html = r.text
    except Exception as e:
        print('Failed downloading and saving', current_word)
        print(e)
        exist_url.append(current_word)
        return None

    # 记录已经爬过的url
    exist_url.append(current_word)
    link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)  # 本页面的维基url
    unique_list = list(set(link_list) - set(exist_url))  # 没爬过的

    for wordInThisPage in unique_list:

        g_writecount += 1
        output = "No." + str(g_writecount) + "\t Depth:" + str(depth) + "\t" + current_word + ' -> ' + wordInThisPage + '\n'
        # 输出到 文件link_12-3.txt
        with open('link_12-3.txt', "a+") as f:
            f.write(output)
            f.close()

        if depth < 2:
            scrappy(wordInThisPage, depth + 1)


scrappy("Wikipedia")
time2 = time.time()
print ("Total time", time2 - time1)
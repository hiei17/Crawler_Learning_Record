# 爬维基相关词 广搜 多线程
# coding=utf-8
import threading
import requests
import re

# 作为锁
g_mutex = threading.Condition()


g_queue_word = []  # 下一层 等待爬取的word(它自己已经记入文件, 它相关的词汇还没记入
g_existWord = []  # 这里面的词, 它关联的词都已经记入文件了

g_write_count = 0  # 已记入的词条数


class Crawler:

    def __init__(self, word, threadnum):

        self.word = word
        self.thread_num = threadnum
        self.thread_pool = []

    def craw(self):

        g_queue_word.append(word)

        depth = 1

        while depth < 3:
            print('Searching depth ', depth, ' ...\n')
            self.download_all() # 这层全部爬完 并更新好下一层待爬词
            depth += 1

    # 把本层的词 用多线程爬完
    def download_all(self):

        global g_queue_word  # 待爬的词条
        had_craw_count = 0  # 已爬记录

        # 循环 直到这层的待爬词 都爬了
        while had_craw_count < len(g_queue_word):

            # 增加的线程到线程池允许的数量 或  词条需要的数量
            start_thread = 0
            while start_thread < self.thread_num and had_craw_count + start_thread < len(g_queue_word):
                self.download(g_queue_word[had_craw_count + start_thread], start_thread)
                start_thread += 1

            # 线程池里面的线程 运行完
            for thread in self.thread_pool:
                thread.join(30)

            had_craw_count += start_thread

        g_queue_word = []

    # 调用多线程爬虫
    def download(self, url, tid):

        craw_thread = CrawlerThread(url, tid)

        self.thread_pool.append(craw_thread)
        craw_thread.start()


class CrawlerThread(threading.Thread):  # 爬虫线程

    def __init__(self, word, tid):

        threading.Thread.__init__(self)
        self.word = word
        self.tid = tid

    # 把 word 页面里面出现的词条 写入文件, 已经写过的词记录一下g_existWord  页面本身 记入g_pages(下一个以此出发)
    def run(self):

        global g_mutex
        global g_write_count
        global g_queue_word

        write_file_words = []
        try:
            print(self.tid, "crawl ", self.word)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            r = requests.get("https://en.wikipedia.org/wiki/" + self.word, headers=headers)
            html = r.text

            link_list2 = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
            unique_list2 = list(set(link_list2))

            for eachone in unique_list2:
                g_write_count += 1
                content2 = "No." + str(g_write_count) + "\t Thread" + str(
                    self.tid) + "\t" + self.word + '->' + eachone + '\n'
                with open('title2.txt', "a+") as f:
                    f.write(content2)
                    f.close()
                write_file_words.append(eachone)

        except Exception as e:

            print('Failed downloading and saving', self.word)
            print(e)
            return None

        # 原子操作
        g_mutex.acquire()
        g_queue_word = list(set(g_queue_word + write_file_words))
        g_existWord.append(self.word)
        g_mutex.release()


if __name__ == "__main__":
    word = "Wikipedia"
    thread_num = 5
    crawler = Crawler(word, thread_num)
    crawler.craw()  # 开爬

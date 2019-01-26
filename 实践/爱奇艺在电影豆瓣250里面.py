from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# todo 拿到豆瓣前250 片名 存list
def get_movies():

    # 浏览器复制下来的头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }

    movie_list = []

    for i in range(0, 10):  # 一共10页

        link = 'https://movie.douban.com/top250?start=' + str(i * 25)

        r = requests.get(link, headers=headers, timeout=10)
        print("豆瓣"+str(i + 1), "页响应状态码:", r.status_code)

        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')

        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

    return movie_list

# 到爱奇艺比对
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe') # 火狐浏览器地址


# 属性
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.stylesheet", 2)  # 限制css
fp.set_preference("permissions.default.image", 2)  # 限制图片
fp.set_preference("javascript.enabled", False)  # 禁止js
# 浏览器 无界面
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps,firefox_options=fireFoxOptions)
movies = get_movies()

# todo for i in range(1,30):
for i in range(1,30):

    aqy = "https://list.iqiyi.com/www/1/-------------11-"+str(i)+"-1-iqiyi--.html"
    driver.get(aqy)  # 打开网页
    time.sleep(3)  # 等一下 等页面加载好
    tagAs = driver.find_elements_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[*]/div[2]/div[1]/p[1]/a[1]")
    for a in tagAs:
        movie_name = a.text
        if movie_name in movies:
            href = a.get_attribute("href")
            print(movie_name+" "+href)








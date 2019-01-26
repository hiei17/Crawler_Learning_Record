from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


def getProxyUrls():
    url = "https://www.xicidaili.com/wt/"

    caps = webdriver.DesiredCapabilities().FIREFOX
    caps["marionette"] = True
    binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')  # 火狐浏览器地址
    # 属性
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.stylesheet", 2)  # 限制css
    fp.set_preference("permissions.default.image", 2)  # 限制图片
    fp.set_preference("javascript.enabled", False)  # 禁止js
    # 浏览器 无界面
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps,firefox_options=fireFoxOptions)
    driver.get(url)  # 打开网页
    time.sleep(3)  # 等一下 等页面加载好
    tds = driver.find_elements_by_xpath('/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[*]/td[2]')
    proxys = []
    for td in tds:
        proxys.append(td.text)

    driver.close()
    return proxys


# urls = getProxyUrls()
# print(urls)
import xicidaili
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fake_useragent import UserAgent

ua = UserAgent()

def getFireFoxProxyDriver():
    user_agent_list = xicidaili.getProxyUrls()
    myProxy = random.choice(user_agent_list)
    print(myProxy)
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy': ''  # set this value as desired
    })

    caps = webdriver.DesiredCapabilities().FIREFOX
    caps["marionette"] = True
    binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')  # 火狐浏览器地址
    # 属性
    fp = webdriver.FirefoxProfile()

    ua_random = ua.random
    print(ua_random)
    fp.set_preference('general.useragent.override', ua_random)
    fp.set_preference("permissions.default.stylesheet", 2)  # 限制css
    fp.set_preference("permissions.default.image", 2)  # 限制图片
    fp.set_preference("javascript.enabled", False)  # 禁止js
    # 浏览器 无界面
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps,
                               firefox_options=fireFoxOptions, proxy=proxy)

    return driver






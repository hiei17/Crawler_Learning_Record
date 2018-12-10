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

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)

driver.get("http://www.santostang.com/2018/07/04/hello-world/")  # 打开网页



time.sleep(3)  # 等一下 等页面加载好

# 找到元素
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)




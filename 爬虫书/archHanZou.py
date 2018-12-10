# 爬杭州airbnb
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

#用 selenium 的 driver 来启动 firefox
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)




for i in range(0,5):
    # 在虚拟浏览器中打开 Airbnb 页面
    link = "https://zh.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&query=%E4%B8%AD%E5%9B%BD%E6%B5%99%E6%B1%9F%E7%9C%81%E6%9D%AD%E5%B7%9E%E5%B8%82%E8%A5%BF%E6%B9%96%E5%8C%BA&allow_override%5B%5D=&s_tag=i-5oFEbfamp%3Bitems_offset%3D18&section_offset=6&items_offset=" + str(i * 18)
    print(link)

    driver.get(link)

    #找到页面中所有的出租房
    rent_list = driver.find_elements_by_css_selector('div._14csrlku')

    #对于每一个出租房
    for eachhouse in rent_list:

        #找到评论数量
        try:
            comment = eachhouse.find_element_by_css_selector('span._1cy09umr')
            comment = comment.text
        except:
            comment = 0

        #找到价格
        price = eachhouse.find_element_by_css_selector('span._1sfeueqe')
        price = price.text[4:]

        #找到名称
        name = eachhouse.find_element_by_css_selector('div._190019zr')
        name = name.text

        #找到房屋类型，大小
        details = eachhouse.find_elements_by_css_selector('small._f7heglr  span')
        details = details[0].text # 注意这里不包括html
        house_type = details.split(" · ")[0]
        bed_number = details.split(" · ")[1]
        print (comment, price, name, house_type, bed_number)


    time.sleep(5)
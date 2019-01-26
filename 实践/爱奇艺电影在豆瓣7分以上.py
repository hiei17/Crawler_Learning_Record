

import time

import Firefox_proxy

driver=Firefox_proxy.getFireFoxProxyDriver()

def is_good_movie(movie_name):


    db_search_url = "https://movie.douban.com/subject_search?search_text=" + movie_name
    driver.get(db_search_url)  # 打开网页
    time.sleep(1)  # 等一下 等页面加载好
    try:
        span = driver.find_element_by_xpath(
            '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]')
        text = span.text
        score = float(text)
        print(movie_name + "分数:" + str(score))
        return score > 7
    except Exception as a:
        print(a)


    return False



# good_movie = is_good_movie("毒液")
# print(good_movie)



def getMovie():

    result=[]
    global driver

    for i in range(1, 2):

        aqy = "https://list.iqiyi.com/www/1/-------------11-" + str(i) + "-1-iqiyi--.html"

        driver.get(aqy)  # 打开网页
        time.sleep(3)  # 等一下 等页面加载好
        tagAs = driver.find_elements_by_xpath(
            "/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[*]/div[2]/div[1]/p[1]/a[1]")

        movie_link = {}
        for a in tagAs:
            movie_name = a.text.strip()
            href = a.get_attribute("href")
            movie_link[movie_name] = href
            print("加入电影 : "+movie_name+href)
        for key in movie_link:
            if is_good_movie(key):
                values = key + " " + movie_link[key]
                print(values)
                result.append(values)

        driver.close()
        driver=Firefox_proxy.getFireFoxProxyDriver()
    return result


result = getMovie()
with open('7score.html','w',encoding="utf-8") as f:
    f.write(str(result))











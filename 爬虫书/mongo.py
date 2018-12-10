import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.blog_database  # mark 使用数据库"blog_database"  如果么有 会创一个
collection = db.blog  # mark 使用集合"blog" 如果么有 会创一个

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r = requests.get(link, headers = headers)

soup = BeautifulSoup(r.text, "lxml")
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    post = {"url": url,
         "title": title,
         "date": datetime.datetime.utcnow()}
    # mark 把一个文档存到集合
    collection.insert_one(post)
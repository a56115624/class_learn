# # 1.抓取PTT電影版的網頁原始碼(HTML)
# import urllib.request as req

# from aiohttp import request
# url = "https://www.ptt.cc/bbs/movie/index9504.html"
# request = req.Request(url,headers={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
#    "cookie": "_ga=GA1.2.21740160.1556005023; __cf_bm=d7OX1.98tBnGT8opQkYHQ2l3y7JnwvqTgnjQSm.MfNA-1642727118-0-AXME8RmvNBIcU7NUTUA+k4LYNKl8VHPzOS8s8i6LFceG2cdSA0ZNEG6f+TcAQRLBGt/nTqJWSbABuRNpNOWb/vo=; _gid=GA1.2.2125954237.1642727117"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
# # print(data)
# # 解析原始碼,取得文章的標題
# import bs4
# root = bs4.BeautifulSoup(data,"html.parser")
# titles = root.find_all("div", calss_="title")
# print(titles)
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

r1 = requests.get("https://www.ptt.cc/bbs/movie/index9504.html",
      headers = {
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "cookie": "_ga=GA1.2.21740160.1556005023; __cf_bm=d7OX1.98tBnGT8opQkYHQ2l3y7JnwvqTgnjQSm.MfNA-1642727118-0-AXME8RmvNBIcU7NUTUA+k4LYNKl8VHPzOS8s8i6LFceG2cdSA0ZNEG6f+TcAQRLBGt/nTqJWSbABuRNpNOWb/vo=; _gid=GA1.2.2125954237.1642727117"
  })
soup = BeautifulSoup(r1.text,'html.parser')
title = soup.find_all("div",{"class" : "title"})
for i in title:
  if i.a !=None:
    print(i.a.string) 


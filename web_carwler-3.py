# AJAX / XHR 網站技術分析
import requests
from bs4 import BeautifulSoup

r1 = requests.get(" https://medium.com/_/graphql",
      headers = {
   "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "cookie": "_ga=GA1.2.893395660.1567675204; _parsely_visitor={%22id%22:%22pid=9f2ecfc9c1c82cbfb917d42260de2eb5%22%2C%22session_count%22:1%2C%22last_session_ts%22:1615332098010}; nonce=Y1WWw96L; uid=1689c14204c7; sid=1:Z8n7MoMdB8N94pEHnilXtMrZ0XZFIYIWtFu+aCflxdSvZXE4SjuaP0mKA9MIq+1H; optimizelyEndUserId=1689c14204c7; __cfruid=a57e07d4f402d871c1b74df7e680f5b9247c1bc5-1642740349; _gid=GA1.2.1979384821.1642740352; xsrf=faba22e0d344; dd_cookie_test_4bbd7e72-50bf-4530-9a60-302bdaca1b80=test; _dd_s=rum=0&expire=1642749484578"
  })

# 解析 json格式的資料,取得每篇文章的標題
import json
data = json.loads(r1)
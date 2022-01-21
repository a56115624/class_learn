import requests
from bs4 import BeautifulSoup
def getData(url):
    r1 = requests.get(f"{url}",
        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "cookie":"_ga=GA1.2.21740160.1556005023; _gid=GA1.2.2125954237.1642727117; __cf_bm=fG2nYgeoEtGv6LsUIR56eYTc1uiG9SmWnO4OIrKagso-1642734315-0-AR0KPwyCGJmc4jnyNMMb1wqBbNdBW/vpJEjMB2+EHIhFpV8SS+gGJxXatG7mfejjEbiM1c9zu+3gMAoXtCCmCrc=; over18=1"
    })
    soup = BeautifulSoup(r1.text,"html.parser")
    title = soup.find_all("div",{"class":"title"})
    for i in title:
            print(i.a.string)
    nextlink = soup.find("a",string = "‹ 上頁")
    return nextlink["href"]

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
i  = getData(url)

# count = 0
# while count<3:
#     url = "https://www.ppt.cc"+getData(url)
#     count=count+1

from sys import modules
import urllib.request as req
import bs4
from googletrans import Translator
# from color import colorprint

def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("h2",class_="post__title")

    for title in titles:
        modtitle=(title.string.replace("\n", ""))
        print(modtitle)
   

#爬取模組頁數
count = 300



getData("https://mcpedl.com/category/mods/")
for i in range(count-1):
    getData("https://mcpedl.com/category/mods/page/"+ str(i+2) + "/")
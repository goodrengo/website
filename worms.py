import urllib.request as req

def data(url):
    #抓原始碼
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #解析原始碼
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    title = root.find_all("h1",class_="GN-lbox2D")

    for titles in title:
         if titles.a !=None:
            print(titles.a.string)
year=input("輸入想要查詢的年份(2004~2022)")
month=input("輸入想要查詢的月份(1~12)")
url="https://gnn.gamer.com.tw/?yy="+year+"&mm="+month
print(data(url))
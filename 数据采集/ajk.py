import time
from bs4 import BeautifulSoup
import requests
import pymysql

#########################################
#            安居客爬虫代码             #
#                                       #
#########################################

class ajk():

    def __init__(self):

        self.conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       passwd="00000",
                       db="51job",
                       charset="utf8")
        self.cur = self.conn.cursor()
        self.company = []
        self.text = ""
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2924.87 Safari/537.36'
        }


    #爬取各个城市的链接
    def link(self):
        url = "https://www.anjuke.com/sy-city.html"
        page = requests.get(url, headers=self.headers).content.decode('utf8')
        bs = BeautifulSoup(page, 'lxml').find("div", class_="letter_city").find_all("a")
        for b in bs:
            cityname= b.contents[0]
            cityurl=b['href']+"/market/"
            cityroomprice= self.getprice(cityurl)
            print(cityname,cityroomprice)
            self.insertDb(cityname,cityroomprice)


    #获取一个城市的房价
    def getprice(self,url):
        page = requests.get(url, headers=self.headers).content.decode('utf8')
        bs = BeautifulSoup(page, 'lxml').find("div", class_="trendR").find("em")
        return bs.contents[0]


    #将数据插入数据
    def insertDb(self,cityname,price):
        sql = "insert into roomprice(cityname, price) values ( '"+cityname+"',"+str(price)+"  )  "
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("error:", e)





if __name__ == "__main__":
    aj=ajk()
    aj.link()
    aj.getprice("https://yancheng.anjuke.com/market/")


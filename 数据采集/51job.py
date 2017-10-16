import time
from bs4 import BeautifulSoup
import requests
import pymysql


#################################################
#             51job网站爬虫代码                 #
#                                               #
#################################################

class JobSpider():
    def __init__(self):
        self.datanum = 0
        self.conn = pymysql.connect(host="localhost",
                                    port=3306,
                                    user="root",
                                    passwd="0000000",
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

    def job_spider(self):
        for lo in range(1, 33):
            loid = str(lo)
            if len(loid) == 1:
                loid = '0' + loid;
            """ 爬虫入口  python """
            url = "http://search.51job.com/list/" + loid + "0000,000000,0000,00,9,99,%2B,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
            urls = [url.format(p) for p in range(1, 2000)]
            num = 1;
            print("当前地区编号：", loid)

            for url in urls:
                time.sleep(3)
                #print("当前第", num, "页")
                num += 1
                # print("当前网址",url)
                # print("获取网页数据.....")
                try:
                    page=requests.get(url, headers=self.headers).content
                    r = page.decode('gbk')
                except Exception as e:
                    print(e)
                    print(page)

                # print("获取网页数据成功，解析中......")
                bs = BeautifulSoup(r, 'lxml').find("div", class_="dw_table").find_all("div", class_="el")

                if len(list(bs)) == 1:
                    print("抓取页数：",num)
                    break;
                for b in bs:
                    try:
                        href, post = b.find('a')['href'], b.find('a')['title']
                        locate = b.find('span', class_='t3').text
                        salary = b.find('span', class_='t4').text
                        d = {'href': href, 'post': post, 'locate': locate, 'salary': salary}
                        salary_num_arg = salary[:-3]
                        args = salary_num_arg.split('-');
                        if len(args) == 2:
                            salary_min = float(args[0])
                            salary_max = float(args[1])
                            if salary.index("千/月"):
                                salary_max *= 1000;
                                salary_min *= 1000;
                            elif salary.index("万/月"):
                                salary_max *= 10000;
                                salary_min *= 10000;
                            elif salary.index("万/年"):
                                salary_max *= 10000 / 12;
                                salary_min *= 10000 / 12;
                        if salary_max>1000 and salary_min>500 :
                            self.insert_into_db(post, locate, salary_max, salary_min, "all", href, lo, num - 1)
                    except Exception:
                        pass

    # 将一条数据插入数据库
    def insert_into_db(self, post, locate, salary_max, salary_min, types, href, locat_num, page):
        self.datanum += 1
        sql = "insert into jobinfo(post, locate, salary_max,salary_min,type,href,locat_num,page) values('" + post + "', '" + locate + "'," + str(
            salary_max) + " ," + str(salary_min) + ",'" + types + "',' " + href + "  '  ," + str(
            locat_num) + " ," + str(page) + "   )"
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            #print("error:", e)
            pass


if __name__ == "__main__":
    spider = JobSpider()
    for i in range(99):
        print("主循环，第",i,"次")
        spider.job_spider()

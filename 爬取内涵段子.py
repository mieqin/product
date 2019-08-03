import urllib.request
import re


class NeihanSpider:
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/njjzw/"
        self.headers = {"user-Agent":"Mozilla/5.0"}
        self.page = 1

    def loadPage(self,url):
        req = urllib.request.Request(self.baseurl,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)

    def parsePage(self,html):
        p = re.compile('<div class="text-.*?title="(.*?)".*?<div class="desc">(.*?)</div>',re.S)
        r_list = p.findall(html)
        self.writerPage(r_list)

    def writerPage(self,r_list):
        for r_tuple in r_list:
            for r_str in r_tuple:
                with open('急转弯.txt','a',encoding='gb18030') as f:
                    f.write(r_str.strip() + '\n')
            with open('急转弯.txt','a',encoding='gb18030') as f:
                f.write('\n')

    def workOn(self):
        self.loadPage(self.baseurl)
        while True:
            c = input('成功，是否继续(y/n)：')
            if c.strip().lower() == 'y':
                self.page += 1
                url = self.baseurl + 'index_' + str(self.page) + '.html'
                self.loadPage(url)
            else:
                print('爬取结束，谢谢使用')
                break

if __name__ == "__main__":
    spider = NeihanSpider()
    spider.workOn()

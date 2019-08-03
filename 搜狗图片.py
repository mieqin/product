# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import re
import time

url = "https://pic.sogou.com/pics?"
headers = {"user-Agent":"Mozilla/5.0"}
proxies = {"http":"http://221.206.100.133:54781"}
key = input("请输入要搜索的图片：")
s = input("要下载的图片数量（48的倍数）：")
params = {"query":key,
          "mode": 1,
          "start": s,
          "reqType": "ajax",
          "reqFrom":" result",
          "tn": 0}

res = requests.get(url,params=params,proxies=proxies,headers=headers)

html = res.text


p = re.compile('"pic_url":"(.*?)"')
r_list = p.findall(html)

for t_list in r_list:
    res = requests.get(t_list,headers=headers)
    res.encoding = 'utf-8'
    html = res.content
    filename = t_list[-9:-4] + '.jpg'
    with open(filename,'wb') as f:
        f.write(html)
        time.sleep(2)

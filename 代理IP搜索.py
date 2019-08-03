# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:00:55 2019

@author: liu
"""
import requests
import time
import re

baseurl = "https://www.kuaidaili.com/free/inha/"
headers = {"User-Agent":"Mozilla/5.0"}
Q = []

for index in range(1,3000):
    try:
        url = baseurl + str(index) + '/'
    #    print(url)
        res = requests.get(url,headers=headers)
        html = res.text
        p = re.compile('<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>',re.S)
        r_lists = p.findall(html)
        for r_list in r_lists:
            r_list = ':'.join(r_list)
            Q.append(r_list)
        time.sleep(5)
    except:
        pass
    
print(len(Q))
    
    
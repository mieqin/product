# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:09:08 2019

@author: liu
"""

import requests
import re
import time

url = "https://image.baidu.com/search/index?tn=baiduimage&"
headers = {"user-Agent":"Mozilla/5.0"}
proxies = {"http":"http://47.100.21.174:8021"}
key = input("请输入要搜索的内容：")
params = {
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': key,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': key,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': 30,
                      'rn': 30,
                      'gsm': '1e',
                      '1526377465547': ''
                      }

res = requests.get(url,params=params,proxies=proxies,headers=headers)
html = res.text

p = re.compile('"objURL":"(.*?)"',re.S)
r_list = p.findall(html)

index = 1
for r_str in r_list:
    name = str(index)
    filename = name + '.jpg'
    res = requests.get(r_str,headers=headers)
    html = res.content
    with open(filename,'wb') as f:
        f.write(html)
        time.sleep(5)
    index += 1

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:00:40 2019

@author: liu
"""

from selenium import webdriver
import time

url = "https://kyfw.12306.cn/otn/resources/login.html"
driver = webdriver.PhantomJS()
driver.get(url)

su = driver.find_element_by_class_name("login-hd-account")
#print(su)
su.click()
time.sleep(1)

new_user = driver.find_elements_by_class_name("input")[0]
new_user.send_keys("1234567")

new_password = driver.find_elements_by_class_name("input")[1]
new_password.send_keys("1234567")

driver.save_screenshot('12306.jpg')
driver.quit()
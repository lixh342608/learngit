#coding=utf-8
'''
Created on 2016年6月21日

@author: admin
'''

from selenium import webdriver
from time import sleep

driver = webdriver.Ie()
url_1='http://www.baidu.com'
url_2='http://news.baidu.com'
#打开第一个页面
driver.get(url_1)
sleep(5)
print driver.title# 把页面title 打印出来

#打开第二个页面
driver.get(url_2)
sleep(5)
print driver.title

#返回第一个页面（百度首页）
driver.back()
sleep(5)
print driver.title

#再次进入第二个页面（新闻页面）
driver.forward()
sleep(5)
print driver.title

sleep(10)
print("准备退出！")
driver.quit()
    
    
#if __name__=="__main__":
    #func(1,2,3,4,5,6,["a","b","c","d"])
    #func(1,2)
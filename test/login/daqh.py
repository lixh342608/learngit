#coding=utf-8
'''
Created on 2015-12-17

@author: admin
'''
from selenium import webdriver
from time import sleep
#定义打开页面函数
def geturl(url="http://120.25.68.186:8080/"):
    global driver
    driver=webdriver.Firefox()
    

    driver.get(url)
    sleep(3)

    driver.maximize_window()
    #return driver
#定义输入函数
def sendkeys(user="admin",pwd="888888",db="4pxtech"):
    driver.find_element_by_id("ACCOUNT").send_keys(user)
    driver.find_element_by_id("PASSWORD").send_keys(pwd)
    driver.find_element_by_id("COMPANY").send_keys(db)
    sleep(5)
def submit():

    driver.find_element_by_xpath(".//*[@id='formID']/div/ul/li[4]/button").click()
    sleep(8)
    
if __name__=="__main__":
    geturl()
    sendkeys()
    submit()
    
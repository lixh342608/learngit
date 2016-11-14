#coding=utf-8
'''
Created on 2016年7月27日

@author: admin
'''
from selenium import webdriver
from time_out import waittime
from getdriver import getdriver

case=getdriver()
case.openbr()
driver=case.geturl()
wait=waittime(driver,30)
wait.get_ele('id','txtUser').send_keys("13612844278")
wait.get_ele('id','txtPass').send_keys('aa123654')
wait.get_ele('id','loginBtn').click()

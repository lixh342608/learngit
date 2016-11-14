#coding=utf-8
'''
Created on 2016年3月24日

@author: admin
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://119.39.48.91:8082/escm")

driver.find_element_by_id("ACCOUNT").send_keys("admin")

driver.find_element_by_id("PASSWORD").send_keys("123456")

driver.find_element_by_id("COMPANY").send_keys("csjdyy")

driver.find_element_by_css_selector(".loginform-container>ul>li>button").click()
sleep(10)




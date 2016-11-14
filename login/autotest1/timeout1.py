#coding=utf-8
'''
Created on 2016年1月4日

@author: admin
'''
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def getfrom(driver,froma,vale):
    #global driver
    if froma.lower()=="id":
        driver.find_element_by_id(vale)
    elif froma.lower()=="name":
        driver.find_element_by_name(vale)
    elif froma.lower()=="classname":
        driver.find_element_by_class_name(vale)
    elif froma.lower()=="tagname":
        driver.find_element_by_tag_name(vale)
    elif froma.lower()=="linktext":
        driver.find_element_by_link_text(vale)
    elif froma.lower()=="xpath":
        dirver.find_element_by_xpath(vale)
    elif froma.lower()=="css":
        driver.find_element_by_css_selector(vale)
    else:
        print "没有这个元素定位方法"
    

def timeout(driver,froma,vale,timeout):
    #global driver
    try:
        element=getfrom(driver, froma, vale)
    except NoSuchElementException:
        if timeout>=3:
            print "没找到元素，3秒后重试"
            sleep(3)
            timeout-=3
            timeout(driver, froma, vale, timeout)
        else:
            raise NoSuchElementException
        
    return element
        
if __name__=='__main__':
    url="http://mail.163.com/"
    login=webdriver.Firefox()
    login.get(url)
    element=timeout(login,"xpath",".//*[@id='idPlaceholder']",timeout=30)
    element.send_keys("15355451791")             
            
    
#coding=utf-8
'''
Created on 2015年12月28日

@author: admin
'''
from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException


#打开163邮箱页面
def geturl(url="http://mail.163.com/"):
    global driver
    print ("""请选择以下任一浏览器过行输入：firefox,ie,chrome
    直接按回画使用默认浏览器""")
    while True:
        browser=raw_input("请输信您要使用的浏览器:")
        if browser.strip()=="" or browser.lower()=="firefox":
            driver=webdriver.Firefox()
            break
        elif browser.lower()=="ie":
            driver=webdriver.Ie()
            break
        elif browser.lower()=="chrome":
            driver=webdriver.Chrome()
            break
        else:
            print("输入错误，请重新输入")
    
    
    driver.maximize_window()
    driver.get(url)
    sleep(5)

#输入用户名
def send_user():
    usern = tk_input("请输入您的帐户(使用默认帐户请按‘提交’键)：","帐户不可含有中文")
    if usern.strip()=="":
        usern="15355451791"
    try:
        driver.find_element_by_css_selector("#idPlaceholder").send_keys(usern)
    except NoSuchElementException as e:
        print(e)

#输入密码
def send_pwd():
    passw = tk_input("请输入您的密码(使用默认帐户密码请按‘提交’键)：","请输入对应帐户的密码")
    if passw.strip()=="":
        passw="5912519"
        print(passw)
    try:
        #driver.find_element_by_css_selector("#pwdPlaceholder").clear()
        driver.find_element_by_id("pwdPlaceholder").send_keys(passw)
    except NoSuchElementException as e:
        print(e)
        
#点击登陆按钮
def click_btn():
    try:
        driver.find_element_by_css_selector("#loginBtn").click()
    except NoSuchElementException as e:
        print(e)
    sleep(10)

#退出页面（关闭浏览器）
def exitit():
    driver.quit()


    
    
#测试以上函数
if __name__=="__main__":
    geturl()
    send_user()
    send_pwd()
    click_btn()
    #exitit()
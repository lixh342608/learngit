#coding=utf-8
'''
Created on 2016年2月29日

@author: admin
'''
from selenium import webdriver
from readfile import readfile

class getdriver:
    def __init__(self):
        self.tab=dict(readfile())
        
    def openbr(self):
            
        if self.tab["browser"].lower()=="chrom":
            self.driver=webdriver.Chrome()
        elif self.tab["browser"].lower()=="ie":
            self.driver=webdriver.Ie()
        else:
            self.driver=webdriver.Firefox()
            
        self.driver.maximize_window()
    def geturl(self):
        self.driver.get(self.tab["url"])
        return self.driver
    
if __name__=="__main__":
    case=getdriver()
    case.openbr()
    driver=case.geturl()
        
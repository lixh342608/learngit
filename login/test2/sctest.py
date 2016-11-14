#coding=utf-8
'''
Created on 2015年12月31日

@author: admin
'''

import re
def strchange(file,reg,newstr):
    #读取文件
    ng=open(file,'r')
    text=ng.read()
    ng.close()
    #以写入方式打开
    ng=open(file,'w')
    #编译传入的正则表达式
    reg=re.compile(reg)
    reg=re.findall(reg,text)
    #循环修改文件内容
    for i in reg:    
        text=re.sub(i,newstr,text)
    ng.write(text)
    ng.close()



if __name__=="__main__":
    
    reg='url="jdbc:oracle:thin:@(.+?)"  username="haitao_test"'
    file="C:/Users/admin/Desktop/test/Database.xml"
    newst="111.111.111.111:1521:orcl"
    strchange(file,reg,newst)
    
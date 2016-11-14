#coding=utf-8
'''
Created on 2016年8月15日

@author: admin
'''
from urllib import request

http=request.urlopen("http://www.baidu.com")
httpstr=http.read().decode("utf-8")

print(httpstr)
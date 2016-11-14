#!/usr/bin/evn python
#coding=utf-8

'''
Created on 2016年4月9日

@author: admin
'''
import os
#查询当前路径
now_path=os.getcwd()
#获取当前路径所有文件列表
dirs=os.listdir(now_path)
#遍历文件列表，含有tomcat的文件将执行清理操作
for dir in dirs:
    if 'tomcat' in dir: 
        log_path=now_path+'/'+dir+'/logs'
        
        
        print log_path
        child_dirs=os.listdir(log_path)
        print child_dirs
        
        
        print dir
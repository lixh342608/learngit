#coding=utf-8
'''
Created on 2016年9月9日

@author: pc
'''
from ftplib import FTP, error_perm
import os


def rm_tree(ftp,parentdir):
    ftp.cwd(parentdir)
    dirs=ftp.nlst()
    for di in dirs:
        if "." in di:
            #this is a file
            ftp.delete(di)
        else:
            #this is a dir
            try:
                ftp.rmd(di)
            except error_perm:
                if ftp.pwd()=="/":
                    ftp.cwd(ftp.pwd()+di)
                else:
                    ftp.cwd(ftp.pwd()+"/"+di)
                rm_tree(ftp,di)
    if ftp.pwd()=="/":
        pass
    else:
        ftp.cwd("..")
        ftp.rmd(parentdir)
        
        
    
if __name__=="__main__":
    ftp=FTP() #设置变量
    ftp.set_debuglevel(0) #打开调试级别2，显示详细信息
    ftp.connect("127.0.0.1","21") #连接的ftp sever和端口
    ftp.login("ftptest","ftptest")#连接的用户名，密码
    print ftp.getwelcome() #打印出欢迎信息
    ftp.cwd("/")
    dirlist=ftp.nlst()
    for di in dirlist:
        rm_tree(ftp)
    ftp.quit()
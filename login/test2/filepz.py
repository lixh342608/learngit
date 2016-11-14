#coding=utf-8
'''
Created on 2016年1月25日

@author: admin
'''
import tk_msginput as tk
from strchange import *
import parftp

inp=tk.tk_Msginput()
lst=inp.tk_input()
term=["file_path","newdb","newurl","moteip","moteport","moteuser","motepwd"]
perfer=dict(zip(term,lst))
sc=strChange(perfer["file_path"],perfer["newurl"],perfer["newdb"])
    
tp=parftp.parftp(perfer['moteip'],int(perfer['moteport']),perfer["moteuser"],perfer["motepwd"])

    
sc.checkdir()
motefile=sc.motevar("/soft/tomcat-xmt-shop/conf/server.xml")
localfile="C:/Users/admin/Desktop/test/server.xml"
tp.get_ftp(localfile, motefile)
    
reg='docBase="(.+?)/webapp/shop" debug="0"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"    
    #修改第二个文件
sc.checkdir()
motefile=sc.motevar("/webapp/shop/WEB-INF/classes/Database.xml")
localfile="C:/Users/admin/Desktop/test/Database.xml"
tp.get_ftp(localfile, motefile)
reg='url="jdbc:oracle:thin:@(.+?)"'
sc.strchange(localfile,reg,sc.newdb)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
    
#修改第三个文件
sc.checkdir()
motefile=sc.motevar("/webapp/shop/WEB-INF/classes/LuceneConfig.xml")
localfile="C:/Users/admin/Desktop/test/LuceneConfig.xml"
tp.get_ftp(localfile, motefile)
reg='path="(.+?)/webapp/shop/WEB-INF/index" searchinterval="10"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
#修改第四个文件
sc.checkdir()
motefile=sc.motevar("/soft/tomcat-xmt-sp/conf/server.xml")
localfile="C:/Users/admin/Desktop/test/server.xml"
tp.get_ftp(localfile, motefile)
reg='docBase="(.+?)/webapp/supplier" debug="0"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
    
#修改第五个文件
sc.checkdir()
motefile=sc.motevar("/webapp/supplier/WEB-INF/classes/Database.xml")
localfile="C:/Users/admin/Desktop/test/Database.xml"
tp.get_ftp(localfile, motefile)
reg='url="jdbc:oracle:thin:@(.+?)"'
sc.strchange(localfile,reg,sc.newdb)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
    
#修改第六个文件
sc.checkdir()
motefile=sc.motevar("/webapp/supplier/editor/ueditor/jsp/config.json")
localfile="C:/Users/admin/Desktop/test/config.json"
tp.get_ftp(localfile, motefile)
reg='"imageUrlPrefix": "http://(.+?)/product"'
sc.strchange(localfile,reg,sc.newurl)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
#修改第七文件
sc.checkdir()
motefile=sc.motevar("/soft/tomcat-xmt-erp/conf/server.xml")
localfile="C:/Users/admin/Desktop/test/server.xml"
tp.get_ftp(localfile, motefile)
reg='docBase="(.+?)/webapp/erp" debug="0"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
#修改第八个文件
sc.checkdir()
motefile=sc.motevar("/webapp/erp/WEB-INF/classes/Database.xml")
localfile="C:/Users/admin/Desktop/test/Database.xml"
tp.get_ftp(localfile, motefile)
reg='url="jdbc:oracle:thin:@(.+?)"'
sc.strchange(localfile,reg,sc.newdb)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
#同步线程配置
#修改第一个文件
sc.checkdir()
motefile=sc.motevar("/webapp/thread/thread-order/Database.xml")
localfile="C:/Users/admin/Desktop/test/Database.xml"
tp.get_ftp(localfile, motefile)
reg='url="jdbc:oracle:thin:@(.+?)"'
sc.strchange(localfile,reg,sc.newdb)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
    #修改第二个文件
sc.checkdir()
motefile=sc.motevar("/webapp/thread/thread-other/Database.xml")
localfile="C:/Users/admin/Desktop/test/Database.xml"
tp.get_ftp(localfile, motefile)
reg='url="jdbc:oracle:thin:@(.+?)"'
sc.strchange(localfile,reg,sc.newdb)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
    
#修改第三个文件
sc.checkdir()
motefile=sc.motevar("/webapp/thread/thread-user/Database.xml")
localfile="C:/Users/admin/Desktop/test/Database.xml"
tp.get_ftp(localfile, motefile)
reg='url="jdbc:oracle:thin:@(.+?)"'
sc.strchange(localfile,reg,sc.newdb)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
    #修改第四个文件
sc.checkdir()
motefile=sc.motevar("/webapp/thread/thread-order/LuceneConfig.xml")
localfile="C:/Users/admin/Desktop/test/LuceneConfig.xml"
tp.get_ftp(localfile, motefile)
reg='path="(.+?)/webapp/shop/WEB-INF/index" searchinterval="10"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
#修改第五个文件
sc.checkdir()
motefile=sc.motevar("/webapp/thread/thread-other/LuceneConfig.xml")
localfile="C:/Users/admin/Desktop/test/LuceneConfig.xml"
tp.get_ftp(localfile, motefile)
reg='path="(.+?)/webapp/shop/WEB-INF/index" searchinterval="10"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
#修改第六个文件
sc.checkdir()
motefile=sc.motevar("/webapp/thread/thread-user/LuceneConfig.xml")
localfile="C:/Users/admin/Desktop/test/LuceneConfig.xml"
tp.get_ftp(localfile, motefile)
reg='path="(.+?)/webapp/shop/WEB-INF/index" searchinterval="10"'
sc.strchange(localfile,reg,sc.file_path)
tp.put_ftp(localfile, motefile)
print motefile+"已完成"  
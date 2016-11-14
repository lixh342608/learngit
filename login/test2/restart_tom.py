#coding=utf-8
'''
Created on 2016年3月17日

@author: admin
'''
import os
while True:
    ret = os.system('tasklist | find "java.exe"')
    if ret==0:
        os.system('TASKKILL /F /IM java.exe"')
    else:
        break
#设置classpath
env=os.getenv('classpath')
value='%CATALINA_HOME%\\lib'
if env==None:
    os.environ['classpath']=value
else:
    if value in env:
        pass
    else:
        os.environ['classpath']=env+';'+value
#设置catalina_home
def catalinset(item):         
    path=os.getcwd()
    parent_path = os.path.dirname(path)
    value=parent_path+'\\'+item
    catal=os.getenv('catalina_home')
    
    os.environ['catalina_home']=value


toms=["tomcat-web","tomcat-service","tomcat-syn-service",
      "tomcat-api-complex","tomcat-api-fop","tomcat-api-fpx"]
for tom in toms:
    catalinset(tom)
    print os.getenv('catalina_home')
    cmd="call %CATALINA_HOME%\\bin\\startup.bat"
    try:
        os.system(cmd)
    except Exception as e:
        print e
        pass
    

        
    

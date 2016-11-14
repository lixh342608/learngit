#!/usr/bin/python
#encoding:utf-8

import os

#获得当前路径
'''path=os.getcwd()
print path

path=os.path.abspath(".")
print path

path=os.path.abspath(os.curdir)
print path'''
#获得环境变量

    env=os.getenv('classpath')
    value='%CATALINA_HOME%/lib'
    if env==None:
        os.environ['classpath']=value
    else:
        if value in env:
            pass
        else:
            os.environ['classpath']=env+';'+value
    print os.getenv('classpath')

def catlinset():
    return os.getenv('path')
    
    
if __name__=='__amin__':
    #env=catlinset()
    #print env
    classptset()
    

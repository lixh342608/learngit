#coding=utf-8
'''
Created on 2016年8月17日

@author: admin
'''
from fabric.api import *

env.host_string='root@192.168.154.129:22'  
env.password='123456'

rootwd=run("more /root/.mysql_secret").split(":")
command="mysql -uroot -p"+rootwd[-1].strip()
#print command
run(command)
run("SET PASSWORD = PASSWORD('123456');")
run("exit")

#print rootwd[-1]
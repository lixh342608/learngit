#coding=utf-8
'''
Created on 2016年8月16日

@author: admin
'''
from fabric.api import *
from readfile import readfile

condict=dict(readfile())

env.host_string=condict["connext"] 
env.password=condict["passwd"]

run("rm -rf /taokey")

run("yum -y remove mysql-libs*")
run("yum -y remove mysql-libs")
run("yum install -y perl-Module-Install.noarch")
run("yum install -y libaio")
run("mkdir -p /taokey/tools/")

with cd("/taokey/tools/"):
    run("wget http://dev.mysql.com/Downloads/MySQL-5.6/MySQL-server-5.6.21-1.rhel5.x86_64.rpm")
    run("wget http://dev.mysql.com/Downloads/MySQL-5.6/MySQL-devel-5.6.21-1.rhel5.x86_64.rpm")
    run("wget http://dev.mysql.com/Downloads/MySQL-5.6/MySQL-client-5.6.21-1.rhel5.x86_64.rpm")
    rpmlist=run("ls ./").split()
    for rpm in rpmlist:
        command="rpm -ivh "+rpm
        run(command)
run("cp /usr/share/mysql/my-default.cnf /etc/my.cnf")
run("sed -i '/\[mysqld\]/a\max_allowed_packet=300M\nmax_connections=1500\nlower_case_table_names=1\nskip-name-resolve' /etc/my.cnf")
run("/usr/bin/mysql_install_db")
run("service mysql start")
run("chkconfig mysql on")
run("chkconfig mysql --list")
rootwd=run("more /root/.mysql_secret").split(":")
passwd=rootwd[-1].strip()
command="mysqladmin -uroot -p%s password '123456'" % passwd
run(command)

run("/usr/bin/mysql -uroot -p123456 -N -e \"use mysql; update user set host='%' where user='root' and host='127.0.0.1';\"")
print 'mysql数据库已安装完成,管理员密码为“root”,默认密码为：123456'
  
    
    
    
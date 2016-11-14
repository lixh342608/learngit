#coding=utf-8
'''
Created on 2016年1月23日

@author: admin
'''

import paramiko,parftp
def commandexecut():
    paramiko.util.log_to_file('paramiko.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("119.39.48.91",10002,"root","JiaDe~!234")
    print("开始解压文件...")
    stdin, stdout, stderr = ssh.exec_command("unzip /opt/test/svn_out.zip -d /opt/test")

    for line in stdout.readlines():
        print(line)
    print("解压完成...")
    ssh.close()

#tp=parftp.parftp("119.39.48.91",119.39.48.91,"root","JiaDe~!234")

#root@119.39.48.91:10002
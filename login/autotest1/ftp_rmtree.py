###coding=gbk
'''
Created on 2016��9��8��

@author: pc
'''
#from cod_utf8 import cod_utf8
from ftplib import FTP,error_perm #����ftpģ��
class rmdir:
    def __init__(self,ip="127.0.0.1",port="21",username="ftptest",passwd="ftptest"):
        
        self.ftp=FTP() #���ñ���
        self.ftp.set_debuglevel(0) #�򿪵��Լ���2����ʾ��ϸ��Ϣ
        self.ftp.connect(ip,port) #���ӵ�ftp sever�Ͷ˿�
        self.ftp.login(username,passwd)#���ӵ��û���������
        print self.ftp.getwelcome() #��ӡ����ӭ��Ϣ
        self.ftp.cwd("/")
    def rmtreed(self,parentdir):
        try:
            self.ftp.delete(parentdir)
        except:
            print "%s is a dir" % parentdir
            try:
                self.ftp.rmd(parentdir)
            except error_perm:
                if self.ftp.pwd()=="/":
                    self.ftp.cwd(self.ftp.pwd()+parentdir)
                else:
                    self.ftp.cwd(self.ftp.pwd()+"/"+parentdir)
            
                dirs=self.ftp.nlst()
                print dirs
                for di in dirs:
                    self.rmtreed(di)
                if self.ftp.pwd()=="/":
                    pass
                else:
                    self.ftp.cwd("..")
                    self.ftp.rmd(parentdir)
            

    def quitdown(self):
        self.ftp.quit()
if __name__=="__main__":
    rmd=rmdir()
    dirs=rmd.ftp.nlst()
    print dirs
    for dir in dirs:
        
        if dir.lower() != "public":
            
            rmd.rmtreed(dir)
        else:
            continue
    rmd.quitdown()
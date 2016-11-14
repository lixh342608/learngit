#coding=utf-8
from Tkinter import *
import sys,time
import linux_mysql as sta
from fabric.api import *


class tk_Msginput:
    def __init__(self):
        self.root=Tk()
    
        self.root.title("mysql数据库安装")
    
        width_n=self.root.winfo_screenwidth()/2-150
        height_n=self.root.winfo_screenheight()/2-250
        
        self.root.geometry('400x200+%s+%s' % (width_n,height_n))
        file="linux_mysql_install.log"
        self.path_file=sta.condict["log_path"]+file
        self.sql=0
    def say_no(self):
            self.root.destroy()
    '''def itm(self):
        while True:
            n=yield
            if not n:
                self.edt.insert(END,"\n正在创建数据库，请等待.....")
                time.sleep(5)
                self.sql=-1
                
            else:
                self.sql=1
                break
    def change_my(self,cls):
        cls.next()
        self.edt.insert(END,"\n正在创建数据库，请等待.....")
        try:
            sta.mysql_install()
        except Exception as e:
            self.edt.insert(END,"\n错误提示："+e)
        else:
            self.edt.insert(END,"\n数据库创建成功，初始密码：root/123456")
        cls.send(1)'''
    def aticon(self):
        self.edt.insert(END,"\n正在创建数据库，请等待.....")
        self.sql=1
    def ab(self):
        self.edt=Text(self.root,height=10)
        self.edt.pack(side=TOP,padx=10,pady=10)
        self.edt.insert(INSERT,"准备初始化数据库，请确认已正确修改配置文件。")
        self.nobut=Button(self.root,text="取消",command=self.say_no).pack(side=LEFT,padx=50)
        self.yesbut=Button(self.root,text="确定",command=self.aticon,state=NORMAL).pack(side=RIGHT,padx=50)
        while True:
            if self.sql==1:
                try:
                    sta.mysql_install()
                except Exception as e:
                    self.edt.insert(END,"\n错误提示："+e)
                else:
                    self.edt.insert(END,"\n数据库创建成功，初始密码：root/123456")
            else:
                pass
                
    
        self.root.mainloop()
if __name__=="__main__":
    pac=tk_Msginput()
    pac.ab()
    
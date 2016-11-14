#coding=utf-8
'''
Created on 2016年8月19日

@author: admin
'''
from Tkinter import *
import tkMessageBox
from distutils.cmd import Command
from pymysql1 import *

class tk_Msginput:
    def __init__(self):
        self.root=Tk()
    
        self.root.title("数据库初始化配置")
    
        self.sql=0
        width_n=self.root.winfo_screenwidth()/2-150
        height_n=self.root.winfo_screenheight()/2-250
        
        self.root.geometry('400x200+%s+%s' % (width_n,height_n))
    def say_no(self):
            self.root.destroy()
    def change_mysql(self):
            if self.sql==0:
                self.sql=-1
            
                sqlinfo=mysqlUp()
                con=sqlinfo.connexts()
                self.edt.insert(END,'\n'+con)
                if sqlinfo.ty==1:
                    con=sqlinfo.exeupdata()
                    self.edt.insert(END,'\n'+con)
                    con=sqlinfo.houseup()
                    self.edt.insert(END,'\n'+con)
                    sqlinfo.quitnow()
                else:
                    self.edt.insert(END,'\n请检查数据库连接参数！')
                self.sql=1
            elif self.sql==-1:
                pass
            else:
                self.root.destroy()
    def ab(self):
        self.edt=Text(self.root,height=10)
        self.edt.pack(side=TOP,padx=10,pady=10)
        self.edt.insert(INSERT,"准备初始化数据库数据，请确认已正确修改配置文件。")
        self.nobut=Button(self.root,text="取消",command=self.say_no).pack(side=LEFT,padx=50)
        self.yesbut=Button(self.root,text="确定",command=self.change_mysql,state=NORMAL).pack(side=RIGHT,padx=50)
        
    
        self.root.mainloop()
        

if __name__=="__main__":
    pac=tk_Msginput()
    pac.ab()

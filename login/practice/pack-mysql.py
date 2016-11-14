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
    
        
        width_n=self.root.winfo_screenwidth()/2-150
        height_n=self.root.winfo_screenheight()/2-250
        
        self.root.geometry('400x200+%s+%s' % (width_n,height_n))
    def ab(self):
        def say_no():
            self.root.destroy()
        def change_mysql():
            self.yesbut['state']=DISABLED
            #sqlinfo=mysqlUp()
            #con=sqlinfo.connexts()
            #self.text.set(con)
            #sqlinfo.upsqlmain()
        
        self.text=StringVar()
        
        self.root.eix=Label(self.root,textvariable=self.text).pack(side=TOP,padx=50,pady=50)
        self.text.set("准备初始化数据库数据，请确认已正确修改配置文件。")
        self.nobut=Button(self.root,text="取消",command=say_no).pack(side=LEFT,padx=50)
        self.yesbut=Button(self.root,text="确定",command=change_mysql,state=NORMAL).pack(side=RIGHT,padx=50)
        
    
        self.root.mainloop()
        

if __name__=="__main__":
    pac=tk_Msginput()
    pac.ab()

#coding=utf-8
'''
Created on 2016年1月29日

@author: admin
'''
from Tkinter import *

root=Tk()
root.title("流程设计")

width_n=root.winfo_screenwidth()/2-150
height_n=root.winfo_screenheight()/2-250
root.geometry('200x400+%s+%s' % (width_n,height_n))
la=Label(root,text="请设计部署流程：").pack()
la1=Label(root,text="源文件：").pack(side=LEFT,fill=BOTH)


root.mainloop()
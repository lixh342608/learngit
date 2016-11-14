#coding=utf-8
'''
Created on 2016年4月21日

@author: admin
'''
from Tkinter import *

root=Tk()
root.title("执行部署")

width_n=root.winfo_screenwidth()/2-200
height_n=root.winfo_screenheight()/2-200
root.geometry('400x400+%s+%s' % (width_n,height_n))
la=Label(root,text="请设计部署流程：",height=7,width=20,relief=SUNKEN,bd=2).grid(row=0,column=0)
la1=Label(root,text="源文件：",height=7,width=20,relief=SUNKEN,bd=2).grid(row=1,column=0)

mainloop()
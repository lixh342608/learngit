#coding=utf-8
'''
Created on 2016年3月11日

@author: admin
'''
from Tkinter import *

root = Tk()

# column 默认值是 0
Label(root, text="远程地址").grid()
Label(root, text="远程端口").grid(row=0,column=2)
Label(root,text="用户名").grid(row=0,column=4)
Label(root,text="密码").grid(row=0,column=6)

Entry(root).grid(row=0,column=1)
Entry(root).grid(row=0, column=3)
Entry(root).grid(row=0,column=5)
Entry(root).grid(row=0,column=7)

mainloop()

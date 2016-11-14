#coding=utf-8
'''
Created on 2015年12月22日

@author: admin
'''

from Tkinter import *
import tkMessageBox


def tk_input():
    global st

    root=Tk()

    root.title("请输入你的帐户名：")

    root.geometry('200x50')

    text_var=StringVar()

    e=Entry(root,textvariable=text_var).pack(side=LEFT)

    text_var.set("")

    def click_on():
        global st
        st=text_var.get()
        if tkMessageBox.showinfo("你输入的内容是：", st):
            root.quit()
        

    b1=Button(root,text="提交",command=click_on).pack(side=RIGHT)
    root.mainloop()

tk_input()
print (st)
#coding=utf-8
'''
Created on 2015年12月25日

@author: admin
'''

from tkinter import *
#import tkMessageBox



def tk_input(title,text):
    st=[]

    root=Tk()

    root.title(title)

    
    width_n=root.winfo_screenwidth()/2-125
    height_n=root.winfo_screenheight()/2-50
    
    root.geometry('250x100+%s+%s' % (width_n,height_n))
    
    lab=Label(root,text=text).pack(side=TOP)

    text_var=StringVar()

    e=Entry(root,textvariable=text_var).pack(side=LEFT)

    text_var.set("")

    def click_on():
        
        ts=text_var.get()
        #if tkMessageBox.showinfo("你输入的内容是：", st):
        st.append(ts)
        root.destroy()
        

    b1=Button(root,text="提交",command=click_on).pack(side=RIGHT)
    root.mainloop()
    return st[0]
if __name__=="__main__":
    st=tk_input("请输入你的姓名","有效字符:\nfirefox,ie,chrome")
    print (st)

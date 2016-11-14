#coding=utf-8
'''
Created on 2015年12月25日

@author: admin
'''

from Tkinter import *
import tkMessageBox

class tk_Msginput:
    def __init__(self):
        self.root=Tk()
    
        self.root.title("预设参数")
    
        
        width_n=self.root.winfo_screenwidth()/2-150
        height_n=self.root.winfo_screenheight()/2-250
        
        self.root.geometry('200x400+%s+%s' % (width_n,height_n))

    def tk_input(self):
        st=[]
    
        
        #设置文件路径
        lab1=Label(self.root,text="请输入文件路径:").pack()
    
        path_var=StringVar()
    
        e1=Entry(self.root,textvariable=path_var).pack()
    
        path_var.set("")
        
        #设置新数据库地址
        lab2=Label(self.root,text="请输入新数据库地址:").pack()
    
        newdb_var=StringVar()
    
        e2=Entry(self.root,textvariable=newdb_var).pack()
    
        newdb_var.set("")
        
        #设置新域名
        lab3=Label(self.root,text="请输入新域名:").pack()
    
        newurl_var=StringVar()
    
        e3=Entry(self.root,textvariable=newurl_var).pack()
    
        newurl_var.set("")
        
        #设置远程主机IP
        lab4=Label(self.root,text="请输入远程主机IP:").pack()
    
        moteip_var=StringVar()
    
        e4=Entry(self.root,textvariable=moteip_var).pack()
    
        moteip_var.set("")
        
        #设置远程主机端口
        lab5=Label(self.root,text="请输入远程主机端口:").pack()
    
        moteport_var=StringVar()
    
        e5=Entry(self.root,textvariable=moteport_var).pack()
    
        moteport_var.set("")
        
        #设置远程主机用户名
        lab6=Label(self.root,text="请输入远程主机用户名:").pack()
    
        moteuser_var=StringVar()
    
        e6=Entry(self.root,textvariable=moteuser_var).pack()
    
        moteuser_var.set("")
        
        #设置远程主机用户密码
        lab7=Label(self.root,text="请输入远程主机用户密码:").pack()
    
        motepwd_var=StringVar()
    
        e7=Entry(self.root,textvariable=motepwd_var).pack()
    
        motepwd_var.set("")
        
        def click_on():
            
            file_path=path_var.get()
            newurl=newurl_var.get()
            newdb=newdb_var.get()
            moteip=moteip_var.get()
            moteport=moteport_var.get()
            moteuser=moteuser_var.get()
            motepwd=motepwd_var.get()
            if file_path and newurl and newdb and moteip and moteport and moteuser and motepwd:
                st.append(file_path)
                
                st.append(newdb)
                st.append(newurl)
                #st.append(moteport)
                st.append(moteip)
                st.append(moteport)
                st.append(moteuser)
                st.append(motepwd)
                self.root.destroy()
            else:
                tkMessageBox.showinfo("提示：","以上所有项不可为空！")
            
                
            
    
        b1=Button(self.root,text="提交",command=click_on).pack()
        self.root.mainloop()
        return st
if __name__=="__main__":
    cl=tk_Msginput()
    st=cl.tk_input()
    print (st)
    c2=Tk()
    button2=Button(c2,text="我是老2")
    button2.pack()
    c2.mainloop()
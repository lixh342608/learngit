#coding=utf-8
'''
Created on 2016年3月13日

@author: Administrator
'''
from Tkinter import *

import tkMessageBox

class par_set:
    def __init__(self):
        self.root=Tk()
        self.root.title("参数设置：")
        width_n=self.root.winfo_screenwidth()/2-150
        height_n=self.root.winfo_screenheight()/2-250
        
        self.root.geometry('600x350+%s+%s' % (width_n,height_n))
        self.ret=0
    
    
    def par_file(self):
        Label(self.root,text="需要部署的环境：",font="汉仪南宫体简").grid(sticky=W)
        items=["tomcat-web","tomcat-serverse","tomcat-syn-serverse",
               "tomcat-api-compile","tomcat-api-fop","tomcat-api-fpx"]
        v=[]
        for item in items:
            v.append(IntVar())
            Checkbutton(self.root,text=item,variable=v[-1]).grid(sticky=W)
            v[-1].set(1)
        Label(self.root,text="请填写部署信息：",font="汉仪南宫体简").grid(row=7,column=0,sticky=W)
        args=[]
        test=[]
        def arg(x,y,textname):
            Label(self.root,text=textname).grid(row=x,column=y)    
            args.append(StringVar())
            Entry(self.root,textvariable=args[-1]).grid(row=x,column=y+1)
            
        textnames=["远程主机IP：","远程主机PORT：","远程主机帐户：","远程主机密码：","数据库连接：","安装路径："]
        x=8
        y=0
        for textname in textnames:
            arg(x,y,textname)
            y+=2
            if y > 2:
                x+=1
                y=0
        def conf():
            for i in args:
                if i.get()=="":
                    tkMessageBox.showinfo("提示：","以上所有项不可为空！")
                    break
            else:
                self.ret=1
                self.root.destroy()
        def exit():
            self.root.destroy()
                
        
        #第十一列
        Button(self.root,text="确定",command=conf).grid(row=11,column=0)
        Button(self.root,text="取消",command=exit).grid(row=11,column=3)
        self.root.mainloop()
        if self.ret==1:
            return dict(zip(items,v)),dict(zip(textnames,args))
        else:
            return None,None
if __name__=="__main__":
    par=par_set()
    #print par
    item,args=par.par_file()
    print item["tomcat-web"].get()
    print args["远程主机帐户："].get()
            
            
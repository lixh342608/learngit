#coding=utf-8
'''
Created on 2016年7月12日

@author: admin
'''
from Tkinter import *

root = Tk()
width_n=root.winfo_screenwidth()/2-200
height_n=root.winfo_screenheight()/2-250
root.geometry('500x500+%s+%s' % (width_n,height_n))
fram=Frame(root,height=500,width=100,bd=10,bg="blue").pack(side=LEFT)
fram=Frame(root,height=100,width=400,bd=10,bg="green").pack(side=TOP)
m=Text(root).pack()
b=Button(root,text="确定").pack()
mainloop()

"""from Tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love FishC.com!\n")
text.insert(INSERT, "鱼C大法好")
# 将任何格式的索引号统一为元祖 (行,列) 的格式输出
def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), ".")))

start = 1.0
while True:
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print(u"找到位置了：", getIndex(text, pos))
    start = pos + "+1c"  # 将 start 指向下一个字符

mainloop()"""
"""def yieldtest(max):
    for i in range(100):
        yield i
y=yieldtest(100) 
for i in y:
    print(i)"""
"""import os   
file="/mapi"
lpath="F:/svn_out"
rpath="/data/wwwroot/51yushtest"

       
localpath=os.path.join(lpath,file)
print localpath
remotepath=os.path.join(rpath,file)
print remotepath"""
    
    
    
"""from math import sqrt

def do_sth(x,*fs):
    req=[f(x_f) for x_f in x for f in fs]
    return req

req=do_sth(range(10),sqrt,abs)
print(req)

def namecode(name):
    return name.capitalize()
if __name__=="__main__":
    l1=["admin","alise","acpt","lucy"]
    l2=list(map(namecode,l1))
    print(l2)"""
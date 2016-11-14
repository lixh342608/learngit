#coding=utf-8

'''import Tkinter
from os import path
 
class Window:
    def __init__(self, root):
        self.root = root
        self.setbtn = Tkinter.Button(root, text='Set Text', command=self.Settxt)
        # 创建一个按钮对象，command= 这个地方就是当按钮按下去时触发的函数
        self.setbtn.place(x=120, y=15)
        self.edit = Tkinter.Text(root)
        self.edit.place(y=50)
        self.edit.insert(Tkinter.END, "this is original text")
 
    def Settxt(self):
        self.edit.insert(Tkinter.END, '\nthis is inster text')
 
 
root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()'''

# 捕获点击鼠标的位置
from Tkinter import *

root = Tk()

def callback(event):
    print(u"点击位置：", event.x, event.y)

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()

mainloop()
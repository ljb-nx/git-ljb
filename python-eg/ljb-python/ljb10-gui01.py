#!/usr/bin/python​
# coding:utf-8

import tkinter
import tkinter.messagebox as mbox

def clickbtn():
    text = entry.get()
    mbox.showinfo("输入的内容：",text)
    #print(text)

root = tkinter.Tk()

root.title("Tkinter 实例")
root.geometry('200x200')

entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root,text='按钮一',command=clickbtn)
button.pack()

root.mainloop()
